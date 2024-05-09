
import matplotlib.pyplot as plt
import math
import numpy as np
data=[('Momos', 4.3, 19.0, 12.5, 0.4, 109.0), ('Rice', 2.7, 28.2, 0.3, 0.4, 130.0), ('Roti', 8.22, 15.0, 1.0, 2.6, 297.0), ('Dal', 7.0, 60.0, 1.0, 8.0, 116.0), ('Sabzi', 1.5, 6.0, 1.0, 3.0, 87.0), ('Chicken curry', 18.0, 1.9, 11.0, 0.0, 195.0), ('Fish curry', 18.0, 1.9, 11.0, 0.0, 116.0), ('Paneer curry', 18.0, 3.0, 18.0, 0.0, 265.0), ('Aloo curry', 2.0, 9.0, 5.0, 2.0, 111.0), ('Bhindi masala', 1.9, 7.0, 10.0, 3.0, 105.0), ('Palak paneer', 5.4, 2.5, 13.0, 2.0, 180.0), ('Tandoori chicken', 17.5, 0.0, 7.0, 0.0, 195.0), ('Butter chicken', 14.3, 9.0, 13.0, 0.0, 312.0), ('Rajma curry', 7.6, 13.9, 1.6, 7.6, 123.0), ('Chole curry', 8.6, 20.0, 3.0, 5.0, 138.0), ('Matar paneer', 7.8, 5.2, 11.0, 3.0, 130.0), ('Biryani', 8.9, 28.0, 15.0, 1.0, 210.0), ('Pulao', 2.6, 27.0, 7.0, 1.0, 119.0), ('Idli', 6.4, 14.0, 0.3, 0.9, 26.0), ('Dosa', 5.0, 18.0, 4.0, 1.9, 133.0), ('Sambar', 2.9, 6.5, 4.0, 1.6, 65.0), ('Vada', 5.0, 13.0, 10.0, 4.9, 138.0), ('Upma', 2.0, 25.0, 4.0, 1.4, 132.0), ('Poha', 3.0, 15.0, 4.0, 1.1, 110.0), ('Uttapam', 7.0, 24.0, 8.0, 1.4, 152.0), ('Masala dosa', 7.0, 18.0, 10.0, 2.6, 180.0), ('Poori', 6.0, 30.0, 14.0, 1.0, 101.0), ('Bhatura', 7.3, 33.3, 18.0, 0.0, 320.0), ('Paratha', 7.5, 23.0, 15.0, 3.0, 267.0), ('Chapati', 6.0, 15.0, 4.0, 5.4, 297.0), ('Naan', 8.0, 46.0, 7.0, 2.0, 330.0), ('Khichdi', 4.0, 28.0, 8.0, 3.0, 120.0), ('Sambhar rice', 4.0, 23.0, 3.5, 1.3, 175.0), ('Curd rice', 3.0, 20.0, 4.0, 0.5, 143.0), ('Lemon rice', 2.9, 28.0, 4.0, 1.1, 167.0), ('Tamarind rice', 2.2, 25.0, 8.0, 1.6, 150.0), ('Coconut rice', 2.7, 20.0, 19.0, 3.3, 403.0), ('Tomato rice', 2.2, 25.0, 5.0, 1.6, 108.0), ('Moong dal khichdi', 5.0, 24.0, 4.0, 2.4, 106.0), ('Raita', 2.6, 3.6, 5.6, 0.6, 75.0), ('Papad', 20.0, 73.0, 24.0, 9.1, 371.0), ('Pakora', 9.0, 10.0, 15.0, 2.5, 350.0), ('Aloo Tikki', 2.3, 24.2, 13.0, 2.5, 278.0), ('Paneer Tikka', 18.5, 5.5, 17.0, 1.5, 268.0), ('Chana masala', 7.3, 15.0, 5.0, 5.0, 138.0), ('Aloo Gobi curry', 2.2, 6.0, 5.0, 3.3, 125.0), ('Baingan Bharta', 2.3, 6.0, 15.0, 5.0, 85.0), ('Chicken Tikka Masala', 18.0, 8.0, 13.0, 2.5, 218.0), ('Aloo Paratha', 7.0, 36.0, 10.0, 1.9, 259.0), ('Gajar ka Halwa', 1.6, 39.0, 20.0, 2.0, 141.0), ('Gulab Jamun', 2.3, 59.0, 13.0, 0.0, 257.0), ('Rasgulla', 2.0, 21.0, 0.6, 0.0, 186.0), ('Jalebi', 1.1, 85.0, 25.0, 0.0, 459.0), ('Ladoo', 4.0, 57.0, 26.0, 0.0, 352.0), ('Samosa', 6.0, 16.0, 14.0, 3.3, 250.0), ('Kachori', 7.0, 24.0, 12.0, 2.9, 200.0), ('Chaat', 3.2, 23.0, 5.0, 1.0, 150.0), ('Pav Bhaji', 3.5, 17.0, 11.0, 3.0, 125.0), ('Dabeli', 4.0, 29.0, 15.0, 5.0, 200.0), ('Dhokla', 3.0, 13.0, 5.0, 1.5, 150.0), ('Khandvi', 6.0, 24.0, 14.0, 5.0, 330.0), ('Mysore Pak', 8.0, 57.0, 39.0, 0.0, 530.0), ('Chole Bhature', 7.5, 60.0, 23.0, 5.0, 450.0), ('Aloo Poori', 5.0, 25.0, 16.0, 2.0, 320.0), ('Chicken Biryani', 17.0, 28.0, 16.0, 0.0, 250.0), ('Hyderabadi Biryani', 17.0, 28.0, 16.0, 0.0, 400.0), ('Chicken 65', 16.0, 7.0, 9.0, 0.0, 320.0), ('Chicken Korma', 16.0, 5.0, 10.0, 2.5, 310.0), ('Fish Fry', 20.0, 0.0, 11.0, 0.0, 305.0), ('Fish Curry', 18.0, 1.9, 11.0, 0.0, 97.0), ('Egg Curry', 13.0, 2.7, 11.0, 0.0, 160.0), ('Egg Bhurji', 13.0, 2.7, 11.0, 0.0, 159.0), ('Anda Masala', 12.5, 1.9, 11.0, 0.0, 250.0), ('Chicken Fry', 23.5, 0.0, 13.0, 0.0, 330.0), ('Mutton Curry', 16.0, 1.0, 16.0, 0.0, 300.0), ('Rogan Josh', 15.0, 7.0, 16.0, 0.0, 375.0), ('Keema', 18.0, 1.0, 16.0, 0.0, 220.0), ('Mutton Biryani', 18.0, 28.0, 16.0, 0.0, 330.0), ('Sheer Khurma', 7.0, 20.0, 16.0, 0.0, 300.0), ('Malai Kofta', 3.2, 10.0, 16.0, 0.0, 350.0), ('Shahi Paneer', 14.0, 8.0, 16.0, 0.0, 350.0), ('Kofta Curry', 3.8, 10.0, 16.0, 0.0, 320.0), ('Dum Aloo', 2.4, 13.0, 16.0, 0.0, 150.0), ('Chicken Do Pyaza', 16.0, 5.0, 16.0, 0.0, 280.0), ('Chicken Saag', 16.0, 7.0, 16.0, 0.0, 200.0), ('Tandoori Roti', 8.22, 15.0, 7.0, 0.0, 280.0), ('Butter Naan', 8.0, 46.0, 7.0, 2.6, 320.0), ('Garlic Naan', 8.0, 46.0, 7.0, 2.6, 330.0), ('Chicken Shawarma', 17.0, 6.0, 16.0, 0.0, 340.0), ('Fish Tikka', 20.0, 1.9, 11.0, 0.0, 240.0), ('Chicken Roll', 20.0, 20.0, 14.0, 0.0, 270.0), ('Kathi Roll', 16.0, 25.0, 14.0, 0.0, 290.0), ('Chicken Momos', 17.0, 20.0, 14.0, 0.0, 250.0), ('Veg Momos', 5.0, 16.0, 14.0, 0.0, 75.0), ('Chicken Noodles', 15.0, 14.0, 14.0, 0.0, 200.0), ('Veg Noodles', 3.0, 19.0, 14.0, 0.0, 150.0), ('Fried Rice', 3.0, 28.0, 14.0, 0.0, 175.0), ('Paneer Butter Masala', 12.0, 9.2, 18.0, 0.0, 350.0), ('Kadai Paneer', 18.0, 9.0, 18.0, 2.0, 320.0), ('Methi Chicken', 20.0, 5.0, 18.0, 3.0, 220.0), ('Amritsari Kulcha', 10.0, 60.0, 20.0, 2.0, 260.0)]

   
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


