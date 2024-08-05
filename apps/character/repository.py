from sqlalchemy import func, select
from sqlalchemy.orm import load_only, selectinload

from apps.character.models import Attribute, Skill
from base.repository.repository import BaseRepository


class AttributeRepository(BaseRepository):
    model = Attribute

    async def get_attributes_with_skills(self):
        async with self.session_factory() as session:
            subquery = (
                select(Skill.attribute_id).group_by(Skill.attribute_id)
                .having(func.count() > 0)
                .subquery()
            )
            query = select(Attribute).options(selectinload(Attribute.skills))
            query = query.filter(Attribute.id.in_(subquery))
            result = await session.execute(query)
            return result.scalars().all()

