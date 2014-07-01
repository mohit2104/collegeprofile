from django.http import HttpResponse
from django.template import RequestContext , loader

from timeline.models import article

def index(request):
	art= article.objects.all();
	template= loader.get_template('timeline/index.html')
	context = RequestContext(request, {
		'latest_article_list' : art,
	})
	return HttpResponse(template.render(context)+str(len(art)))


