# ERP MultiClubes
> Última atualização:  | Responsável: Nivando Soares

> Detalhamento por sistema (MultiVendas Retaguarda, MultiVendas PDV, Id Control, EzPoint Web) está em [/sistemas/](sistemas/). Este arquivo trata do MultiClubes como ERP central.

O MultiClubes controla a operação ponta a ponta: vendas online, gestão de sócios, ativação de pulseira, vendas, PDV, TEF, portaria, catraca e integrações. O ERP e o backup são 100% cloud. **Backup, atualização e administração do ERP são responsabilidade da fornecedora.**

## White list de IP

Após um ataque ao ERP no RJ, a fornecedora fechou as rotas de entrada e criou uma white list de IP público: o acesso depende de sair por um IP autorizado. Nosso IP autorizado é o da **Eldorado Telecom**: .

Se a saída mudar para um IP não autorizado, o acesso ao ERP quebra mesmo que a internet continue funcionando. Foi o que ocorreu no failover StarLink, cujo IP público mudava. **StarLink não serve hoje como failover do ERP:** o antigo ponto foi reaproveitado para distribuição da rede do ISP atual.

Antes de mudar link ou IP público, combine a autorização com a fornecedora e valide o acesso. . Ainda falta um plano B de link autorizado para o ERP.

## O que é nosso x o que é da fornecedora

| Nosso lado | Lado da fornecedora |
| --- | --- |
| Energia, computadores, maquininhas e conectividade local | Administração e atualização do ERP cloud |
| Redes fechadas de PDV e saída pelo IP Eldorado autorizado | Controle da white list e liberação do acesso ao ERP |
| Diagnóstico local, abertura de chamados e validação com a operação | Backup cloud e execução da restauração do ERP |
|  |  |

### PDV, TEF, catraca, portaria e ativação de pulseira

Todos esses fluxos fazem parte do MultiClubes; não tratá-los como sistemas independentes ao abrir chamado. As **30 maquininhas do ERP só entram em redes fechadas**, nunca nas redes abertas dos rádios/parque.

Para validar uma correção, acompanhe os fluxos afetados, incluindo ativação de pulseira e passagem pela portaria/catraca: .

## Quem chamar / SLA

| Necessidade | Quem chamar | Como chamar | SLA |
| --- | --- | --- | --- |
| Indisponibilidade ou falha operacional |  |  |  |
| Problemas de TEF |  |  |  |
| Configurações de Adquirente |  |  |  |

## Referências da operação

| Item | Referência |
| --- | --- |
| Acesso ao ERP |  |
| Catraca e portaria |  |
| Ativação de pulseira |  |
| PDV e TEF | 30 maquininhas em redes fechadas;  |
| Vendas online e gestão de sócios |  |
| Integrações |  |
| Backup cloud |  |

## Em caso de falha

1. Registre horário, sintoma, mensagem e áreas afetadas: .
2. Confira conectividade, rede fechada dos PDVs e saída pela Eldorado; se o IP público mudou, confirme a white list com a fornecedora. Consulte [procedimentos](06-procedimentos.md).
3. Acione a fornecedora pelos canais acima e registre o protocolo: .
4. Alinhe a continuidade da operação: .
5. Após a correção, valide os fluxos afetados com a operação e registre o resultado.

## Acesso ao ERP fora do parque — Tailscale e exit node

**Requisito informado pelo responsável em 19/10/2026:** para acessar o ERP fora das instalações, usar Tailscale com um **exit node no servidor de acesso da rede interna do parque**. Assim, o cliente externo deve utilizar a saída do parque com IP público autorizado pela fornecedora.

O uso desse servidor como exit node já é citado em [ferramentas de acesso](sistemas/06-ferramentas-externas.md). Identificação do servidor, sistema operacional, aprovação, permissões e teste atual: **pendentes de levantamento**. Estar conectado à TailNet, por si só, não confirma que o cliente utiliza o exit node.

A validação deve comparar o IP público observado no cliente externo com o IP autorizado confirmado pela fornecedora e testar o acesso real ao ERP. A referência `177.12.159.224` consta no [índice](README.md), mas não foi revalidada nesta revisão. Esse acesso depende do servidor e da conectividade do parque; não constitui um link de contingência.

Levantamento necessário e critérios de conclusão: [avaliação e plano de preenchimento](12-avaliacao-e-plano.md). Funcionamento do recurso: [documentação oficial do Tailscale](https://tailscale.com/docs/features/exit-nodes).
