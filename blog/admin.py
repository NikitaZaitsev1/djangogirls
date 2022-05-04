from django.contrib import admin
from blog.models import Post
from blog.models import FeedBack

admin.site.register(Post)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("email", "active")


admin.site.register(FeedBack, FeedBackAdmin)
