# put your name and highet in meters and your weight in kilograms
name =  
height_m = 
weight_kg = 
bmi = weight_kg / (height_m ** 2)

print("bmi: ")
print(bmi)

if bmi < 25:
    print(name)
    print("Is not overweight")
else:
    print (name)
    print("is overweight")
