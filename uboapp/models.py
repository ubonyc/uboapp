from django.db import models



# Create your models here.
class Building(models.Model):
    streetname = models.CharField(("Street name"),max_length=200, default=0)
    streetnumber = models.CharField(("Street number"),max_length=5, default=0)
    zipcode = models.CharField(("Zipcode"),max_length=5, default=0)
    latitude = models.CharField(("Latitude"),max_length=10, default=0)
    longitude = models.CharField(("Longitude"),max_length=10, default=0)
    yearbuilt = models.IntegerField(default=2000);



    def save(self, *args, **kwargs):
        self.streetname = self.streetname.upper()
        super(Building, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Building")
        verbose_name_plural = ("Buildings")

    def __str__(self):
        return str(self.streetname)

    @property
    def images(self):
        return self.imgbuilding_set.all()

    @property
    def image(self):
        return self.images.first()

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def comment(self):
        return self.comments.first()

def building_upload_to(instance, filename):
    filename = filename.lower()
    return 'hotel/%s/%s' % (instance.hotel.name, filename)


class ImgBuilding(models.Model):
    image = models.ImageField(upload_to='', default = "evil.gif")
    tri = models.IntegerField(default=0)
    building = models.ForeignKey(Building)

    def save(self, *args, **kwargs):
        super(ImgBuilding, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Building Gallery")
        verbose_name_plural = ("Building Galleries")
        ordering = ("tri",)

    def __str__(self):
        return self.building.streetname


class Comment(models.Model):
    comment = models.CharField(("Comment"),max_length=200, default=0)
    tri = models.IntegerField(default=0)
    building = models.ForeignKey(Building)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")
        ordering = ("tri",)

    def __str__(self):
        return self.building.comment.comment