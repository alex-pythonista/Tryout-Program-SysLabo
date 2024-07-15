from django.db import models


class BaseModel(models.Model):
    """
        Base model for inheritting common fields
    """
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True