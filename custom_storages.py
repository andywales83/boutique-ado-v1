from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storages


class StaticStorage(S3Boto3Storage):
    loacation = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    loacation = settings.MEDIAFILES_LOCATION