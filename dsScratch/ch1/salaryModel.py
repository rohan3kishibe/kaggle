from collections import defaultdict

salaries_and_tenures = [
    (830000, 8.3),
    (80000, 8.1),
    (48000, 0.7),
    (63000, 6),
    (69000, 6.5),
    (48000, 1.9),
]

# keys are eas ,values are lists of the salareis for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# keys will be years ,each value is the avergae salary for that tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print(average_salary_by_tenure)


##bucketing the tenures
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than 2"
    elif tenure < 5:
        return "between 2 and 5 "
    else:
        return "more than 5"


# then grouping together the salaries correspondign to each bucket
# keys will be tenure buckets,values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salary_by_tenure:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# and then finally computing the average salary for each group

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

