from tutorial.models import Article
from tutorial.models import Supplier

all_articles = Article.objects.all()
empty_articles = Article.objects.filter(article_sensor_status=True)
all_supplier = Supplier.objects.filter(article__article_sensor_status=True)

empty_article_list = list()
article_supplier_list = list()

for article in empty_articles:
    empty_article_list.append(Supplier.objects.filter(article__article_id=article.article_id))
            
