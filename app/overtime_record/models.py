from django.db import models


class OvertimeRecord(models.Model):
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.reason