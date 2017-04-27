# py-s3-cache
Super minimal python S3 cache

[![PyPI version](https://badge.fury.io/py/py-s3-cache.svg)](https://badge.fury.io/py/py-s3-cache) 
[![Build Status](https://travis-ci.org/nricklin/py-s3-cache.svg?branch=master)](https://travis-ci.org/nricklin/py-s3-cache)
[![codecov](https://codecov.io/gh/nricklin/py-s3-cache/branch/master/graph/badge.svg)](https://codecov.io/gh/nricklin/py-s3-cache)

# Installation
```
pip install py-s3-cache
```

# Example
```python
from py_s3_cache import Cache

cache = Cache('<bucket>','<prefix>')

# cache something for an hour
cache.set(key, value, 3600)

# get something out of the cache
value = cache.get(key)
if not value:
    print "didn't find it in the cache"
```
