from django.db import models
from django.urls import reverse



MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # Changing this instance method
    # does not impact the database, therefore
    # no makemigrations are necessary
    def __str__(self):
        return f'{self.name} ({self.id})' 
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
        )
    
    def __str__(self):
        # nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
