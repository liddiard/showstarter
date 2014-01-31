from django.db import models


class Show(models.Model):
    name = models.CharField(max_length=128)
    year = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.year)


class Episode(models.Model):
    show = models.ForeignKey('Show')
    name = models.CharField(max_length=128, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    season = models.PositiveIntegerField()
    episode = models.PositiveIntegerField()

    def __unicode__(self):
        return "(%s.%s) %s" % (self.season, self.episode, self.name)
