import enum


class WeaponType(enum.Enum):
    HEAVY = 'HEAVY'
    ASSAULT_RIFLE = 'ASSAULT_RIFLE'
    PISTOL = 'PISTOL'

    @classmethod
    def choices(cls):
        return ((value.name, value.value) for value in cls)


class OrderStatus(enum.Enum):
    PENDING = 'PENDING'
    PACKAGING = 'PACKAGING'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'

    @classmethod
    def choices(cls):
        return ((value.name, value.value) for value in cls)
