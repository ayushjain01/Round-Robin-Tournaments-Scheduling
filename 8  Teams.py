"""
Created by Ayush Jain
This Program generates a match schedule for 8 teams competing against each other
using the Round Robin Match scheduling algorithm.

"""


import random


def teamer():
    start_team1 = random.randint(1, 8)
    start_team2 = random.randint(1, 8)
    while start_team1 == start_team2:
        start_team1 = random.randint(1, 8)
        start_team2 = random.randint(1, 8)
    return (start_team1, start_team2)


def tempmaker(a):
    temp.append(a)
    for i in range(1, 9):
        if i == a:
            pass
        else:
            temp.append(i)


def listshift(a):
    x1 = a.pop(4)
    x2 = a.pop(3)
    a.insert(1, x1)
    a.insert(7, x2)
    return a


def swap(a):
    team1 = ""
    team2 = ""
    x = a.index(" ")
    team1 = a[:x]
    a = a[x+1:]
    x = a.index(" ")
    team2 = a[x+1:]
    return f"{team2} vs {team1}"


def matchprint(a, n):
    for i in range(4):
        for j in range(4):
            if i == j:
                game = f'{n[a[0][i]]} vs {n[a[1][j]]}'
                if game not in played_list:
                    played_list.append(game)
                    print(game)
                else:
                    played_list.remove(game)
                    print(swap(game))
            else:
                continue


def matchwrite(a, n):
    global file_name
    for i in range(4):
        for j in range(4):
            if i == j:
                game = f'{n[a[0][i]]} vs {n[a[1][j]]}'
                if game not in played_list:
                    played_list.append(game)
                    file_name.write(f"{game}\n")
                else:
                    played_list.remove(game)
                    file_name.write(f"{swap(game)}\n")
            else:
                continue


total_teams = 8
num = {}
rounds = int(input(
    "Enter number of rounds(That is a pair of teams plays how many matches together) - "))
pref = input(
    "Do you ant to print the match schedule on a file ? Type Y for yes and N for no? ")
mode = "Console"
mode_func = matchprint
file_open = False
if pref == "Y" or pref == "y":
    file_name = open(
        f"Match-Schedule-{total_teams}-Teams-{rounds}-Rounds.txt", "w")
    mode = "File"
    mode_func = matchwrite
    file_open = True
teamlist = []
team1 = []
team2 = []
temp = []
played_list = []
for i in range(total_teams):
    num[i+1] = input(f"Enter team {i+1}'s name -")

start_team1, start_team2 = teamer()
tempmaker(start_team1)

for ro in range(rounds):
    for i in range(total_teams-1):
        c = 0
        team1 = []
        team2 = []
        teamlist = []
        for j in temp:
            if c < 4:
                team1.append(j)
                c = c + 1
            else:
                team2.append(j)
                c = c + 1
        teamlist = [team1, team2]
        mode_func(teamlist, num)
        temp = listshift(temp)
    temp = []
    tempmaker(start_team2)
if file_open == True:
    file_name.close()
