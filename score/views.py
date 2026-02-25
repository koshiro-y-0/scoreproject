from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView

from django.urls import reverse_lazy

from .forms import ScoreForm 

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

# 成績入力用のモデル（DB）をインポート
from .models import Score, Subject

''' ホームページ '''
@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ログインユーザーの全成績を取得
        user_scores = Score.objects.filter(user=self.request.user)

        # 統計情報
        context['total_records'] = user_scores.count()

        # 登録科目数
        context['total_subjects'] = user_scores.values('subject').distinct().count()

        # 最近の成績記録（5件）
        context['recent_scores'] = user_scores.order_by('-date')[:5]

        # 科目別の最新スコア一覧
        subjects_latest = []
        for subject in Subject.objects.all():
            latest = Score.objects.filter(
                user=self.request.user,
                subject=subject
            ).order_by('-date').first()

            if latest is None:
                bar_color = 'secondary'
                score_val = None
            elif latest.score >= 80:
                bar_color = 'success'
                score_val = latest.score
            elif latest.score >= 60:
                bar_color = 'warning'
                score_val = latest.score
            else:
                bar_color = 'danger'
                score_val = latest.score

            subjects_latest.append({
                'id': subject.id,
                'name': subject.subject,
                'score': score_val,
                'bar_color': bar_color,
            })

        context['subjects_latest'] = subjects_latest

        return context


''' 成績入力 '''
@method_decorator(login_required, name='dispatch')
class InScoreView(CreateView):
    form_class = ScoreForm
    template_name = 'in-score.html'
    success_url = reverse_lazy('score:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

''' 成績入力完了 '''
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'



''' 成績詳細（科目一覧） '''
class SubjectDetailView(TemplateView):
    template_name = 'detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 全ての科目を取得
        subjects = Subject.objects.all()
        
        # 各科目の統計情報を計算
        subject_list = []
        colors = ['primary', 'warning', 'success', 'danger', 'info', 'secondary']

        for index, subject in enumerate(subjects):
            scores = Score.objects.filter(
                user=self.request.user,
                subject=subject
            ).order_by('-date')

            score_count = scores.count()

            if score_count > 0:
                score_values = [s.score for s in scores]
                latest_score  = score_values[0]
                max_score     = max(score_values)
                min_score     = min(score_values)
                avg_score     = round(sum(score_values) / score_count, 1)

                if latest_score >= 80:
                    bar_color = 'success'
                elif latest_score >= 60:
                    bar_color = 'warning'
                else:
                    bar_color = 'danger'
            else:
                latest_score = max_score = min_score = avg_score = None
                bar_color = 'secondary'

            subject_list.append({
                'id':           subject.id,
                'name':         subject.subject,
                'latest_score': latest_score,
                'max_score':    max_score,
                'min_score':    min_score,
                'avg_score':    avg_score,
                'count':        score_count,
                'color':        colors[index % len(colors)],
                'bar_color':    bar_color,
            })

        context['subjects'] = subject_list
        
        return context


''' 科目別成績一覧 '''
@method_decorator(login_required, name='dispatch')
class SubjectScoreListView(ListView):
    template_name = 'subject_score_list.html'
    context_object_name = 'score_records'
    paginate_by = 10
    
    def get_queryset(self):
        # URLから科目IDを取得
        subject_id = self.kwargs['pk']
        # ログインユーザーの該当科目の成績を取得
        return Score.objects.filter(
            user=self.request.user,
            subject_id=subject_id
        ).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 科目情報を取得
        subject_id = self.kwargs['pk']
        subject = get_object_or_404(Subject, pk=subject_id)
        context['subject'] = subject
        
        # 統計情報を計算
        scores = self.get_queryset()
        if scores.exists():
            context['max_score'] = max(s.score for s in scores)
            context['min_score'] = min(s.score for s in scores)
            context['total_count'] = scores.count()
        else:
            context['max_score'] = None
            context['min_score'] = None
            context['total_count'] = 0
        
        return context
