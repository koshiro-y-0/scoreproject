# フォームで使用するUserCreationFormをインポート
from django.contrib.auth.forms import UserCreationForm

# 連携するモデル（DB）のCustomUserをインポート
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # 連携するモデル
        model = CustomUser
        # 使用するフォームのフィールド
        # 学生番号、メール、パスワード１、パスワード２（確認用）
        fields = ('student_number', 'email')
