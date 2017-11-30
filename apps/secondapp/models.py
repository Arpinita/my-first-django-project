from django.db import models


class Animals(models.Model):
    COLOR_CHOICES = (
        ('none', 'Without color'),
        ('green', 'Green'),
        ('white', 'White'),
    )

    name = models.CharField(max_length=250)
    voice = models.CharField(max_length=200)
    weight = models.IntegerField(default=30)
    height = models.IntegerField(default=100)
    color = models.CharField(
        choices=COLOR_CHOICES,
        max_length=44,
        default='none',
    )
    age = models.IntegerField(default=0)
    owner = models.ForeignKey('Owners', on_delete=None)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animals'


class Owners(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Owners'
