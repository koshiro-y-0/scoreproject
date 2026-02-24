from django.contrib import admin
from .models import Subject,Score, Profile

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    # 表示する項目
    list_display = ('subject',)
    # 項目をクリックしたら詳細を表示できるようにリンク設定
    list_display_links = ('subject',)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('subject', 'score')
    list_display_links = ('subject', 'score')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade')
    list_display_links = ('name', 'grade')

# adminサイトで閲覧できるように登録
# Categoryモデル、PhotoPostMeadを登録
# 追加で管理ページで表示するクラスを登録（CategoryAdmin, PhotoPostAdmin）
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Profile, ProfileAdmin)