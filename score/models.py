from django.db import models


# Create your models here.

from accounts.models import CustomUser

''' 科目管理 '''
class Subject(models.Model):
    subject = models.CharField(verbose_name='科目名', max_length=50)
    def __str__(self):
        return self.subject

''' プロフィール '''
class Profile(models.Model):
    # ユーザー：CustomUserモデルと紐づけ
    # 名前
    # アイコン
    # 学年

    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    name = models.CharField(verbose_name='名前', max_length=100)

    icon = models.ImageField(
        verbose_name='アイコン',
        upload_to='icons',
        blank=True,
        null=True
    )

    grade = models.IntegerField(verbose_name='学年')

    def __str__(self):
        return self.name

''' 成績入力 '''
class Score(models.Model):
    # ユーザー：CustomUserモデルと紐づけ
    # 科目：Subjectモデルと紐づけ
    # 日付
    # 得点
    # 投稿日時

    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    # CASCADE：ユーザーを削除したら、成績データもすべて削除

    subject = models.ForeignKey(
        Subject,
        verbose_name='科目',
        on_delete=models.PROTECT
    )
    # PROTECT：成績データがある科目は削除できない

    date = models.DateField(verbose_name='日付')

    score = models.IntegerField(verbose_name='得点')

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    # auto_now_add：日時を自動追加

    def __str__(self):
        return f'{self.subject.subject} - {self.score}点 ({self.date})'
