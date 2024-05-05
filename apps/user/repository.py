from apps.user.models import User
from base.repository.repository import BaseRepository


class UserRepository(BaseRepository):
    model = User
