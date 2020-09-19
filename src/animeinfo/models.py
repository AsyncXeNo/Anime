from django.db import models

# Create your models here.


class AnimeSeries(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(null=False, blank=False)
    isairing = models.BooleanField(
        name="Is Airing?", null=False, default=True, db_index=True)
    episode_count = models.PositiveSmallIntegerField(
        name="Episodes Aired", null=False)
    episodes_total = models.PositiveSmallIntegerField(
        name="Episodes Planned/Total", null=False)
    slug = models.SlugField(max_length=100)
    airing_from = models.DateField(db_index=True)
    airing_to = models.DateField(blank=True, null=True)
    year = models.IntegerField(null=False, blank=False, db_index=True)
    season = models.CharField(max_length=10,
                              choices=[('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall')], db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'animeseries'
        verbose_name = 'Anime Series'
        verbose_name_plural = 'Anime Series'
