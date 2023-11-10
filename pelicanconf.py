AUTHOR = 'Anthony Herrera'
SITENAME = 'Anthony Herrera'

# SITEURL = '/posts'
# OUTPUT_PATH = 'output/blog'
# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
        ('Home', '/'),
        ('Programming', '/category/programming.html'),
        ('About Me', '/pages/about-me.html')
        ]

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/')
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing

#RELATIVE_URLS = True
GOOGLE_ANALYTICS = 'G-2VE7CHY0WH'

IGNORE_FILES = ['templates']
