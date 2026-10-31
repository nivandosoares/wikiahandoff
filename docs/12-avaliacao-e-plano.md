# Avaliação da wiki e plano de preenchimento
> Revisão documental: 19/10/2026 | Responsável pela transição: Nivando Soares

## Objetivo e escopo

Organizar a Wiki de Infraestrutura e Operações de TI da ACQUAVILLE PARK SHOW LTDA para que o próximo técnico consiga manter vendas, portaria, acesso de visitantes e conectividade com o ERP. A prioridade é documentar o ambiente real e seus caminhos de recuperação.

Esta avaliação cruza os 22 Markdown existentes com o contexto fornecido pelo responsável. Não houve nova consulta aos equipamentos, teste de contingência ou validação presencial. A data desta revisão não atualiza a validade das configurações coletadas em 08/10/2026.

## Classificação das informações

- **Confirmado e validado:** acompanhado de fonte, data e resultado da verificação. Uma coleta antiga comprova somente o estado daquela data.
- **Histórico, sujeito a confirmação:** relato ou configuração anterior sem nova verificação operacional.
- **Pendente de levantamento:** informação, evidência ou teste ainda indisponível; usar `` para o dado faltante.
- **Descontinuado:** retirada de uso explicitamente registrada, com fonte e data quando disponíveis. Não classificar uma ferramenta como descontinuada apenas por não apresentar tráfego.

Recomendações e procedimentos propostos devem ser identificados como tais até serem testados e aceitos pelo responsável. Não registrar senhas, tokens, chaves ou códigos de recuperação.

## Estrutura atual e lacunas

A estrutura existente pode ser mantida. Os temas abaixo cabem nos artigos atuais; novos runbooks poderão ser separados quando houver dados suficientes.

| Área | Conteúdo existente | Lacuna operacional |
| --- | --- | --- |
| Visão geral e entrada do sucessor | [Índice](README.md), [onboarding](00-onboarding.md), [fluxo NFC](01b-fluxo-operacao.md) | Horários críticos, responsáveis e critérios de aceite; confirmar o fluxo real das catracas |
| Topologia e conectividade | [Topologia](01-topologia.md), [MikroTik](03-mikrotik.md) | Mapa físico de cabos e switches, caminhos por setor, sub-redes dos roteadores intermediários e validação atual das WANs |
| Equipamentos | [Equipamentos](02-equipamentos.md), [inventário](09-inventario.md) | Uma linha por ativo, localização, alimentação, uplink, IP/DHCP, acesso de gestão e responsável; incluir servidor de acesso, balanças e áudio/vídeo |
| ERP e sistemas | [ERP central](04-erp-multiclubes.md), [sistemas](sistemas/02-multiclubes.md) e artigos específicos | URLs, passos reais de operação, contatos, TEF, integração das catracas e comportamento durante indisponibilidade |
| Acesso remoto e segurança | [Acessos](08-credenciais-e-acessos.md), [ferramentas](sistemas/06-ferramentas-externas.md) | Identificação do servidor de acesso, exit node, permissões, recuperação da conta e transferência de administração |
| Operação e runbooks | [Procedimentos](06-procedimentos.md) | Muitos passos ainda dependem de informação ausente; faltam resultados esperados, escalonamento, validação e reversão por cenário |
| Incidentes e diagnóstico | [Problemas conhecidos](07-problemas-conhecidos.md), [histórico](11-historico.md) | Registrar lentidão no almoço, CFTV diferente por provedor e falhas físicas como relatos históricos; coletar datas, evidências e desfechos |
| Fornecedores e serviços web | [Serviços externos](05-servicos-externos.md), ERP e acessos | Contatos de urgência, contratos/SLA, domínio/DNS, hospedagem, renovação, backup e recuperação do WordPress |
| Continuidade e transição | [Pendências](10-pendencias.md), [checklist](checklist-saida.md) | Responsáveis, prazos, cópia protegida do MikroTik, restauração testada e aceite do sucessor |

## Inconsistências que precisam de confirmação

| Tema | Evidência documental | Tratamento até confirmar |
| --- | --- | --- |
| Starlink e múltiplas WANs | O contexto relata PCC, políticas e failover históricos. Topologia e MikroTik registram retirada da StarLink do failover e reaproveitamento do ponto | Não assumir redundância disponível. Conferir links físicos, rotas efetivas, scripts e autorização do ERP antes de propor testes de troca |
| IP público do ERP | O README informa `177.12.159.224`; o artigo central ainda apresenta informação ausente | Preservar a referência como dado documental a revalidar com saída atual e confirmação da fornecedora. Não confundir com gateway WAN nem IP de destino do ERP |
| Id Control e catracas | O artigo Id Control diz que não está associado ao MultiClubes, mas suas seções seguintes e outros artigos descrevem integração | Não afirmar integração como validada. Separar identificação do controlador, software de gestão e fluxo da pulseira; confirmar se existem controles de acesso distintos |
| Câmeras | O contexto cita VLAN `200` e NVR `192.168.200.195`. A coleta descrita mostra bridge `Cameras` e porta sem link | Rede `192.168.200.0/24` não comprova VLAN 200. VLAN, NVR e caminho físico permanecem históricos, sujeitos a confirmação |
| DHCP | Há relato de MikroTik distribuindo somente na faixa 88, mas a coleta encontrou DHCP de câmeras e pool incluindo o gateway | Conferir servidor habilitado, interface, pool, concessões e reservas antes de alterar |
| Backup | A fornecedora cuida do ERP; não há recuperação testada do MikroTik registrada | Não estender a cobertura do backup do ERP a PCs, servidor de acesso, WordPress ou equipamentos de rede |
| Ferramentas | Tailscale, UltraVNC e RDP têm uso relatado; WireGuard aparece habilitado sem funcionamento comprovado na coleta | Classificar separadamente produção, teste e descontinuado. ZeroTier, The Dude, Zabbix, LibreNMS, Netwatch e descoberta de câmeras precisam de levantamento de uso real |

## Ordem proposta por criticidade

A ordem abaixo é uma proposta de trabalho, não um registro de mudanças implantadas. Cada módulo deve ser concluído e revisado antes de ampliar o seguinte.

| Ordem | Módulo e motivo | Entrega e critério de conclusão |
| --- | --- | --- |
| 1 | ERP, saída autorizada e acesso externo: afetam vendas e suporte | Confirmar URL, IP autorizado, contato do fornecedor e servidor de acesso; validar ERP em posto interno e em cliente externo pelo exit node; registrar evidências e escalonamento |
| 2 | Recuperação do MikroTik e conectividade: falha pode afetar todo o parque | Localizar roteador, energia e WAN; obter cópia protegida, dependências de scripts e caminho de gestão; documentar restauração e reversão compatíveis com equipamento/versão, com teste em janela acordada |
| 3 | Distribuição física e PDVs: falhas por setor podem parecer falha geral | Mapear uplinks, switches, Decos, redes fechadas e DHCP por setor; documentar diagnóstico de um PDV e de todos os PDVs, com validação de venda/TEF pelo fluxo autorizado |
| 4 | Portaria, pulseiras e catracas: impacto na entrada e saída | Resolver a divergência Id Control/MultiClubes, identificar controladores e dependências; registrar teste de passagem e procedimento de continuidade aprovado pela operação |
| 5 | Rotina de incidentes e desempenho | Criar rotinas de verificação e runbooks para internet, ERP e lentidão no almoço; registrar horário, abrangência, latência, tráfego, interface/WAN e testes comparativos, distinguindo hipótese de causa confirmada |
| 6 | CFTV e periféricos | Validar rede, VLAN e NVR; comparar acesso local/remoto e serviços cloud por link disponível; documentar ponto, impressoras, balanças e áudio/vídeo com seus responsáveis |
| 7 | Serviços web e encerramento da transição | Completar WordPress, domínio, DNS, atendimento, renovações, backup e contatos; concluir transferência de acessos, rotação e aceite das pendências |

A transferência dos acessos críticos e a definição de quem acionar começam no módulo 1 e acompanham todos os demais.

## Perguntas para iniciar o módulo 1

1. Qual é o nome do servidor de acesso, sistema operacional, localização, IP interno e nome exibido na TailNet? Quem o administra?
2. O exit node já está anunciado, aprovado e selecionado nos computadores externos? Quais usuários dependem dele hoje?
3. O IP `177.12.159.224` continua sendo o IP público autorizado pela fornecedora? Onde está a confirmação da white list?
4. Qual é a URL ou aplicação exata usada para abrir o ERP e qual contato/canal atende indisponibilidade e bloqueio por IP?
5. Quem autoriza e acompanha o teste externo e a validação operacional, sem gerar cobrança ou movimentação indevida?

## Padrão para os próximos módulos

Usar objetivo, contexto, dependências, pré-requisitos, procedimento, validação, rollback, problemas conhecidos, referências e última verificação somente quando aplicáveis. Em diagnóstico sem alteração, registrar que não há mudança a reverter. Em alterações, identificar a configuração anterior e a condição de retorno antes da execução.

Cada incidente deve registrar sintoma, horário, setores afetados, testes e resultados, hipótese, causa confirmada quando houver, ação, protocolo, responsável e validação final. A data do relato não substitui a data do incidente.

## Necessidade de Tailscale com exit node no servidor de acesso

**Requisito informado pelo responsável em 19/10/2026:** o acesso ao ERP fora das instalações do parque deve utilizar Tailscale com um **exit node no servidor de acesso, conectado à rede interna**. O artigo de ferramentas já menciona esse papel do servidor. Sua identificação e o funcionamento atual permanecem pendentes de validação.

O caminho exigido é: computador externo autorizado → Tailscale → exit node no servidor de acesso → saída de internet do parque com IP público autorizado → ERP. Apenas ingressar na TailNet não comprova o uso dessa saída; o cliente precisa utilizar o exit node aprovado. O recurso encaminha o tráfego de internet do cliente por esse equipamento, conforme a [documentação oficial do Tailscale](https://tailscale.com/docs/features/exit-nodes).

Critério de conclusão: identificar o servidor e o administrador, confirmar permissões e seleção do exit node, comparar o IP de saída observado no cliente externo com o IP autorizado confirmado pela fornecedora e validar acesso real ao ERP. Registrar data, equipamento, responsável e resultado. Não inserir credenciais na wiki.

A disponibilidade desse acesso depende do servidor de acesso, Tailscale e saída autorizada do parque. Ele não substitui um segundo link autorizado para contingência do ERP. Antes de redigir comandos de instalação ou recuperação, levantar o sistema operacional e a configuração vigente.

## 🧭 Notas do handover

- A revisão preserva os conteúdos existentes e explicita divergências; nenhuma configuração de rede foi alterada.
- Próximo passo: responder às perguntas do módulo 1 e registrar a validação do ERP e do exit node.
