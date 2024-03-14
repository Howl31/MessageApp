from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserMessage(models.Model):
    user = models.ForeignKey(User, related_name='user_message', on_delete=models.DO_NOTHING, null=False, blank=False)
    msg = models.TextField(null=False, blank=False)
    scheduled_date = models.DateField(null=False, blank=False)
    scheduled_time = models.TimeField(null=False, blank=False)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.msg}"
    
