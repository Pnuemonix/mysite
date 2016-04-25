from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Skill

# class IndexView(generic.ListView):
# 	template_name = 'myCV/skills.html'
# 	context_object_name = 'skill_list'

# 	def get_queryset(self):
# 		return Skill.objects.order_by('-title')

# 	def skills(request):
# 	skills = Product.objects.all()
# 	context = {'products': products}
# 	template = 'products/all.html'	
# 	return render(request, template, context)
	
def all_skills(request):
	skills = Skill.objects.all()
	context = {'skills': skills}
	template = 'myCV/skills.html'	
	return render(request, template, context)
	