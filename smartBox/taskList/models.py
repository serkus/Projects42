from django.db import models

class TaskList(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=200)
	Url = models.CharField(max_length=200)









































































































































