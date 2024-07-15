from dependency_injector.wiring import Provide

from apps.character.enums import AttributeType, SocialStatus, RegionType, ImportantEventType
from apps.character.repository import AttributeRepository
from base.repository.repository import BaseRepository
from config.registry import Registry


class ProjectInitialization:

    @classmethod
    async def start(cls, app):
        await cls.create_races()
        await cls.create_region()
        await cls.create_family_fate()
        await cls.create_parent_fate()
        await cls.create_family_situation()
        await cls.create_friend()
        await cls.create_important_events()
        await cls.create_attributes()

    @classmethod
    async def create_races(
            cls, race_repository: BaseRepository = Provide[Registry.character_container.race_repository]
    ):
        if not await race_repository.exists():
            items = [
                {
                    "name": "Люди",
                    "description": "Lorem",
                    "social_status": SocialStatus.EQUALITY,
                },
                {
                    "name": "Эльфы",
                    "description": "Lorem",
                    "social_status": SocialStatus.HATE,
                },
                {
                    "name": "Краснолюды",
                    "description": "Lorem",
                    "social_status": SocialStatus.TOLERANCE,
                },
                {
                    "name": "Ведьмаки",
                    "description": "Lorem",
                    "social_status": SocialStatus.HATE,
                },
                {
                    "name": "Маги",
                    "description": "Lorem",
                    "social_status": SocialStatus.HATE,
                },
            ]
            await race_repository.bulk_create(items)

    @classmethod
    async def create_region(cls, region_repository: BaseRepository = Provide[
        Registry.character_container.region_repository]):
        if not await region_repository.exists():
            items = [
                {
                    "name": "Королевства севера",
                    "region_type": RegionType.NORTH
                },
                {
                    "name": "Нильфгард",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "name": "Старшие народы",
                    "region_type": RegionType.ENDER_NATIONS,
                },
            ]
            await region_repository.bulk_create(items)

    @classmethod
    async def create_family_fate(cls, repository: BaseRepository = Provide[
        Registry.character_container.family_fate_repository]):
        if not await repository.exists():
            items = [
                {
                    "description": "Из-за войн ваша семья была вынуждена разделиться, и вы не знаете, где большинство родственников.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Вашу семью посадили в тюрьму за преступление или по ложному обвинению. Вы единственный, кому удалось сбежать. И теперь вы хотите освободить родных... или не хотите?",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Дом вашей семьи проклят. Либо на полях нет урожая, либо в комнатах бродит дух. Оставаться там слишком опасно.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Из-за войн ваша семья оказалась вынуждена покинуть дом. Вам пришлось встать на пути преступности.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Ваша семья в долгах из-за азартных игр или займов. Вам очень нужны деньги.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Ваша семья в ссоре с другой семьей. Возможно, вы даже не помните, с чего всё началось.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "По какой-то причине вашу семью ненавидят в родном городе, и никто не хочет иметь дела с вашими родственниками.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Однажды вашу семью дочиста ограбила банда разбойников. Всех ваших родных зарезали, вы единственный выживший.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "В вашей семье есть злодейская тайна. Если о ней кто-то узнает, вас убьют. Вы можете скрывать эту тайну сами или оставить это на совесть ведущего.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Член вашей семьи предал вас и теперь работает на врага. Он говорит другие вещи за вашей спиной, и если брат предаст вас, ваши родные не сомневаются.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Ваша семья обращена в рабство за преступление против Империи или по ложному обвинению. Только вам удалось сбежать.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Вашу семью изгнали в пустыню Корат, и, скорее всего, большую часть ночей вы проводили в попытках выжить в этих суровых условиях.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Вашу семью убил метежный маг, когда вы были маленькими. Ни следов, ни криков, ни крови.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Вы не знаете, где ваши родственники. Все, что осталось — это обрывки воспоминаний.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Вашу семью казнили за государственную измену. Только вам удалось избежать столь мрачной участи.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "По какой-то причине вашу семью лишили всех титулов. Вы оказались на улице и вынуждены выживать среди простолюдинов.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Ваш родственник-маг заплатил свою жизнь, чтобы дать вам какой-то магический дар, словно проклятье.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Война очередной раз вас искала на службе Империи. Те, что вы знали, как свои пять пальцев, были найдены мертвыми.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Считается, что ваша семья симпатизирует людям, поэтому ваши родственники не очень любят на родине.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Ваши родные стали изгоями из-за того, что не согласны с мнением большинства, и вас практически не упоминали. Ваша семья не разорялась.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Ваша семья погибла в войне против людей. Нильфгаардская армия уже занимает города, и ваша жизнь стоит того, чтобы выжить в их покровительстве.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Ваша семья была убита за вздор. Возможно, вы один в этом доме. Возможно, выжили двое-трое, но семья вашей любви сломалась и вы оказались вынуждены.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "По какой-то причине вашу семью выселили из дома, и вы её конечный кончик концами.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Когда вы были совсем юны, ваша семья совершала набеги на человеческие города, чтобы добыть еду или, возможно, убивать людей.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "В доме вашей семьи поселилось проклятие, и все умерли, кроме вас. И с тех пор вы вынуждены бежать против людей.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Ваша семья разбрасывается из-за несчастного случая. Возможно, вашего единственного члена осудили за преступление, а другого — не нашли.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один из ваших предков был убит людьми за то, что оказался (или казалось) поддерживать предательство, либо вышли из суда сами.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Одна из ваших предков убили при попытке предательства. Осталась только горькая память, и вы не в силах признать преданность и жить среди семьи, которые не так любят.",
                    "region_type": RegionType.ENDER_NATIONS
                }
            ]
            await repository.bulk_create(items)

    @classmethod
    async def create_parent_fate(cls, repository: BaseRepository = Provide[
        Registry.character_container.parent_fate_repository]):
        if not await repository.exists():
            items = [
                {
                    "description": "Один или оба ваших родителя погибли во время войны с Нильфгаардом. Скорее всего, это был отец, но мать также могла сражаться или стать жертвой войны.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Родители бросили вас в лесу. Возможно, семья не могла прокормить ещё один рот, а может, это была случайность.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителя попали под магический кон или взорвались от ярости колдуна.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Родители продали вас за золото или оказались в плену у Нильфгаарда. Похоже, деньги были им нужнее, чем вы.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителя вступили в банду. Вы часто встречались с членами той банды, а порой были вынуждены на неё работать.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителей были чудовищем. Решите сами, что это была за тварь.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителей казнены по ложному обвинению. Вы стали孤孤ник",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителей умерли от чумы. Болезнь была неизлечима, оставив лишь мертвенные страдания.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителей проданы в рабство в Нильфгаарде. Вы никогда не видели их снова.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Один или оба ваших родителей обманули вас ради золота. Скорее всего, вы были преданы королевской семье или брату, или же вас сбили с пути.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Ваш отец погиб в одной из Северных войн. Возможно, он уже был военным или же его призвали на службу, когда началась война.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей отравили. Возможно, это хотели убрать их с пути.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Тайная полиция забрала кого-то из ваших родителей и оставила на дороге. Неделю спустя он был найден мертвым.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей посадили за незаконное перемещение магии — либо за истинное преступление, либо по навету.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей изгнали в пустыню Корат. Они не смогли выжить в этих суровых условиях.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей проклял маг. Скорее всего, он хотел таким образом отомстить.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей осудили за ложное обвинение и убили. Вы живёте, чтобы отомстить.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Однажды ваши родители попали в рабство и исчезли. Вероятно, вы больше никогда их не увидите.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей продали в рабство за преступление против Империи или по ложному доносу.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей похитили и держат в рабстве, пока вы служите императору.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Одного или обоих ваших родителей считают членами банды скоя’таэлей, из-за чего на них косо смотрят.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Одного или обоих ваших родителей предали свои народ и стали членами Стражи Народов. Вам так что им не рады на родине.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя одержимы восстановлением былой славы своего народа и жертвуют всем ради этой цели.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя изгнаны с родины за несогласие с мнением большинства и желают кого-либо обвинить в своём положении.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя прокляты колдуном. Выберите эффект и принимайте на усмотрение ведущего.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Ваши родители отдали вас друзьям на воспитание из-за того, что верили в плохие предзнаменования и не могли позаботиться о вас.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя попали в рабство к людям за преступление против Империи или по ложному доносу.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя предали вас ради достижения цели, требующей жертвоприношений.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя убили и сожгли за предательство, оставив вас сиротой.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Один или оба ваших родителя преданы своим народом за измену, и вы не в силах признать преданность и жить среди тех, кто вас предал.",
                    "region_type": RegionType.ENDER_NATIONS
                }
            ]
            await repository.bulk_create(items)

    @classmethod
    async def create_family_situation(
            cls, repository: BaseRepository = Provide[Registry.character_container.family_situation_repository]
    ):
        if not await repository.exists():
            items = [
                {
                    "description": "Аристократия: Вы выросли в богатом особняке, где слуги исполняли любую вашу прихоть. От вас ожидали хорошего поведения и умения производить впечатление. Начальное снаряжение: дворянская грамота (+2 к репутации).",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Под опекой мага: В юном возрасте вас отдали под опеку мага. Вы жили в комфортных условиях, но обучение магии практически не прекращалось. Начальное снаряжение: талисман (+1 к Образованию).",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Рыцарство: Вы жили в особняке, где из вас растили настоящего лорда или леди. Ваша судьба была предрешена с рождения. Начальное снаряжение: личный герб (+1 к репутации).",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Семья торговцев: Вы выросли в купеческой среде, под крики продавцов и звон монет. Начальное снаряжение: 2 знакомства.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Семья мастеров: Вы выросли в ремесленной мастерской, где каждый день слышали звук молотков или других инструментов. Начальное снаряжение: 2 набора чертежей/формул.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Семья артистов: Вы выросли в актёрской труппе. Возможно, вы вместе с ними путешествовали и даже выступали на сцене. Начальное снаряжение: личный инструмент и друг.",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Крестьянская семья: Вы выросли в сельской местности, помогая семье выращивать урожай. Начальное снаряжение: статуэтка или талисман (+1 к Удаче).",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Аристократия: Вы выросли в богатом особняке, где вас неплохо научили навыкам этикета и ведению интриг. Роскошная служба лишь стимулировала эти умения. Начальное снаряжение: дворянская грамота (+2 к репутации).",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Высшее жречество: Ваши родители были жрецами великих богов. Вас учили религии, медитациям и благословениям. Теперь вы сами нашли путь. Начальное снаряжение: священный символ (+1 к Храбрости).",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Рыцарство: Вы росли, зная, что ваш долг — служить Императору и идти по его стопам. Награда за будущую службу. Начальное снаряжение: личный герб (+1 к репутации).",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Семья мастеров: Вы выросли в мастерской, учась создавать вещи, которые продают ваши родители. Вы освоили ремесло и узнали цену мастерству. Начальное снаряжение: 2 набора чертежей/формул.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Семья торговцев: Вы росли, продавая товары на рынке. Вы научились работать с клиентами и обладаете обширными связями. Начальное снаряжение: 2 знакомства.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Рабство: Вы родились рабом. Жизнь в рабстве научила вас многому. Начальное снаряжение: знание темных умений.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Семья аристократов: Вы выросли в семье аристократов, где навыки и знания передавались от поколения к поколению. Начальное снаряжение: личный инструмент и друг.",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Крестьянская семья: Вы выросли на ферме, помогая родителям растить урожай и заботиться о животных. Начальное снаряжение: статуэтка или талисман (+1 к Удаче).",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Аристократия: Вы выросли во дворе, где вас постоянно напоминали о славных прошлых временах, чтобы быть достойным своих предков. Начальное снаряжение: дворянская грамота (+2 к репутации).",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Благородный воин: Ваши родители были воинами. Вы взяли их кодекс чести и обучение, чтобы стать настоящим воином. Начальное снаряжение: личный герб (+1 к репутации).",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Семья торговцев: Вы выросли в семье странствующих торговцев. Хотя жизнь была трудна, вы создали широкую сеть контактов и узнали цену торговле. Начальное снаряжение: 2 знакомства.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Семья грамотеев: Вы выросли в семье грамотеи. Ваши близкие всё знали про древние рукописи и язык истории. Начальное снаряжение: статуэтка или талисман (+1 к Образованию).",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Артисты: . Начальное снаряжение: 1 музыкальный инструмент и 1 друг.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Артисты: . Начальное снаряжение: 1 музыкальный инструмент и 1 друг.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Семья мастеров: . Начальное снаряжение: 3 обычных чертежа/формулы.",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Низкое происхождение: Вы выросли в бедности и жестокой борьбе за выживание. Начальное снаряжение: статуэтка или талисман (+1 к Удаче).",
                    "region_type": RegionType.ENDER_NATIONS
                },
            ]
            await repository.bulk_create(items)

    @classmethod
    async def create_friend(cls, repository: BaseRepository = Provide[Registry.character_container.friend_repository]):
        if not await repository.exists():
            items = [
                {
                    "description": "На вас сильно повлияла местная религия. Вы ежедневно проводили много часов в церкви. Снаряжение: священный текст",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Культ Великого Солнца оказал на вас сильное влияние. Вы постоянно ходили на их ритуалы и исповеди. Снаряжение: церемониальная маска",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Человек. Наибольшее влияние на вас оказал человек, благодаря которому вы узнали, что расами не всегда можно основываться. Снаряжение: соломенная кукла",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Вдохновленным вам служит ремесленник, научивший ценить искусство и мастерство. Снаряжение: изготовленный им сувенир",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Наибольшее влияние на вас оказал знатный аристократ, научивший вас этикету. Снаряжение: драгоценный подарок",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Вдохновленным вам служит ремесленник, научивший ценить искусство Старших Народов. Снаряжение: изготовленный им сувенир",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Граф. Наибольшее влияние на вас оказал граф (родственник, научивший брать с себя пример). Снаряжение: серебряное кольцо",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Граф. Наибольшее влияние на вас оказал граф, научивший вас этикету и осторожности. Снаряжение: серебряное кольцо",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Благородный воин. Наибольшее влияние на вас оказал благородный воин, научивший вас гордости и правилам этикета. Снаряжение: кольцо-печатка",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Маг. Наибольшее влияние оказал маг, научивший не бояться магии и не подвергать сомнению. Снаряжение: подвеска",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Следователь. Наибольшее влияние на вас оказал имперский детектив. Вы провели много времени в разгадывании тайн. Снаряжение: эмблема",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Мудрец. Наибольшее влияние на вас оказал мудрец, научивший вас законам Старших Народов. Снаряжение: серебряное украшение",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Ведьма. Наибольшее влияние на вас оказала деревенская ведьма, показавшая ценность знаний. Снаряжение: кукла для чёрной магии",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Следователь. Наибольшее влияние на вас оказал имперский детектив, научивший вас искусству шпионажа. Снаряжение: лупа",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Человек. Наибольшее влияние на вас оказал человек, благодаря которому вы узнали, что расы не так важны. Снаряжение: вещь умершего отца",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Проходимец. Наибольшее влияние на вас оказал человек, встретивший вас на жизненном пути. Снаряжение: нож",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Охотник на монстров. Наибольшее влияние на вас оказал охотник на монстров, научивший вас обороне. Снаряжение: лук",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Охотник. Наибольшее влияние на вас оказал охотник, обучивший вас выслеживанию. Снаряжение: нож",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Артист. Наибольшее влияние на вас оказал артист, что научил вас искусству и тому, как правильно себя вести. Снаряжение: приглашение на бал",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Артист. Наибольшее влияние на вас оказал певец, научивший вас манерам. Снаряжение: маска",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Артист. Наибольшее влияние на вас оказал артист, научивший вас красноречию. Снаряжение: пьеса",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Торговец. Наибольшее влияние оказал человек, научивший вас торговле и сообразительности. Снаряжение: амулет",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Разумное существо. Наибольшее влияние на вас оказало разумное существо, научившее вас, что не все животные - звери. Снаряжение: амулет",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Охотник. Наибольшее влияние на вас оказал охотник, научивший вас выслеживать. Снаряжение: нож",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Преступник. Наибольшее влияние на вас оказал преступник, научивший вас, как себя обезопасить. Снаряжение: маска",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Преступник. Наибольшее влияние на вас оказал преступник, научивший вас, как не попадаться. Снаряжение: маска",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Крестьянин. Наибольшее влияние на вас оказал крестьянин, обучивший вас выживать. Снаряжение: крестьянская лопата",
                    "region_type": RegionType.ENDER_NATIONS
                },
                {
                    "description": "Воин. Наибольшее влияние на вас оказал солдат, научивший вас бою. Снаряжение: боевой трофей",
                    "region_type": RegionType.NORTH
                },
                {
                    "description": "Воин. Наибольшее влияние на вас оказал солдат, обучивший вас боевым техникам. Снаряжение: боевой трофей",
                    "region_type": RegionType.NILFGAARD
                },
                {
                    "description": "Крестьянин. Наибольшее влияние на вас оказал крестьянин, научивший вас жизни. Снаряжение: крестьянская лопата",
                    "region_type": RegionType.ENDER_NATIONS
                }
            ]
            await repository.bulk_create(items)

    @classmethod
    async def create_important_events(cls, repository: BaseRepository = Provide[Registry.character_container.important_event_repository]):
        if not await repository.exists():
            items = [
                {
                    "description": "Джекпот: Благодаря какому-то событию или по счастливой случайности вы получаете 1d10×100 крон.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Учитель: Вы обучались под опекой учителя. Получите +1 к любому навыку Инт или же выберите новый навык Инт с бонусом +2.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Благодарность дворянина: Вы что-то сделали для дворянина, и теперь он вам должен 1 услугу.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Боевой инструктор: Вы учились боевым искусствам у настоящего воина. Получите +1 к любому боевому навыку или же выберите новый боевой навык с бонусом +2.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Благодарность ведьмака: Как-то раз вы выручили ведьмака и оказали ему услугу. Теперь он вам должен услугу в ответ.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Дружба с разбойниками: Вы подружились с разбойнической шайкой. Раз в месяц вы можете попросить их об 1 услуге.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Приручённый зверь: Вы сумели приручить дикое животное. Совершите бросок 1d10: от 1 до 7 — это дикая собака (см. параметры собак на стр. 310), от 8 до 10 — волк (см. стр. 286).",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Благодарность мага: Могущественный маг, которому вы помогли, должен вам 1 услугу.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Благословение мера: У вас есть священный символ. Вы можете пожертвовать его, если понадобится помощь. Получите постоянный бонус +2 к Харизме при общении с ним.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Рыцарская честь: В случайно выбранном королевстве за вас заступился рыцарь. Вы можете рассчитывать на его поддержку в этом королевстве.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Долг: Вы задолжали 1d10×100 крон.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Заключение: За какое-то преступление (или по ложному обвинению) вы попали в тюрьму на 1d10 месяцев.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Зависимость: У вас есть зависимость на ваш выбор. См. правила зависимости на полях.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Любимый, друг или родственник убит: Сделайте бросок 1d10: от 1 до 5 — это был несчастный случай; от 6 до 8 — убит чудовищем; и 9 или 10 — убит разбойниками.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Ложное обвинение: Сделайте бросок 1d10: от 1 до 3 — воровство; 4 или 5 — трусость или предательство; от 6 до 8 — убийство; 9 — изнасилование; 10 — нелегальное колдовство.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "В розыске: Сделайте бросок 1d10. Вас разыскивают... От 1 до 3 — несколько странников; от 4 до 6 — в поиске 7 или 8 — в городе; 9 или 10 — во всём королевстве.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Предательство: Сделайте бросок 1d10: от 1 до 3 — вас шантажируют; от 4 до 7 — ваша тайна раскрыта; от 8 до 10 — вас предал кто-то из близких.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Несчастный случай: Сделайте бросок 1d10: от 1 до 4 — вы изуродованы, измените ваш социальный статус на опальный; 5 или 6 — вы лишились 1d10 месяцев; 7 или 8 — вы потеряли память о 1d10 месяцах того года; 9 или 10 — вы начали жуткие кошмары (с вероятностью 7 из 10 каждую ночь по время сна).",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Физическая или психическая травма: Сделайте бросок 1d10: от 1 до 3 — вас отравили, нанеся потерю 5 ПЗ; от 4 до 7 — вы страдаете от панических атак и должны испытать Устойчивость (каждые 5 дней) в стрессовой ситуации; от 8 до 10 — вас захватили, вы попали в рабство, были ранены, лишены речи или слуха, нарушена память, тело или голос, за которое отвечает ведущий.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                },
                {
                    "description": "Проклятие: Вас прокляли. Подробнее см. раздел «Проклятия» на стр. 230.",
                    "event_type": ImportantEventType.FORTUNE_OR_MISFORTUNE
                }
            ]

    @classmethod
    async def create_attributes(cls, attribute_repository: AttributeRepository = Provide[
        Registry.character_container.attribute_repository]):
        print(await attribute_repository.exists())
        if not await attribute_repository.exists():
            attributes = [
                {
                    "name": "Интеллект",
                    "short_name": "Инт",
                    "description": "Решение загадок, проведение научных исследований, дедукция и прочие занятия, "
                                   "требующие умственных усилий.",
                    "code": AttributeType.INTELLIGENCE
                },
                {
                    "name": "Реакция",
                    "short_name": "Реа",
                    "description": "Необходимо в бою для уклонения от ударов и для занятий требующих быстрой "
                                   "реакции и точных движений",
                    "code": AttributeType.REACTION
                },
                {
                    "name": "Ловкость",
                    "short_name": "Лвк",
                    "description": "Lorem",
                    "code": AttributeType.DEXTERITY
                },
                {
                    "name": "Телосложение",
                    "short_name": "Тел",
                    "description": "Lorem",
                    "code": AttributeType.PHYSIQUE
                },
                {
                    "name": "Скорость",
                    "short_name": "Скор",
                    "description": "Lorem",
                    "code": AttributeType.SPEED,
                },
                {
                    "name": "Эмпатия",
                    "short_name": "Эмп",
                    "description": "Lorem",
                    "code": AttributeType.EMPATHY
                },
                {
                    "name": "Ремесло",
                    "short_name": "Рем",
                    "description": "Lorem",
                    "code": AttributeType.CRAFT
                },
                {
                    "name": "Воля",
                    "short_name": "Воля",
                    "description": "Lorem",
                    "code": AttributeType.VOLITION
                },
                {
                    "name": "Удача",
                    "short_name": "Удч",
                    "description": "Lorem",
                    "code": AttributeType.LUCK,
                },
                {
                    "name": "Энеогия",
                    "short_name": "Энг",
                    "description": "Lorem",
                    "code": AttributeType.ENERGY
                },
                {
                    "name": "Устойчивость",
                    "short_name": "Ус",
                    "description": "Lorem",
                    "code": AttributeType.SUSTAINABILITY
                },
                {
                    "name": "Бег",
                    "short_name": "Бег",
                    "description": "Lorem",
                    "code": AttributeType.RUNNING
                },
                {
                    "name": "Прыжок",
                    "short_name": "Прж",
                    "description": "Lorem",
                    "code": AttributeType.JUMPING
                },
                {
                    "name": "Пункты здоровья",
                    "short_name": "ПЗ",
                    "description": "Lorem",
                    "code": AttributeType.HEALTH_POINTS
                },
                {
                    "name": "Выносливость",
                    "short_name": "Вын",
                    "description": "Lorem",
                    "code": AttributeType.STAMINA
                },
                {
                    "name": "Переносимый вес",
                    "short_name": "Вес",
                    "description": "Lorem",
                    "code": AttributeType.TRANSFERABLE_WEIGHT
                },
                {
                    "name": "Отдых",
                    "short_name": "Отд",
                    "description": "Lorem",
                    "code": AttributeType.REST
                },
                {
                    "name": "Удар рукой",
                    "short_name": "уд рк",
                    "description": "Lorem",
                    "code": AttributeType.PUNCH
                },
                {
                    "name": "Удар ногой",
                    "short_name": "Уд нu",
                    "description": "Lorem",
                    "code": AttributeType.KICK
                },
            ]
            await attribute_repository.bulk_create(attributes)
