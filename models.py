import uuid

from django.db import models


class AuthService(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class AuthClient(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    client_name = models.CharField(max_length=255, db_index=True)
    ip_address = models.GenericIPAddressField(db_index=True)
    enabled = models.BooleanField(default=False, db_index=True)

    service = models.ForeignKey(AuthService, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name




