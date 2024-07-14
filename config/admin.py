from sqladmin import Admin

from apps.user.admin import UserAdmin
from apps.character.admin import (CharacterAdmin, EquipmentAdmin, RaceAdmin, RegionAdmin, FamilyFateAdmin,
                                  ParentFateAdmin, FamilySituationAdmin, FriendAdmin, RelativeAdmin,
                                  ImportantEventAdmin, ProfessionAdmin, AttributeAdmin,
                                  SkillAdmin
                                  )
from config.database import db_helper


def admin_router(app):
    admin = Admin(app, db_helper.engine)
    admin.add_view(UserAdmin)
    admin.add_view(CharacterAdmin)
    admin.add_view(EquipmentAdmin)
    admin.add_view(RaceAdmin)
    admin.add_view(RegionAdmin)
    admin.add_view(FamilyFateAdmin)
    admin.add_view(ParentFateAdmin)
    admin.add_view(FamilySituationAdmin)
    admin.add_view(FriendAdmin)
    admin.add_view(RelativeAdmin)
    admin.add_view(ImportantEventAdmin)
    admin.add_view(ProfessionAdmin)
    admin.add_view(AttributeAdmin)
    admin.add_view(SkillAdmin)
