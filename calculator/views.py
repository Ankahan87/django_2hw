from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def ret_ingridients_dict(name = "", persons=0):
	dict_result = DATA[name]
	result = {}
	if persons !=0:
		keys = dict_result.keys()
		for key in keys:
			try:
				int_res = int(dict_result[key])
				dict_result[key] = int_res*persons
			except:
				int_res = 0
	result['recipe'] = dict_result
	return result

def omlet(request):
	servings = request.GET.get('servings')
	try:
		persons = int(servings)
	except:
		persons = 0
	result = ret_ingridients_dict('omlet', persons)
	return render(request, 'calculator/index.html', result)

def pasta(request):
	servings = request.GET.get('servings')
	try:
		persons = int(servings)
	except:
		persons = 0
	result = ret_ingridients_dict('pasta', persons)
	return render(request, 'calculator/index.html', result)

def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Рецепт омлета': reverse('omlet'),
        'Рецепт спагетти': reverse('pasta')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)