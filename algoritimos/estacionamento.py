import math
from datetime import datetime
placas_existentes = []
veiculos_estacionados = []
total_arrecadado = []


#Essa função confere quantos minutos um certo veiculo ficou estacionado e retorna o valor de acordo com quantos minutos o veiculo ficou estacionado
def calcular_valor(minutos):
    if minutos <= 15:
        return 0
    else:
        if minutos <= 60:
            return 1.50
        else:
            if minutos > 60:
                return math.ceil((minutos-60) / 60) + 1.5



#Essa função calcula os minutos estacionados e retorna o total de minutos que um veiculo ficou estacionado
def calcular_minutos_estacionados(hora_entrada, hora_saida):
    
    partes_entrada = hora_entrada.split(":")
    partes_saida = hora_saida.split(":")
    
    #Converte as horas em minutos e soma com os minutos restantes
    total_minutos_entrada = int(partes_entrada[0]) * 60 + int(partes_entrada[1])
    total_minutos_saida = int(partes_saida[0]) * 60 + int(partes_saida[1])
    
    diferenca_minutos =  total_minutos_saida - total_minutos_entrada
        
 
    return diferenca_minutos



#Essa função é a principal, contendo uma função para cada opção do menu
def principal():
    print("Bem vindo ao --XXX--- |UniCesumar Parking| ---XXX--")
    menu_dias_semana()
    dia_semana = int(input("Escolha uma opção: "))
    aberto = [1, 2, 3, 4, 5, 6 ]
    fechado = [7]
    if dia_semana in aberto:
        
        print("===========================================")
        print("O estacionamento |UniCesumar Parking| está aberto")
        print("===========================================")
        
    elif dia_semana in fechado:
        print("===========================================")
        print(f"O estacionamento |UniCesumar Parking| está fechado")
        print("===========================================")
        return principal()
        
    else:
        print("===========================================")
        print("Opção invalida")
        print("===========================================")
        return principal()
    
    while True:
        mostrar_menu()
        print("Escolha uma opção: ")
        opcao = int(input())
        if opcao == 1:
            entrada_veiculo()
        elif opcao == 2:
            saida_veiculo()
        elif opcao == 3:
            quantidade_veiculos_estacionados_tipo()
        elif opcao == 4:
            valor_total_arrecadado()
        elif opcao == 5:
            print("=======================================================================")
            print(f"Até o momento temos: {quantidade_veiculos_isentos()} veiculos isentos.")
            print("=======================================================================")
        elif opcao == 6:
            fechar_estacionamento()
            break
        elif opcao == 7:
            print("Programa encerrado")
            break
    
    
#Essa função da a entrada de veiculos, guarda o valor da hora entrada, tipo de veiculo e placa
def entrada_veiculo():
    print("=========================================================")
    tipo_veiculo = input("Tipo do veiculo(carro, moto ou camionete): ")
    
    
    if tipo_veiculo == "carro" or tipo_veiculo == "moto" or tipo_veiculo == "camionete":
        print("Veiculo autorizado")
    else: 
        print("Veiculo não autorizado")
        return 
    hora_entrada = input("Hora de entrada: ")
    
    if ":" not in hora_entrada:
        print("Formato inválido! Use HH:MM")
        return
    elif hora_entrada >= "8:00" or hora_entrada < "18:00":
        print("Estacionamento Aberto")
    else:
        print("ESTACIONAMENTO FECHADO")
        print("HORÁRIO DE ATENTIMENTO: 8:00 até ás 18:00")
        return 
    
    
    
    
    
    while True:
        placa = input("Placa do veiculo: ").upper()

        if placa in placas_existentes:
            print("Placa já existente, tente outra.")
        else:
            print(f"Placa {placa} registrada com sucesso!")
            placas_existentes.append(placa)
            veiculo = {"tipo": tipo_veiculo, "hora_entrada": hora_entrada, "placa": placa}
            veiculos_estacionados.append(veiculo)
            print("=========================================================")
            break
       


#Essa função da a saida do veiculo, a pessoa digita a hora de saida e placa e o programa retorna o valor a ser pago
def saida_veiculo():
    print("=========================================================")
    hora_saida = input("Hora saida: ")
    if ":" not in hora_saida:
        print("Formato inválido! Use HH:MM")
        return 
    
    partes_saida = hora_saida.split(":") 
    partes_saida = partes_saida[0]
    
    if int(partes_saida) > 18:
        print("ESTACIONAMENTO FECHADO")
        print("HORÁRIO DE ATENTIMENTO: 8:00 até ás 18:00")
        
    elif int(partes_saida) >= 8:
        print("HORÁRIO VÁLIDO")
    
    else: 
        print("Formato inválido! Use HH:MM")
        return saida_veiculo()
    
    placa = input("Digite sua placa: ").upper()
    veiculo = buscar_veiculo_por_placa(placa)
    minutos = calcular_minutos_estacionados(veiculo["hora_entrada"], hora_saida)
    valor = calcular_valor(minutos)
    valor_arrecadado = 0
    valor_arrecadado += valor
    total_arrecadado.append(valor_arrecadado)
    
    
    
    veiculos_estacionados.remove(veiculo)
   
    print(f"Valor total a ser pago: {valor} R$")
    print("|OBRIGADO PELA PREFERÊNCIA, UNICESUMAR PARKING AGRADECE|")
    print("=========================================================")
    
    
#Nessa função verificamos se a quantidade do carro tiver o respectivo nome acrescenta mais um a variavel
def quantidade_veiculos_estacionados_tipo():  
    print("=========================================================")
    
    quantidade_carro = 0
    quantidade_moto = 0
    quantidade_camionete = 0
    for veiculo in veiculos_estacionados:
        if veiculo["tipo"] == "carro":
            quantidade_carro += 1
            
        elif veiculo["tipo"] == "moto":
            quantidade_moto += 1
            
        elif veiculo["tipo"] == "camionete":
            quantidade_camionete += 1
            
        
    print(f"O total de carros é igual a: {quantidade_carro}")
    print(f"O total de motos é igual a: {quantidade_moto}")
    print(f"O total de camionetes é igual a: {quantidade_camionete}")

    print("=========================================================")
    
    
    
#Nesssa função  apenas damos um print da variavel global (total_arrecadado) com a função (sum(soma todos os valores de um vetor)) 
#O calculo para isso está apartir da linha 155
def valor_total_arrecadado():

    print("=========================================================")
    print(f"O valor arrecadado até o momento é de: {sum(total_arrecadado)} R$")
    print("=========================================================")


#Essa função calcula o total de veiculos isentos usando a hora atual e a hora de entrada digitada pelo cliente e retorna se o veiculo esta isento ou não
def quantidade_veiculos_isentos():

    quantidade_isentos = 0
    for veiculo in veiculos_estacionados:
        
        hora_atual = datetime.now().strftime('%H:%M')
        minutos = calcular_minutos_estacionados(veiculo["hora_entrada"], hora_atual)
        valor = calcular_valor(minutos)
        if valor == 0:
            quantidade_isentos += 1 

    return quantidade_isentos
    
    
#Esta função busca  veiculo pela placa, passando por um if para saber se o parâmetro placa é igual a placa do veiculo que esta no vetor, se sim retorna o veiculo se não retorna NADA
def buscar_veiculo_por_placa(placa):
    for veiculo in veiculos_estacionados:
        if placa == veiculo["placa"]:
            return veiculo
        
    return None


#Essa função fecha o estacionamento, se ouver algum veiculo no estacionamento vai fechar sua conta automaticamente e vai calcular quanto o veiculo deve pagar.
def fechar_estacionamento():
    
    print("Estacionamento fechado:") 
    for veiculo in veiculos_estacionados:
     
        tipo_veiculo = veiculo["tipo"]
        placa_veiculo = veiculo["placa"]
        valor_total = calcular_valor(calcular_minutos_estacionados(veiculo["hora_entrada"],"18:00"))
        print(f"---VEICULO: {tipo_veiculo}--- | ---PLACA: {placa_veiculo}--- |  ---VALOR: {valor_total}---")
       
        
#Essa função mostra o menu principal
def mostrar_menu():
    print("Opção 1: Entrada de veiculos ")
    print("Opção 2: Saida de veiculos")
    print("Opção 3: Quantidade de veiculos estacionados por tipo ")
    print("Opção 4: Valor total arrecadado até o momento ")
    print("Opção 5: Quantidade de veiculos isentos ")
    print("Opção 6: Fechar estacionamento ")
    print("Opção 7: Encerrar programa")
  
  
#Essa função é o menu dos dias da semana  
def menu_dias_semana():
    print("Opção 1: Segunda-Feira ")
    print("Opção 2: Terça-Feira ")
    print("Opção 3: Quarta-Feira ")
    print("Opção 4: Quinta-Feira ")
    print("Opção 5: Sexta-Feira ")
    print("Opção 6: Sábado ")
    print("Opção 7: Domingo ")
    

principal()
