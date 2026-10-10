class ElemWater:

    def __add__(self, other):
        if isinstance(other, ElemAir):
            return ElemStorm()
        elif isinstance(other, ElemFire):
            return ElemSteam()
        elif isinstance(other, ElemEarth):
            return ElemDirt()
        else:
            return None


class ElemAir:

    def __add__(self, other):
        if isinstance(other, ElemWater):
            return ElemStorm()
        elif isinstance(other, ElemFire):
            return ElemLightning()
        elif isinstance(other, ElemEarth):
            return ElemDust()
        else:
            return None


class ElemFire:

    def __add__(self, other):
        if isinstance(other, ElemWater):
            return ElemSteam()
        elif isinstance(other, ElemAir):
            return ElemLightning()
        elif isinstance(other, ElemEarth):
            return ElemLava()
        else:
            return None


class ElemEarth:

    def __add__(self, other):
        if isinstance(other, ElemWater):
            return ElemDirt()
        elif isinstance(other, ElemAir):
            return ElemDust()
        elif isinstance(other, ElemFire):
            return ElemLava()
        else:
            return None


class ElemStorm:

    def __str__(self):
        return 'Шторм'


class ElemSteam:

    def __str__(self):
        return 'Пар'


class ElemDirt:

    def __str__(self):
        return 'Грязь'


class ElemLightning:

    def __str__(self):
        return 'Молния'


class ElemDust:

    def __str__(self):
        return 'Пыль'


class ElemLava:

    def __str__(self):
        return 'Лава'


water = ElemWater()
air = ElemAir()
fire = ElemFire()
earth = ElemEarth()

result = water + air
print(f'𖦹 Вода + Воздух = {result}')

result = water + fire
print(f'𖦹 Вода + Огонь = {result}')

result = water + earth
print(f'𖦹 Вода + Земля = {result}')

result = air + fire
print(f'𖦹 Воздух + Огонь = {result}')

result = air + earth
print(f'𖦹 Воздух + Земля = {result}')

result = fire + earth
print(f'𖦹 Огонь + Земля = {result}')
