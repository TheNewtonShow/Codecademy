lovely_lovesesat = "lovely loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
Lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
Luxurious_lamp = 52.15
sales_tax = 0.088
customer_one_total = 30
customer_one_itemization = "1x Lovely loveseat, 1x Luxurious lamp"
customer_one_tax = customer_one_total * sales_tax
customer_one_tax += sales_tax
customer_one_tax += customer_one_total

print("Customer One Items")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_tax)