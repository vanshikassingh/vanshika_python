runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# display player scoring more than 500
print("The players scoring more than 500 are:")
for player, score in runs.items():
    if score>500:
        print(player)

# 2. Find the Orange Cap winner
orangecap=max(runs, key= runs.get)
print("\n Orange cap:",orangecap,f"({runs[orangecap]})")


# 3. Find the lowest scorer
lowest=min(runs,key=runs.get)
print("\n lowest :", lowest ,f"({runs[lowest]})")

# 4. Calculate total runs scored
total=sum(runs.values())
print("\nTotal runs are :", total)

# 5. Create a list of players scoring below 400
below400=[]
for player,score in runs.items():
    if score <400:
        below400.append(player)
print("Players csoring below 400 is :", below400)

## 6. Count players scoring between 400 and 600 runs
count =0
for score in runs.values():
    if 400 <= score <= 600:
        count = count +1
print(" count of the players :", count )
