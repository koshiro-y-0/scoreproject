from django.contrib import admin

# Register your models here.
from .models import OmbPost

# Register your models here.
class OmbPostAdmin(admin.ModelAdmin):
    # 表示する項目
    list_display = ('id', 'name', 'subject', 'posted_at')
    list_display_links = ('id', 'name')

# adminサイトで閲覧できるように登録
admin.site.register(OmbPost, OmbPostAdmin)