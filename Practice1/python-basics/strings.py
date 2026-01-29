a = "Hello, World!"
print(a[1], len(a))

for x in "banana":
  print(x)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
else:
  print("No, 'free' is not present.")

b = "    Hello, World!"
print(b.upper(), b.strip(), b.replace("H", "J"))

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)