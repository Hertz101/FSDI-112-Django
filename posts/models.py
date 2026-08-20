from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Create your models here.
# SELECT * FROM table
# DELETE FROM table WHERE id = ?
# UPDATE (name, lastname) VALUES (?,?) WHERE id = ?
# CREATE table (
# id INTEGER PRIMARY_KEY AUTOINCREMENT,
# name VARCHAR(100),
# ...
#)
class Post(models.Model):
  title = models.CharField(max_length=128)            # String Max characters 128
  subtitle = models.CharField(max_length=128)         # String Max characters 128
  body = models.TextField()                           # String big amount of info
  created_on = models.DateTimeField(auto_now_add=True)# Added automatically
  author = models.ForeignKey(                         # Field to add a relation to another table
    User,                                             # What model is related to
    on_delete=models.CASCADE                          # The action IF a user gets deleted
  )

  def __str__(self):
    return f"{self.title} by {self.author}"

  def get_absolute_url(self):
    #Automatically redirect the user to an specific endpoint when a success POST request is made
    return reverse("post_detail", args=[self.id])