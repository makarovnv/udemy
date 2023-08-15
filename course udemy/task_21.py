class Chain():
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return "Chain with " + str(self.number_of_items)

    def __len__(self):
        return self.number_of_items


chain_1 = Chain(23)
chain_2 = Chain(32)

print(chain_1)
print(chain_2)

print(len(chain_1))
print(len(chain_2))