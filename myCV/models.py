from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CV(models.Model):
	name = models.CharField(max_length=120, blank=False)
	address = models.CharField(max_length=120)
	phone = models.CharField(max_length=20)
	email = models.EmailField()
	homepage = models.URLField()
	career_goal = models.TextField()
	nationality = models.CharField(max_length=120)
	interests = models.CharField(max_length=120)

	def __str__(self):
		return self.name

SKILL_TYPE = (
	('business', 'Business'),
	('technical', 'Technical'),
)

SKILL_LEVEL = (
	('beginner', 'Beginner'),
	('intermediate', 'Intermediate'),
	('expert', 'Expert'),
)

class Skill(models.Model):
	title = models.CharField(max_length=120, unique=True, blank=False)
	description = models.CharField(max_length=120)
	skill_type = models.CharField(max_length=120, choices=SKILL_TYPE)
	level = models.CharField(max_length=120, choices=SKILL_LEVEL)

	def __str__(self):
		return self.title

JOB_TYPE = (
	('parttime', 'Part Time'),
	('fulltime', 'Full Time'),
	('contract', 'Contract'),
	('temporary', 'Temp'),
	('voluntary', 'Volunteer'),
)

class Job(models.Model):
	role = models.CharField(max_length=120, blank=False)
	employer = models.CharField(max_length=120, blank=False)
	location = models.CharField(max_length=120)
	job_type = models.CharField(max_length=120, choices=JOB_TYPE, default='fulltime')
	current_job = models.BooleanField(default=False)
	start_date = models.DateField(auto_now_add=False, auto_now=False)
	end_date = models.DateField(auto_now_add=False, auto_now=False)
	job_skills = models.ManyToManyField('Skill')

	def __str__(self):
		return "Job: %s, for %s"%(self.title, self.role)

class Achievement(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	achieve_text = models.TextField(blank=False)

	def __str__(self):
		return self.achieve_text

class Education(models.Model):
	course_name = models.CharField(max_length=120, blank=False)
	course_text = models.CharField(max_length=120)
	course_date_completed = models.DateField(auto_now_add=False, auto_now=False)

	def __str__(self):
		return self.course_name

	