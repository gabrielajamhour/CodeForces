n = int(input())
teams = []

for _ in range(n):
    team_name = str(input())
    teams.append(team_name)

most_frequent_team = None
most_frequent_num = 0

for team in teams:
    count_team = teams.count(team)
    if count_team > most_frequent_num:
        most_frequent_team = team
        most_frequent_num = count_team

print(most_frequent_team)
