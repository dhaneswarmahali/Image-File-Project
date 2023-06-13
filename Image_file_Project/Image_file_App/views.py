from django.shortcuts import render,redirect
from django.http import HttpResponse
from Image_file_App.models import UploadedImage
from Image_file_App.forms import UploadedImageForm
from datetime import datetime
import pytesseract
from PIL import Image
import io


def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        uploaded_image = UploadedImage(image=image)
        uploaded_image.save()
        return redirect('extract_data', image_id=uploaded_image.id)
    return render(request, 'upload.html')

def extract_data(request, image_id):
    uploaded_image = UploadedImage.objects.get(id=image_id)
    
    # Open the uploaded image file using PIL
    pil_image = Image.open(uploaded_image.image)

    # Convert the PIL image to grayscale
    pil_image = pil_image.convert('L')

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(pil_image)

    # Save the extracted text to the UploadedImage model
    uploaded_image.extraction_data = extracted_text
    uploaded_image.save()

    return redirect('success')

def success(request):
    uploaded_images = UploadedImage.objects.all()
    return render(request, 'success.html', {'uploaded_images': uploaded_images})