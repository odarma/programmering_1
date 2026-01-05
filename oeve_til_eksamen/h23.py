import json
meny={
    'ribbe':145.90,
    'pinnekjøtt':155.90,
    'lutefisk':135.90,
    'nøttestek':135.90,
    'reinsdyrstek':155.90
}
#3.1
def vis_meny_rett(meny,rett):
    for key,value in meny.items():
        if key == rett:
            print(f'{rett} - {value}kr')
    return
for key,value in meny.items():
    print(key)
valg_rett=input(f'vilke rett vil du se prisen for? kopier retten over')
vis_meny_rett(meny,valg_rett)

#3.2
def bestill(ribbe=0,pinne=0,lute=0,nut=0,rein=0):
    bestilling={}
    bestilling={'ribbe':ribbe,'pinnekjoett':pinne,'lutefisk':lute,'noettestek':nut,'reinsdyrstek':rein}
    if rein>0:
        print('buhuu')
    return bestilling
ribbe_inn=int(input('hvor mange ribbe vil du ha?'))
pinne_inn=int(input('hvor mange pinnekjøtt vil du ha?'))
lute_inn=int(input('hvor mange lutefisk vil du ha?'))
nut_inn=int(input('hvor mange nøttestek vil du ha?'))
rein_inn=int(input('hvor mange reinsdyrstek vil du ha?'))
bestilling=bestill(ribbe_inn,pinne_inn,lute_inn,nut_inn,rein_inn)

#3.3a
def kalkuler_pris(meny,antall):
    total_pris_ut=0
    for (rett,pris),(rett2,antalll) in zip(meny.items(),antall.items()):
        total_pris_ut+=pris*antalll
    print(f'totalt: {total_pris_ut}kr')
    return total_pris_ut
kalkuler_pris(meny,bestilling)

#3.3b
def vis_pris(meny,bestilling):
    total_pris_ut=0
    for (rett,pris),(rett2,antalll) in zip(meny.items(),bestilling.items()):
        total_pris_ut+=pris*antalll
        print(f'{rett2} - ({antalll}) - {pris*antalll} kr')
    return
vis_pris(meny,bestilling)

#3.4
def bekreft_bestilling(kostnad):
    valg=input(f'den totale prisen er {float(kostnad)}kr, godtar du bestillingen? ja/nei\n').lower()
    if valg == 'ja':
        print('rudolf er grønn på nesen!')
        return True
    elif valg == 'nei':
        print('rudolf er rød på nesen!')
        return False
bekreft_bestilling(kalkuler_pris(meny,bestilling))

#3.5
liste=[]
def lagre_data(bestilling,liste):
    liste.append(bestilling)
    return liste
lagre_data(bestilling,liste)

#3.6a
def lagre_i_fil(bestilling,filnavn='bestilling.json'):
    with open(filnavn, "a") as fil:
        json.dump(bestilling, fil, indent=4,separators=(','))
    return
lagre_i_fil(bestilling)

#3.6b
def laste_inn_fra_fil(filnavn='bestilling.json'):
    with open(filnavn,'r') as fil:
        print(json.load(fil))
        fil.close()
    return
laste_inn_fra_fil()