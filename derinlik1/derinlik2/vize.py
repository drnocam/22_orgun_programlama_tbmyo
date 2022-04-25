
module_degiskeni = 20

def bmi_hesap(kilo,boy):
    """
    kilo ve boy cm ve kg cinsinden giriniz.
    """
    bmi = kilo // boy**2
    durum = "ideal"
    if(bmi<18.5) :
        durum = "Zayıf"
    elif (bmi <25) :
        durum = "Normal"
    elif (bmi < 30) :
        durum = "Kilolu"
    elif (bmi < 35) :
        durum = "Obez"
    else :
        durum = "Morbit"
    print( f"{boy}m.,{kilo}kg. bmi ={bmi}, durum={durum}")
