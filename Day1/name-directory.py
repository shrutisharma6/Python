import operator

def person_lister(f):
    def inner(people):
        for p in people:
            p[2] = int(p[2])
        sorted_people =  (sorted(people, key=operator.itemgetter(2)))
        l = []
        for i in sorted_people:
            l.append(("Mr. " if i[3] == "M" else "Ms. ") + i[0] + " " + i[1])
        return l
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')