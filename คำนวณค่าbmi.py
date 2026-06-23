weight = float(input("กรอกน้ำหนัก (กก.): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))
