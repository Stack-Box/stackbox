from client.s3 import S3Client
from config.config import Config


class S3Handler:

    def __init__(self, aws_access_key_id, aws_secret_access_key, bucket, region):
        self.s3_client = S3Client(aws_access_key_id, aws_secret_access_key, bucket, region)
        self.bucket = bucket

    def s3_object_list(self):
        res = dict()
        try:
            keys = self.s3_client.get_s3_keys(self.bucket)
            if not isinstance(keys, str):
                if len(keys) > 0:
                    res["s3 objects"] = keys
                else:
                    res["error"] = "No objects in bucket"
            else:
                res["s3 objects"] = keys
        except:
            res["error"] = "Connection failed"
        return res

    def get_object(self, object_key):
        res = dict()
        res["url"] = self.s3_client.get_presigned_url(object_key)
        return res
