from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
