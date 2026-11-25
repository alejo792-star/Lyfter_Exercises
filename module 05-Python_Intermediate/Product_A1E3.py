def show_menu():
    print("-"*30)
    print("⭐️Welcome To Incventory App⭐️")
    print("-"*30)
    print("1.Add product")
    print("2.Show all products")
    print("3.Calculate all inventory")    
    print("4.Exit")

def get_option():
    
        while True:
            try:
                option_menu = int(input("Select a option: "))
                if 1 <= option_menu <= 4:
                    return option_menu
                else:
                    print("please select option (1 to 4)")
                
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    


class Product:
    def __init__(self):
        while True:
            try:
                name = input("Gime a product name").strip()
                if not name:
                    raise ValueError("Product name cannot be empty.")

                price = float(input("Give a product price"))
                amount = float(input("Gime a product Amount"))
                if price <=0 or amount <0:
                    raise ValueError("Price must be greater than zero and quantity cannot be negative. ")
                self.name=name 
                self.price=price
                self.amount=amount
                break
            except ValueError as f:
                print(F"ValueError:{f}")

            

class Inventory:
    def __init__(self):
        self.list_products = []

    def add_product(self,product):
        
        for existing_product in self.list_products:
                if (
                    existing_product.name.lower().strip() == product.name.lower().strip()
                    
                ):
                    existing_product.amount += product.amount
                    print(f"Quantity updated. Existing price kept: {existing_product.price:.2f}")
                    return
                
        self.list_products.append(product)
        print("-"*30)
        print("Product has been added ✅")
        print("-"*30)


    def show_products(self):
        if not self.list_products:
            print("-"*30)
            print(f"{"No products in inventory".upper()}")
            print("-"*30)
            return
        print(f"{"⭐️____INVENTORY____⭐️".center(30)}")
        for existing_product in self.list_products:
            print(f"{"PRODUCT NAME:":<16} {existing_product.name}\n"
                f"{"PRODUCT AMOUNT:":<16}{existing_product.amount}\n"
                f"{"PRODUCT PRICE:":<16}{existing_product.price}\n"
                "----------"

                )
            

    def calculate_total_inventory(self):
        total= 0
        for existing_product in self.list_products:
            total += (existing_product.price*existing_product.amount)
        return total
    
def main ():
    inventary = Inventory()
    while True:
        show_menu()
        user_option=get_option()
        if user_option == 1:
            newproduct = Product()
            inventary.add_product(newproduct)
        elif user_option == 2:
            inventary.show_products()
        elif user_option == 3:
            total_inventary = inventary.calculate_total_inventory()
            print(f"The total in the inventary is {total_inventary}")
        elif user_option == 4:
            print("thanks for using ... good bye ✌️")
            break



if __name__ == "__main__":
    main()