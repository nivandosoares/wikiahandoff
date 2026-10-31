# Handover de infraestrutura
>  Responsável: Nivando Soares

## Os 5 pontos mais críticos

1. **MultiClubes manda na operação inteira:** vendas online, sócios, ativação de pulseira, vendas, PDV, TEF, portaria e catraca.
2. **O ERP só aceita o IP público autorizado da Eldorado Telecom.** Mudar a saída de internet pode bloquear o acesso de forma que o acesso a internet segue normal, **mas os Pontos de venda não**. StarLink não é mais failover; o antigo ponto virou distribuição do ISP atual. o IP público de sáida é **177.12.159.224** e pode ser verificado com uma requisição simples HTTP em [https://api.ipify.org/](https://api.ipify.org/) a partir de qualquer dispositivo conectado a rede.
3. **As 30 maquininhas do ERP só entram em rede fechada.** 
4. **Não existe cofre de senhas corporativo.** A implantação e a transferência segura dos acessos são pendências: 
5. **Backup e administração do ERP são 100% cloud e da fornecedora.** Tenha o contato e o links relevantes: .

## Índice

- [00 — Onboarding](00-onboarding.md)
- [01 — Topologia](01-topologia.md)
- [01b — Fluxo da Operação](01b-fluxo-operacao.md)
- [02 — Equipamentos](02-equipamentos.md)
- [03 — MikroTik](03-mikrotik.md)
- [04 — ERP MultiClubes](04-erp-multiclubes.md)
- [05 — Serviços externos](05-servicos-externos.md)
- [06 — Procedimentos](06-procedimentos.md)
- [07 — Problemas conhecidos](07-problemas-conhecidos.md)
- [08 — Credenciais e acessos](08-credenciais-e-acessos.md)
- [09 — Inventário](09-inventario.md)
- [10 — Pendências](10-pendencias.md)
- [11 — Histórico](11-historico.md)
- [Checklist de saída](checklist-saida.md)
- [MultiVendas Retaguarda](sistemas/01-multivendas-retaguarda.md)
- [MultiClubes — Detalhamento](sistemas/02-multiclubes.md)
- [MultiVendas PDV](sistemas/03-multivendas-pdv.md)
- [EzPoint Web](sistemas/04-ezpoint-web.md)
- [Id Control](sistemas/05-id-control.md)
- [Ferramentas Externas de Acesso e Suporte](sistemas/06-ferramentas-externas.md)
- [Rede — Básico para o Dia a Dia](sistemas/07-rede-basico.md)


## Evolução da documentação

- [Avaliação da estrutura, lacunas e ordem de preenchimento](12-avaliacao-e-plano.md) — revisão documental de 19/10/2026.
