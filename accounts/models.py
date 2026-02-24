from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 学生番号フィールド
    student_number = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name='学生番号'
    )
    
    # メールアドレス
    email = models.EmailField(
        verbose_name='メールアドレス',
    )
    
    # 学年フィールドを追加
    grade = models.IntegerField(
        verbose_name='学年',
        null=True,
        blank=True,
        choices=[
            (1, '1年生'),
            (2, '2年生'),
            (3, '3年生'),
        ]
    )
    
    # usernameは内部的に使用（学生番号と同じ値を自動設定）
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.student_number
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'