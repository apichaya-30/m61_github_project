# คำนวณภาษี

salary = float(input("กรอกเงินเดือน: "))

tax = salary * 0.03
remaining = salary - tax

print("ภาษี 3% =", tax, "บาท")
print("เงินคงเหลือ =", remaining, "บาท")
