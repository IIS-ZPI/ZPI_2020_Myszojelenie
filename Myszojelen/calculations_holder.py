class CalculationsHolder:
    id = 0
    state_name = None
    category_name = None
    product_name = None
    product_unit_price = None
    product_selling_price = None
    calculated_price = None
    amount = None

    def __init__(self, state, cat, pronam, prounipr, proselpri, calpri, amount):
        super().__init__()
        self.state_name = state
        self.category_name = cat
        self.product_name = pronam
        self.product_unit_price = prounipr
        self.product_selling_price = proselpri
        self.calculated_price = calpri
        self.amount = amount

    def __str__(self) -> str:
        return "Stan: " + self.state_name + " Kategoria: " + self.category_name + " Produkt: " + self.product_name + "Cena jednostkowa: " + self.product_unit_price + " Cena sprzedaży: " + self.product_selling_price + " Wyliczona marża: " + self.calculated_price

    # porownywanie dopoki nie ogarne jak zrobic sortowania tabeli w htmlu
    def __lt__(self, other):
        return self.product_name < other.product_name

    def setid(self, id_in_list):
        self.id = id_in_list