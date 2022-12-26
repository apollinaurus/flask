first_file = open("first_tour.txt", "r")
second_file = open("second_tour.txt", "w")

K = first_file.readline().split()[-1]

for line in first_file:
    score = line.split()[-1]
    if score > K:
        second_file.write(line)
