from django.db import models
from django.urls import reverse

class Requests(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField('Опис', max_length=1024)
    location = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    offer = models.ForeignKey('offers.Offers', on_delete=models.CASCADE)
    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("requests_detail", kwargs={"pk": self.pk})