from django.contrib import admin
from .models import *


class CopyInline(admin.TabularInline):
    model = TweetCopy 
    extra = 1


class LFCopyInline(admin.TabularInline):
    model = LongFormCopy 
    extra = 1


class TweetLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "published", )
    list_filter = ("domain", "published",)
    # exclude = ['author','pic',]
    inlines = [CopyInline, LFCopyInline]


class TweetCopyAdmin(admin.ModelAdmin):
    list_display = ("link", "published", "running" )
    list_filter = ("link", "published", "running")
    # exclude = ['author','pic',]

# Register your models here.
admin.site.register(TweetLink, TweetLinkAdmin)
admin.site.register(TweetUser,)
admin.site.register(TweetCopy,TweetCopyAdmin)
admin.site.register(TweetList)
