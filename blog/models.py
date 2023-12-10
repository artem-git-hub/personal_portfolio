from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	descriprion = models.TextField()

	def __str__(self):
		return self.title