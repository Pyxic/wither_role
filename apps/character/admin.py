from sqladmin import ModelView
from wtforms.fields.numeric import IntegerField
from wtforms.form import Form
from wtforms.validators import DataRequired

from apps.character.models import Character, Equipment, Race, Region, FamilyFate, ParentFate, FamilySituation, Friend, \
    Relative, ImportantEvent, Profession, Attribute, Skill, CharacterAttribute, CharacterSkill


class CharacterAdmin(ModelView, model=Character):
    column_list = [
        Character.id, Character.name, Character.age, Character.user_id,
        Character.profession_id, Character.race_id, Character.region_id
    ]
    column_searchable_list = ['name']
    column_filters = ['age', 'user_id', 'profession_id', 'race_id', 'region_id']

    form_columns = [
        'name', 'age', 'user_id', 'parent_fate_type', 'clothes', 'hairstyle',
        'jewelry', 'who_is_valued', 'what_value', 'thinks_about_people',
        'profession_id', 'race_id', 'region_id', 'family_fate_id',
        'parent_fate_id', 'family_situation_id', 'friend_id', 'character_attributes'
    ]

    # Дополнительные формы для атрибутов и навыков
    inline_models = [
        CharacterAttribute, CharacterSkill
    ]


class EquipmentAdmin(ModelView, model=Equipment):
    column_list = [Equipment.id, Equipment.name]


class RaceAdmin(ModelView, model=Race):
    column_list = [Race.id, Race.name]


class RegionAdmin(ModelView, model=Region):
    column_list = [Region.id, Region.name]


class FamilyFateAdmin(ModelView, model=FamilyFate):
    column_list = [FamilyFate.id, FamilyFate.description]


class ParentFateAdmin(ModelView, model=ParentFate):
    column_list = [ParentFate.id, ParentFate.description]


class FamilySituationAdmin(ModelView, model=FamilySituation):
    column_list = [FamilySituation.id, FamilySituation.description]


class FriendAdmin(ModelView, model=Friend):
    column_list = [Friend.id, Friend.description]


class RelativeAdmin(ModelView, model=Relative):
    column_list = [Relative.id, Relative.age]


class ImportantEventAdmin(ModelView, model=ImportantEvent):
    column_list = [ImportantEvent.id]


class ProfessionAdmin(ModelView, model=Profession):
    column_list = [Profession.id, Profession.name]


class AttributeAdmin(ModelView, model=Attribute):
    column_list = [Attribute.id, Attribute.short_name, Attribute.name, Attribute.code]


class SkillAdmin(ModelView, model=Skill):
    column_list = [Skill.id, Skill.name]



