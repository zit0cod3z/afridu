# import qrcode
# import base64
# from io import BytesIO

# def generate_qr_code(data):
#     # Create a string to embed in the QR code
#     qr_data = f"Name: {data['name']}, Nationality: {data['nationality']}, Date of Birth: {data['dob']}, Country: {data['country']},  Email: {data['email']}, Attachment: {data['attachment']}, Organization: {data['organization']}, Position: {data['position']}, Event: {data['event']}, Submitted: {data['submitted_at']}"
    
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,  # Adjust this value for size
#         border=4,  # Adjust this value for border size
#     )
#     qr.add_data(qr_data)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#     buffer = BytesIO()
#     img.save(buffer, format='PNG')
#     return base64.b64encode(buffer.getvalue()).decode()

import os 
import qrcode
import base64
from django.conf import settings
from io import BytesIO
from .models import *

def generate_qr_code(qr_data, filename):
    qr_data = f"Name: {qr_data['name']}, Nationality: {qr_data['nationality']}, Date of Birth: {qr_data['dob']}, Country: {qr_data['country']},  Email: {qr_data['email']}, Attachment: {qr_data['attachment']}, Organization: {qr_data['organization']}, Position: {qr_data['position']}, Event: {qr_data['event']}, Submitted: {qr_data['submitted_at']}"

    qr = qrcode.QRCode(
        version=1,  # Adjust version for size; higher numbers increase size
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
        # Save to a file for testing
    # img.save("test_qr_code.png")
    # Save the image to a BytesIO object
    # Save the image to the media directory
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    img.save(file_path)

    return file_path  # Return the path to the saved file