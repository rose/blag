# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

#!! This is the configuration of Nikola. !!#
#!!  You should edit it to your liking.  !!#


# Data about this site
BLOG_AUTHOR = "Rose Ames"
BLOG_TITLE = "Superluser"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://rose.github.io/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
BASE_URL = "http://rose.github.io/"
BLOG_EMAIL = "rose@happyspork.com"
BLOG_DESCRIPTION = "# sudo man sudo"

DEFAULT_LANG = "en"
TRANSLATIONS = { DEFAULT_LANG: "", }
TRANSLATIONS_PATTERN = "{path}.{ext}.{lang}"
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/archive.html', 'Archives'),
        ('/categories/index.html', 'Tags'),
        ('/rss.xml', 'RSS'),
    ),
}

# Below this point, everything is optional

POSTS = (
("posts/*.rst", "posts", "post.tmpl"),
("posts/*.txt", "posts", "post.tmpl"),
)
PAGES = (
("stories/*.rst", "stories", "story.tmpl"),
("stories/*.txt", "stories", "story.tmpl"),
)

COMPILERS = {
"rest": ('.rst', '.txt'),
"markdown": ('.md', '.mdown', '.markdown'),
"textile": ('.textile',),
"txt2tags": ('.t2t',),
"bbcode": ('.bb',),
"wiki": ('.wiki',),
"ipynb": ('.ipynb',),
"html": ('.html', '.htm'),
}

THEME = "bootdark"
# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
CODE_COLOR_SCHEME = 'friendly'
EXTRA_HEAD_DATA = "<link rel=\"stylesheet\" type=\"text/css\" href=\"http://fonts.googleapis.com/css?family=Droid+Sans|Droid+Sans+Mono\">"

COMMENT_SYSTEM = "disqus"
COMMENT_SYSTEM_ID = "superluser"

INDEX_TEASERS = True
# READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

LICENSE = ""

CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year,
                                       license=LICENSE)

STRIP_INDEXES = True
PRETTY_URLS = True

DEPLOY_DRAFTS = False

SCHEDULE_RULE = 'RRULE:FREQ=WEEKLY;BYDAY=SU;BYHOUR=20;BYMINUTE=0;BYSECOND=0'
SCHEDULE_ALL = False
SCHEDULE_FORCE_TODAY = True

TIMEZONE = 'UTC'

LOGGING_HANDLERS = { 'stderr': {'loglevel': 'WARNING', 'bubble': True}, }

GLOBAL_CONTEXT = {}

# DEPLOY_COMMANDS = []

# FILES_FOLDERS = {'files': '' }
OUTPUT_FOLDER = 'output/'

# TAG_PAGES_ARE_INDEXES = True
# STORY_INDEX = False

# LESS_COMPILER = 'lessc'
# LESS_OPTIONS = []
# SASS_COMPILER = 'sass'
# SASS_OPTIONS = []

# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# INDEX_DISPLAY_POST_COUNT = 10

# RSS_TEASERS = True

# USE_CDN = False

# ADDITIONAL_METADATA = {}

# DISABLED_PLUGINS = ["render_galleries"]
# EXTRA_PLUGINS_DIRS = []

#SEARCH_FORM = """
#<!-- Custom search -->
#<form method="get" id="search" action="http://duckduckgo.com/"
# class="navbar-form pull-left">
#<input type="hidden" name="sites" value="%s"/>
#<input type="hidden" name="k8" value="#444444"/>
#<input type="hidden" name="k9" value="#D51920"/>
#<input type="hidden" name="kt" value="h"/>
#<input type="text" name="q" maxlength="255"
# placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
#<input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
#</form>
#<!-- End of custom search -->
#""" % SITE_URL
# 
# OR
#
#SEARCH_FORM = """
#<!-- Custom search with google-->
#<form id="search" action="http://google.com/search" method="get" class="navbar-form pull-left">
#<input type="hidden" name="q" value="site:%s" />
#<input type="text" name="q" maxlength="255" results="0" placeholder="Search"/>
#</form>
#<!-- End of custom search -->
#""" % SITE_URL
# 
# OR
#
# SEARCH_FORM = """
# <span class="navbar-form pull-left">
# <input type="text" id="tipue_search_input">
# </span>"""
#
# BODY_END = """
# <script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
# <script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
# <script type="text/javascript">
# $(document).ready(function() {
    # $('#tipue_search_input').tipuesearch({
        # 'mode': 'json',
        # 'contentLocation': '/assets/js/tipuesearch_content.json',
        # 'showUrl': false
    # });
# });
# </script>
# """

# EXTRA_HEAD_DATA = """
# <link rel="stylesheet" type="text/css" href="/assets/css/tipuesearch.css">
# <div id="tipue_search_content" style="margin-left: auto; margin-right: auto; padding: 20px;"></div>
# """
# ENABLED_EXTRAS = ['local_search']
#

# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }

