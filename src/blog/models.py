from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=120)  # max_length = required
	content = models.TextField(blank=True,null=True)
	active = models.BooleanField(default=True)

	description = models.TextField(blank=True,null=True)
	price = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10000)
	summary = models.TextField(blank=False,null=False)
	featured = models.BooleanField(default=False)     #null=True, default=True

	def get_absolute_url(self):
		# return f"/products/{self.id}/"
		return reverse("articles:article-detail",kwargs={"id":self.id})   # 这里这个my_id把我坑了好久