fp = open("day1.txt","r")

elves=[]
sum=0
day1part1max=0

for line in fp:
    if line != "\n":
        sum=sum+int(line)
    else:
        if day1part1max < sum:
            day1part1max=sum
        sum=0
        # elves.append(sum)
        # sum=0

print(f'Day1 Part1 Calories: {day1part1max}')
fp.close

fp = open("day1.txt","r")

elves=[]
sum=0

for line in fp:
    if line != "\n":
        sum=sum+int(line)
    else:
        elves.append(sum)
        sum=0

elves.sort(reverse=True)
print(f'Day1 Part2 Calories: {elves[0]+elves[1]+elves[2]}')