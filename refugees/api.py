from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from refugees.models import Record

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		filtering = {
			'username': ALL,
		}

class RecordResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')

	class Meta:
		queryset = Record.objects.all()
		resource_name = 'record'
		authorization = Authorization()
		filtering = {
			'user': ALL_WITH_RELATIONS,
		}
