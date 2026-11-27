with open("data/blood_counts (1).csv") as file:
    header = file.readline().strip().split(",")
    content = {header[0]:[],header[1]:[],header[2]:[],header[3]:[]}
    for line in file:
        fields = line.strip().split(",")
        for i in range(len(header)):
            content[header[i]].append(fields[i])
print(content)