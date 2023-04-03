from django.db import models
from django.urls import reverse

class Offers(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField('Опис', max_length=255)
    url_image = models.URLField(blank=True, null=True)
    location = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    request = models.ForeignKey('requests.Requests', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("offers_detail", kwargs={"pk": self.pk})
