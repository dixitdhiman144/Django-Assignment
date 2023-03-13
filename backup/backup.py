import os
import psycopg2
import boto3
from datetime import datetime

DATABASE_NAME = os.environ.get('sufofire_db')
DATABASE_USER = os.environ.get('assig_db')
DATABASE_PASSWORD = os.environ.get('sudofire_screat')
S3_BUCKET_NAME = os.environ.get('S3_SUDOFIRE_ASSIG')
AWS_ACCESS_KEY_ID = os.environ.get('AWS-SUDOFIRE-ACCESS-KEY-ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS-SUDOFIRE-SECRET-ACCESS-KEY')

def backup_database():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD)

    # Create a backup of the database
    backup_file_name = f'{DATABASE_NAME}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.dump'
    with open(backup_file_name, 'w') as f:
        conn.dump(f)

    # Upload the backup to AWS S3
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.upload_file(backup_file_name, S3_BUCKET_NAME, backup_file_name)

    # Close the database connection
    conn.close()
