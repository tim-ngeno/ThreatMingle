from django.db import models


class LearningModel(models.Model):
    """
    Defines the models for learning content on CyberSec
    """
    title = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the learning model
        """
        return self.title
