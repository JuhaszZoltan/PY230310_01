from module2 import *

egitestek:list[Egitest] = []
file = open(file='egitestek.txt', mode='r', encoding='utf-8')
for sor in file: egitestek.append(Egitest(sor))

print(f'égitestek száma: {len(egitestek)}')

nkksz:int = 0
for e in egitestek:
    if e.hol_kering == 'Nap': nkksz += 1
print(f'nap körül keringő égitestek száma: {nkksz}')

lti:int = 0
for i in range(1, len(egitestek)):
    if egitestek[i].tavolsag < egitestek[lti].tavolsag:
        lti = i
print(f'a legközelebb a bolygójához a {egitestek[lti].elnevezes} van')

holdak:list[str] = []
for e in egitestek:
    if not e.direktirany:
        holdak.append(e.elnevezes)
print('A Földdel ellentétes ker. irányú égitestek:')
for h in holdak:
    print(f'\t- {h}')

ker_egit:str = input('keresett égitest neve: ')

for e in egitestek:
    if e.elnevezes == ker_egit:
        if e.felfedezo_neve == '---':
            print('\tnincs adat a felfedezés körülményeiről')
        else:
            print(f'\tfelfedező neve: {e.felfedezo_neve}')
            print(f'\tfelfedezés éve: {e.felfedezes_eve}')
        break
else: print('\tnincs nevű égitest!')