#---------------------------------------- FROM WEB

The simplest way to get a list of Author instances from a
db.ListProperty(db.Key) is:
authors = [db.get(key) for key in book.authors] 

# change property of Model
p.properties()[s].get_value_for_datastore(p) 

#---------------------------------------- NOT USING

FAKE_STORY_DATA = {
                   "My day at the zoo": "I lost my freeze pop, and the lion ate my cousin. Pretty fun day.",
                   "Let's all be friends": "It was my first day of school, and the teacher sat on me.",
                   "The tree fell on my house": "It was my second best tiny stick house, and a branch fell on it and squashed it.",
                   "My foot hurts": "Don't trust salespeople in shoe stores.",
                   "The newt turned back": "So I filled up the little pond, and a newt didn't like it, so he climbed out. Then the dog sniffed him and he climbed back in. (true story!)",
                   "There it is": "Every time I give up on finding something, there it is! What's up with that?",
                   "Lovely junk": "So I put this old plastic toy in the attic and now the kids love it because it's junk.",
                   "The story of our town": "Our town was built by a giant. Last week a massive tree fell onto it. We are rebuilding.",
                   "Shorts": "I like to take my shorts out in January and put them on and pretend I'm on the other side of the world.",
                   "The dead frog": "We found a dead frog in the stream. For a while we didn't drink the water, but then we forgot about it.",
                   }

FAKE_COMMENTS = {
                 "What?": "Come on, that didn't really happen.",
                 "Yep": "Same thing happened to me.",
                 "Liar!": "I think you totally made that up.",
                 "I was there!": "I think you have distorted things a little, haven't you?",
                 "You have helped me": "I can't tell you how much your story has touched my life.",
                 }

def CreateABunchOfFakeData():
    aMember = Member(users.get_current_user())

    
    for title in FAKE_STORY_DATA.keys():
        aStory = Story(title=title, text=FAKE_STORY_DATA[title], creator=aMember, )
    aStory = Story(
                  title="My day at the zoo",
                  text="I lost my freeze pop, and the lion ate my cousin. Pretty fun day.",
                  creator=aMember,
                  attribution="member",
                  tookPlace=datetime.datetime(2009, 4, 2),
                  collected=datetime.datetime.now)
    aStory.put()
    aComment = Comment(
                       subject="Your cousin??", 
                       post="Is that really true about your cousin?",
                       article=aStory,
                       creator=anotherMember,
                       attribution="personification",
                       personification=aPersonification,
                       collected=datetime.datetime.now)

# --------------------------------- NOT USING

class JoinCommunityPage(webapp.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {'url': url, 'url_linktext': url_linktext,'communities': models.Community.all().fetch(1000)}
        if users.get_current_user():
            path = os.path.join(os.path.dirname(__file__), 'templates/joinCommunity.html')
        else:
            path = os.path.join(os.path.dirname(__file__), 'templates/notLoggedIn.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        user = users.get_current_user()
        if user:
            okayToJoin = False
            community = db.get(self.request.get('community_key')) 
            if community:
                if community.passwordIsRequired:
                    passwordEntered = self.request.get('password')
                    if passwordEntered == community.password:
                        okayToJoin = True
                    else:
                        self.redirect('/badPassword')
                else:
                    okayToJoin = True
            if okayToJoin:
                member = models.Member(
                    googleAccountID=user.user_id(),
                    community=community,
                    nickname = self.request.get('nickname'),
                    nicknameIsRealName = self.request.get('nickname_is_real_name')=="yes",
                    profileText = self.request.get('profile_text)'))
                member.put()
                self.redirect('/')
            else:
                self.redirect('/couldNotJoin')
                
class CouldNotJoinPage(webapp.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {'url': url, 'url_linktext': url_linktext}
        path = os.path.join(os.path.dirname(__file__), 'templates/couldNotJoin.html')
        self.response.out.write(template.render(path, template_values))

# ------------------------------- NOT USING

                      <td>
                      {% if aMember.isManager %} 
                          <form action="/manageCommunity_Members" method="post">
                          <input type="submit" name="removeManager|{{aMember.googleAccountID}}" value="Remove as Manager">
                          </form>
                      {% else %}
                          <form action="/manageCommunity_Members" method="post">
                          <input type="submit" name="addManager|{{aMember.googleAccountID}}" value="Make Manager">
                          </form>
                      {% endif %}
                      {% ifequal current_member.googleAccountID aMember.googleAccountID %}
                          {% if current_member.isOwner %}
                              <P>Owner
                          {% else %}
                              <p>(not Owner)
                          {% endif %}
                      {% else %}
                          {% if current_member.isOwner %}
                              {% if aMember.isOwner %} 
                                  <form action="/manageCommunity_Members" method="post">
                                  <input type="submit" name="removeOwner|{{aMember.googleAccountID}}" value="Remove as Owner">
                                  </form>
                              {% else %}
                                  <form action="/manageCommunity_Members" method="post">
                                  <input type="submit" name="addOwner|{{aMember.googleAccountID}}" value="Make Owner">
                                  </form>
                              {% endif %}
                          {% endif %}
                      {% endifequal %}
                      </td>
                      
# ------------------------------- NOT USING

                      
# --------------------------------------------------------------------------------------------
# System
# --------------------------------------------------------------------------------------------

class System(db.Model):
    """ Stores system-wide (above the community level) info
    """
    pass

    def getCommunities(self):
        return Community.all()
    
    def getGlobalCommunityQuestions(self):
        return Question.all().filter("community = ", None).filter("refersTo = ", "community").fetch(1000)
    
    def getGlobalAnnotationQuestions(self, articleType):
        return Question.all().filter("community = ", None).filter("refersTo = ", articleType).fetch(1000)
    
    def getGlobalMemberQuestions(self):
        return Question.all().filter("community = ", None).filter("refersTo = ", "member").fetch(1000)
    
    def getGlobalRules(self):
        return Rule.all().filter("community = ", None).fetch(1000)
    
# ----------------------------- NOT USING

    config = ConfigParser.RawConfigParser()
    config.read('rakontu_installation.cfg')
    configSections = config.sections()
    systemQuestions = {}
    for refersToConstant in QUESTION_REFERS_TO:
        for section in configSections:
            (refersToInCFG, name) = section.split(" - ")
            if refersToInCFG == refersToConstant:
                if not systemQuestions.has_key(refersToConstant):
                    systemQuestions[refersToConstant] = []
                newQuestion = Question(
                                       community=None,
                                       type=config.get(section, "Type")
                
                

    
                systemQuestions[refersToConstant].append(config.)

# ----------------------------- NOT USING

"""
# Note, In this early version the rules and community questions are not used, and community managers/owners
# just choose from lists of questions about things. These will be used later.

[community - Geographic]
Text=Is this a geographic community?
Type=nominal
Choices=yes|no
Multiple=false

[Rule]
Name=Where if geographic
CommunityQuestion=Geographic
Test=same as
TestValues=yes
IncludeIf=true
AnnotationQuestion=Where took place
MemberQuestion=Where live
"""

# ---------------------------- NOT USING - was chooseCommunityToManage.html

<html>
    <head>
        <link type="text/css" rel="stylesheet" href="/stylesheets/base.css" />
    </head>
    <body>
        <form action="/chooseCommunityToManage" method="post">
            {% if communities %}
                Which community do you want to manage?
                <div><select name="community_key" size=5>
                {% for community in communities %}
                    <option value="{{ community.key }}">{{ community.name }}</option>
                {% endfor %}
                </select></div>
                <div><input type="submit" value="Manage Selected Rakontu Community"></div>
            {% else %}
                You are not a manager or owner in any communities.
            {% endif %}
        </form>
    <a href="{{ url }}">{{ url_linktext }}</a>
    <p><a href="/">Main page</a>
    </body>
</html>

# ------------------------ NOT USING - was chooseCommunityToVisit.html

<html>
    <head>
        <link type="text/css" rel="stylesheet" href="/stylesheets/base.css" />
    </head>
    <body>
        <form action="/chooseCommunityToVisit" method="post">
            {% if communities %}
                Which community do you want to visit?
                <div><select name="community_key" size=5>
                {% for community in communities %}
                    <option value="{{ community.key }}">{{ community.name }}</option>
                {% endfor %}
                </select></div>
                <div><input type="submit" value="Visit Selected Rakontu Community"></div>
            {% else %}
                You are not a member of any communities.
            {% endif %}
        </form>
    <a href="{{ url }}">{{ url_linktext }}</a>
    <p><a href="/">Main page</a>
    </body>
</html>

# ---------------------- NOT USING - was manageCommunity.html

<html>
    <head>
        <link type="text/css" rel="stylesheet" href="/stylesheets/base.css" />
    </head>
    <body>
        You are {{ current_user.nickname }}<p>
          <p>Options for managing the community "{{ community.name|escape }}" are:<p>
          <a href="/manageCommunity_Members">Memberships</a><p>
          <a href="/manageCommunity_Settings">Settings</a><p>
          <a href="/manageCommunity_Questions">Questions</a><p>
          <a href="/manageCommunity_Personifications">Personifications</a><p>
          <a href="/manageCommunity_Technical">Backup</a><p>
    <a href="{{ url }}">{{ url_linktext }}</a>
    </body>
    <p><a href="/">Main page</a>
</html>

# --------------------- NOT USING - was notLoggedIn.html

<html>
    <head>
        <link type="text/css" rel="stylesheet" href="/stylesheets/base.css" />
    </head>
    <body>
    Welcome to Rakontu! 
    <p>
    You are not logged in. Log in to your Google account to proceed.
    <a href="{{ url }}">{{ url_linktext }}</a>
    </body>
</html>


