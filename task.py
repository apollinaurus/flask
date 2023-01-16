with open('first_tour.txt', 'r') as first_file:
    players = []
    k = int(first_file.readline().strip('\n'))
    for line in first_file:
        players += (line.split(),)

players.sort(key=lambda x: int(x[2]), reverse=True)

i = 0
while i < len(players):
    if int(players[i][2]) > k:
        players[i] = "{}) {}. {} {}\n".format(str(i + 1), players[i][1][0], players[i][0], players[i][2])
        i += 1
    else:
        del players[i:len(players)]
        break
number_of_passed = str(len(players))

with open('second_tour.txt', 'w') as second_file:
    second_file.write(number_of_passed)
    second_file.write('\n')
    second_file.writelines(players)
