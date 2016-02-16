from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.body

		
class Comment(models.Model):
	body = models.TextField()
	user = models.OneToOneField(User)
	message = models.ForeignKey(Message)

	def __unicode__(self):
		return str(self.user)