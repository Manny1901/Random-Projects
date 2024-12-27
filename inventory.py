products = {
    "ps5":3,
    "iphone 14":4,
    "iphone 15":5,
    "dolls":20,
    "lego":15,
    "robot":32
}
name  = input("what should be the name of the file")
file = open(f"{name}.txt","w")
file.write(str(products))
file.close()
print("to add product select a to update stock select u to check quantity select c")
while True:
    question = input("what operation do you want to perform").capitalize()
    if question=="A":
        add = (input("what product do you want to add "))
        quantity = int(input("what is the quantity"))
        products[add] = quantity
    if question == "U":
        print("select a product in the catalogue")
        selection = input("what did you select").lower()
        change = (int(input("what do you want to add or subtract")))
        if selection in products:
            products[selection]+=change
        else:
            print("product does not exist")
    if question == "C":
        print("here are the products")
        print(products)



