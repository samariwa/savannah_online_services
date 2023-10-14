from botocore.exceptions import ClientError
from app import app
from app.response import respond
import boto3

def delete_backup_file(object_name):
    session = boto3.Session(
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    )
    bucket_name = 'symphafresh-system-backup'
    s3 = session.resource('s3')
    # object_name - S3 object name (can contain subdirectories)
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    try:
        s3.Object(bucket_name, object_name).delete()
        return respond('200')
    except ClientError as e:
        app.logger.error(f"Unexpected {e=}")
        return False
    return True