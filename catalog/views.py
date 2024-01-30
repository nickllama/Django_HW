from django.shortcuts import render
from .forms import FeedbackForm

def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def FeedbackForm(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (например, сохранение в базу данных)
            # Здесь можно добавить логику для обработки отправленной обратной связи

            # После обработки формы, можно, например, перенаправить пользователя
            return render(request, 'thank_you_page.html')
    else:
        form = FeedbackForm()

    return render(request, 'contacts.html', {'form': form})


