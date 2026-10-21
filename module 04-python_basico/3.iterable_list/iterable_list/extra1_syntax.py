product_cost = float(input("Enter the product cost:💲"))
if product_cost < 100:
    discount = product_cost * 0.02
else:
    discount = product_cost * 0.1
final_cost = product_cost - discount
print(f"The product cost is: {product_cost:.2f}")
print(f"The final cost after discount is: {final_cost:.2f} 😎")
print(f"The discount applied is: {discount:.2f}")
print("Thank you for using the discount calculator!😊")
