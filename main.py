#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
produkts = []
cenas = []
names = []
pass

import json

while True:
    print("\nKases aparāta Menu:")
    print("1. Pievienot precu")
    print("2. Dzēst preci pēc numura")
    print("3. Samaksāt")


    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            name = input("Enter a precu nosaukums: ")
            cena = float(input("Enter precu cena: "))
            atlaide = float(input("Enter precu atlaide: "))
            
            if len(name) > 120 or len(name) < 2:
                print("Kļuda, nosaukums nevar būt mazāk ka 2 un lielak ka 120")
                break
            if cena < 0:
                print("Kļuda, cena nevar būt mazāk ka nule")
                break
            
            if cena > 9999:
                print("Kļuda, cena nevar būt lielak ka 9999")
                break
            if atlaide == 0:
                atlaide + 1
                produkt = {"Precu nosaukums": name, "Precu cena": cena, "Precu atlaide": atlaide }
            
            if atlaide > 0:
                produkt = {"Precu nosaukums": name, "Precu cena": cena, "Precu atlaide": atlaide}
            if atlaide < 0:
                print("Kļuda, atldaide nevar būt mazāk ka nule")
                break
            
            produkts.append(produkt)
            cenas.append(cena)
            names.append(name)
            print(produkts)

            pass
            atbilde = input("vēl vairāk preču?: ")
            if atbilde == "n":
                break
            if atbilde == "y":
                pass
    if choice == "2":
        index_1 = int(input("Kuru produktu vēlaties dzēst?: "))
        index_2 = index_1 - 1
        produkts.pop(index_2)
        print(produkts)
        pass
    if choice == "3":
        suma = sum(cenas)
        balance = float(input("Cik naudas jums ir?: "))
        produkta_cena = cena / 100 * atlaide
        pirkums = balance - produkta_cena
        if pirkums < 0:
            print("Nepietiek naudas")
            break
        if pirkums > 0:
            print("Pirkums bija veiksmīgs, atlikums šeit ie čeks: ")
            ček = {"Precu nosaukumi": names, "Precu cena bez atlaide": suma, "Precu cena": produkta_cena, "Atlikums":pirkums }
            print(ček)
            with open("produkts.json", "w") as outfile:
                json.dump(ček, outfile)   
            break

    
       
  
  


            
        

        
        
        
        