from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import OmbPost
from .forms import OmbPostForm
from score.models import Subject

''' トップページ '''
class IndexView(TemplateView):
    template_name = 'top.html'

''' コメント一覧を表示 '''
# https://qiita.com/har_0320/items/d2224c3aef470ea5e855 4-1
class OmbListView(ListView):
    template_name = 'omb_list.html'
    model = OmbPost
    context_object_name = 'omb_records'
    paginate_by = 5
    def get_queryset(self):
        # デフォルトは投稿日時の降順
        queryset = OmbPost.objects.select_related('subject').order_by('-posted_at')
        
        # クエリパラメータ 'subject' がある場合はフィルタリング
        subject_id = self.request.GET.get('subject')
        if subject_id:
            queryset = queryset.filter(subject=subject_id)
        
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        # フィルタ中の科目IDをテンプレートへ渡す（アクティブ状態の表示用）
        subject_id = self.request.GET.get('subject')
        context['current_subject_id'] = int(subject_id) if subject_id else None
        return context

''' コメントを投稿 '''
class OmbCreateView(CreateView):
    template_name = 'omb_post.html'
    form_class = OmbPostForm
    success_url = reverse_lazy('omb:list') # 投稿完了後は一覧へ
    def form_valid(self, form):
        # 必要であればここでユーザー紐づけなどを行うが、今回は入力された名前を使用
        return super().form_valid(form)