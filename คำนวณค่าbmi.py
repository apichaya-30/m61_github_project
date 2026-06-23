 โปรแกรมคำนวณค่า BMI พร้อมแปลผล

weight = float(input("กรอกน้ำหนัก (กก.): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

bmi = weight / (height ** 2)

print("ค่า BMI =", round(bmi, 2))

if bmi < 18.5:
    print("อยู่ในเกณฑ์ผอม")
elif bmi < 23:
    print("อยู่ในเกณฑ์ปกติ")
elif bmi < 25:
    print("น้ำหนักเกิน")
elif bmi < 30:
    print("โรคอ้วนระดับ 1")
else:
    print("โรคอ้วนระดับ 2")
