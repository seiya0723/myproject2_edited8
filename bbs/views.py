from django.shortcuts import render,redirect
from django.views import View


#ビュークラスに継承させることで、認証状態をチェックする
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Topic,Category
from .forms import TopicForm


from django.db.models import Q

#LoginRequiredMixinを引数に入れる。これで未認証ユーザーはアクセスできない
#class BbsView(LoginRequiredMixin,View):
class BbsView(View):

    def get(self, request, *args, **kwargs):

        categories  = Category.objects.all()

        if "search" in request.GET:

            if request.GET["search"] == "" or request.GET["search"].isspace():
                return redirect("bbs:index")

            search      = request.GET["search"].replace(" ","　")
            search_list =search.split(" ")

            query       = Q()
            for word in search_list:
                query &= Q(title__contains=word)

            topics  = Topic.objects.filter(query)
        else:
            topics  = Topic.objects.all()


        context = { "topics":topics,
                    "categories":categories,
                   }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form = TopicForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")

index   = BbsView.as_view()



class BbsDeleteView(LoginRequiredMixin,View):
#class BbsDeleteView(View):

    def post(self,request, pk, *args, **kwargs):

        topic = Topic.objects.filter(id=pk).first()
        topic.delete()

        return redirect("bbs:index")

delete = BbsDeleteView.as_view()

# Create your views here.
