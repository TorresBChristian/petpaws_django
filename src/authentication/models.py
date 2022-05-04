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

    def __init__(self, pet_name, pet_size, pet_age, pet_gender, post_desc,
                 post_picture, post_pub, owner_name, owner_lastname,
                 owner_email, owner_phonenumber):
        self.pet_name = pet_name
        self.pet_size = pet_size
        self.pet_age = pet_age
        self.pet_gender = pet_gender
        self.post_description = post_desc
        self.post_picture = post_picture
        self.post_publication = post_pub
        self.owner_name = owner_name
        self.owner_lastname = owner_lastname
        self.owner_email = owner_email
        self.owner_phonenumber = owner_phonenumber

    def __str__(self):
        return self.pet_name
