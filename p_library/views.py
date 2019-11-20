from django.shortcuts import render
from .models import Book, Edition
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Author
from .forms import AuthorForm, BookForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
# Create your views here.


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    # success_url = reverse_lazy('p_library:author_list')
    success_url = reverse_lazy('author_list')
    template_name = 'authors_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'


def author_create_many(request):
    # Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`,
    # в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    # Наш обработчик будет обрабатывать и GET и POST запросы.
    # POST запрос будет содержать в себе уже заполненные данные формы
    if request.method == 'POST':
        # Здесь мы заполняем формы формсета теми данными, которые пришли в запросе.
        # Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм,
        # но и разных формсетов, этот параметр позволяет их отличать в запросе.
        author_formset = AuthorFormSet(
            request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():  # Проверяем, валидны ли данные формы
            for author_form in author_formset:
                author_form.save()  # Сохраним каждую форму в формсете
            # После чего, переадресуем браузер на список всех авторов.
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:  # Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        # Инициализируем формсет и ниже передаём его в контекст шаблона.
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=1)
    BookFormSet = formset_factory(BookForm, extra=1)
    if request.method == 'POST':
        author_formset = AuthorFormSet(
            request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset
        }
    )


def book_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

# Добавьте новый view - redactions


def redactions(request):

    # Создан новый шаблон, который выводит контент в виде списка
    template = loader.get_template('redactions.html')

    # Формируем выборку всех редакций
    biblio_data = {
        'editions': Edition.objects.all(),
    }

    # Передаем в шаблон все редакции
    return HttpResponse(template.render(biblio_data, request))


def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')
