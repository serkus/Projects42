from django.db import models

class TaskList(models.Model):
	def  __int__(self):
		Id = models.AutoField(primary_key=True)
		Name = models.CharField(max_length=200)
		Url = models.UrlField()
		