import boto3
from botocore.exceptions import ClientError
from app import app
from flask import send_file

def download_backup_file(object_name):
    s3 = boto3.client('s3')
    session = boto3.Session(
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    )
    bucket_name = 'symphafresh-system-backup'
    s3 = session.client('s3')
    # Filename - File to download
    # Bucket - Bucket to download from (the top level directory under AWS S3)
    # Filepath - The local path to download the file to
    try:
        #s3.download_file(bucket_name, object_name, f"{file_path}backup_data_{object_name}")

        # Get the S3 object and its metadata
        s3_object = s3.get_object(Bucket=bucket_name, Key=object_name)
        content_type = s3_object['ContentType']

        # Send the file directly to the client
        return send_file(
            s3_object['Body'],
            as_attachment=True,
            download_name=f"backup_data_{object_name}",
            mimetype=content_type
        )
    except ClientError as e:
        app.logger.error(f"Unexpected {e=}")
        return False