def menu_not_auth(request):
    menu = [{'title': 'Каталог', 'url_name': 'catalog'},
            {'title': 'Карзина', 'url_name': 'users:cart'},
            {'title': 'Войти', 'url_name': 'users:login'},
            {'title': 'Регистрация', 'url_name': 'users:reg'}
            ]
    return {'menu_not_auth': menu}


def menu_is_auth(request):
    menu = [{'title': 'Каталог', 'url_name': 'catalog'},
            {'title': 'Избранное', 'url_name': 'users:favourites'},
            {'title': 'Корзина', 'url_name': 'users:cart'},
            {'title': 'Профиль', 'url_name': 'users:profile'},
            {'title': 'Выйти', 'url_name': 'users:logout'}
            ]
    return {'menu_is_auth': menu}


