# --------------------------------------------------------------------------------------------
# RAKONTU
# Description: Rakontu is open source story sharing software.
# Version: pre-0.1
# License: GPL 3.0
# Google Code Project: http://code.google.com/p/rakontu/
# --------------------------------------------------------------------------------------------

from google.appengine.ext import webapp
import logging
from pytz import timezone
import pytz

import utils
from translationLookup import *

register = webapp.template.create_template_register()

# from http://stackoverflow.com/questions/35948/django-templates-and-variable-attributes
def dictLookup(dict, key):
	if dict:
		if key in dict:
			return dict[key]
		else:
			return None
	else:
		return None
	
def listLookup(list, index):
	if list:
		try:
			number = int(index)
		except:
			return None
		if number >= 0 and number <= len(list) - 1:
			return list[number]
		else:
			return None
	else:
		return None
	
def get(object, fieldName):
	if object:
		if callable(getattr(object, fieldName)):
			function = getattr(object, fieldName)
			return function()
		else:
			return getattr(object, fieldName)
	else:
		return None
	
def length(list):
	return len(list)
	
def makeRange(numberString):
	result = []
	try:
		number = int(numberString)
	except:
		return result
	for i in range(number):
		result.append(i)
	return result

def makeRangeFromListLength(list):
	return range(len(list))

def add(numberString, addString):
	try:
		number = int(numberString)
		addNumber = int(addString)
		return str(number + addNumber)
	except:
		return numberString
	
def dividesBy(value, divideBy):
	return value != 0 and value % divideBy == 0
	
def timeZone(time, zoneName):
	if time:
		if time.tzinfo:
			return time.astimezone(timezone(zoneName))
		else:
			timeUTC = time.replace(tzinfo=pytz.utc)
			return timeUTC.astimezone(timezone(zoneName))
	else:
		return None
	
def notNone(value):
	return value != None and value != "None"

def orNbsp(value):
	if value:
		if value == "None":
			return "&nbsp;"
		else:
			return value
	else:
		return "&nbsp;"

def orNone(value):
	if value:
		return value
	else:
		return TERMS["NONE"]
	
def orNothing(value):
	if value:
		if value == "None":
			return ""
		else:
			return value
	else:
		return ""
	
def sorted(value):
	result = []
	value.sort()
	result.extend(value)
	return result

def infoTipCaution(value, type):
	helpText = utils.helpTextLookup(value, type)
	if helpText:
		return '<a href="/help?%s"><img src="../images/%s.png" alt="help" border="0" valign="center" title="%s"/></a>' % (value, type, helpText)
	else:
		return ""

def info(value):
	return infoTipCaution(value, "info")

def tip(value):
	return infoTipCaution(value, "tip")

def caution(value):
	return infoTipCaution(value, "caution")

def upTo(value, number):
	if value:
		result = value[:number]
		if len(value) > number:
			result += "..."
	else:
		result = value
	return result

def yourOrThis(value):
	if value:
		return TERMS["YOUR"]
	else:
		return TERMS["THISMEMBERS"]

def youOrThis(value):
	if value:
		return TERMS["YOU"]
	else:
		return TERMS["THISMEMBER"]
	
def toString(value):
	return "%s" % value

def toUnicode(value):
	if value:
		return unicode(value)
	else:
		return None
	
def equalTest(value, otherValue):
	if value == otherValue:
		return True
	return False

def spacify(value):
	return value.replace("_", " ").capitalize()
	
register.filter(listLookup)
register.filter(dictLookup)
register.filter(makeRange)
register.filter(makeRangeFromListLength)
register.filter(timeZone)
register.filter(notNone)
register.filter(orNbsp)
register.filter(orNone)
register.filter(orNothing)
register.filter(sorted)
register.filter(info)
register.filter(tip)
register.filter(caution)
register.filter(upTo)
register.filter(yourOrThis)
register.filter(youOrThis)
register.filter(dividesBy)
register.filter(add)
register.filter(length)
register.filter(toString)
register.filter(toUnicode)
register.filter(equalTest)
register.filter(get)
register.filter(spacify)


