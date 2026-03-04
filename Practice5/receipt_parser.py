import re

with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice5/raw.txt",
          "r", encoding="utf-8") as file:
    text=file.read()


product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text) # returns a list of strings containing all matches 
                                             #in the order they are found

price_pattern=r"Стоимость\n(\d{1,3}(?:\s\d{3})*,\d{2})"
item_totals=re.findall(price_pattern, text)


total_pattern=r"ИТОГО:\n([\d\s,]+)"
total_match=re.search(total_pattern, text)    #takes two arguments: a pattern and a string.
if total_match:                                 #returns a match object. If not, it returns None.
    total=total_match.group(1)   # returns the part of the string where there is a match  
else: 
    None


datetime_pattern=r"Время:\s*([\d\.]+\s[\d:]+)"
datetime_match=re.search(datetime_pattern, text)
if datetime_match:
    datetime=datetime_match.group(1)  
else:
    None


payment_pattern=r"(Банковская карта|Наличные)"
payment_match=re.search(payment_pattern, text)
if payment_match:
    payment_method=payment_match.group(1)  
else:
    "Unknown"




print(f"{'Product Name':95} {'Item Total':10}")
print("="*110)

for name, price in zip(products, item_totals):
    print(f"{name:90} {price:>15}")

print("="*110)
print(f"{'TOTAL:':91} {total:>15}")
print(f"{'Date & Time:':15} {datetime}")
print(f"{'Payment Method:':15} {payment_method}")