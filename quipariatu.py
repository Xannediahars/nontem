from django.contrib import messages
from sea_view.models import Notification

def my_view(request):
    # ...
    notification = Notification.objects.create(
        recipient=request.user,
        notification_type='email',
        notification_subtype='welcome',
    )
    sea_view.send_notification(notification)
    # ...
