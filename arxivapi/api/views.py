from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

from .models import Paper, Author, Category


def paper_list(request):
    papers = Paper.objects.all()
    paginator = Paginator(papers, 10)  # Change the page size as desired
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
        'previous_page': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'results': [
            {
                'id': paper.id,
                'title': paper.title,
                'abstract': paper.abstract,
                'authors': [author.name for author in paper.authors.all()],
                'categories': [category.name for category in paper.categories.all()],
                'publication_date': paper.publication_date
            }
            for paper in page_obj
        ]
    }

    return JsonResponse(data, safe=False)


def paper_detail(request, id):
    paper = get_object_or_404(Paper, id=id)
    data = {'id': paper.id, 'title': paper.title, 'abstract': paper.abstract,
            'authors': [author.name for author in paper.authors.all()],
            'categories': [category.name for category in paper.categories.all()],
            'publication_date': paper.publication_date}
    return JsonResponse(data)


def author_list(request):
    authors = Author.objects.all()
    data = [{'id': author.id, 'name': author.name} for author in authors]
    return JsonResponse(data, safe=False)


def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    papers = Paper.objects.filter(authors=author)
    data = {'id': author.id, 'name': author.name,
            'papers': [{'id': paper.id, 'title': paper.title, 'abstract': paper.abstract,
                        'publication_date': paper.publication_date} for paper in papers]}
    return JsonResponse(data)


def category_list(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    papers = Paper.objects.filter(categories=category)
    data = {'id': category.id, 'name': category.name,
            'papers': [{'id': paper.id, 'title': paper.title, 'abstract': paper.abstract,
                        'publication_date': paper.publication_date} for paper in papers]}
    return JsonResponse(data)
