from django.db import models

class Cities(models.Model):
    title = models.CharField(max_length= 200)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self) -> str:
        return self.title

    def get_brigades(self):
        return Brigade.objects.filter(city__title = self.title)

class Brigade(models.Model):
    title = models.CharField(max_length=200)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE , related_name='City')
    count_of_workers = models.IntegerField()
    appointment = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

    def get_facility(self):
        return Facility.objects.filter(brigade__title = self.title)

class Facility(models.Model):
    title = models.CharField(max_length=200)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='Brigade')
    count_of_workers = models.IntegerField()
    appointment = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title