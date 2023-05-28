print("           bahre------hasab    ")
wengelawi = {1: "zemene matiwos", 2: "zemen markos", 3: "zemene lukas", 0: "zemen yohannes"}
day = ["a", "b", "friday", "thursday", "wednsday", "tuesday", "monday", "sunday", "saturday"]
month = ["Pagumen", "meskerem", "tikimti", "hdar", "tahsas", "tiri", "yekatit", "megabit", "miyazya", "gunbet", "sene", "hamle", "nehase"]
ametemhret = int(input("enter ametete_mhret : "))
amete_alem = ametemhret + 5500
rbiet = amete_alem // 4
tnteon = ((rbiet + amete_alem) % 7) - 1
if tnteon == -1:
    tnteon = 6
elif tnteon == 0:
    tnteon = 7
else:
    tnteon = tnteon
medeb = amete_alem % 19
if (medeb == 0):
    wenber = 18
elif (medeb == 1):
    wenber = 0
else:
    wenber = medeb - 1
abekte = (wenber * 11) % 30
metqi = (wenber * 19) % 30
if metqi == 0:
    metqi = 30
def መዓልቲ(monthss, date):
    months = month.index(monthss)
    tnteon = ((rbiet + amete_alem) % 7) - 1
    days = (tnteon + 2 * (months - 1) + date + 2) % 7
    if days == 3:
        return "tuesday"
    elif days == 4:
        return "wednsday"
    elif days == 5:
        return "thursday"
    elif days == 6:
        return "friday"
    elif days == 0:
        return "saturday"
    elif days == 1:
        return "sunday"
    elif days == 2:
        return "monday"


print(" press 1 to look fixed hoildays")
print(" press 2 to look at the daynamic holidays ")
choice = input("\n:")
if choice=='1':
    print("total_year  : " + str(amete_alem))
    print("metene_rabiet  : " + str(rbiet))
    print("medeb: " + str(medeb))
    print("wenber: " + str(wenber))
    print("abekte " +  str(abekte))
    print("metke:" + str(metqi))
    print("tinteon " + str(tnteon))
elif (choice=='2'):
    def zemen():
        ametealem = ametemhret + 5500
        wengel = ametealem % 4
        print(wengelawi[wengel])
    a = "meskerem"
    b = int(1)
    መዓልቲ(a, b)
    new_year = "ሓድሽ ዓመት : "
    print(new_year + መዓልቲ(a, b))
    zemen()
    if metqi < 14:
        if metqi == 0:
            metqi = 30
            a = "meskerem"; b = 30
            መዓልቲ(a, b)
            mebajahamer = metqi + day.index(call)
            print("metke " + መዓልቲ(a, b) + " meskerem " + str(b))
        else:
            a = "tikimti";b = metqi
            መዓልቲ(a, b)
            mebajahamer = b + day.index(መዓልቲ(a, b))
            print("metke " + መዓልቲ(a, b) + " tikimti " + str(metqi))
        print("mebaja_hamer = " + str(mebajahamer % 30))
        a = "yekatit";b = int(mebajahamer)
        መዓልቲ(a, b)
        print("neneveh = " + መዓልቲ(a, b) + " yekatit " + str(mebajahamer % 30))
        neneveh = mebajahamer % 30
        tsome_arbea = neneveh + 14
        debrezeit = neneveh + 11
        hosaena = neneveh + 2
        sklet = neneveh + 7
        tnsaie = neneveh + 9
        rkeb_kahnat = neneveh + 3
        erget = neneveh + 18
        peraklitos = neneveh + 28
        hawariat = neneveh + 29
        dhnet = neneveh + 1
        if tsome_arbea <= 30:
            a = "yekatit";b = int(tsome_arbea)
            elet = መዓልቲ(a, b)
            print("tsome_arbea = " + elet + " yekatit " + str(tsome_arbea))
        elif tsome_arbea > 30:
            a = "megabit";b = int(tsome_arbea % 30)
            elet = መዓልቲ(a, b)
            print("tsome_arbea =" + elet + " megabit " + str(tsome_arbea % 30))
        if debrezeit <= 30:
            a = "megabit";b = int(debrezeit)
            call = መዓልቲ(a, b)
            print("debrezeyt : " + elet + " megabit " + str(debrezeit))
        elif debrezeit > 30:
            a = "miyazya";b = int(debrezeit)
            call = መዓልቲ(a, b)
            print("debrezeyt = " + elet + " miyazya " + str(debrezeit))
        if hosaena <= 30:
            a = "miyazya";b = int(hosaena)
            call = መዓልቲ(a, b)
            print("hosaena: " + elet + " miyazya " + str(hosaena))
        if sklet <= 30:
            a = "miyazya";b = int(sklet)
            elet = መዓልቲ(a, b)
            print("arbi_sklet = " + elet + " miyazya " + str(sklet))
        if tnsaie <= 30:
            a = "miyazya";b = int(tnsaie)
            elet = መዓልቲ(a, b)
            print("tinsae : " + elet + " miyazya " + str(tnsaie))
        if rkeb_kahnat <= 30:
            a = "gunbet";b = int(rkeb_kahnat)
            elet = መዓልቲ(a, b)
            print("rkbe_kahnat : " + elet + " gunbet " + str(rkeb_kahnat))
        if erget <= 30:
            a = "gunbet";b = int(erget)
            elet = መዓልቲ(a, b)
            print("erget = " + elet + " gunbet " + str(erget % 30))
        elif erget > 30:
            a = "sene";b = int(erget % 30)
            elet = መዓልቲ(a, b)
            print("erget = " + elet + " sene " + str(erget % 30))
        if peraklitos <= 30:
            a = "gunbet";b = int(peraklitos)
            elet = መዓልቲ(a, b)
            print("peraklitos : " + elet + " gunbet " + str(peraklitos))
        if peraklitos > 30:
            a = "sene";b = int(peraklitos % 30)
            elet = መዓልቲ(a, b)
            print("peraklitos = " + elet + " sene " + str(peraklitos % 30))
        if hawariat > 30:
            a = "sene";b = int(hawariat % 30)
            elet = መዓልቲ(a, b)
            print("tsome_haweryat = " + elet + " sene " + str(hawariat % 30))
        if dhnet <= 30:
            a = "sene";b = int(dhnet)
            elet = መዓልቲ(a, b)
            print("tsome_dhnet = " + elet + " sene " + str(dhnet % 30))
    elif metqi > 14:
        a = "meskerem";b = metqi
        elet = መዓልቲ(a, b)
        mebajahamer = b + day.index(elet)
        print("metek : " + elet + " mekerem " + str(metqi))
        if mebajahamer <= 30:
            print("mebaja_hamer = " + str(ametemhret) + " A.C" + str(mebajahamer))
            a = "tiri";b = int(mebajahamer)
            elet = መዓልቲ(a, b)
            print("neneveh : " + elet + " tiri " + str(mebajahamer))
            neneveh = mebajahamer % 30
            tsome_arbea = neneveh + 14

            if tsome_arbea <= 30:
                a = "tiri";b = int(tsome_arbea)
                elet = መዓልቲ(a, b)
                print("tsome_arbea " + elet + " tiri " + str(tsome_arbea))
            elif tsome_arbea > 30:
                a = "yekatit";b = int(tsome_arbea % 30)
                elet = መዓልቲ(a, b)
                print("tsome_arbea " + elet + " yekatit " + str(tsome_arbea % 30))

            debrezeit = neneveh + 11
            if debrezeit <= 30:
                a = "yekatit";b = int(debrezeit)
                elet = መዓልቲ(a, b)
                print("debre_zeyt = " + elet + " yekatit " + str(debrezeit))
            elif debrezeit > 30:
                a = "megabit";b = int(debrezeit % 30)
                elet = መዓልቲ(a, b)
                print("debre_zeyt = " + elet + " megabit " + str(debrezeit % 30))

            hosaena = neneveh + 2
            if hosaena <= 30:
                a = "megabit";b = int(hosaena)
                elet = መዓልቲ(a, b)
                print("hosaena = " + elet + " megabit " + str(hosaena))
            elif hosaena > 30:
                a = "miyazya";b = int(hosaena % 30)
                elet = መዓልቲ(a, b)
                print("hosaena = " + call + " miyazya " + str(hosaena % 30))

            sklet = neneveh + 7
            if sklet <= 30:
                a = "megabit";b = int(sklet)
                elet = መዓልቲ(a, b)
                print("arbi_sklet = " + elet + " megabit " + str(sklet))
            elif sklet > 30:
                a = "miyazya";b = int(sklet % 30)
                elet = መዓልቲ(a, b)
                print("arbi_sklet = " + elet + " miyazya " + str(sklet % 30))

            tnsaie = neneveh + 9
            if tnsaie <= 30:
                a = "megabit";b = int(tnsaie)
                call = መዓልቲ(a, b)
                print("tinsae : " + elet + " megabit " + str(tnsaie))
            elif tnsaie > 30:
                a = "mmiyazya";b = int(tnsaie % 30)
                elet = መዓልቲ(a, b)
                print("tinsae: " + elet + " miyazya " + str(tnsaie % 30))

            rkeb_kahnat = neneveh + 3
            if rkeb_kahnat <= 30:
                a = "miyazya";b = int(rkeb_kahnat)
                elet = መዓልቲ(a, b)
                print("rkbr_kahnat = " + elet + " miyazya " + str(rkeb_kahnat))
            elif rkeb_kahnat > 30:
                a = "gunbet";b = int(rkeb_kahnat % 30)
                elet = መዓልቲ(a, b)
                print("rkbe_kahnat = " + elet + " gunbet " + str(rkeb_kahnat % 30))

            erget = neneveh + 18
            if erget - 30 <= 30:
                a = "gunbet";b = int(erget % 30)
                elet = መዓልቲ(a, b)
                print("erget " + elet + " gunbet " + str(erget - 30))
            elif erget - 30 > 30:
                a = "sene";b = int(erget % 30)
                elet = መዓልቲ(a, b)
                print("erget: " + elet + " sene " + str(erget % 30))

            peraklitos = neneveh + 28
            if peraklitos - 30 <= 30:
                a = "gunbet";b = int(peraklitos % 30)
                elet = መዓልቲ(a, b)
                print("peraklitos " + elet + " gunbet " + str(peraklitos % 30))
            elif peraklitos - 30 > 30:
                a = "sene";b = int(peraklitos % 30)
                elet = መዓልቲ(a, b)
                print("peraklitos " + elet + " sene " + str((peraklitos) % 30))

            hawariat = neneveh + 29
            if hawariat - 30 <= 30:
                a = "gunbet";b = int(hawariat % 30)
                elet = መዓልቲ(a, b)
                print("tsome_hawaryat " + elet + " gunbet " + str((hawariat) % 30))
            elif hawariat - 30 > 30:
                a = "sene";b = int(hawariat % 30)
                elet = መዓልቲ(a, b)
                print("tsome_hawerayt " + elet + " sene " + str((hawariat) % 30))

            dhnet = neneveh + 1
            if dhnet <= 30:
                a = "gunbet";b = int(dhnet)
                elet = መዓልቲ(a, b)
                print("tsome_dhnet " + elet + " gunbet " + str(dhnet))
            elif dhnet > 30:
                a = "sene";b = int(dhnet % 30)
                elet = መዓልቲ(a, b)
                print("tsome_dhnet " + elet + " sene " + str(dhnet % 30))

        elif mebajahamer > 30:
            print("mebaja_hamer " + str(ametemhret) + " " + str(mebajahamer % 30))
            a = "yekatit";b = int(mebajahamer % 30)
            elet = መዓልቲ(a, b)
            print("neneveh " + elet + " yekatit " + str(mebajahamer % 30))
            neneveh = mebajahamer % 30
            tsome_arbea = neneveh + 14
            debrezeit = neneveh + 11
            hosaena = neneveh + 2
            sklet = neneveh + 7
            tnsaie = neneveh + 9
            rkeb_kahnat = neneveh + 3
            erget = neneveh + 18
            peraklitos = neneveh + 28
            hawariat = neneveh + 29
            dhnet = neneveh + 1
            if tsome_arbea <= 30:
                a = "yekatit";b = int(tsome_arbea)
                elet = መዓልቲ(a, b)
                print("tsome_arbea " + elet + " yekatit " + str(tsome_arbea))
            elif tsome_arbea > 30:
                a = "megabit";b = int(tsome_arbea % 30)
                elet = መዓልቲ(a, b)
                print("tsome_arbea " + elet + " megabit " + str(tsome_arbea % 30))
            if debrezeit <= 30:
                a = "megabit";b = int(debrezeit)
                elet= መዓልቲ(a, b)
                print("debre_zeyt " + elet + " megabit " + str(debrezeit))
            elif debrezeit > 30:
                a = "miyazya";b = int(debrezeit)
                elet = መዓልቲ(a, b)
                print("debre_zeyt = " + elet + " miyazya " + str(debrezeit))
            if hosaena <= 30:
                a = "ሚያዝያ";b = int(hosaena)
                elet = መዓልቲ(a, b)
                print("hosaena: " + elet + " miyazya " + str(hosaena))
            if sklet <= 30:
                a = "miyazya";b = int(sklet)
                elet = መዓልቲ(a, b)
                print("arbi_sklet " + elet + " miyazya " + str(sklet))
            if tnsaie <= 30:
                a = "miyazya";b = int(tnsaie)
                elet = መዓልቲ(a, b)
                print("tinsae: " + elet + " miyazya " + str(tnsaie))
            if rkeb_kahnat <= 30:
                a = "gunbet";b = int(rkeb_kahnat)
                elet = መዓልቲ(a, b)
                print("rkbe_kahnat " + elet + " gunbet " + str(rkeb_kahnat))
            if erget <= 30:
                a = "gunbet";b = int(erget)
                elet = መዓልቲ(a, b)
                print("erget: " + elet + " gunbet " + str(erget % 30))
            elif erget > 30:
                a = "sene";b = int(erget % 30)
                elet = መዓልቲ(a, b)
                print("erget: " + elet + " gunbet " + str(erget % 30))
            if peraklitos <= 30:
                a = "gunbet";b = int(peraklitos)
                elet = መዓልቲ(a, b)
                print("peraklitos " + elet + " gunbet " + str(peraklitos))
            if peraklitos > 30:
                a = "sene";b = int(peraklitos % 30)
                elet= መዓልቲ(a, b)
                print("peraklitos " + elet + " sene " + str(peraklitos % 30))
            if hawariat > 30:
                a = "sene";b = int(hawariat % 30)
                elet = መዓልቲ(a, b)
                print("tsome_haweryat " + elet + " sene " + str(hawariat % 30))
            if dhnet <= 30:
                a = "sene";b = int(dhnet)
                elet = መዓልቲ(a, b)
                print("tsome_dhnet " + elet + " sene " + str(dhnet % 30))

elif (choice == '3'):
    a = "meskerem";b = 17
    elet=መዓልቲ(a, b)
    print("beale_meskel = " + elet + " meskerem 17")
    a = "hdar";b = 15
    elet = መዓልቲ(a, b)
    print("tsome_nebyat = " + elet + " hdar 15")
    a = "tahsas";b = 29
    elet = መዓልቲ(a, b)
    print("ldet = " + elet + " tahsas 29")
    a = "tiri";b = 6
    elet = መዓልቲ(a, b)
    print("gizret: " + elet + " tiri 6")
    a = "tiri";b = 11
    elet = መዓልቲ(a, b)
    print("tikimti " + elet + " tiri 11")
    a = "yekatit";b = 8
    elet = መዓልቲ(a, b)
    print("beale_simon = " + elet + " yekatit 8")
    a = "megabit";b = 29
    elet = መዓልቲ(a, b)
    print("tsinset = " + elet + " megabit 29")
    a = "nehase";b = 1
    elet = መዓልቲ(a, b)
    a = "nehase";b = 16
    hel = መዓልቲ(a, b)
    print("tsome_flseta " + elet + " nehase_1 to " + hel + " nehase 16")
    a = "ነሓሰ";b = 13
    elet = መዓልቲ(a, b)
    print("debre_tabor " + elet + " nehase 13")
    a = "nehase";b = 16
    elet = መዓልቲ(a, b)
    print("ergeta_l_mariam = " + elet + "ነሓሰ 16")

