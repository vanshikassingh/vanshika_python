temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

#1. Display cities having temperature above 40°C.  
print("\nThe cities having temp above 40C:")
for city, temp in temperature.items():
    if temp>=40:
        print(city)

#2. Find the hottest city.  
hot=max(temperature, key=temperature.get)
print("\nThe hottest city is :", hot,f"({temperature[hot]})")

# 3. Find the coolest city
cool = min(temperature, key= temperature.get)
print("\nThe coolest city is:", cool,f"({temperature[cool]})")

## 4. Calculate average temperature
avg=sum(temperature.values())/len(temperature)
print("\nThe average temnperature: ", avg)

#create a list for pleasant cities (temperature < 35°C)
pleasant=[]
for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)
print("\nPleasant cities :", pleasant)

# 6. Count cities with temperature between 35°C and 40°C 
count=0
for temp in temperature.values():
    if 35 <= temp <=40:
        count = count+1
print("\nThe no of cities with temperature between 35 and 40 C:", count)
