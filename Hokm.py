import random

hokm = ''
hokms = ['PK','DL','GE','KE']
players = {0 : 0, 1 : 0, 2 : 0, 3 : 0}
teams = {0 : 0, 1 : 0}
user = ['', '', '', '']
first = 0
asli = ''
lst_all = {}

for i in hokms :
    for j in range(1,14) :
        p = {f'{i}' ' ' f'{j}' : j}
        lst_all.update(p)
        
# k, v = random.choice(list(lst_all.items()))

for i in range(4) :                                 # baraye 4 nafar nafari 5 ta cart mindaze
    person = {}
    for pastoor in range(5) :
        k, v = random.choice(list(lst_all.items()))
        d = {k : v}
        lst_all.pop(k)
        person.update(d)
    user[i] = person

# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# print(user[3])

lst = []
for cart in user[first] :
    lst.append(cart)
print('PLAYER ',first+1,':')
print(sorted(lst))
print('----')

while hokm not in hokms :                           # hokm moshakhas mishe
    print('PLAYER : ',first+1)
    hokm = input('HOKM KONID (PK)(DL)(GE)(KE) : ')

print('----')
print ('HOKM SHOD :',hokm)
print('----')

for i in range(4) :                                 # baraye 4 nafar nafari 8 ta cart dge mindaze
    person = {}
    for pastoor in range(8) :
        k, v = random.choice(list(lst_all.items()))
        d = {k : v}
        lst_all.pop(k)
        person.update(d)
    user[i].update(person)

# print(user)

for i in range(4) :
    D = {}
    for k, v in user[i].items() :
        if hokm in k :
            v += 13
        d = {k : v}
        D.update(d)
    user[i] = D

for dast in range(13) :
    miz = {}
    mx = 0
    zamine = ''
    for i in range(4) :

                                                      # ba 'first' mifahmim ki bayad aval bendaze
        if first == 4 :
            first = 0
            
        d = {}
        lst = []
        for cart in user[first] :
            lst.append(cart)
        print('PLAYER ',first+1,':')
        print(sorted(lst))

        print('----')

        varagh = ''

        while varagh not in user[first].keys() and zamine in hokms :
            for cart in user[first] :
                if cart[0:2] == zamine :
                    hanuz_daram = True
                    break
                else :
                    hanuz_daram = False

            if hanuz_daram == True :
                while varagh not in user[first].keys() or zamine != varagh[0:2] :
                    varagh = input(f'NOBATE PLAYER {first+1} YE VARAGH BENDAZID (ZAMINE {zamine} AST) : ')

            elif hanuz_daram == False :
                asli = user[first]
                d = {}
                for k , v in user[first].items() :
                    if k[0:2] == hokm :
                        v = v
                    else :
                        v = 0
                    D = {k : v}
                    d.update(D)
                user[first] = d
                varagh = input(f'NOBATE PLAYER {first+1} YE VARAGH BENDAZID (SHOMA {zamine} NADARID VA HOKM : {hokm} ) : ')
            # print(zamine)
            # print(hanuz_daram)

        while varagh not in user[first].keys() or zamine == '' :
            varagh = input(f'NOBATE PLAYER {first+1} YE VARAGH BENDAZID : ')
            if varagh[0:2] in hokms :
                zamine = varagh[0:2]
            # print(zamine)



        print('----')

        if varagh in user[first].keys() :
            v = user[first][varagh]
            if v > mx :
                mx = v
                winner = first
            k = varagh
            x = user[first].pop(k)

            if asli == type(dict) :

                x = asli.pop(k)
                user[first] = asli
                print(user[first])
                print(asli)

            d = {first : {k : v}}
            miz.update(d)
        first += 1
    players[winner] += 1

    if winner == 0 or winner == 2 :
        teams[0] += 1
        
    if winner == 1 or winner == 3 :
        teams[1] += 1

    # print(players)
    # print(teams)

    print(f'PLAYER {winner+1} IN DASTO BORD')
    print('TEAM 1 (PLAYER 1 , PLAYER 3) : ',teams[0])
    print('TEAM 2 (PLAYER 2 , PLAYER 4) : ',teams[1])
    first = winner

    
    print('----')

maxx = 0
for k,v in teams.items() :
    if v > maxx :
        maxx = v
        winner_asli_dast = k
    
print('TEAM',winner_asli_dast+1,'WINNER')

# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# print(user[3])