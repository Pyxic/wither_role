from sqladmin import ModelView

from apps.user.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]
