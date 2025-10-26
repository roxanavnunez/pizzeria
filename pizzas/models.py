from django.db import models

class Pizza(models.Model):
    """A pizza to order."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.title()

class Topping(models.Model):
    """Toppings for a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f"Toppings: {self.name}"
