# ClearFunds

**ClearFunds** é um projeto que simula o sistema de uma **adquirente** ou **subadquirente** com foco no **registro de agendamentos de pagamento**, como **liquidações** e **antecipações**.

O principal objetivo é criar uma base sólida que reflita operações reais do mercado de meios de pagamento, com práticas estruturadas e orientadas a serviços.

Este projeto também faz parte do meu **processo de transição de carreira e aprimoramento como desenvolvedor de software**. Com ele, busco exercitar e consolidar **boas práticas adotadas pelo mercado**.


---

## ✨ Funcionalidades Atuais

- Registro de estabelecimentos (merchants)
- Interação com o usuário via terminal
- Salvamento de dados por meio de serviços internos
- Estrutura modular com organização em pastas (`models`, `services`)

## 🔮 Funcionalidades Planejadas

- Processamento de um conjunto de transações por estabelecimento
- Aplicação de taxas por tipo de transação
- Geração de agendamentos de pagamento para datas específicas
- Simulação de liquidação financeira
- Geração de extrato de pagamentos para cada merchant
---

## 📁 Estrutura do Projeto
```bash
ClearFunds/
ClearFunds/
├── data/                   # Simulated database (JSON files)
│   ├── merchants.json
│   ├── received_transactions.json
│   ├── scheduled_payments.json
│   ├── settled_payments.json
├── models/                 # Class definitions
│   ├── merchant.py
│   ├── transaction.py
│   ├── schedule.py
│   ├── statement.py
├── services/               # Business logic
│   ├── merchant_service.py
│   ├── transaction_service.py
│   ├── schedule_service.py
│   ├── settlement_service.py
│   ├── statement_service.py
├── firebase/               # Firebase integration (future)
│   ├── firebase_connector.py
├── main.py                 # Main entry point (menu system)
├── .gitignore              # Git configuration
```


---

## 🛠️ Tecnologias e Práticas Utilizadas
- Python 3.x 
- Programação Orientada a Objetos (POO)
- Estrutura modular
- Boas práticas de versionamento (git)
- Commits semânticos (feat, chore, fix, etc.)


---

## 🚀 Como Executar
Você pode rodar o projeto diretamente pelo seu editor de código (como VS Code ou PyCharm).

1. Abra o arquivo `main.py`
2. Clique em "Run" ou execute o script no terminal com:
```bash
python main.py
```


---

## 📌 Observações
Este projeto está em desenvolvimento contínuo.
Novas funcionalidades serão adicionadas ao longo da minha jornada de aprendizado, como:

- Persistência em banco de dados 
- Testes automatizados
- Interface gráfica ou API REST

