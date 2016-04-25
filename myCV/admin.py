from django.contrib import admin

from .models import CV, Achievement, Job, Skill, Education

class AchievementInline(admin.TabularInline):
	model = Achievement
	extra = 3

class JobAdmin(admin.ModelAdmin):
	fieldsets = [
		('Job Information', {'fields': ['role', 'employer', 'location', 'job_type', 'current_job']}),
		('Date Information', {'fields': ['start_date', 'end_date']}),
		('Job Skills', {'fields': ['job_skills']}),
	]
	inlines = [AchievementInline]
	list_display = ('role', 'employer', 'location', 'end_date')
	list_filter = ['start_date']

admin.site.register(Job, JobAdmin)
admin.site.register(CV)
admin.site.register(Skill)
admin.site.register(Education)