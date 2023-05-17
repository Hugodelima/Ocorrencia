from datetime import datetime


def captura_data_hora_cadastro(ocorrencia):
    arquivo = open('log.txt', 'a', encoding='utf-8')
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    arquivo.write(str(data_e_hora_em_texto)+' Foi cadastrado com sucesso a ocorrencia:'+str(ocorrencia)+'\n')

    arquivo.close()

def captura_data_hora_atividade(ocorrencia,backup):
    arquivo = open('log.txt', 'a', encoding='utf-8')
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    arquivo.write(str(captura_data_hora_atividade)+' Foi Alterado os status de'+str(backup) + 'Para' + str(ocorrencia)+'\n')

    arquivo.close()




def menu_ocorrencias(lista_ocorrencias, count):
    opcao = 1
    while opcao != 0:
        print("---Menu de Ocorrências---")
        print("1 - Cadastro de ocorrência")
        print("2 - Listar todas ocorrências")
        print("3 - Listar todas ocorrências ativas")
        print("4 - Buscar Ocorrência por título")
        print("5 - Alterar atividade da ocorrência")
        print("6 - Remover Ocorrência")
        print("7 - Listar Ocorrências por mês")
        print("8 - Listar Ocorrências contendo a palavra")
        print("0 - Sair")
        opcao = int(input("Entre com a opção>>"))
        if opcao == 1:
            print("---Cadastro---")
            cadastro(lista_ocorrencias, count)
            count += 1

        elif opcao == 2:
            print("---Listagem---")
            listagem(lista_ocorrencias)
            editar_e_excluir_ocorrencia(lista_ocorrencias)

        elif opcao == 3:
            print("Listagem[ATIVAS]")
            listagem_ativas(lista_ocorrencias)
           
        elif opcao == 4:
            print("Busca por título")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
            else:
                print("Ocorrência não encontrada!")
        elif opcao == 5:
            print("Alteração de Status de Atividade")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
                resp = input("Deseja alterar a situação da atividade " 
                      "da ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias[posicao]["status"] = not lista_ocorrencias[posicao]["status"]
                    editar_e_excluir_ocorrencia(lista_ocorrencias)
                    print("Alteração realizada com sucesso!")
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não encontrada!")
        elif opcao == 6:
            print("Remoção de Ocorrência")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
                resp = input("Deseja remover a ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias.pop(posicao)
                    editar_e_excluir_ocorrencia(lista_ocorrencias)
                    print("Remoção realizada com sucesso!")
                    
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não encontrada!")
        elif opcao == 7:
            print("Listagem de Ocorrências por mês")
            mes = input("Entre com o mês de ocorrência:")
            lista_m = buscar_ocorrencia_mes(lista_ocorrencias, mes)
            if lista_m:
                print("***Ocorrência(s) Encontrada(s)!***")
                listagem(lista_m)
            else:
                print("Não existem ocorrências para o mês ", mes, "!")
        elif opcao == 8:
            print("Listagem de Ocorrências que contem a palavra:")
            titulo = input("Entre a palavra buscada na ocorrência:")
            lista_m = buscar_ocorrencia_palavra(lista_ocorrencias, titulo)
            if lista_m:
                print("***Ocorrência(s) Encontrada(s)!***")
                listagem(lista_m)
            else:
                print("Não existem ocorrências com a palavra ", titulo, "!")
        elif opcao == 0:
            print("Saindo do programa!!!")
        else:
            print("Opção Inválida!")

def cadastro(lista_ocorrencias, count):
    id = count
    titulo = input("Entre com o título da ocorrência:")
    descricao = input("Entre com a descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input("Está em atividade? (sim|não)")
    status = True if em_atividade == "sim" else False
    data = input("Entre com a data de inclusão:")
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    ocorrencia = dict(id = id, titulo = titulo, 
                      descricao = descricao, 
                      implicacoes = implicacoes, 
                      status = status, data = data, prazo = prazo)
    captura_data_hora_cadastro(ocorrencia)
    lista_ocorrencias.append(ocorrencia)
    grava_ocorrencia(ocorrencia)
    
    print("Ocorrência cadastrada com sucesso!")

def listagem(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências---")
        for i in range(tamanho):
           impressao_ocorrencia(lista_ocorrencias[i], i)  
    else:
        print("Não existem ocorrências cadastradas.")
    
def listagem_ativas(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências ativas---")
        existem_ativas = False
        for i in range(tamanho):
            if lista_ocorrencias[i]["status"] == True:
                impressao_ocorrencia(lista_ocorrencias[i], i)
                existem_ativas = True
        if not existem_ativas:
            print("Não existem ocorrências ativas")
                
    else:
        print("Não existem ocorrências cadastradas.")

def impressao_ocorrencia(ocorrencia, i):
    print("###Ocorrência ", i + 1, "###")
    print("Id:", ocorrencia["id"])
    print("Título:",ocorrencia["titulo"])
    print("Descrição:",ocorrencia["descricao"])
    print("Implicações:",ocorrencia["implicacoes"])
    print("Em atividade:",
    "sim" if ocorrencia["status"] == True
        else "não")
    print("Data de inclusão: ", ocorrencia["data"])
    print("Prazo (em dias):",ocorrencia["prazo"])

def buscar_ocorrencia(lista_ocorrencias, titulo):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        for i in range(tamanho):
            if lista_ocorrencias[i]["titulo"] == titulo:
                return i
        return -1
    else:
        return -1

def buscar_ocorrencia_mes(lista_ocorrencias, mes):
    tamanho = len(lista_ocorrencias)
    lista_mes = []
    if tamanho > 0:
        for i in range(tamanho):
            corte_mes = lista_ocorrencias[i]["data"]
            if corte_mes[3:5] == mes:
                lista_mes.append(lista_ocorrencias[i])
        return lista_mes
    else:
        return lista_mes

def buscar_ocorrencia_palavra(lista_ocorrencias, titulo):
    tamanho = len(lista_ocorrencias)
    lista_occ = []
    if tamanho > 0:
        for i in range(tamanho):
            if titulo in lista_ocorrencias[i]["titulo"]:
                lista_occ.append(lista_ocorrencias[i])
        return lista_occ
    else:
        return lista_occ

def grava_ocorrencia(ocorrencia):
  arquivo = open("ocorrencias.txt","a")
  arquivo.write("Id:"+str(ocorrencia["id"])+"\n")
  arquivo.write("Título:"+ocorrencia["titulo"]+"\n")
  arquivo.write("Descrição:"+ocorrencia["descricao"]+"\n")
  arquivo.write("Implicações:"+ocorrencia["implicacoes"]+"\n")
  arquivo.write("Status:"+str(ocorrencia["status"])+"\n")
  arquivo.write("Data de inclusão:"+ocorrencia["data"]+"\n")
  arquivo.write("Prazo (em dias):"+str(ocorrencia["prazo"])+"\n")
  arquivo.close()

def carregar_ocorrencias(count):
  arquivo = open("ocorrencias.txt", "r")
  lista_ocorrencias = []
  for linha in arquivo:
    id = int(linha[3:len(linha)-1])
    linha = arquivo.readline()
    titulo = linha[7:len(linha)-1]
    linha = arquivo.readline()
    descricao = linha[10:len(linha)-1]
    linha = arquivo.readline()
    implicacoes = linha[12:len(linha)-1]
    linha = arquivo.readline()
    em_atividade = linha[7:len(linha)-1]
    status = True if em_atividade == "True" else False
    linha = arquivo.readline()
    data = linha[17:len(linha)-1]
    linha = arquivo.readline()
    prazo = linha[16:len(linha)-1]
    
    ocorrencia = dict(id = id, titulo = titulo, 
                      descricao = descricao, 
                      implicacoes = implicacoes, 
                      status = status, data = data, prazo = prazo)
    lista_ocorrencias.append(ocorrencia)
    count = id + 1
  arquivo.close()
  return lista_ocorrencias, count

def editar_e_excluir_ocorrencia(ocorrencia):
    arquivo = open("ocorrencias.txt", "w")
    backup = ocorrencia
    for x in backup:
        backup = grava_ocorrencia(ocorrencia)

    captura_data_hora_atividade(ocorrencia,backup)

    arquivo.close()
    for i in ocorrencia:
        grava_ocorrencia(i)



       



#execução
count = 0

lista_ocorrencias, count = carregar_ocorrencias(count)
menu_ocorrencias(lista_ocorrencias, count)

