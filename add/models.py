# # add/models.py

# from django.db import models
# import random
# import string

# def generate_short_code():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# class UrlModel(models.Model):
#     title = models.CharField(max_length=100)
#     original_url = models.URLField()
#     short_url = models.CharField(max_length=10, unique=True, blank=True)
# class Meta:
#     db_table = 'add_url' 

#     def save(self, *args, **kwargs):
#         if not self.short_url:
#             self.short_url = generate_short_code()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.title} - {self.short_url}"



# from django.contrib.auth.models import User
# from django.db import models
# import random
# import string

# def generate_short_code():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# class UrlModel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=100)
#     original_url = models.URLField()
#     short_url = models.CharField(max_length=10, unique=True, blank=True)

#     class Meta:
#         db_table = 'add_url'
    
#     class Meta:
#         db_table = 'add_url_model'

#     def save(self, *args, **kwargs):
#         if not self.short_url:
#             self.short_url = generate_short_code()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.title} - {self.short_url}"


# from django.db import models
# from django.contrib.auth.models import User

# class Url(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     url = models.URLField()

#     def __str__(self):
#         return self.url




from django.contrib.auth.models import User
from django.db import models
import random
import string
from django.utils import timezone


def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class UrlModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table = 'add_url_model'  # Use only one Meta class

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.short_url}"







