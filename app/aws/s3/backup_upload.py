from botocore.exceptions import ClientError
from app import app
import boto3

def upload_backup_file(file_path, object_name):
    session = boto3.Session(
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    )
    bucket_name = 'symphafresh-system-backup'
    s3 = session.resource('s3')
    # Filename - File to upload
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    # Key - S3 object name (can contain subdirectories). If not specified then file_name is used
    try:
        s3.meta.client.upload_file(Filename=file_path, Bucket=bucket_name, Key=object_name)
        return f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
    except ClientError as e:
        app.logger.error(f"Unexpected {e=}")
        return False