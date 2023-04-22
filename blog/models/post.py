from django.db import models
from django.core.validators import MinLengthValidator
from .tag import Tag
from .author import Author

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name= "posts")
    tags = models.ManyToManyField(Tag)
    # models.Foreighkey sluzi da bi neku sporednu klasu npr Author (Author.py)(sa svojim modelima-name,last name npr)
    # ubacili kao klasu author u Post klasi-modelu
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    # OVDE SMO KLASU post SPOJILI SA KLASOM Post iZNAD, A OVO CASCADE SLUZI DA AKO SE OBRISE OVO POLJE MODEL DA CE
    # SVE -Comment klase koje se naprave, KOJE DELE OVAJ POST BITI OBRISANE

# ove dve klase su modeli koje koristimo u glavnom projektu, menjamo ih i pravimo nove preko admina