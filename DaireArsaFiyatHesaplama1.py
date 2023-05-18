deniz_kenari=1.6
sehir_merkezi=1.2
kirsal=0.8
def cember_cevre_hesaplama(yaricap):
    PI=3.14
    sonuc=2*PI*yaricap
    return sonuc
def dıkdortgen_cevre_hesaplama(kenar1,kenar2):
    sonuc=2*(kenar1+kenar2)
    return sonuc
def arsa_fiyat_cember(konum,yaricap):
    global deniz_kenari
    global sehir_merkezi
    global kirsal

    if konum==1:
        sonuc=deniz_kenari*cember_cevre_hesaplama(yaricap)*1000
        return sonuc
    elif konum==2:
        sonuc=sehir_merkezi*cember_cevre_hesaplama(yaricap)*1000
        return sonuc
    elif konum==3:
        sonuc=kirsal*cember_cevre_hesaplama(yaricap)*1000
        return sonuc
cikis='h'
while cikis!='E' and cikis!='e':
    print("1-Daire Fiyati Hesaplama")
    print("2-Arsa Fiyati Hesaplama")
    print("0-cikis")
    sayi=int(input("Seçiminizi giriniz: "))
   
