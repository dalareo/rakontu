# --------------------------------------------------------------------------------------------
# RAKONTU
# Description: Rakontu is open source story sharing software.
# Version: pre-0.1
# License: GPL 3.0
# Google Code Project: http://code.google.com/p/rakontu/
# --------------------------------------------------------------------------------------------

from visit import *
from create import *
from help import *
from manage import *
from admin import *

application = webapp.WSGIApplication(
									 [('/', StartPage),
									  
									  # visiting
									  ('/visit', BrowseEntriesPage),
									  ('/visit/', BrowseEntriesPage),
									  ('/visit/look', BrowseEntriesPage),
									  ('/visit/read', ReadEntryPage),
									  ('/visit/readAnnotation', ReadAnnotationPage),
									  
									  ('/visit/members', SeeCommunityMembersPage),
									  ('/visit/member', SeeMemberPage),
									  ('/visit/character', SeeCharacterPage),
									  ('/visit/community', SeeCommunityPage),
									  ('/visit/new', NewMemberPage),
									  ('/visit/profile', ChangeMemberProfilePage),
									  ('/visit/help', GetHelpPage),
									  
									  # entering entries
									  ('/visit/story', EnterEntryPage),
									  ('/visit/retell', EnterEntryPage),
									  ('/visit/remind', EnterEntryPage),
									  ('/visit/respond', EnterEntryPage),
									  ('/visit/pattern', EnterEntryPage),
									  ('/visit/collage', EnterEntryPage),
									  ('/visit/invitation', EnterEntryPage),
									  ('/visit/resource', EnterEntryPage),
									  ('/visit/entry', EnterEntryPage),
									  
									  # answering questions
									  ('/visit/answers', AnswerQuestionsAboutEntryPage),
									  ('/visit/preview', PreviewPage),
									  ('/visit/previewAnswers', PreviewPage),
									  
									  # entering annotations
									  ('/visit/request', EnterAnnotationPage),
									  ('/visit/tagset', EnterAnnotationPage),
									  ('/visit/comment', EnterAnnotationPage),
									  ('/visit/nudge', EnterAnnotationPage),
									  ('/visit/annotation', EnterAnnotationPage),
									  
									  # entering links
									  ('/visit/relate', RelateEntryPage),
									  
									  # helping roles
									  ('/visit/curate', ReadEntryPage),
									  ('/visit/flag', FlagOrUnflagItemPage),
									  ('/curate', CurateFlagsPage),
									  ('/curate/', CurateFlagsPage),
									  ('/curate/flags', CurateFlagsPage),
									  ('/curate/gaps', CurateGapsPage),
									  ('/curate/attachments', CurateAttachmentsPage),
									  ('/curate/tags', CurateTagsPage),
									  ('/guide/', ReviewResourcesPage),
									  ('/guide', ReviewResourcesPage),
									  ('/guide/resource', EnterEntryPage),
									  ('/guide/resources', ReviewResourcesPage),
									  ('/guide/requests', ReviewRequestsPage),
									  ('/liaise/', ReviewOfflineMembersPage),
									  ('/liaise', ReviewOfflineMembersPage),
									  ('/liaise/batch', BatchEntryPage),
									  ('/liaise/review', ReviewBatchEntriesPage),
									  ('/liaise/members', ReviewOfflineMembersPage),
									  
									  # managing
									  ('/createCommunity', CreateCommunityPage),
									  ('/manage', ManageCommunitySettingsPage),
									  ('/manage/', ManageCommunitySettingsPage),
									  ('/manage/members', ManageCommunityMembersPage),
									  ('/manage/settings', ManageCommunitySettingsPage),
									  ('/manage/questions_list', ManageCommunityQuestionsListPage),
									  ('/manage/questions_story', ManageCommunityQuestionsPage),
									  ('/manage/questions_pattern', ManageCommunityQuestionsPage),
									  ('/manage/questions_collage', ManageCommunityQuestionsPage),
									  ('/manage/questions_invitation', ManageCommunityQuestionsPage),
									  ('/manage/questions_resource', ManageCommunityQuestionsPage),
									  ('/manage/questions_member', ManageCommunityQuestionsPage),
									  ('/manage/questions_character', ManageCommunityQuestionsPage),
									  ('/manage/questions_questions', ManageCommunityQuestionsPage),
									  ('/manage/characters', ManageCommunityCharactersPage),
									  ('/manage/character', ManageCommunityCharacterPage),
									  ('/manage/technical', ManageCommunityTechnicalPage),
									  
									  # general result handler
									   ('/result', ResultFeedbackPage),
									  
									  # file handlers
									  ('/img', ImageHandler),
									  ('/visit/img', ImageHandler),
									  ('/manage/img', ImageHandler),
									  ('/visit/attachment', AttachmentHandler),
									  
									  # site admin
									  ('/admin/showAllCommunities', ShowAllCommunities),
									  ('/admin/showAllMembers', ShowAllMembers),
									  ('/admin/generateSystemQuestions', GenerateSystemQuestionsPage),
									  ('/admin/generateHelps', GenerateHelpsPage),
									  ('/admin/generateSystemResources', GenerateSystemResourcesPage),
									  ],
									 debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
