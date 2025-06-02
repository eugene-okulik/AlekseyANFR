class Flower:
    def __init__(self, name, color, price, life, fresh, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.life = life
        self.fresh = fresh
        self.stem_length = stem_length


class Rose(Flower):
    def __init__(self, color, price, fresh, stem_length):
        super().__init__('Роза', color, price, 7, fresh, stem_length)


class Tulip(Flower):
    def __init__(self, color, price, fresh, stem_length):
        super().__init__('Тюльпан', color, price, 5, fresh, stem_length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_price(self):
        total = 0
        for f in self.flowers:
            total += f.price
        return total
    

    def get_wilt_time(self):
        if len(self.flowers) == 0:
            return 0
        total_life = 0
        for f in self.flowers:
            total_life += f.life
        return total_life / len(self.flowers)

    def sort_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.fresh)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def find_color(self, color):
        result = []
        for f in self.flowers:
            if f.color == color:
                result.append(f)
        return result


rose1 = Rose("red", 100, 8, 30)
rose2 = Rose("white", 80, 9, 25)
tulip = Tulip("yellow", 50, 7, 20)

my_bouquet = Bouquet()
my_bouquet.add_flower(rose1)
my_bouquet.add_flower(rose2)
my_bouquet.add_flower(tulip)

print("Total price:", my_bouquet.get_price())
print("Will wilt in:", my_bouquet.get_wilt_time(), "days")

print("\nSorted by color:")
my_bouquet.sort_by_color()
for f in my_bouquet.flowers:
    print(f"{f.color} {f.name}")


print("\nFind red flowers:")
red_flowers = my_bouquet.find_color("red")
for f in red_flowers:
    print(f"{f.name} - {f.color}")
