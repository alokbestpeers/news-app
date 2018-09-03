from django.db import models
from django.utils.text import Truncator


class News(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=10000)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def shortContent(self):
		shortContent = Truncator(self.content)
		return shortContent.chars(100)



