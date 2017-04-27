from py_s3_cache import Cache
from moto import mock_s3
import boto3
import unittest
import time

class CacheTests(unittest.TestCase):

    @mock_s3
    def test_simple_cache(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        thing = {1:2, 'a':'b'}
        cache.set('key',thing)
        assert cache.get('key') == thing

    @mock_s3
    def test_string_cache(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        thing = 'abcdefg'
        cache.set('key',thing)
        assert cache.get('key') == thing

    @mock_s3
    def test_forwardslash_in_key(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        thing = 'abcdefg'
        cache.set('ke/y',thing)
        assert cache.get('ke/y') == thing

    @mock_s3
    def test_backslash_in_key(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        thing = 'abcdefg'
        cache.set('ke\y',thing)
        assert cache.get('ke\y') == thing

    @mock_s3
    def test_space_in_key(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        thing = 'abcdefg'
        cache.set('ke y',thing)
        assert cache.get('ke y') == thing

    @mock_s3
    def test_nonexistent_key_returns_none(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        assert cache.get('doesntexist') == None

    @mock_s3
    def test_expired_key_returns_none(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        cache.set('expiredkey','stringtocache',3)
        time.sleep(4)
        assert cache.get('expiredkey') == None

    @mock_s3
    def test_expired_key_before_expiration_time(self):
        #### Create mocked Bucket #####
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        cache = Cache('mybucket','prefix1')
        cache.set('expiredkey2','stringtocache',30)
        time.sleep(4)
        assert cache.get('expiredkey2') == 'stringtocache'

