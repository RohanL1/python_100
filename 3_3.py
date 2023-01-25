bmi=round(int(input("enter weight in kg :"))/float(input("enter height in m :"))**2, 2)
#msg=""
if bmi < 18.5:
    msg="underweight"
elif bmi > 18.5 and bmi <25 :
    msg="normal"
elif bmi > 25 and bmi <30 :
    msg="overweight"
elif bmi > 30 and bmi <35 :
    msg="obese"
else :
    msg="clinically obese"

print(f"BMI : {bmi}, Result : {msg}")



#print(round(int(input("enter weight in kg :"))/float(input("enter height in m :"))**2, 2))
#print(str(int(float(input("enter weight in kg :"))/float(input("enter height in m :"))**2)))
