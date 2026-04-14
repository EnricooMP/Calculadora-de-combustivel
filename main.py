E = (1.70)
D = (2.00)

while True:
    try:
        litros = float(input("\nQuantidade de litros abastecido: "))
        escolha = input("\nEscolha o combustivel Etanol(E), Diesel(D) ou sair: ").upper().strip()

        if escolha in ["ETANOL", "E"]:
            if litros <= 15:
                porcentagem = 0.02
                msg_desconto = "2%"
            else:
                porcentagem = 0.04
                msg_desconto = "4%"
                
            valor_total = litros * E
            valor_desconto = valor_total * porcentagem
            valor_pagar = valor_total - valor_desconto
            print(f"\nValor à ser pago com {msg_desconto} de desconto é: R${valor_pagar:.2f}")

        elif escolha in ["DIESEL", "D"]:
            if litros <= 15:
                porcentagem = 0.03
                msg_desconto = "3%"
            else:
                porcentagem = 0.05
                msg_desconto = "5%"
                
            valor_total = litros * D
            valor_desconto = valor_total * porcentagem
            valor_pagar = valor_total - valor_desconto
            print(f"\nValor à pagar com {msg_desconto} de desconto é: R${valor_pagar:.2f}")
        else:
            print("\nErro: combustível inválido! Escolha entre 'E' ou 'D'.")
            continue

    except ValueError:
        print("Erro: Digite apenas números")
        continue

    pergunta = input("\nDeseja realziar outro cáclulo? (s/n)") 
    if pergunta != 's':
        print("Até logo!")
        break
