# scoreproject メモリ

## GitHub
- リポジトリ: https://github.com/koshiro-y-0/scoreproject
- SSH: git@github.com:koshiro-y-0/scoreproject.git
- デフォルトブランチ: main

## ブランチ運用ルール（GitHub Flow）
- main への直接 push は禁止
- 機能開発・修正は必ず feature ブランチで行う
- ブランチ命名規則:
  - 機能追加: `feature/機能名`
  - バグ修正: `fix/バグ内容`
  - 緊急修正: `hotfix/内容`
- 開発完了後は PR（Pull Request）を作成して main にマージ
- ユーザーから機能の指示があったら feature ブランチを作成してから作業開始

## 作業ルール
- ファイルを修正したら必ず `git push` すること
- 作業は必ず feature ブランチで行い、完了後に PR を作成する

## プロジェクト概要
- Django 4.0、SQLite、Bootstrap 5.2.3
- アプリ: score（成績管理）、accounts（認証）、omb（掲示板）
- 詳細は 仕様書.md を参照

## 主要ファイルパス
- 設定: scoreproject/settings.py
- ルートURL: scoreproject/urls.py
- 成績モデル: score/models.py
- ユーザーモデル: accounts/models.py
- 掲示板モデル: omb/models.py
