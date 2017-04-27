import boto3
import botocore
import pickle
import arrow

class Cache(object):
    bucket = None
    prefix = None
    s3 = None

    def __init__(self, bucket, prefix):
        self.s3 = boto3.resource('s3')
        self.bucket = bucket
        self.prefix = prefix

    def get(self, key):
        """
        Get an item from the cache.
        """
        obj = self.s3.Object(self.bucket,self.prefix + '/' + key)

        try:
            pickled = obj.get()['Body'].read()
        except botocore.exceptions.ClientError as e:
            return None

        data = pickle.loads(pickled)

        if arrow.utcnow() > arrow.get(data['expires_at']):
            return None
        else:
            return data['value']

    def set(self, key, value, ttl=None):
        """
        Save an item to the cache.  It expires after ttl seconds.  ttl=None implies forever.
        """
        obj = self.s3.Object(self.bucket,self.prefix + '/' + key)

        if ttl:
            expires_at = str( arrow.utcnow().replace(seconds=ttl) )
        else:
            expires_at = str( arrow.utcnow().replace(years=100) )

        data = {
            "value": value,
            "expires_at": expires_at
        }
        obj.put(Body=pickle.dumps(data))
