from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserAccountInfo(models.Model):
    """ Generic User Account """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional info
    date_joined = models.DateField(auto_now_add=True)

    # TODO: THE FOLLOWING IS FOR REFERENCE, NEEDS TO BE REMOVED

    # Different Jobs
    # VOLUNTEER = 'V'
    # DONOR = 'D'
    # JOB_CHOICES = [
    #     (VOLUNTEER, 'Volunteer'),
    #     (DONOR, 'Donor'),
    #
    # job = models.CharField(max_length=1, choices=JOB_CHOICES)
    #
    # def is_donor(self):
    #     """ Returns true iff user is a donor """
    #     return self.job == 'D'
    #
    #     def __str__(self):
    #         return "False"
    #
    # def is_volunteer(self):
    #     """ Returns true iff user is a volunteer """
    #     return self.job == 'V'
