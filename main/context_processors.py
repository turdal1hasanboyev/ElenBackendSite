from apps.elen.models import Category, Tag


def objects(request):
    categories = Category.objects.all().order_by('name')
    tags = Tag.objects.all().order_by('name')

    return {
      "categories": categories,
      "tags": tags,
    }
