placa = input("Digite a placa: ")
data = input("Digite a data: ")
item = input("Descreva o item ou serviço: ")
destino = input("Digite o destino (placa do caminhçao ou estoque): ")
Naf = input("Digite numero da nota fiscal: ")
rota = input("Digite a rota: ")

print(f"""
===== CADASTRO =====
Data: {data}
Placa: {placa}
item/serviço: {item}
Destino: {destino}
Nota Fiscal: {Naf}
Rota: {rota}      
""")

with open("Projeto 1/dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{data};{placa};{item};{destino};{Naf};{rota}\n")
