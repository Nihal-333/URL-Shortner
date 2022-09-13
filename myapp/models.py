from django.db import models

# Create your models here.
class LongToShort(models.Model):
	Long_url = models.URLField(max_length = 500)
	Short_url = models.CharField(max_length=50, unique=True)
	Date = models.DateField(auto_now_add=True) 
	Clicks = models.IntegerField(default=0)

	
