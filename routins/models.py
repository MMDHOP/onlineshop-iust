import uuid
from django.db import models
from django.conf import settings
from products.models import Product

class Routine(models.Model):
    routine_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='routines')
    plan_name = models.CharField(max_length=255)
    steps = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Routine: {self.plan_name} for {self.user.username}"
