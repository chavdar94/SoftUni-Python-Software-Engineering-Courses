contests = {}

current_contest = input()
while current_contest != 'end of contests':
    current_contest = current_contest.split(':')
    contest_name = current_contest[0]
    contest_password = current_contest[1]
    contests[contest_name] = contest_password
    current_contest = input()

print(contests)