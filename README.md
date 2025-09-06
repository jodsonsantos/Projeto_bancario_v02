Sistema Bancário V2

Descrição

Sistema bancário de console desenvolvido em Python, versão 2, para simular operações de um banco fictício. O projeto foi criado para praticar modularização, passagem de argumentos (positional-only e keyword-only) e gerenciamento de dados. Funcionalidades incluem:





Depósito: Permite adicionar valores positivos à conta, usando argumentos positional-only (saldo, valor, extrato).



Saque: Permite até 3 saques diários com limite de R$ 500 por saque, com validação de saldo, usando argumentos keyword-only (saldo, valor, extrato, limite, numero_saques, limite_saque).



Extrato: Exibe o histórico de transações e o saldo atual no formato R$ xxx.xx, com argumentos positional (saldo) e keyword (extrato).



Criar Usuário: Cadastra clientes com nome, data de nascimento, CPF (somente números, sem duplicatas) e endereço (logradouro, nro - bairro - cidade/estado).



Criar Conta Corrente: Cria contas com agência fixa "0001", número sequencial e vínculo a um usuário por CPF.



Listar Contas: Mostra todas as contas cadastradas com agência, número e nome/CPF do usuário.

O sistema é ideal para demonstrar habilidades em Python, incluindo estruturas de dados (listas, dicionários), validações e modularização, voltado para o mercado de TI em Portugal.

Como executar





Instale o Python 3.8+ (www.python.org).



Clone o repositório: git clone https://github.com/jodsonsantos/Projeto_bancario_v02.git


Execute: python sistema_bancario_v2.py.

Tecnologias





Python 3.8+



Sem dependências externas

Autor

Jodson Santos de Jesus -  Análista e Desenvolvimento de Sistemas, Portugal

Licença

MIT License