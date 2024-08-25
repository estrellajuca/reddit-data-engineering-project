from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY
import s3fs

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key = AWS_ACCESS_KEY_ID,
                               secret = AWS_ACCESS_KEY)
        return s3
    except Exception as ex:
        print(ex)




def create_bucket_if_not_exist(s3:s3fs.S3FileSystem, bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f'Bucket {bucket} created')
        else:
            print(f'Bucket {bucket} already exists')
    except Exception as ex:
        print(ex)

def load_to_s3(s3:s3fs.S3FileSystem, local_file_path: str, bucket:str, s3_file_name:str):
    try:
        s3.put(local_file_path, bucket+'/raw/'+s3_file_name)
        print(f'File {s3_file_name} uploaded to s3')
    except FileNotFoundError:
        print('File not found')
