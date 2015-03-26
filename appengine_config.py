"""`appengine_config` gets loaded when starting a new application instance."""
from google.appengine.ext import vendor

# insert `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions.
vendor.add('lib')
