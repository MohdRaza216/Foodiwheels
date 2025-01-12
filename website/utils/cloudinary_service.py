import cloudinary
import cloudinary.uploader
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)

def upload_image(file_path_or_url, public_id=None):
    try:
        result = cloudinary.uploader.upload(file_path_or_url, public_id=public_id)
        return result.get("secure_url", None)
    except Exception as e:
        print(f"Error uploading image: {e}")
        return None
