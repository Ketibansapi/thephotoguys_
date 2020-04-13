# from django_elasticsearch_dsl import DocType, Index
# from core.models import Item

# items = Index ('items')

# @items.doc_type
# class ItemDocument(DocType):
#     class Meta:
#         model = Item

#         fields = [
#             'title', 
#             'price', 
#             'discount_price',
#             'category',
#             'label',
#             'slug',
#             'description',
#             'image',
#         ]