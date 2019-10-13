import os
from django.db import models
from io import StringIO
from PIL import Image
# from django.core.urlresolvers import reverse

from django.core.files import File
from django.utils.safestring import mark_safe
from django.utils.html import escape

# from django.contrib.sites.models import Site
from django.utils.text import slugify

from versatileimagefield.fields import VersatileImageField
from django.core.files.storage import FileSystemStorage


Ts = FileSystemStorage(location='media/tweet/')



class TweetUser(models.Model):
    handle = models.CharField(max_length=220, blank=True, null=True)
    fb_page = models.CharField(max_length=64, blank=True, null=True)

    token = models.CharField(max_length=220, blank=True, null=True)
    token_key = models.CharField(max_length=220, blank=True, null=True)
    secret = models.CharField(max_length=220, blank=True, null=True)
    secret_key = models.CharField(max_length=220, blank=True, null=True)

    published = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Tweet User"

    def __str__(self):
        return "%s" % self.handle


class TweetList(models.Model):
    owner = models.ForeignKey('TweetUser', blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=220, blank=True, null=True)
    list_id = models.CharField(max_length=128, blank=True, null=True)
    handle_list = models.TextField(blank=True, null=True)
    used_handles = models.TextField(blank=True, null=True)
    
    published = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Tweet List"

    def __str__(self):
        return "%s" % self.name

# Create your models here.
class TweetCopy(models.Model):
    copy_text = models.TextField(max_length=260, blank=True, null=True)
    link = models.ForeignKey('TweetLink', blank=True, null=True, on_delete=models.PROTECT)
    tweeter = models.ManyToManyField(TweetUser, related_name="Tweeter_sc", blank=True, null=True)
    hList = models.ForeignKey(TweetList, blank=True, null=True, on_delete=models.PROTECT)
    facebook = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    running = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = "Tweet Copy"

    def __str__(self):
        return "%s" % self.id


class LongFormCopy(models.Model):
    copy_text = models.TextField(blank=True, null=True)
    link = models.ForeignKey('TweetLink', blank=True, null=True, on_delete=models.PROTECT)
    tweeter = models.ManyToManyField(TweetUser, related_name="Tweeter_lf")
    facebook = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    running = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Long Form Copy"

    def __str__(self):
        return "%s" % self.id


    rt_id = models.CharField(max_length=512, blank=True, null=True)


class TweetPics(models.Model):
    twt_media_id = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.ForeignKey('TweetLink', related_name='tweet_imgs', blank=True, null=True, on_delete=models.PROTECT)
    pic = VersatileImageField(storage=Ts, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Gallery Pics"

    def __unicode__(self):
        return "/media/tweet/%s/" % self.id

    def gpic(self):
        x = str(self.pic)
        x = x[2:]
        return "/media/tweet/%s" % x


class TweetLink(models.Model):
    domain = models.ForeignKey('TweetUser', blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=32, blank=True, null=True)
    link = models.CharField(max_length=120, blank=True, null=True)
    foto = VersatileImageField(storage=Ts, blank=True, null=True)

    description = models.TextField(max_length=220, blank=True, null=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tweet Links"

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name
