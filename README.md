# ClearFunds
🌐 This README is available in: [Português](#-versão-em-português)
## 🇬🇧 English Version

**ClearFunds** is an academic project created to help me learn system development concepts. The goal is to simulate a real financial application that registers businesses (merchants) and processes transactions. The system applies business rules and generates settlement files — just like in a real acquirer or sub-acquirer environment.

It also includes important topics from the payment industry, such as ISO 8583 standards, PCI/DSS mentions, and other real-world financial system concepts.

---

## ✨ Current Features

- Register merchants (businesses)
- User interaction through the terminal
- Data saved using JSON files
- Modular structure (`models`, `services`, `data` folders)

---

## 🔮 Planned Features (Roadmap)

- Process multiple transactions per merchant
- Apply fees based on transaction type
- Create payment schedules (D+X simulation)
- Simulate financial settlement
- Generate payment reports for each merchant
- Use a real database for data persistence
- Add automated tests
- Create a GUI or REST API
- Firebase integration
- AI to detect possible fraud and suggest credit based on forecasts

---

## 📁 Project Structure

```bash

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
├── firebase/               # Future Firebase integration
│   ├── firebase_connector.py
├── main.py                 # Main script (menu system)
├── .gitignore              # Git configuratio
```

---

## 🛠️ Technologies and Practices
- Python 3.x
- Object-Oriented Programming (OOP)
- Modular structure
- Good versioning practices (git)
- Semantic commits (feat, chore, fix, etc.)

---

## 🚀 How to Run
You can run the project directly from your code editor (such as VS Code or PyCharm).
1. Clone the repository
2. Open the main script and run it in your terminal or IDE:
```bash

python main.py
```

---

## 📌 Notes
This project is a work in progress and will evolve as I continue to learn.

---

## 🇧🇷 Versão em Português
ClearFunds é um projeto acadêmico voltado ao meu aprendizado de conceitos de desenvolvimento de sistemas. O objetivo é simular uma aplicação financeira real que realiza o cadastro de estabelecimentos e o processamento de transações, com regras de negócio aplicadas e geração de arquivos de liquidação — reproduzindo o ambiente de uma adquirente ou subadquirente.

O sistema também traz elementos típicos do setor de pagamentos, como referências a padrões ISO 8583, menções ao PCI/DSS e conceitos aplicáveis à indústria financeira.

---

## ✨ Funcionalidades Atuais
- Registro de estabelecimentos (merchants)
- Interação com o usuário via terminal 
- Salvamento de dados em arquivos JSON 
- Estrutura modular (divisão em `models`, `services`, `data`)

---

## 🔮 Funcionalidades Planejadas (Roadmap)
- Processamento de múltiplas transações por estabelecimento 
- Aplicação de taxas por tipo de transação
- Geração de agendamentos de pagamento (simulando D+X)
- Simulação de liquidação financeira
- Geração de extrato de pagamentos por estabelecimento
- Persistência em banco de dados
- Testes automatizados
- Interface gráfica ou API REST 
- Integração com Firebase 
- Implementação de IA para prevenção a fraudes e análise de crédito

---

## 📁 Estrutura do Projeto
```bash

ClearFunds/
├── data/                   # Base simulada (arquivos JSON)
│   ├── merchants.json
│   ├── received_transactions.json
│   ├── scheduled_payments.json
│   ├── settled_payments.json
├── models/                 # Definições de classes
│   ├── merchant.py
│   ├── transaction.py
│   ├── schedule.py
│   ├── statement.py
├── services/               # Regras de negócio
│   ├── merchant_service.py
│   ├── transaction_service.py
│   ├── scheduler_service.py
│   ├── settlement_service.py
│   ├── statement_service.py
├── firebase/               # Integração futura com Firebase
│   ├── firebase_connector.py
├── main.py                 # Ponto de entrada do sistema (menu)
├── .gitignore              # Configuração do Git
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
