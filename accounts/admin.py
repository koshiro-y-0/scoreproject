from django.contrib import admin

# Register your models here.
from .models import CustomUser


# 管理サイトCustomUserモデルを追加
# 「http://127.0.0.1:8000/admin」で管理できるように
class CustomUserAdmin(admin.ModelAdmin):
    # CustomUserモデル（テーブル）は13項目のうち、管理サイト（/admin）に表示するのは下記の2つ
    # ※パスワードは不可（管理者でも不可）
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

# createsuperuserで作成した管理者も登録する
admin.site.register(CustomUser, CustomUserAdmin)