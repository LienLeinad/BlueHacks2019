from django.db import models


# Create your models here.
# Model to store the day
class Day(models.Model):
    day_made = models.DateField()
    time_stamp = models.DateTimeField(auto_now = True)
    def __str__(self):    
        return str(self.day_made)

# model to store plans within the day
class Plans(models.Model):
    PHYSICAL = 'Physical'
    EMOTIONAL = 'Emotional'
    SOCIAL = 'Social'
    OCCUPATIONAL = 'Occupational'
    INTELLECTUAL = 'Intellectual'
    SPIRITUAL = 'Spiritual'
    day = models.ForeignKey(Day, on_delete = models.CASCADE)
    time_start = models.TimeField('Time Start')
    time_end = models.TimeField('Time End')
    plan_title = models.CharField(max_length = 20)
    plan_desc = models.TextField(max_length = 300)
    TAG_CHOICES = (
        (PHYSICAL, 'Physical'),
        (EMOTIONAL, 'Emotional'),
        (SOCIAL, 'Social'),
        (OCCUPATIONAL, 'Occupational'),
        (INTELLECTUAL, 'Intellectual'),
        (SPIRITUAL,'Spiritual'),
    )
    plan_tag = models.CharField(
        max_length = 10,
        choices = TAG_CHOICES     
    )
    def __str__(self):
        return self.plan_title
    