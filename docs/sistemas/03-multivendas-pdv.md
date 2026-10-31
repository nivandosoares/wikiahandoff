# MultiVendas PDV
> Última atualização:  | Responsável: Nivando Soares

## 1. O que é

Sistema de PDV usado nas **30 maquininhas** da operação, integrado ao TEF para pagamentos por crédito/débito.

## 2. Para que usamos aqui

- Registrar consumo nos pontos de venda, como bar e restaurante, vinculado ao código de barras da pulseira.
- Realizar pagamentos por crédito/débito com TEF.

## 3. Como acessar

- Onde fica: nas maquininhas; .
- Com quem está: .
- Referência: [credenciais e acessos](../08-credenciais-e-acessos.md).

## 4. Dependências de rede

- **Rede fechada obrigatória.** As 30 maquininhas não devem usar as redes abertas dos rádios/parque.
- Os Decos operam em modo router, com DHCP próprio: .
- A operação do ERP depende da saída pelo IP público Eldorado autorizado. Veja [white list do MultiClubes](../04-erp-multiclubes.md).

## 5. Operações do dia a dia

## 6. Integrações com outros sistemas

- [MultiClubes](02-multiclubes.md): vínculo do consumo com cliente e cartão de consumo pelo código de barras da pulseira.
- TEF: pagamentos por crédito/débito; .
- [MultiVendas Retaguarda](01-multivendas-retaguarda.md): retaguarda financeira; .
- Contexto: [fluxo da operação](../01b-fluxo-operacao.md).

## 7. Fornecedor / suporte

| Necessidade | Quem chamar | Como chamar | SLA |
| --- | --- | --- | --- |
| Falha no PDV |  |  |  |
| Falha no TEF |  |  |  |

## 8. Problemas conhecidos

- Uso de PDV em rede aberta é um problema registrado na documentação. A regra operacional é manter as maquininhas em redes fechadas.
- Saída por IP público não autorizado bloqueia o acesso ao ERP.
- Falha de leitura da pulseira interrompe o fluxo: .

- Referência: [problemas conhecidos](../07-problemas-conhecidos.md).

## 9. Procedimentos específicos

- Em falha, registrar posto, horário, mensagem e etapa afetada, conferir a rede fechada e a saída autorizada, e acionar o suporte. Veja [procedimentos gerais](../06-procedimentos.md).

## 🧭 Notas do handover
