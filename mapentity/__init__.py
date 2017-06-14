from __future__ import unicode_literals

from .registry import Registry
from .settings import app_settings

__all__ = ['app_settings', 'registry']

registry = Registry()
