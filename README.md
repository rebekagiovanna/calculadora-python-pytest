CALCULADORA ARITMÉTICA PARA TESTES EM PYTHON

Este projeto foi desenvolvido para a disciplina de Teste de Software Aplicado do curso de Sistemas e Mídias Digitais na Universidade Federal do Ceará, no semestre 2025.2. O objetivo é demonstrar a aplicação de Testes Manuais de Usabilidade e Testes Automáticos de Unidade utilizando Python e o framework Pytest.

A aplicação consiste em uma calculadora funcional, embora simples, que realiza as quatro operações básicas. O foco do desenvolvimento foi a implementação de uma estrutura robusta capaz de tratar erros de entrada e regras de negócio específicas, como o bloqueio da divisão por zero. O projeto valida a resiliência do software tanto na interface com o usuário quanto na lógica interna das funções.

DETALHES TÉCNICOS

    Linguagem: Python 3.14.2.

    Framework de Teste: Pytest 9.0.2.

    Ferramentas: Visual Studio Code com ajuste de variáveis de ambiente (PATH) para funcionamento do PIP.

    Arquivos: main.py (aplicação principal) e main_test.py (suíte de testes automatizados).

TUTORIAL BÁSICO

    1. Certifique-se de ter o Python instalado e execute o comando abaixo para instalar o framework de testes: pip install pytest

    2. Para testar a aplicação manualmente e interagir com o menu, utilize: python main.py

    3. Para rodar a bateria de testes e visualizar o relatório de sucessos e falhas, utilize: pytest -v

ANÁLISE DE RESULTADOS

O projeto conta com casos de teste que validam fluxos normais e comportamentos sob erro. Um ponto importante na execução foi o uso do pytest.raises para confirmar o tratamento de exceções. Durante os testes automatizados, foi identificada uma falha no teste de tipos, que no caso foi uma multiplicação de inteiro por string. Não se preocupe, foi construído intencionalmente para que o código pudesse testar como o código se comportaria sob estresse dentro dos parâmetros de comportamento nativos da linguagem.

PARA MAIS DETALHES, acesse o arquivo do Documento principal da atividade acadêmica à qual este código se refere: https://drive.google.com/drive/folders/1eGu-EhmI14URNqblyKqYPbG_rzoIkZ3b?usp=sharing
