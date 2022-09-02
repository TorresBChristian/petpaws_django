from django.db import models

pet_size_choices = [
    ("Pe","Pequeño"),
    ("Me","Mediano"),
    ("Gr","Grande")
    ]

class PetPost(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_age = models.IntegerField()
    pet_size = models.CharField(max_length=50, choices=pet_size_choices)
    pet_gender = models.CharField(max_length=50)
    pet_description = models.CharField(max_length=400)
    pet_picture = models.ImageField(upload_to ='uploads/', blank=True)
    pet_publication = models.DateTimeField('date published')
    owner_name = models.CharField(max_length=50)
    owner_lastname = models.CharField(max_length=50)
    owner_email = models.EmailField(max_length=150)
    owner_phonenumber = models.IntegerField()

    def __str__(self):
        return self.pet_name