from django.db import models
# from django.forms import ModelForm

pet_size_choices = [
    ("Pe","Pequeño"),
    ("Me","Mediano"),
    ("Gr","Grande")
    ]

class PetPost(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_size = models.CharField(max_length=50, choices=pet_size_choices)
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

# class PetPostForm(ModelForm):
#     class Meta:
#         model = PetPost
#         fields = ["pet_name", "pet_size", "pet_age", "pet_gender", "post_description", "post_picture",
#                   "post_publication", "owner_name", "owner_lastname", "owner_email", "owner_phonenumber"]