from django.db import models


# Create your models here.
# Model to store the day
class Day(models.Model):
    day_made = models.DateField()
    time_stamp = models.DateTimeField(auto_now = True)
    # def __str__(self):
    #     return self.day_made

# model to store plans within the day
class Plans(models.Model):
    day = models.ForeignKey(Day, on_delete = models.CASCADE)
    time_start = models.TimeField('Time Start')
    time_end = models.TimeField('Time End')
    plan_title = models.CharField(max_length = 20)
    plan_desc = models.TextField(max_length = 300)
    def __str__(self):
        return self.plan_title
    