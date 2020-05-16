from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Notes, Comments, Tags
from django.views.generic import View, ListView
from .forms import NoteForm, CommentForm, TagForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .utils import ObjCreateMixin, ObjUpdateMixin, ObjDeleteMixin
from django.core.paginator import Paginator
from django.db.models import Q


def custom_processor(request):
    tag = Tags.objects.all()
    tags = {'tags': tag}
    return tags


def index(request):
    search_request = request.GET.get('search', '')

    if search_request:
        list_note = Notes.objects.filter(Q(title__icontains=search_request) | Q(text__icontains=search_request))
    else:
        list_note = Notes.objects.all()

    paginator = Paginator(list_note, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'notes': page,
        'is_paginated': is_paginated,
        'prev_url':prev_url,
        'next_url':next_url
        }

    return render(request, 'News/index.html', context)


def note_detail(request, note_id):
    try:
        note = Notes.objects.get(pk=note_id)
        context = {'note': note, 'panel': note, 'detail': True}
        if request.user.is_authenticated:
            context['form'] = CommentForm
    except Notes.DoesNotExist:
        raise Http404('Статьи не существует!')
    return render(request, 'News/note_detail.html', context)


def tag_detail(request, tag_id):
    try:
        tag = Tags.objects.get(pk=tag_id)
        context = {'tag': tag}
    except Tags.DoesNotExist:
        Http404('Тэга не существует!')
    return render(request, 'News/tag_detail.html', context)


class NoteCreate(PermissionRequiredMixin ,LoginRequiredMixin, View, ObjCreateMixin):
    permission_required = ('comments.can_see_author', 'comments.can_edit')
    model_form = NoteForm
    template = 'News/note_create_form.html'
    raise_exception = True

class TagCreate(View, ObjCreateMixin):
    model_form = TagForm
    template = 'News/tag_create_form.html'
    raise_exception = True


class NoteUpdate(LoginRequiredMixin, View, ObjUpdateMixin):
    raise_exception = True
    data = Notes
    model_form = NoteForm
    template = 'News/note_update_form.html'


class TagUpdate(View,ObjUpdateMixin):
    raise_exception = True
    data = Tags
    model_form = TagForm
    template = template = 'News/tag_update_form.html'


class NoteDelete(LoginRequiredMixin, View, ObjDeleteMixin):
    raise_exception = True
    template = 'News/note_delete_form.html'
    data = Notes

class TagDelete(View, ObjDeleteMixin):
    raise_exception = True
    template = 'News/tag_delete_form.html'  
    data = Tags

class MyNotesByUserListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'News/list_notes_user.html'

    def get_queryset(self):
        return Notes.objects.filter(author = self.request.user).order_by('pub_date')


@login_required
def add_comment(request, note_id):
    form = CommentForm(request.POST)
    note = get_object_or_404(Notes, id = note_id)

    if form.is_valid():
        comment = Comments()
        comment.fk_note = note
        comment.author = request.user
        comment.text = form.cleaned_data['comment_text']
        comment.save()
    return redirect(note.get_absolute_url())


