from django.db import models

# Create your models here.
from score.models import Subject
class OmbPost(models.Model):
    ''' 科目別コメントを管理するテーブル '''
    # 投稿名
    # 科目：Subjectモデルと紐づけ
    # コメント
    # 投稿日時
    name = models.CharField(
        verbose_name='投稿名',
        max_length=50
    )
    subject = models.ForeignKey(
        Subject,
        verbose_name='科目',
        on_delete=models.PROTECT
    )
    # CASCADE：科目を削除したら、紐づくコメントもすべて削除
    comment = models.TextField(
        verbose_name='コメント'
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    # auto_now_add：日時を自動追加
    def __str__(self):
        return self.name