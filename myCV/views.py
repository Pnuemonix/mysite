from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Skill

class IndexView(generic.ListView):
	template_name = 'myCV/index.html'
	context_object_name = 'skill_list'

	def get_queryset(self):
		return Skill.objects.order_by('-title')
	