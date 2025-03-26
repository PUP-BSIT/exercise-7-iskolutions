def get_order():
    product_name = input("\nEnter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    return [product_name, price, quantity]
 
def get_customer_details():
    customer_name = input("\nEnter customer name: ")
    senior_id = input("Enter senior ID number (leave blank if none): ")
    
    return [customer_name, senior_id]

def compute_total(order_list, senior_id):
    total = 0
    for order in order_list:
        total += order[1] * order[2]

    if senior_id:
        total *= 0.9
    
    return total

#TODO (Pearl Franco): Display inputs & total, apply discount if senior  

#TODO (Miko Causon): Call functions in order & manage program flow