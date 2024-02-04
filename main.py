import boto3
import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

s3 = boto3.resource(
    service_name="s3",
    endpoint_url=os.getenv("ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("REGION_NAME"),
)

stickers_bucket = s3.Bucket(os.getenv("BUCKET_NAME"))

sticker_name = input("Введите название стикера после /stickers/ без слэшей: ")
count = int(input("Сколько стикеров написано на странице?: "))
object_name = input("Как назовёте объект в хранилище?: ")

sticker_data = "https://chpic.su/_data/stickers/" + sticker_name[0].lower() + '/' + sticker_name + '/' + sticker_name + '_'
def upload(object_name, content, number):
    print(stickers_bucket.put_object(
        ACL="public-read",
        Key=object_name + "/default/" + str(number) + '.webp',
        Body=content,
    ))

for i in range(count):
    i += 1

    if i < 10:
        id = "00" + str(i)
    elif i >= 10:
        id = "0" + str(i)
    else:
        id = str(id)

    content = requests.get(sticker_data + id + ".webp").content
    upload(object_name, content, i)
