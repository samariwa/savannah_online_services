import boto3
from app import app
from botocore.exceptions import ClientError

def fetch_backups_list():
    s3 = boto3.client('s3')
    session = boto3.Session(
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    )
    bucket_name = 'symphafresh-system-backup'
    s3 = session.client('s3')
    bucket = s3.list_objects_v2(Bucket=bucket_name)
    try:
        if bucket.get('Contents'):
            return [{'Name': file['Key'], 'Size': ("{:.2f}".format(file['Size']/1048576)) , 'LastModified': file['LastModified']} for file in bucket['Contents']]
        else:
            return []
    except ClientError as e:
        app.logger.error(f"Unexpected {e=}")
        return False