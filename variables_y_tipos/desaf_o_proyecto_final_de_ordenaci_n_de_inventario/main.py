# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[:9]
candy2 = items[11:20]
dry_goods = items[22:]
Candy_Aisle = categories[0:11]
Pasta_Aisle = categories[13:]
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
print(f"We have {candy1} for {bubblegum_price} in the {Candy_Aisle} ")
print(f"We have {candy2} for {chocolate_price} in the {Candy_Aisle}")
print(f"We have {dry_goods} for {pasta_price} in the {Pasta_Aisle}")