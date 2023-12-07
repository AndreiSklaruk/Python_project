import uuid
from datetime import timedelta
from django.utils.timezone import now
from celery import shared_task
from users.models import User, EmailVerification


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(user=user, expiration=expiration, code=uuid.uuid4())
    record.send_verification_email()