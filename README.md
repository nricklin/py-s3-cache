# py-s3-cache
Super minimal python S3 cache

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
