# tutorial/views.py
from django.shortcuts import render
from .models import Sensor
from .models import Article
from .models import Supplier
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect


def sensor(request):
    return render(request, 'tutorial/people.html', {'people': Sensor.objects.all()})


def kuh(request, kuhid):
    return render(request, 'tutorial/muh.html')  # , {'kuhid': kuhid})


def warehouse(request):
    if request.method == 'POST':
        try:
            article = Article.objects.get(article_id=request.POST['article'])
            article.article_sensor_status = False
            article.save()
            print("true")
        except Article.DoesNotExist:
            raise Http404("Gibts nicht")
        return HttpResponseRedirect(reverse('warehouse'))
    else:
        try:
            all_articles = Article.objects.all()
            empty_articles = Article.objects.filter(article_sensor_status=True)
            all_supplier = Supplier.objects.all()#(article__article_sensor_status=True)

        except Article.DoesNotExist:
            raise Http404("Gibts nicht")
        return render(request, 'Warehouse.html',
                  {'all_articles': all_articles,
                   'empty_articles': empty_articles,
                   'all_supplier': all_supplier})


def ordered(request):
    try:
        article = Article.objects.get(article_id=request.POST['article'])
        article.article_sensor_status=False
        article.save()
        print("true")
    except Article.DoesNotExist:
        raise Http404("Gibts nicht")
    return redirect('warehouse')
    #return render(request, 'ordered',{'article': article})
