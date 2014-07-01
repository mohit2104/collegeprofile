from django.db import models
from django.contrib.auth.models import User
import datetime

class Branch(models.Model):
	branch_name=models.CharField(max_length=100)
	def __unicode__(self):
		return self.branch_name

class Student(models.Model):
	student=models.ForeignKey(User)
	branch=models.ForeignKey(Branch)
	date_of_birth=models.DateTimeField('dat of birth')
	def __unicode__(self):
		return self.student.username

class Custom_data(models.Model):
	student=models.ForeignKey(User)
	field=models.CharField(max_length=100)
	value=models.CharField(max_length=500)
	def __unicode__(self):
		return self.student.username+' - '+self.field


class Subscriber(models.Model):
	student=models.ForeignKey(User,related_name="user")
	subscriber=models.ForeignKey(User, related_name="subscriber")
	TYPE = (('a','ALL') , ('t','TIMELINE') , ('b','BLOG'))
  	type = models.CharField(max_length=1 , choices=TYPE ,	default = 'a')

	class Meta:
		unique_together = ('student' , 'subscriber')
  
	def __unicode__(self):
		return self.student.email+' '+self.subscriber.email+' '+self.type

class Tag(models.Model):
	tag_name = models.CharField(max_length=30)

class Article(models.Model):
	user=models.ForeignKey(User)
	heading=models.CharField(max_length=100)
	content=models.TextField()
	upload=models.DateTimeField(default=datetime.datetime.now())
	edited=models.DateTimeField()
	tags=models.ManyToManyField(Tag)

	
