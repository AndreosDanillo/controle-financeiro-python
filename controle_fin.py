# Importa o módulo "os", usado para limpar o terminal
import os

# Lista que guarda todos os gastos
# Cada gasto é um dicionário: {"descricao": ..., "categoria": ..., "valor": ...}
gastos = []

# ---------- ORÇAMENTO MENSAL ----------
orcamento = float(input('Digite um orçamento mensal: R$ ').replace(',', '.'))

# Repete até o usuário digitar um valor maior que zero
while orcamento <= 0:
    os.system("cls" if os.name == "nt" else "clear")
    print('O orçamento deve ser maior que zero!')
    orcamento = float(input('Digite novamente: R$ ').replace(',', '.'))

os.system("cls" if os.name == "nt" else "clear")
print(f'Orçamento de R$ {orcamento:.2f}')
input('Aperte ENTER para continuar...')
os.system("cls" if os.name == "nt" else "clear")


while True:
    print('----- MENU -----')
    print('1. Adicionar gasto')
    print('2. Listar gastos')
    print('3. Ver resumo')
    print('4. Verificar orçamento')
    print('5. Sair')
    print('-' * 16)

    opcao = input('Marque qual opção deseja: ')
    os.system("cls" if os.name == "nt" else "clear")

    # ---------- OPÇÃO 1: ADICIONAR GASTO ----------
    if opcao == '1':
        descricao = input('Descrição do gasto (ex: Almoço, Roupas, Cinema): ')
        # strip() remove espaços sobrando; title() deixa em maiúsculo
        categoria = input('Categoria (ex: Alimentação, Lazer, Contas): ').strip().title()
        valor = float(input('Qual foi o valor: R$ ').replace(',', '.'))

        while valor <= 0:
            print('Digite um valor maior que zero!')
            valor = float(input('Qual foi o valor: R$ ').replace(',', '.'))

        gasto_add = {"descricao": descricao, "categoria": categoria, "valor": valor}
        gastos.append(gasto_add)
        print(f'Gasto "{descricao}" de R$ {valor:.2f} foi adicionado!')

    # ---------- OPÇÃO 2: LISTAR GASTOS ----------
    elif opcao == '2':
        if not gastos:
            print('Nenhum gasto cadastrado!')
        else:
            print('----- GASTOS -----')
            # start=1 para a numeração começar em 1
            for numero, gasto in enumerate(gastos, start=1):
                print(f'{numero}. {gasto["descricao"]} | {gasto["categoria"]} | R$ {gasto["valor"]:.2f}')

    # ---------- OPÇÃO 3: VER RESUMO ----------
    elif opcao == '3':
        if not gastos:
            print('Nenhum gasto cadastrado para resumir!')
        else:
            # Total gasto
            total = 0
            for gasto in gastos:
                total += gasto["valor"]

            # Média (sem risco de divisão por zero, pois a lista não está vazia)
            media = total / len(gastos)

            # Total por categoria: se já existe, soma; senão, cria
            por_categoria = {}
            for gasto in gastos:
                cat = gasto["categoria"]
                if cat in por_categoria:
                    por_categoria[cat] += gasto["valor"]
                else:
                    por_categoria[cat] = gasto["valor"]

            print('----- RESUMO -----')
            print(f'Total gasto: R$ {total:.2f}')
            print(f'Média por gasto: R$ {media:.2f}')
            print('\nGasto por categoria:')
            for cat, valor_cat in por_categoria.items():
                print(f'{cat}: R$ {valor_cat:.2f}')

    # ---------- OPÇÃO 4: VERIFICAR ORÇAMENTO ----------
    elif opcao == '4':
        if not gastos:
            print('Nenhum gasto cadastrado ainda!')
        else:
            total = 0
            for gasto in gastos:
                total += gasto["valor"]

            # Quanto sobra (negativo se estourou)
            saldo = orcamento - total

            print('----- ORÇAMENTO -----')
            print(f'Orçamento: R$ {orcamento:.2f}')
            print(f'Total gasto: R$ {total:.2f}')

            # A ordem importa: o Python para na primeira condição verdadeira
            if total > orcamento:
                print(f'Orçamento ESTOURADO em R$ {abs(saldo):.2f}!')
            elif total == orcamento:
                print('Você usou exatamente todo o orçamento.')
            elif total >= orcamento * 0.8:
                print(f'Atenção: você já usou 80% ou mais. Restam R$ {saldo:.2f}.')
            else:
                print(f'Dentro do orçamento! Restam R$ {saldo:.2f}.')

    # ---------- OPÇÃO 5: SAIR ----------
    elif opcao == '5':
        print('Saindo...')
        break

    # ---------- OPÇÃO INVÁLIDA ----------
    else:
        print('Opção inválida! Digite novamente.')

    # Pausa única para todas as opções (a 5 não chega aqui, por causa do break)
    input('\nAperte ENTER para continuar...')
    os.system("cls" if os.name == "nt" else "clear")