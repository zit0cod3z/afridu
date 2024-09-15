from django.shortcuts import render, redirect
from django.http import HttpResponse
from afridu_app.models import Registration
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import *
from .utils import generate_qr_code
import base64
from io import BytesIO
import os
import qrcode
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

def register(request):
	if request.method == "POST":
		name = request.POST.get("name")
		nationality = request.POST.get("nationality")
		country = request.POST.get("country")
		dob = request.POST.get("dob")
		email = request.POST.get("email")
		attachment= request.FILES.get("attachment")
		organization = request.POST.get("organization")
		position = request.POST.get("position")
		event = request.POST.get("event")
		instance = Registration(name=name, nationality=nationality, country=country, dob=dob, email=email, attachment=attachment, organization=organization, position=position, event=event)
		user_data = Registration.objects.create(name=name, nationality=nationality, country=country, dob=dob, email=email, attachment=attachment, organization=organization, position=position, event=event)
		# qr = Registration.objects.get(id=qr_id)
		qr_code_data = {'name': user_data.name, 'nationality': user_data.nationality, 'country': user_data.country, 'dob': user_data.dob, 'email': user_data.email, 'attachment': user_data.attachment, 'organization': user_data.organization, 'position': user_data.position, 'event': user_data.event, 'submitted_at': user_data.submitted_at}
		filename = f"qr_code.png"
		qr_code_path = generate_qr_code(qr_code_data, filename)
		# qr_code_url = f"http://{'127.0.0.1:8000'}{settings.MEDIA_URL}{filename}"
		current_site = get_current_site(request)
		if settings.DEBUG:
			qr_code_url = f"http://{current_site.domain}{settings.MEDIA_URL}{filename}"
		else:
			qr_code_url = f"https://afridu-registration.onrender.com{settings.MEDIA_URL}{filename}"
		instance.save()

		# mail = EmailMessage(
		# 	'AFRIDU REGISTRATION CONFIRMATION',
		# 	f'Hello {name}, \n  Thank you for registering to attend the upcoming AFRIDU HOMECOMING Event in Abuja, Nigeria. Scheduled to take place from 17th to 27th October 2024.\n Please note: Your visitor pass will be emailed to you the week before the event. Please ensure you bring it to registration on arrival with a form of identification. \n AFRIDU Office Address: 13B, Mambila Street off Aso Drive, Abuja.\n  Please note that only VIP delegate pass holders will be permitted to attend all events premises.\n We look forward to welcoming you to the HOMECOMING EVENT October 16th to 27th 2024 INTERNATIONAL GATHERING IN HONOUR OF AFRICAN DESCENDANTS IN DIASPORA \n .............................................................\n Yours In Nation Building Arch. Prof, Chidiebere Analechi Ogbu AFRIDU President\n ................................................................\n For Delegate, Sponsorship and Exhibition Opportunities please contact: Diplomatic Administrator Dr.Breakforth Onwubuya on +234 803 349 4643 or email AFRIDU.ORG \n Get the latest updates afridu.org.',
		# 	settings.EMAIL_HOST_USER,
		# 	[email]

		# )
		my_subject = "AFRIDU REGISTRATION CONFIRMATION"
		my_recipient = email
		mailer = settings.EMAIL_HOST_USER
		welcome_message = name


		html_message = render_to_string("afridu_app/email.html", {"name": user_data.name, "nationality": user_data.nationality, "country": user_data.country, "dob": user_data.dob, "email": user_data.email, "attachment": user_data.attachment, "organization": user_data.organization, "position": user_data.position, "event": user_data.event, "submitted_at": user_data.submitted_at, "qr_code_url": qr_code_url})
		plain_message = strip_tags(html_message)

		message = EmailMultiAlternatives(
			subject = my_subject,
			body = plain_message,
			from_email = mailer,
			to = [my_recipient],
		)

		message.attach_alternative(html_message, "text/html")
		message.send()
		return render(request, 'afridu_app/thanks.html')


	return render(request, 'afridu_app/index.html')

def thanks(request):
	return render(request, 'afridu_app/thanks.html')
