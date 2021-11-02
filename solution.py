class Factory:
    cakes = []

    def __init__(self):
        pass

    def bake_cake(self, toppings: int, base: int) -> int:
        cakes = []
        count = 0
        try:
            if base != toppings:
                raise WrongIngredientsAmountException

            if base > 1:
                if base > 4:
                    a = base // 5
                    while a:
                        baking = Cake(base, toppings, cake_type='large')
                        cakes.append(baking)
                        count += 1
                        a -= 1
                    if base % 5:
                        a = base // 5
                        b = base - a * 5
                        if b > 1:
                            c = b // 2
                            while c:
                                baking = Cake(base, toppings, cake_type='medium')
                                cakes.append(baking)
                                count += 1
                                c -= 1
                            if b % 2:
                                baking = Cake(base, toppings, cake_type='basic')
                                cakes.append(baking)
                                count += 1
                        else:
                            baking = Cake(base, toppings, cake_type='basic')
                            cakes.append(baking)
                            count += 1
                else:
                    a = base // 2
                    while a:
                        baking = Cake(base, toppings, cake_type='medium')
                        cakes.append(baking)
                        count += 1
                        a -= 1
                    if base % 2:
                        baking = Cake(base, toppings, cake_type='basic')
                        cakes.append(baking)
                        count += 1

            else:
                baking = Cake(base, toppings, cake_type='basic')
                cakes.append(baking)
                count += 1
            self.cakes = cakes
        except:
            pass
        return count

    def get_last_cakes(self, n: int) -> list:
        last_cakes = []
        if n > 0:
            last_cakes = self.cakes[-n:]
        return last_cakes

    def get_cakes_baked(self) -> list:
        return self.cakes

    def __str__(self):
        pass


class Cake:

    def __init__(self, base_amount, toppings_amount, cake_type='basic'):
        self.base = base_amount
        self.toppings = toppings_amount
        self.cake_type = cake_type

    @property
    def type(self):
        return self.cake_type

    def __repr__(self):
        rep = 'Cake(' + self.type + ')'
        return rep

    def __eq__(self, other):
        pass


class WrongIngredientsAmountException(Exception):
    """Wrong Ingredients Amount"""
    pass

    # def __init__(self, message="):
    #     self.message = message
    #     super().__init__(self.message)
    #
    # def __str__(self):
    #     return self.message