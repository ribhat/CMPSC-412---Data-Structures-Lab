#-----------------------------------------------------------------------------
# Rishabh Bhat Tues. 03/01/22
# CmpSc472, Spring 2022
# Lab: Read Baseball Stats
# Reading Baseball Stats from a text file and calculating/displaying batting average and slugging percentage
#-----------------------------------------------------------------------------



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # opening baseball.txt
    file = open("baseball.txt", "r")
    data = file.read()
    lines = data.split("\n")

    batting_data = []
    player_name = lines[0]

    # appending the batting data into the list
    for i in range(1, len(lines)):
        words = list(map(int, lines[i].split(","))) # map all values to int so they can be used for calcs
        batting_data.append([words[0], words[1], words[2], words[3], words[4], words[5]])

    at_bats = hits = doubles = triples = homeruns = walks = 0

    for j in range(len(batting_data)):
        at_bats += batting_data[j][0]
        hits += batting_data[j][1]
        doubles += batting_data[j][2]
        triples += batting_data[j][3]
        homeruns += batting_data[j][4]
        walks += batting_data[j][5]

    batting_average = round((hits * 1000 / at_bats), 2)
    slugging_percentage = ((homeruns * 4) + (triples * 3) + (doubles * 2) + walks) / at_bats

    print(player_name)
    print("Batting Average:", batting_average)
    print("Slugging Percentage:", slugging_percentage)
    print("Total number of Singles:", walks)
