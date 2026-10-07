with open("Projeto 1/dados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

placa_busca = input("Digite a placa para busca: ").strip() .upper() #usando o upper para ler tanto maiuscolo ou minusculo
nota_busca = input("Digite o numero da Naf").strip()
mes_busca = input("Digite o mês (numero)").strip() #quebra os espaços assim ajudando na leitura de dados e impedindo erro humano

if mes_busca.isdigit() and len(mes_busca) == 1:  #usuario pode colocar tanto o "2" ou "02" que vai ler "02"
    mes_busca = "0" + mes_busca

achou = False

for linha in linhas:
    dados = linha.strip() .split(";") #faz o a busca no banco de dados tirando o ";" (split) - strip ja quebra a linha invisivel que serio o "/n"

    if len(dados) < 6: #evitar erro de leitura lendo assim somente os 6 indices dos dados
        continue

    data = dados[0]
    placa = dados[1]
    nota = dados[4]

    mes = data.split("/")[1].zfill(2) #divide e sepera a index onde preciso da informação no caso seria a "[1]" pois preciso do mês (ex: 01/02/2020 para 01 "2" 2020)
                            # ja o zfill é para garantir que o mês tenha dois digitos
    cond_placa = (placa_busca == "" or placa == placa_busca) #para que com uma so informão ainda possa fazer a pesquisa  o ( "" ) estando vazio entende com o usuario possa dar enter e colocar o dado desejado para relatorio
    cond_nota = (nota_busca == "" or nota == nota_busca)
    cond_mes = (mes_busca == "" or mes == mes_busca)

    if cond_placa and cond_nota and cond_mes:
        print(dados)
        achou = True
if not achou:
    print("Nenhum resultado encontrado.")