stock = {"apple":200,"banana":150,"orange":300}
while True:
    name = input("enter the name : ")
    if name == "done":
        break
    Quantity = int(input("enter your quantity : "))
    if name in stock:
        price = stock [name]
        total = price * Quantity
        print("name ",name)
        print("price",price)
        print("quantity",Quantity)
        print("total",total)
    else:
        print("stock is not found ...")