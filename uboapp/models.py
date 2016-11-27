from django.db import models


# Create your models here.
class Building(models.Model):
    streetname = models.CharField(("Street name"),max_length=200, default="NA")
    streetnumber = models.CharField(("Street number"),max_length=5, default="NA")
    zipcode = models.CharField(("Zipcode"),max_length=5, default=0)
    latitude = models.CharField(("Latitude"),max_length=10, default=0)
    longitude = models.CharField(("Longitude"),max_length=10, default=0)

    buildingtype = models.CharField(("Building class"),max_length=200, default="NA")
    yearbuilt = models.IntegerField(default=2000);
    stories = models.IntegerField(default=0);
    res_units = models.IntegerField(default=0);
    com_units = models.IntegerField(default=0);

    structure_type = models.CharField(("Structure type"), max_length=200, default="NA")
    grade = models.CharField(("Grade"), max_length=200, default="NA")
    construction_type = models.CharField(("Construction type"), max_length=200, default="NA")
    area = models.IntegerField(default=100000);
    lotsize = models.IntegerField(default=50000);

    marketvalue = models.IntegerField(default=10000000);

    one = models.IntegerField(default=0);
    two = models.IntegerField(default=0);
    three = models.IntegerField(default=0);
    four = models.IntegerField(default=0);
    five = models.IntegerField(default=0);



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
    def texts(self):
        return self.text_set.all()

    @property
    def text(self):
        return self.text.first()

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
    text = models.TextField()
    building = models.ForeignKey(Building)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.building.text