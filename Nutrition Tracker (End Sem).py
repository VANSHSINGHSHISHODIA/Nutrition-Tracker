import mysql.connector as ms
import matplotlib.pyplot as plt
import math
import numpy as np

con=ms.connect(host="localhost",user="root",passwd="Aman",database="food")
cursor=con.cursor()
cursor.execute("select * from chart;")
data=cursor.fetchall()
D=[]
for i in data:
    D.append(i[0])
arr=np.array(D)
print(arr)

#print(data)
    
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\tWelcome to Nutrition tracker System!!!")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
x=str(input("Would you like to see the stats for your Breakfast/Lunch/Dinner or Overall stats Combined--->"))


total_protein=0
total_carbs=0
total_fats=0
total_fiber=0
total_calorie=0
def Dinner():
    num=int(input("Enter the number of food items you eat for Dinner--->"))
    global total_protein, total_carbs, total_fats, total_fiber, total_calorie
    protein=0
    fiber=0
    fats=0
    carbs=0
    calorie=0
    for i in range(1,(num+1)):
        name=input("Enter the name of Food item No."+str(i)+"--->")
        quantity=float(input("Enter the quantity in Grams--->"))
        for j in data:
            if j[0]==name:
                protein=protein+(quantity*j[1]*0.01)
                carbs=carbs+(quantity*j[2]*0.01)
                fats=fats+(quantity*j[3]*0.01)
                fiber=fiber+(quantity*j[4]*0.01)
                calorie=calorie+(quantity*j[5]*0.01)
    total_protein=total_protein+protein
    total_carbs=total_carbs+carbs
    total_fats=total_fats+fats
    total_fiber=total_fiber+fiber
    total_calorie=total_calorie+calorie
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your nutritional stats for Dinner are as follows:-->")         
    print("Protein-->",protein,"g")
    print("Carbohydate-->",carbs,"g")   
    print("Fasts-->",fats,"g")
    print("Fiber-->",fiber,"g")
    print("Calorie-->",calorie,"kcal")

    
def Lunch():
    num=int(input("Enter the number of food items you eat for Lunch--->"))
    global total_protein, total_carbs, total_fats, total_fiber, total_calorie
    protein=0
    fiber=0
    fats=0
    carbs=0
    calorie=0
    for i in range(1,(num+1)):
        name=input("Enter the name of Food item No."+str(i)+"--->")
        quantity=float(input("Enter the quantity in Grams--->"))
        for j in data:
            if j[0]==name:
                protein=protein+(quantity*j[1]*0.01)
                carbs=carbs+(quantity*j[2]*0.01)
                fats=fats+(quantity*j[3]*0.01)
                fiber=fiber+(quantity*j[4]*0.01)
                calorie=calorie+(quantity*j[5]*0.01)
    total_protein=total_protein+protein
    total_carbs=total_carbs+carbs
    total_fats=total_fats+fats
    total_fiber=total_fiber+fiber
    total_calorie=total_calorie+calorie
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your nutritional stats for Lunch are as follows:-->")         
    print("Protein-->",protein,"g")
    print("Carbohydate-->",carbs,"g")   
    print("Fasts-->",fats,"g")
    print("Fiber-->",fiber,"g")
    print("Calorie-->",calorie,"kcal")

    
def Breakfast():
    num=int(input("Enter the number of food items you eat for Breakfast--->"))
    global total_protein, total_carbs, total_fats, total_fiber, total_calorie
    protein=0
    fiber=0
    fats=0
    carbs=0
    calorie=0
    for i in range(1,(num+1)):
        name=input("Enter the name of Food item No."+str(i)+"--->")
        quantity=float(input("Enter the quantity in Grams--->"))
        for j in data:
            if j[0]==name:
                protein=protein+(quantity*j[1]*0.01)
                carbs=carbs+(quantity*j[2]*0.01)
                fats=fats+(quantity*j[3]*0.01)
                fiber=fiber+(quantity*j[4]*0.01)
                calorie=calorie+(quantity*j[5]*0.01)
    total_protein=total_protein+protein
    total_carbs=total_carbs+carbs
    total_fats=total_fats+fats
    total_fiber=total_fiber+fiber
    total_calorie=total_calorie+calorie
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your nutritional stats for Breakfast are as follows:-->")         
    print("Protein-->",protein,"g")
    print("Carbohydate-->",carbs,"g")   
    print("Fasts-->",fats,"g")
    print("Fiber-->",fiber,"g")
    print("Calorie-->",calorie,"kcal")

    
def Overall():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your overall nutritional stats are as follows:-->")         
    print("Protein-->",total_protein,"g")
    print("Carbohydate-->",total_carbs,"g")   
    print("Fasts-->",total_fats,"g")
    print("Fiber-->",total_fiber,"g")
    print("Calorie-->",total_calorie,"kcal")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

if x =="Breakfast":
    Breakfast()
elif x=="Lunch":
    Lunch()
elif x=="Dinner":
    Dinner()
elif x=="Overall":
    Breakfast()
    Lunch()
    Dinner()
    Overall()
labels=["Protein("+str(total_protein)+")","Carbohydrate("+str(total_carbs)+")","Fats("+str(total_fats)+")","Fiber"+str(total_fiber)+")"]
shares=[total_protein,total_carbs,total_fats,total_fiber]
plt.style.use("ggplot")
plt.title("Niturition Distribuition")
plt.pie(x=shares,labels=labels,autopct="%.2f%%",shadow=True,startangle=90)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
class Person:
    def __init__(self, gender, weight, height, age):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age

    def calculate_BMR(self):
        if self.gender.lower() == "male":
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender.lower() == "female":
            return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        else:
            raise ValueError("Invalid gender. Please enter 'Male' or 'Female'.")
y_n = input("Do you want to calculate your BMR? (Yes/No): ")
if y_n.lower() == "yes":
    gender = input("Enter your gender (Male/Female): ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = float(input("Enter your age in years: "))
    try:
        person = Person(gender, weight, height, age)
        BMR = person.calculate_BMR()
        print("Your daily BMR is:", BMR, "calories")
        calorie_difference = abs(BMR - total_calorie)
        if BMR > total_calorie:
            print(f"You consumed {calorie_difference:.2f} calories more than your BMR.")
        elif BMR < total_calorie:
            print(f"You consumed {calorie_difference:.2f} calories less than your BMR.")
        else:
            print("You consumed exactly equivalent of your BMR.")
    except ValueError as e:
        print(e)
plt.show()


