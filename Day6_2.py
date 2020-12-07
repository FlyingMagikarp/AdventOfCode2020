import time
start_time = time.time()


def parse(data):
    return data.split('\n')


def intersection(str1, str2):
    inters = set(str1).intersection(str2)
    return ''.join(inters)


def getCommonAnswers(answers):
    common = answers[0]
    for a in answers:
        common = intersection(common, a)
    return common


with open("resources/6_1_answers.txt") as f:
    grpAnswers = [parse(fields) for fields in f.read().split('\n\n')]

total = 0
for g in grpAnswers:
   total += len(getCommonAnswers(g))

print(total)
print("--- %s seconds ---" % (time.time() - start_time))
