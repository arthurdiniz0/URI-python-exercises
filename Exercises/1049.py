c1 = input()

if c1 == 'vertebrado':
    c2 = input()
    if c2 == 'ave':
        c3 = input()
        if c3 == 'carnivoro':
            print('aguia')
        elif c3 == 'onivoro':
            print('pomba')
    elif c2 == 'mamifero':
        c3 = input()
        if c3 == 'onivoro':
            print('homem')
        elif c3 == 'herbivoro':
            print('vaca')
elif c1 == 'invertebrado':
    c2 = input()
    if c2 == 'inseto':
        c3 = input()
        if c3 == 'hematofago':
            print('pulga')
        elif c3 == 'herbivoro':
            print('lagarta')
    elif c2 == 'anelideo':
        c3 = input()
        if c3 == 'hematofago':
            print('sanguessuga')
        elif c3 == 'onivoro':
            print('minhoca')