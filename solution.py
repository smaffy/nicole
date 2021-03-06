class Factory:
    def __init__(self):
        self.all_cakes = []
        self.all_cakes_count = len(self.all_cakes)

    def baking(self, cakes, count, num):
        baking = Cake(num, num)
        cakes.append(baking)
        count += 1

    def bake_cake(self, toppings: int, base: int) -> int:
        cakes = []
        count = 0

        if base != toppings:
            raise WrongIngredientsAmountException

        while toppings > 0 or base > 0:
            if base % 5 == 0:
                baking = Cake(5, 5)
                cakes.append(baking)
                count += 1
                base -= 5
            elif base % 2 == 0:
                baking = Cake(2, 2)
                cakes.append(baking)
                count += 1
                base -= 2
            elif base % 1 == 0:
                baking = Cake(1, 1)
                cakes.append(baking)
                count += 1
                base -= 1
        # self.cakes_amount = cakes
        # return cakes

        # if base > 1:
        #     if base > 4:
        #         a = base // 5
        #         while a:
        #             # cake_type='large'
        #             num = 5
        #             self.baking(cakes, count, num)
        #             # baking = Cake(5, 5)
        #             # cakes.append(baking)
        #             # count += 1
        #             a -= 1
        #         if base % 5:
        #             a = base // 5
        #             b = base - a * 5
        #             if b > 1:
        #                 c = b // 2
        #                 while c:
        #                     # cake_type='medium'
        #                     baking = Cake(2, 2)
        #                     cakes.append(baking)
        #                     count += 1
        #                     c -= 1
        #                 if b % 2:
        #                     # cake_type='basic'
        #                     baking = Cake(1, 1)
        #                     cakes.append(baking)
        #                     count += 1
        #             else:
        #                 # cake_type='basic'
        #                 baking = Cake(1, 1)
        #                 cakes.append(baking)
        #                 count += 1
        #     else:
        #         f = base // 2
        #         while f:
        #             # cake_type='medium'
        #             baking = Cake(2, 2)
        #             cakes.append(baking)
        #             count += 1
        #             f -= 1
        #         if base % 2:
        #             # cake_type='basic'
        #             baking = Cake(1, 1)
        #             cakes.append(baking)
        #             count += 1
        #
        # else:
        #     # cake_type='basic'
        #     baking = Cake(1, 1)
        #     cakes.append(baking)
        #     count += 1
        self.cakes = cakes
        self.all_cakes_count += count
        return count

    def get_last_cakes(self, n: int) -> list:
        last_cakes = []
        if n > 0:
            last_cakes = self.cakes[-n:]
        return last_cakes

    def get_cakes_baked(self) -> list:
        return self.cakes

    def __str__(self):
        num = self.all_cakes_count
        if num == 1:
            return f'Factory with {num} cake.'
        if num > 1:
            return f'Factory with {num} cakes.'


class Cake:
    def __init__(self, base_amount, toppings_amount):
        self.base = base_amount
        self.toppings = toppings_amount
        if base_amount in {1, 2, 5}:
            if base_amount == 5:
                self.cake_type = 'large'
            elif base_amount == 2:
                self.cake_type = 'medium'
            elif base_amount == 1:
                self.cake_type = 'basic'
        else:
            self.cake_type = None
            raise WrongIngredientsAmountException('You have a problem')

    @property
    def type(self):
        return self.cake_type

    def __repr__(self):
        rep = 'Cake(' + self.type + ')'
        return rep

    def __eq__(self, other):
        return self.base == other.base


class WrongIngredientsAmountException(Exception):
    """Wrong Ingredients Amount"""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Wrong Ingredients Amount, {0} '.format(self.message)
        else:
            return 'Wrong Ingredients Amount'
