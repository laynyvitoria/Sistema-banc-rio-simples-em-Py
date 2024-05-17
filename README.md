# README

## Controle de Transações Bancárias

Este é um programa simples em Python que simula um sistema de controle de transações bancárias. Ele oferece as seguintes funcionalidades:

- Depósito de dinheiro na conta.
- Saque de dinheiro da conta, com limite máximo de saques.
- Verificação do saldo disponível na conta.
- Encerramento do programa.

## Funcionamento

O programa exibe um menu de opções para o usuário, permitindo que ele escolha o que deseja fazer. As opções disponíveis são:

- [D] Depósito: Permite ao usuário realizar um depósito na conta. O valor do depósito é adicionado ao saldo da conta.
- [S] Sacar: Permite ao usuário realizar um saque da conta. O programa verifica se há saldo suficiente na conta e se o valor do saque não ultrapassa o limite estabelecido. Além disso, o programa controla o número máximo de saques permitidos.
- [E] Extrato: Exibe o saldo disponível na conta.
- [P] Encerrar programa: Encerra a execução do programa.

O programa continua em execução em um loop infinito até que o usuário escolha a opção de encerrar o programa.

## Limitações

- Limite de Saques: O programa impõe um limite máximo de três saques durante a execução do programa. Isso é controlado pela variável `quantidades_saques`, que é incrementada cada vez que um saque é realizado com sucesso.
- Limite de Saque: Além do limite de quantidade de saques, há também um limite de valor para cada saque, definido como R$ 500. Isso é controlado pela variável `limite_saque`.
