from djongo import models


class Gateway(models.Model):

    uid = models.CharField(max_length=30,unique=True);
    name = models.CharField(max_length=30);
    ssid = models.CharField(max_length=30);
    key = models.CharField(max_length=30);
    encryption = models.CharField(max_length=10)

    objects = models.DjongoManager()

    def __str__(self):
        return self.uid+'-'+self.name
