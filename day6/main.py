from string import ascii_lowercase

splitted = open('input').read().split('\n\n')

def get_score1(dec_form):
    score = 0
    for letter in ascii_lowercase:
        if letter in dec_form:
            score += 1
    return score

def get_score2(dec_form):
    score = 0
    for letter in ascii_lowercase:
        if all(letter in i for i in dec_form.split('\n')):
            score += 1
    return score


print(sum(map(get_score1,splitted)))
print(sum(map(get_score2,splitted)))

