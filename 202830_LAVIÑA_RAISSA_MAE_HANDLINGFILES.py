products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(code):
    code_value = products[code]
    return code_value

def get_property(code, property):
    code_property = products[code][property]
    return code_property

def main():
    customer_order = []

    while(True):
        clerk_input = input("Please input customer's order/s [format: {product_code},{quantity}]:")
        if clerk_input == "/":
            break
        else:
            code_check = clerk_input.split(",")[0]
            qty_check = clerk_input.split(",")[1]

            if code_check in products.keys() and qty_check.isdigit() == True:
                customer_order.append(clerk_input.split(","))
            elif code_check not in products.keys():
                print("Please enter valid product code.")
            elif qty_check.isdigit() == False:
                print("Please enter valid quantity.")

    total = 0
    order_list = []

    for i in customer_order:    
        code = i[0]
        qty = int(i[1])
        product_checker = [code, qty]
        order_list.append(product_checker)
        for j in order_list[:-1]:                     # loop through all elements in order_list except last
            if code in j:
                order_list[order_list.index(j)][1] += qty 
                order_list.remove(product_checker)          
            else:
                pass

    order_list.sort()
    with open("receipt.txt", "a") as receipt:
        receipt.write("==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")
        for i in order_list:
            name = get_property(i[0],"name")
            subtotal = int(get_property(i[0],"price"))*int(i[1])
            print_line = "{:<20} {:<30} {:<27} {:<10}".format(i[0], name, i[1], subtotal)+"\n"
            receipt.write(print_line)
            total += subtotal

        receipt.write(f"\nTotal:\t\t\t\t\t\t\t\t\t\t{total}\n==")
main()
