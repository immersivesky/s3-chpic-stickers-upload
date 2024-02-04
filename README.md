# Что это?

Я решил написать небольшой скрипт, который позволит мне переносить стикеры из CHPic в S3 хранилище VK Cloud.

# Как запустить?

Требования:
- Python3 (у меня 3.11)
- установленные библиотеки (pip install boto3)
- S3 хранилище (у меня "бесплатное" в VK Cloud)

1. Меняем значения в .env на свои, пример в .env.example
2. Пишем "python3 main.py"
3. Вводим запрашиваемые данные
4. Профит!

Могут быть ошибки. В Python3 пока разбираюсь хуёва.

# Источники

Отсюда брал инфу:
- https://habr.com/ru/articles/210238
- https://www.gormanalysis.com/blog/connecting-to-aws-s3-with-python
- https://www.radishlogic.com/aws/s3/how-to-upload-a-local-file-to-s3-bucket-using-boto3-and-python
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object.html
- https://all-python.ru/osnovy/os.html
- https://habr.com/ru/articles/472674
