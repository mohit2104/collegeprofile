from django.contrib.auth.models import User
from django.template import RequestContext , loader
from django.http import HttpResponse
import json

def register(request , **kwargs):
	if request.method == 'POST':
		try:
			passwd=request.POST['password']
			email = request.POST['email']
			username = request.POST['roll_no']
			user=User.objects.create_user(username,email,passwd)
			user.save()
			return HttpResponse('user saved')			
		except Exception as e:
			response_data={}
			response_data['status']='failed'
			response_data['msg']=str(e)
			return HttpResponse(json.dumps(response_data),content_type="application/json")

	template=loader.get_template('new/index.html')
	context=RequestContext(request, {})
	return HttpResponse(template.render(context))


