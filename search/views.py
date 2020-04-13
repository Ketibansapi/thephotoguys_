# from django.shortcuts import render

# from search.documents import PostDocument

# def search(request):
#     q = request.GET.get('q')

#     if q:
#         items = PostDocument.search().query("match", title=q)
#     else:
#         items = ''

#     return render(request, 'search/search.html', {'items': items})
