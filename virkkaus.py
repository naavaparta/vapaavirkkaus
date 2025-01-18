# tuo random-kirjaston arpomaan satunnaisuuksia

import random

# lisää lankojen värejä lisäämällä hakasulkujen sisään väri adessiivissä, '-merkkien välissä, pilkulla aiemmista erotettuna, poista ottamalla pois '-merkit, niiden välinen sana ja edeltävä pilkku

langat = ['pinkillä', 'punaisella', 'vihreällä', 'sinisellä', 'valkoisella', 'harmaalla', 'monivärisellä']

lanka = random.choice(langat)

# lisää erilaisia silmukkatyylejä hakasulkujen sisään sopivassa taivutusmuodossa (partitiivi tai instruktiivi yleensä), poista ottamalla pois '-merkit, niiden välinen ilmaisu ja edeltävä pilkku

silmukat = ['kerrosta kiintein silmukoin', 'ketjusilmukkaa', 'piilosilmukkaa', 'kiinteää silmukkaa', 'puolipylvästä', 'pylvästä', 'pitkää pylvästä', 'erikoispitkää pylvästä', 'kertaa kaksi pylvästä yhteen silmukkaan', 'kertaa kolme pylvästä yhteen silmukkaan', 'kertaa neljä pylvästä yhteen silmukkaan', 'popcornia']

silmukka = random.choice(silmukat)

# lisää ohjeita laittamalla ne '-merkkien välissä hakasulkujen sisään, pilkulla aiemmista erotettuna; poista ottamalla pois '-merkit, niiden välissä olevat sanat sekä edeltävä pilkku

ohjeet = ['suoraan edeten', 'taaksepäin siitä missä olet', 'päinvastaiseen kohtaan kuin missä nyt olet', 'yllättävään kohtaan työssäsi', 'keskelle työtäsi', 'hankalaan kohtaan työssäsi', 'kohtaan, johon et oikeastaan tahtoisi tehdä']

ohje = random.choice(ohjeet)

# arpoo lukumäärän, ensimmäinen on pienin arvonnassa tuleva, jälkimmäinen suurin, muokkaa mieleiseksesi

nro = random.randint(2,9)

# arpoo, kehotetaanko vaihtamaan langan juoksevuutta

juoksevuus_bool = random.choice([True, False])
def juoksevuus():
    if juoksevuus_bool == True:
        return "Vaihdahan langan juoksevuutta myös."
    else:
        return ""

# arpoo bonuksena joko yksittäisen ohjeen toistamisen muualle työhön tai kehottaa ryhtymään virkkaamaan

bonus_bool = random.choice([True, False])

def bonusing():
    if bonus_bool == True:
        return "Ja tee sama vielä jonnekin toisaalle työssäsi. Sitten ei kun virkkaamaan!"
    else:
        return "Ja sitten ei kun virkkaamaan!"
    
# luo ja tulostaa lopullisen ohjeistuksen

ohjeistus = f"Tee {lanka} {nro} {silmukka} {ohje}. {juoksevuus()} {bonusing()}"

print(ohjeistus)