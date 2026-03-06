soubor = "polednice.txt"

with open (soubor, "r", encoding="UTF-8") as f:
    text = f.read()
    
slova = text.split()
print("Pocet slov v textu:", len(slova))

text_bez_mezer = text.replace(" ", "").replace("\n", "")

pocty_pismen = {}

for pismeno in text_bez_mezer:
    if pismeno in pocty_pismen:
        pocty_pismen[pismeno] +=1
    else:
        pocty_pismen[pismeno] = 1
        
serazena_pismena = sorted(pocty_pismen.items(), key=lambda x: x[1], reverse=True)

print("\nNejcastejsi pismena:")
for pismeno, pocet in serazena_pismena[:10]:
        print(pismeno, pocet)

pocty_slov = {}

for slovo in slova:
    if slovo in pocty_slov:
        pocty_slov[slovo] += 1
    else:
        pocty_slov[slovo] = 1

        
serazena_slova = sorted(pocty_slov.items(), key=lambda x: x[1], reverse=True)

print("Nejčastější slova:")
for slovo, pocet in serazena_slova[:10]:  
    print(slovo, pocet)

                
    
    