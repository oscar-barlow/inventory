"""
Django settings for testing.

These settings extend the base settings but configure the database for testing.
"""

from .settings import *  # noqa

# Use an in-memory SQLite database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST': {
            'NAME': ':memory:',
        },
    }
}

# Disable debug for testing
DEBUG = False

# Add test-specific apps if needed
# INSTALLED_APPS += ['test_app']