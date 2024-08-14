from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
	book_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	genre = models.CharField(max_length=255)
	year_published = models.IntegerField()
	summary = models.TextField()
	class Meta:
        db_table = "books"

class reviews():
	review_id = models.AutoField(primary_key=True)
	book_id =  models.ForeignKey(Book, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	review_text = models.CharField(max_length=255)
	rating = models.IntegerField()


	class Meta:
        db_table = "reviews"