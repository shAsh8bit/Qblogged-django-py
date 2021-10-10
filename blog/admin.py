from django.contrib import admin
from blog.models import Contact,Blog,DiscussionQ,DiscussionA

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','blogger','head','time')
    # prepopulated_fields = {'slug': ('head',)}
class DiscussiomQAdmin(admin.ModelAdmin):
    list_display=('id','head')    
class DiscussiomAAdmin(admin.ModelAdmin):
    list_display=('id','post')
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog,BlogAdmin)
admin.site.register(DiscussionQ, DiscussiomQAdmin)
admin.site.register(DiscussionA,DiscussiomAAdmin)

