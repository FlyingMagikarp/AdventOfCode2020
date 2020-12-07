import time
start_time = time.time()


def parse(data):
    return data.split('\n')


def addAnswersAndGetUnique(answers):
    complete = ""
    for a in answers:
        complete += a
    return set(complete)


with open("resources/6_1_answers.txt") as f:
    grpAnswers = [parse(fields) for fields in f.read().split('\n\n')]

total = 0
for g in grpAnswers:
   total += len(addAnswersAndGetUnique(g))

print(total)
print("--- %s seconds ---" % (time.time() - start_time))
