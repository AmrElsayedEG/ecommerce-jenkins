from django.db import models

class AppVersion(models.Model):
    version = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Version: {self.version} - Date: {self.date}"