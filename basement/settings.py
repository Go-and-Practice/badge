# -*- coding: utf-8 -*-
import os

from redis import Redis

PYPI_URL = "https://pypi.python.org/pypi/%s/json"
SHIELD_URL = "http://img.shields.io/badge/%s-%s-%s.%s"
# SHIELD_URL = "http://localhost:9000/badge/%s-%s-%s.%s"  # pypip.in uses a local version of img.shields.io
FILE_CACHE = "/tmp/badge.py/"
CACHE_TIME = (60 * 60) * 24  # 24 hours
REDIS_EXPIRE = 60 * 10  # 10 minutes
BASE_DIR = PROJECT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir)
)

STATIC_DIR = os.path.join(BASE_DIR, 'static/')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates/')

redis = Redis()
