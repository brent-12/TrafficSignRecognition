from google_images_download import google_images_download

# Create an instance of the class
response = google_images_download.googleimagesdownload()

# Define search arguments
arguments = {
    "keywords": "stop sign",
    "limit": 100,  # Number of images to download
    "output_directory": "./stop_signs",  # Save images in this folder
    "format": "jpg",
    "type": "photo",
    "size": ">400x300",  # Optional: Filter by size
}

# Download images
response.download(arguments)