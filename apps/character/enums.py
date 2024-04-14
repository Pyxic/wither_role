import enum


class SocialStatus(enum.Enum):
    EQUALITY = "equality"
    TOLERANCE = "tolerance"
    FEAR = "fear"
    HATE = "hate"


class RegionType(enum.Enum):
    NORTH = "Kingdom of the North"
    NILFGAARD = "Nilfgaard"
    ENDER_NATIONS = "Lands of the Elder Nations"


class ParentFateType(enum.Enum):
    MOTHER = "Mother"
    Father = "Father"
    BOTH = "Both"


class GenderType(enum.Enum):
    MALE = "male"
    FEMALE = "female"


class AgeType(enum.Enum):
    ELDER = "elder"
    YOUNGER = "younger"
    TWIN = "twin"


class AttitudeType(enum.Enum):
    WISH_DEAD = "wishes you dead"
    HATE_YOU = "hate you"
    ENVIES_YOU = "envies you"
    NO_BIG_DEAL = "no big deal"
    LOVE_YOU = "love you"
    EQUALS_YOU = "equals you"
    JEALOUS_OF_YOU = "jealous of you"


class CharacterTraitType(enum.Enum):
    MODESTY = "modesty"
    AGGRESSION = "aggression"
    KINDNESS = "kindness"
    FREAKY = "freaky"
    THOUGHTFULNESS = "thoughtfulness"
    CHATTINESS = "chattiness"
    ROMANTICISM = "romanticism"
    SEVERITY = "severity"
    DESPONDENCY = "despondency"
    INFANTILIZATION = "infantilization"


class ImportantEventType(enum.Enum):
    FORTUNE_OR_MISFORTUNE = "Fortune or misfortune"
    ALLIES_OR_ENEMIES = "Allies or enemies"
    LOVE = "Love"