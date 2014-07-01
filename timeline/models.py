from django.db import models

class tag(models.Model):
        tag_name=models.CharField(max_length=100)

        def __str__(self):
                return self.tag_name


class article(models.Model):
        title=models.CharField(max_length=100)
        content=models.CharField(max_length=500)
	tags=models.ManyToManyField(tag)
        def __str__(self):
                return self.title






