from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.
class POST(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255, unique=True)
	summary = models.CharField(max_length=300)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	images = models.ImageField(upload_to='img',blank=True,null=True) #anytime after add a new field , need to do migrate- python ./manage.py makemigrations, ...migrate

	class Meta:
		ordering = ['-created']

		def __unicode__(self):
			return u'%s'% self.title

	def get_absolute_url(self):
			return reverse('blog.views.post',args=[self.slug])

#then do migration to connect with database
