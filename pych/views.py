from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'name': name}
    return render(request, 'pybo/question_detail.html', context)
