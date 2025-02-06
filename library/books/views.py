from django.shortcuts import render
from django.utils import timezone
from .models import Books
from .forms import BookForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def book_list(request):
    books = Books.objects.filter(publishing__lte=timezone.now()).order_by('publishing')
    return render(request, 'C:\\Users\\altna\\OneDrive\\Рабочий стол\\django project library\\books\\library\\books\\templates\\book_list.html', {'books': books})
def book_new(request):
    if request.method =="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.author=request.user
            book.publishing=timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form=BookForm()
    return render(request, 'C:\\Users\\altna\\OneDrive\\Рабочий стол\\django project library\\books\\library\\books\\templates\\book_edit.html', {'form': form})
def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, 'C:\\Users\\altna\\OneDrive\\Рабочий стол\\django project library\\books\\library\\books\\templates\\book_detail.html', {'book': book})