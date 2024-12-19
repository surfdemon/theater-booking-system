from django.db import models


class Signup(models.Model):
    """
    Model representing a user signup.
    """
    fname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the Signup object.
        """
        return self.email
