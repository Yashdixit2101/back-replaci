from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.conf import settings
import boto3
import uuid
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if 'image' not in request.FILES:
            return Response({"error": "No image file provided"}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES['image']
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )

        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        unique_file_key = f"uploads/{uuid.uuid4().hex}_{image.name}"

        try:
            s3_client.upload_fileobj(
                image,
                bucket_name,
                unique_file_key,
                ExtraArgs={"ACL": "public-read", "ContentType": image.content_type}
            )
            file_url = f"https://{bucket_name}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{unique_file_key}"

            uploaded_image = UploadedImage.objects.create(image_url=file_url)
            serializer = UploadedImageSerializer(uploaded_image)
            return Response({"message": "Upload successful", "data": serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImageListView(APIView):
    def get(self, request, *args, **kwargs):
        images = UploadedImage.objects.all()
        serializer = UploadedImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ImageDeleteView(APIView):
    def delete(self, request, image_id, *args, **kwargs):
        try:
            image = UploadedImage.objects.get(id=image_id)
            s3_client = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_S3_REGION_NAME,
            )
            file_key = image.image_url.split('/')[-1]
            s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_key)
            image.delete()
            return Response({"message": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except UploadedImage.DoesNotExist:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)