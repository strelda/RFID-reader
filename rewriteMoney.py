#číslo řádku ve functions.js, na kterém je "const users = {" is
ln = 22
# počet účastníků
nu = 4
# počet řádků na jednoho účastníka (musí být všude stejná)
db = 9

with open('functions.js', 'r') as file:
    # read a list of lines into data
    data = file.readlines()


print(" - pro přepsání statusu napiš číslo, pokud chceš přičíst, či odečíst napiš před číslo '+', resp. '-' \n - Pokud jsi posledního uživatele pokaňkal, tak se k němu vrať napsáním a odentrováním 'b' \n")
i = 0
while i<nu:
    print(data[ln+db*i][5:-4])

    previous = int(data[ln+4+db*i][18:-2])
    statusIn = input()

    if statusIn!='b':
        if statusIn[0]=='+':
            newStatus =  previous + int(statusIn[1:])
        elif statusIn[0]=='-':
            newStatus = previous -int(statusIn[1:])
        else:
            newStatus = statusIn
        
        data[ln+4+db*i] = '        "status": '+str(newStatus)+',\n'
        i+=1
    else:
        i-=1


print('n')
for q in ["napiš 'ano', pokud si přeješ zapsat změny", "fakt ne? Máš druhou možnost napsat 'ano', jestli sis to rozmyslel"]:
    print(q)
    ready = input()
    if ready=='ano':
        with open('functions.js', 'w') as file:
            file.writelines( data )
