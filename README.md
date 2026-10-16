💰 Controle Financeiro em Python

Programa de terminal para controlar gastos mensais, desenvolvido em Python como projeto de estudo.

📌 Sobre o projeto

O usuário define um orçamento mensal e vai cadastrando seus gastos por categoria. O programa calcula o total, a média e o gasto por categoria, e avisa se o orçamento está sob controle ou foi estourado. Foi criado para praticar lógica de programação, cálculos e estruturas de dados básicas do Python.

✅ Funcionalidades

- Orçamento mensal: definido no início, com validação (precisa ser maior que zero)
- Adicionar gasto: cadastra descrição, categoria e valor
- Listar gastos: mostra todos os gastos numerados
- Ver resumo: exibe total gasto, média por gasto e total por categoria
- Verificar orçamento: compara o total com o orçamento e classifica a situação:
  - dentro do orçamento
  - atenção (80% ou mais utilizado)
  - orçamento utilizado por completo
  - orçamento estourado
- Sair: encerra o programa

 🛠️ Conceitos utilizados

- Listas e dicionários (lista de dicionários)
- Laços while (menu e validações) e for com enumerate()
- Estruturas condicionais (if, elif, else)
- Operadores aritméticos, relacionais e lógicos
- f-strings com formatação de casas decimais (:.2f)
- Métodos de string (replace, strip, title)
- Módulo "os" (limpeza do terminal)

▶️ Como executar

1. Tenha o Python 3 instalado
2. Clone este repositório:

   https://github.com/AndreosDanillo/controle-financeiro-python.git

3. Entre na pasta do projeto:

   cd Controle Financeiro

4. Execute o programa:

   python controle_fin.py

💻 Exemplo de uso


Orçamento de R$ 1000.00

----- MENU -----
1. Adicionar gasto
2. Listar gastos
3. Ver resumo
4. Verificar orçamento
5. Sair
----------------
Marque qual opção deseja: 3

----- RESUMO -----
Total gasto: R$ 90.00
Média por gasto: R$ 30.00

Gasto por categoria:
Alimentação: R$ 50.00
Lazer: R$ 40.00
```

## 🚀 Melhorias futuras

- [ ] Tratar entradas inválidas (letras no lugar de números) com `try/except`
- [ ] Organizar o código em funções
- [ ] Salvar os gastos em arquivo (`.json` ou `.csv`) para não perdê-los ao fechar
- [ ] Permitir remover ou editar gastos
- [ ] Criar orçamento individual por categoria

## 👤 Autor

**Danillo Menezes**
[GitHub](https://github.com/AndreosDanillo)