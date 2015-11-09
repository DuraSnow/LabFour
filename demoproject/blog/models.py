from django.db import models

# Create your models here.
class Author(models.Model):
	#AuthorID (PK), Name, Age, Country
    name = models.CharField(max_length=30)
    authorid = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    def   _unicode_ (self):
    	return self.name
    	
class Books(models.Model):
	#ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    authorid = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=30)    
    price = models.IntegerField()

