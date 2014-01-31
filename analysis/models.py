from django.db import models
from django.template.defaultfilters import slugify


class Show(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    year = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(name)
        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.year)


class Episode(models.Model):
    show = models.ForeignKey('Show')
    name = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=128)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    season = models.PositiveIntegerField()
    episode = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(name)
        super(Episode, self).save(*args, **kwargs)

    def __unicode__(self):
        return "(%s.%s) %s" % (self.season, self.episode, self.name)
