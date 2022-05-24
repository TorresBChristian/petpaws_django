from django.db import models

class PetPost(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_size = models.CharField(max_length=50)
    pet_age = models.IntegerField()
    pet_gender = models.CharField(max_length=50)
    post_description = models.CharField(max_length=400)
    post_picture = models.ImageField(upload_to ='uploads/')
    post_publication = models.DateTimeField('date published')
    owner_name = models.CharField(max_length=50)
    owner_lastname = models.CharField(max_length=50)
    owner_email = models.EmailField(max_length=150)
    owner_phonenumber = models.IntegerField()

    def __str__(self):
        return self.pet_name
