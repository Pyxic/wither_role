from apps.character.models import Attribute
from base.repository.repository import BaseRepository


class AttributeRepository(BaseRepository):
    model = Attribute
