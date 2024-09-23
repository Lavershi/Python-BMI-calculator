name =  "fill this up with your name"
height_m = " your height in meters"
weight_kg = " you weight in kilograms"

bmi = weight_kg / (height_m ** 2)

print("bmi: ")
print(bmi)

if bmi < 25:
    print(name)
    print("Is not overweight")
else:
    print (name)
    print("is overweight")
