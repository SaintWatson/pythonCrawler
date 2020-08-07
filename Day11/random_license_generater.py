import random
def random_char():
    rng = random.Random()
    rc = rng.randint(65,90)
    return chr(rc)
def random_digit():
    rng = random.Random()
    return str(rng.randint(0,9))
def random_license():
    rng = random.Random()
    License = []
    for i in range(6):
        a = rng.randint(0,1)
        if a==0:
            License.append(random_char())
        else:
            License.append(random_digit())
    _ = rng.randint(1,3)
    output = ''
    for i in range(6):
        output += License[i]
        if i==_:
            output += '-'
    return output+'\n'
def make_data(n):
    with open('license_data.txt', 'w') as f:
        for i in range(n):
            f.writelines(random_license())
