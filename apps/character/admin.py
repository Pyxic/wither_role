from sqladmin import ModelView

from apps.character.models import Character, Equipment, Race, Region, FamilyFate, ParentFate, FamilySituation, Friend, \
    Relative, ImportantEvent, Profession, Attribute, Skill


class CharacterAdmin(ModelView, model=Character):
    column_list = [Character.id, Character.name]


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
    column_list = [Attribute.id, Attribute.name]


class SkillAdmin(ModelView, model=Skill):
    column_list = [Skill.id, Skill.name]



