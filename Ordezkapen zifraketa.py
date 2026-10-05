import collections

def main():
    print("Sartu deszifratu nahi duzun kriptograma (lerro anitzekoa izan daiteke).")
    print("Amaitzean, sakatu Enter bi aldiz (lerro huts bat utzi) jarraitzeko:")
    
    # 1. Kriptograma erabiltzaileari eskatu
    lerroak = []
    while True:
        lerroa = input()
        if lerroa == "":
            break
        lerroak.append(lerroa)
    
    kriptograma = "\n".join(lerroak).strip()
    
    if not kriptograma:
        print("Ez duzu mezurik sartu. Programa bukatzen...")
        return

    # Irudiko maiztasun taularen araberako ordena (euskara)
    maiztasun_helburua = ['a', 'i', 'r', 'e', 't', 'o', 'u', 'n', 'k', 'l', 
                          'z', 's', 'd', 'g', 'b', 'm', 'p', 'h', 'x', 'f', 
                          'j', 'c', 'y', 'v', 'w', 'q']
    
    # Kriptogramako hizkien maiztasuna kalkulatu (hizkiak bakarrik)
    kriptograma_maius = kriptograma.upper()
    hizkiak_soilik = [c for c in kriptograma_maius if c.isalpha()]
    kontagailua = collections.Counter(hizkiak_soilik)
    
    # Kriptogramako hizkiak maiztasunaren arabera ordenatu
    kriptograma_ordenatua = [hizkia for hizkia, kopurua in kontagailua.most_common()]
    
    # Hasierako hiztegia (mapping) sortu
    hiztegia = {}
    for i in range(len(kriptograma_ordenatua)):
        if i < len(maiztasun_helburua):
            hiztegia[kriptograma_ordenatua[i]] = maiztasun_helburua[i].upper()
        else:
            hiztegia[kriptograma_ordenatua[i]] = '?'

    def erakutsi_mezua():
        emaitza = ""
        for c in kriptograma_maius:
            if c.isalpha() and c in hiztegia:
                emaitza += hiztegia[c]
            else:
                emaitza += c
        print("\n--- DESZIFRATUTAKO MEZUA ---")
        print(emaitza)
        print("----------------------------\n")

    print("\nMaiztasun analisiaren programa interaktiboa abiarazten...")
    
    # Begizta interaktiboa
    while True:
        erakutsi_mezua()
        print("Uneko loturak (Kriptograma -> Deskodetua):")
        loturak = [f"{k}->{v}" for k, v in hiztegia.items()]
        print(" ".join(loturak))
        
        erantzuna = input("\nIdatzi bi hizki trukatzeko (adibidez: 'A E') edo 'irten' bukatzeko: ").strip().upper()
        
        if erantzuna == 'IRTEN':
            print("Programa bukatuta. Agur!")
            break
        
        atiak = erantzuna.split()
        if len(atiak) == 2:
            h1, h2 = atiak[0], atiak[1]
            
            kripto1 = kripto2 = None
            for k, v in hiztegia.items():
                if v == h1: kripto1 = k
                if v == h2: kripto2 = k
            
            if kripto1 and kripto2:
                # Trukatu hiztegian
                hiztegia[kripto1], hiztegia[kripto2] = hiztegia[kripto2], hiztegia[kripto1]
                print(f"\n=> '{h1}' eta '{h2}' ongi trukatu dira.")
            else:
                print(f"\n=> ERROREA: '{h1}' edo '{h2}' ez daude uneko loturetan.")
        else:
            print("\n=> Mesedez, idatzi bi hizki zuriune batez banatuta (adib. 'A E').")

if __name__ == "__main__":
    main()