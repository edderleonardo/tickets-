from .settings import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = 'django-insecure-test-key-do-not-use-in-production'

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# DEBUGGING FOR TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['debug'] = True  # type: ignore # noqa: F405

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = 'http://media.testserver'

# DATABASE
# ------------------------------------------------------------------------------
# Use a faster test database
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'test_db.sqlite3'}}


# Disable migrations for tests
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# Disable DEBUG for tests
DEBUG = False

# Your additional test-specific settings...
