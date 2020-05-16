
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="url_index"),
    path('<int:note_id>', views.note_detail, name="url_detail"),
    path('tag/<int:tag_id>', views.tag_detail, name="url_tag"),
    path('note_create/', views.NoteCreate.as_view(), name="url_note_create"),
    path('<int:obj_id>/note_update/',
         views.NoteUpdate.as_view(), name="url_note_update"),
    path('<int:obj_id>/note_delete/',
         views.NoteDelete.as_view(), name="url_note_delete"),
    path('tag_create/', views.TagCreate.as_view(), name="url_tag_create"),    
    path('mynotes/', views.MyNotesByUserListView.as_view(), name='mynotes'),
    path('comment/<int:note_id>', views.add_comment, name = 'add_comment'),
    path('tag/<int:obj_id>/tag_update/',
         views.TagUpdate.as_view(), name="url_tag_update"), 
    path('tag/<int:obj_id>/tag_delete/',
         views.TagDelete.as_view(), name="url_tag_delete"),      
]
