# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
wind_speed = input("Enter the average wind speed here:") #(m/s)
operating_efficiency = input("Enter the turbines operating efficiency in decimal form here:")
radius_turbine = input("Enter the turbines radius in meters here:")
density = 1.2 #The density of air (kg/m^3)
area = 3.14159*(int(float(radius_turbine)))*int(float(radius_turbine))
pmax = 0.5*density*area*(int((float(wind_speed))))*(int((float(wind_speed))))*(int((float(wind_speed)))) #maximum amount of power
print("The maximum amount of energy produced is:", pmax)
p_act = pmax*int(float(operating_efficiency))
print("The actual amount of energy produced is",p_act)

