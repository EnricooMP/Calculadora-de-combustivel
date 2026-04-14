# Calculadora de Combustível com Desconto Progressivo ⛽

Este programa simula o sistema de um posto de combustível, calculando o valor final a ser pago com base na quantidade de litros e no tipo de combustível escolhido, aplicando descontos automáticos.

## 📋 Regras de Desconto

O sistema aplica descontos diferentes dependendo do volume abastecido:

| Combustível | Até 15 Litros | Acima de 15 Litros | Preço Base (L) |
| :--- | :--- | :--- | :--- |
| **Etanol (E)** | 2% de desconto | 4% de desconto | R$ 1,70 |
| **Diesel (D)** | 3% de desconto | 5% de desconto | R$ 2,00 |

## ✨ Funcionalidades

- **Seleção de Combustível:** Aceita "E" para Etanol e "D" para Diesel (independente de maiúsculas ou minúsculas).
- **Cálculo Automático:** Aplica a porcentagem de desconto correta baseada no volume.
- **Validação de Dados:** Bloqueia entradas que não sejam números e avisa se o combustível for inválido.
- **Loop de Uso:** Permite realizar múltiplos cálculos sem precisar reiniciar o programa manualmente.

## 🚀 Como usar

1. Execute o script Python:
   ```bash
   python main.py
