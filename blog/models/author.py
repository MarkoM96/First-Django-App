from django.db import models

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    # klasa author,post,comment i tag su klase koje koristimo u bazi a preko admina ih menjamo,pravimo nove i brisemo