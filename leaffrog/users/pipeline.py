from django.contrib.auth.models import Group

"""Все авторизованные через github пользователи получают группу social, чтобы иметь возможность
изменить у них поведение в редактировании профиля, а именно убрать возможность изменять пароль
(в любом случае они это сделать не смогут, из-за обязательного введения старого пароля, который формируется
автоматически)"""


def new_users_handler(backend, user, response, *args, **kwargs):
    group = Group.objects.filter(name='social')
    if len(group) and not user.is_superuser:
        user.groups.add(group[0])
