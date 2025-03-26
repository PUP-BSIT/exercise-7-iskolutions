CONTINUE_OPTION = 'y'
EXIT_OPTION = 'n'

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

def display_order(order_list, customer_name, senior_id, grand_total):
    print("\nOrder Details:\n")
    for order in order_list:
        print(f"Item:\t\t{order[0]}")
        print(f"Price:\t\t{order[1]}")
        print(f"Quantity:\t{order[2]}")
        print(f"Total:\t\t{order[1] * order[2]}\n")

    print(f"\nCustomer Name: {customer_name}")
    print(f"Senior ID: {senior_id}")
    
    if senior_id:
        print("A 10% senior discount has been applied.")

    print(f"\nGrand Total: {grand_total}")

def main():
    order_list = []
    choice = CONTINUE_OPTION
    
    while choice == CONTINUE_OPTION:
        order_list.append(get_order())
        choice = input("Add another item? (y/n): ").lower()
    
    customer_name, senior_id = get_customer_details()
    grand_total = compute_total(order_list, senior_id)
    display_order(order_list, customer_name, senior_id, grand_total)
    
main()