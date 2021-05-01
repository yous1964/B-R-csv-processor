import pandas as pd

df = pd.read_excel('C:/Users/Guilherme/Code/MTG Desafio Histórico/Desafio Histórico Bans extras.xlsx')

dates = df['Data'].tolist()

formatlist = 0

mostrecentset = df['Most Recent Set'].tolist()

if formatlist == 0:
    bans = df['Vintage Bans'].tolist()
    unbans = df['Vintage Unbans'].tolist()

    restricts = df['Vintage Restricts'].tolist()
    unrestricts = df['Vintage Unrestricts'].tolist()


current_bans = []
current_restricts = []

output = open('banlist.txt', 'w')

for pops in range(len(dates)):
    changes = 0
    bans[pops] = bans[pops].split("\n")
    unbans[pops] = unbans[pops].split("\n")
    restricts[pops] = restricts[pops].split("\n")
    unrestricts[pops] = unrestricts[pops].split("\n")
    string = ""

    # Existe ban ou unban, restrict ou unrestrict?
    if bans[pops] != ['---'] or unbans[pops] != ['---']:
        print("\nData:",dates[pops])
        string = "\nData: {}\nSet mais recente: {}\n".format(dates[pops],mostrecentset[pops])
        output.write(string)

        print("Bans:",bans[pops])
        string = "Bans: {}\n".format(bans[pops])
        output.write(string)

        print("Unbans:",unbans[pops],"\n")
        string = "Unbans: {}\n".format(unbans[pops])
        output.write(string)

    # Se houve ban, adicionar cartas banidas à lista de banidas atuais
    if bans[pops] != ['---']:
        for i in range (len(bans[pops])):
            if bans[pops][i] != ['---'] and bans[pops][i] != '---':
                current_bans.append(bans[pops][i])
        changes = 1

    # Se houve unban, remover cartas desbanidas da lista atual
    if unbans[pops] != ['---']:
        for i in range (len(unbans[pops])):
            if unbans[pops][i] in current_bans:
                current_bans.remove(unbans[pops][i])
        changes = 1

    # Se houve restrição ou desrestrição, modificar listas de acordo
    if restricts[pops] != ['---'] or unrestricts[pops] != ['---']:
        # Se não houve ban ou unban, escrever data
        if changes == 0:
            print(mostrecentset[pops])
            print("\nData:",dates[pops])
            string = "\nData: {}\nSet mais recente: {}\n".format(dates[pops],mostrecentset[pops])
            output.write(string)

        # Imprimir e escrever restritas
        print("Restricts:",restricts[pops])
        string = "Restricts: {}\n".format(restricts[pops])
        output.write(string)

        # Imprimir e escrever desrestritas
        print("Unrestricts:",unrestricts[pops],"\n")
        string = "Unrestricts: {}\n".format(unrestricts[pops])
        output.write(string)


    if restricts[pops] != ['---']:
        for i in range (len(restricts[pops])):
            if restricts[pops][i] != ['---'] and restricts[pops][i] != '---':
                current_restricts.append(restricts[pops][i])
        changes = 1

    if unrestricts[pops] != ['---']:
        for i in range (len(unrestricts[pops])):
            if unrestricts[pops][i] in current_restricts:
                current_restricts.remove(unrestricts[pops][i])
        changes = 1
    

    # Se houve mudança, imprimir e escrever data e listas atuais no arquivo 
    if changes == 1:
        print("Current Banlist:",current_bans)
        string = "\nBanlist Vigente:\n"
        output.write(string)

        for i in range(len(current_bans)):
            string = "{}\n".format(current_bans[i])
            output.write(string)

        print("Current Restricted:",current_restricts)
        string = "\nRestricted List Vigente:\n"
        output.write(string)

        for i in range(len(current_restricts)):
            string = "{}\n".format(current_restricts[i])
            output.write(string)
        changes = 0
    


output.close()