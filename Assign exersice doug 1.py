#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assign the string below to the variable in the exersice.
"its always darkest before dawn"

str = "its always darkest before dawn"

print(str)


# In[1]:


#By using first, second and last characters of the string, create a new string from the string;

str = "its always darkest befor dawn"

new_string = str[1] + str[2] + str[-1]
 
print(new_string)


# In[2]:


#from the string "its always darkest before dawn." replace(.) with (!) using the replace ()

str = "its always darkest before dawn."

new_str =str.replace('.',"!")

print(new_str)


# In[6]:


#Str="Every strike brings me closer to the next Home run" Reassign str so that, all its characters are lowercase.

str="Every strike brings me closer to the next Home run"

new_low_str = str.lower()

print(new_low_str)


# In[7]:


#Str="dont stop me now ". Now make everything in str uppercase

str="dont stop me now"

upk = str.upper()

print(upk)


# In[12]:


#Using.index()method, identify the index of cha

str= "the best revenge is massive success"

net= str.index("v")

print(net)


# In[13]:


print(len("the best revenge is massive success"))


# In[18]:



print(isspace("  "))


# In[19]:


shopping_list = ['bag', 'shoe', 'jewelery', 'clothes'] #this is what we should buy 

bought = shopping_list[1:3] # we did not buy jewlery and clothes

print(bought) #what we bought


# In[ ]:


# HEIGHT, WEIGHT & BMI CALCULATOR

human_input = input("Do you want to calculate 'Height', 'Weight' or 'BMI'?: ")

# Height calculation
if human_input == "Height" or human_input == "height":
    height = int(input("Enter your height: "))
    convert_unit_height = input("Did you enter your height in 'm' or 'cm'?: ")

    if (
        convert_unit_height == "cm"
        or convert_unit_height == "CM"
        or convert_unit_height == "Cm"
        or convert_unit_height == "cM"
    ):
        converted_height_cm = height / 100
        print(f"Your height in metres is {converted_height_cm}m.")

    elif convert_unit_height == "m" or convert_unit_height == "M":
        converted_height_m = height * 100
        print(f"Your height in centimetres is {converted_height_m}cm.")

    else:
        print("Error: Invalid unit.")

# Weight calculation
elif human_input == "Weight" or human_input == "weight":
    weight = int(input("Enter your weight: "))
    convert_unit_weight = input("Did you enter your height in 'kg' or 'g'?: ")

    if (
        convert_unit_weight == "kg"
        or convert_unit_weight == "Kg"
        or convert_unit_weight == "kG"
        or convert_unit_weight == "KG"
    ):
        converted_weight_kg = weight * 1000
        print(f"Your weight in grams is {converted_weight_kg}g.")

    elif convert_unit_weight == "g" or convert_unit_weight == "G":
        converted_weight_g = weight / 1000
        print(f"Your weight in kilograms is {converted_weight_g}kg.")

    else:
        print("Error: Invalid unit.")

# BMI calculation
elif human_input == "bmi" or human_input == "Bmi" or human_input == "BMI":
    height_bmi = int(input("Enter your height: "))
    unit_bmi_height = input("Did you enter your height in 'cm' or 'm'?: ")

    if (
        unit_bmi_height == "cm"
        or unit_bmi_height == "CM"
        or unit_bmi_height == "Cm"
        or unit_bmi_height == "cM"
    ):
        bmi_height_in_m = height_bmi / 100

    elif unit_bmi_height == "m" or unit_bmi_height == "M":
        bmi_height_in_m = height_bmi

    else:
        print("Error: Invalid unit.")

    weight_bmi = int(input("Enter your weight: "))
    unit_bmi_weight = input("Did you enter your weight in 'g' or 'kg'?: ")

    if (
        unit_bmi_weight == "kg"
        or unit_bmi_weight == "Kg"
        or unit_bmi_weight == "kG"
        or unit_bmi_weight == "KG"
    ):
        bmi_weight_in_kg = weight_bmi

    elif unit_bmi_weight == "g" or unit_bmi_weight == "G":
        unit_bmi_weight = weight_bmi / 1000

    else:
        print("Error: Invalid unit.")

    calculated_bmi = bmi_weight_in_kg / (bmi_height_in_m ** 2)

    if calculated_bmi < 18.5:
        print(f"Your BMI is {calculated_bmi}. You are underweight.")

    elif calculated_bmi >= 18.5 and calculated_bmi <= 24.9:
        print(f"Your BMI is {calculated_bmi}. You are having a normal weight.")

    elif calculated_bmi >= 25.0 and calculated_bmi <= 29.9:
        print(f"Your BMI is {calculated_bmi}. You are overweight.")

    elif calculated_bmi >= 30.0 and calculated_bmi <= 34.9:
        print(f"Your BMI is {calculated_bmi}. You are having a obesity class I.")

    elif calculated_bmi >= 35.0 and calculated_bmi <= 39.9:
        print(f"Your BMI is {calculated_bmi}. You are having a obesity class II.")

    elif calculated_bmi > 40:
        print(f"Your BMI is {calculated_bmi}. You are having obesity class III.")

    else:
        print("Error: Cannot calculate BMI.")

else:
    print("Error: Invalid input")

print("Thank you for using 'HEIGHT, WEIGHT & BMI CALCULATOR'!")


# In[27]:


list = [1,1,2,3,13,1,4,34]

list.sort()

print(list)


# In[25]:


letters = ["a","b","c","d","e","f","g"]

print("h" in letters)


# In[26]:


letters = ["a","b","c","d","e","f","g","a","f","a"]

print(letters.count("a"))


# In[ ]:


#COPY THE CODE BELOW;
#AND ADD COMMENTS WHERE (IN THE LINE)  YOU UNDERSTAND WHAT THE CODER IS DOING.

# -*- coding: utf-8 -*-
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("input your name: ") #collecting user name and age
age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon #converting tp interger
day = 0

begin_year = int(localtime.tm_year) - year #calculate begin year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year) # calculate the leap year
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="") # print thde result
print("%d months or %d days" % (month, day))


# In[ ]:





# In[ ]:





# In[ ]:




