from django.db import models

# Create your models here.

class Record(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	ask = models.BigIntegerField(default=0)
	identify = models.BigIntegerField(default=0)
	diagnosis = models.BigIntegerField(default=0)
	refer = models.BigIntegerField(default=0)
	reinforce = models.BigIntegerField(default=0)
	recommend = models.BigIntegerField(default=0)
	reduce = models.BigIntegerField(default=0)
	attune = models.BigIntegerField(default=0)
	prescribe = models.BigIntegerField(default=0)
	close = models.BigIntegerField(default=0)
	burnout = models.BigIntegerField(default=0)
	def __str__(self):
		return self.first_name + " " + self.last_name
