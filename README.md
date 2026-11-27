# Calculadora de Sub-redes IPv4

Aplicação desktop em Python com interface gráfica (`tkinter`) para calcular informações de sub-redes IPv4 a partir de um endereço IP e máscara decimal ou prefixo CIDR.

## Funcionalidades

- Cálculo do **endereço de rede**, **máscara de sub-rede** e **endereço de broadcast**.
- Exibição do **total de IPs**, **hosts utilizáveis** e **faixa de hosts** (quando aplicável).
- Aceita máscara de sub-rede em formato decimal (ex.: `255.255.255.0`) ou prefixo CIDR (ex.: `24`).
- Utiliza o módulo nativo `ipaddress` do Python, sem necessidade de instalar bibliotecas externas.

## Como executar

1. Certifique-se de ter o **Python 3** instalado (com `tkinter` disponível, padrão na instalação oficial no Windows/macOS).
2. Abra a pasta do projeto no **VS Code**.
3. Execute o arquivo `calculadora_ipv4.py` clicando em **Play** (`▷`) ou rodando no terminal:
   ```bash
   python calculadora_ipv4.py