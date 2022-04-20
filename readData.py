import csv

from requests import head

total_issues = 0
issues ={}
issues['summary']= {}
issues["total_types"] = 0
#read my data file
with open("all_issues.csv") as csvfile:
    issues_reader = csv.reader(csvfile, delimiter=",")
    header_row = next(issues_reader)
    print('header row', header_row)
    for issue in issues_reader:
        #count total number of issues
        total_issues = total_issues +1
        #how many open
        #how many closed
        current_status = issue[1]
        if current_status in issues:
            issues[current_status] = issues[current_status] +1
        else:
            issues[current_status] =1

        current_summary = issue[2]
        if current_summary not in issues['summary']:
            issues["summary"][current_summary] = 1
            issues["total_types"] = issues["total_types"] +1
        else:
            issues["summary"][current_summary] = issues["summary"][current_summary]  +1
        # if current_status =="Open":
        #     open_issues = open_issues +1
        # elif current_status =="Closed":
        #     closed_issues = closed_issues +1
        #how many types


print(f'Total issues reported: {total_issues}')
# print(f'open issues: {open_issues}')
# print(f'closed issues { closed_issues}')
print(issues)



