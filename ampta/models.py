from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

# Login form 
class LoginForm(forms.Form):
	username = forms.CharField(max_length = 30)
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput)

# Login form 
class SearchForm(forms.Form):
	search = forms.CharField(max_length = 30)

# Create your models here.
class Status(models.Model):
	name = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.name

class Project(models.Model):
	users = models.ManyToManyField(User, related_name="project_users")
	owner = models.ForeignKey(User, related_name="project_owner")
	name = models.CharField(max_length=80)
	description = models.CharField(max_length=2500)
	start_date = models.DateField()
	end_date = models.DateField()
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.name

	def is_owner(self, user):
		return self.owner == user

	def is_member(self, user):
		if user in self.users.all() or self.owner == user:
			return True
		else:
			return False

class Ticket(models.Model):
	status = models.ForeignKey(Status, related_name="ticket_status")
	project = models.ForeignKey(Project, related_name="tickets")
	owner = models.ForeignKey(User, related_name="tickets")
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=2500)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.name

	def is_owner(self, user):
		return self.owner == user

class ProjectForm(ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Project
		exclude = ('owner', 'pub_date')

class TicketForm(ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Ticket
		exclude = ('owner', 'project', 'pub_date')