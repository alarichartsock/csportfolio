from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse


class BlogSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modified_date

    def location(self, obj):
        # Return the absolute URL for each post
        return reverse("blog:post_detail", args=[obj.pk])


class MainSiteMap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return ["index", "resume", "license", "robots"]

    def location(self, item):
        return reverse(item)
