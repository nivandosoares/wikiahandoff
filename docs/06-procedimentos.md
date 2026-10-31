# Procedimentos operacionais
> Última atualização:  | Responsável: Nivando Soares

## Queda de internet ou bloqueio do ERP

1. Registre horário e alcance da falha: .
2. Confira alimentação, cabos e estado das interfaces no [MikroTik](03-mikrotik.md); compare com outro posto para distinguir falha local de falha geral.
3. Confira a saída pela Eldorado. Se outros serviços funcionam e o ERP não, compare o IP público com o autorizado: .
4. Não acione StarLink como failover: o antigo ponto é distribuição do ISP atual. Se o IP público mudou, peça à fornecedora do ERP a autorização; .
5. Acione Eldorado para falha de link ou MultiClubes para bloqueio do ERP; registre protocolo e previsão: .
6. Alinhe  e, após a recuperação, valide PDV, TEF, pulseira, catraca e portaria pela saída autorizada.

## Falha no MultiClubes, PDV, TEF, catraca ou portaria

1. Registre posto, horário, mensagem e transação afetada, sem dados de pagamento: .
2. Confira energia, conexão, rede fechada dos PDVs, saída Eldorado autorizada e se outros postos apresentam o mesmo sintoma.
3. Para TEF com resultado incerto, confirme o estado da transação pelo fluxo  antes de repetir a cobrança.
4. Abra chamado com a fornecedora conforme [MultiClubes](04-erp-multiclubes.md), informando impacto e verificações realizadas.
5. Acione  e valide os fluxos afetados após a correção.

## Acesso remoto, UltraVNC interno e RDP de urgência

1. Use o equipamento e a conta autorizados: .
2. Conecte pelo Tailscale e confira o destino: .
3. Para gestão interna, use UltraVNC via IP; para urgência, RDP pelo caminho autorizado: .
4. Registre a intervenção e encerre a sessão: .

## Falha na catraca interna/servidor web ou EzpointWeb

1. Identifique o sistema e o sintoma: .
2. Confira conectividade e acesso em outro posto; registre a mensagem apresentada.
3. Consulte .
4. Execute eventual reinício conforme ; confirme o funcionamento com .

## Câmera sem imagem ou falha no NVR

1. Identifique se a falha afeta uma câmera ou todo o conjunto: .
2. Confira alimentação, conexão e acesso pela faixa dedicada: .
3. Registre o sintoma e acione .
4. Valide imagem e gravação conforme .

## Solicitar restauração do ERP

1. Registre o ocorrido, o período afetado e os dados necessários: .
2. Obtenha a autorização de .
3. Solicite à fornecedora o ponto disponível, o prazo e o impacto sobre dados posteriores, pelos canais de [MultiClubes](04-erp-multiclubes.md).
4. Combine a execução com a operação e valide o resultado: .

## Reinício de equipamentos

1. Identifique o equipamento e os serviços afetados no [inventário](09-inventario.md); combine a parada com .
2. Registre o sintoma e a configuração necessária para voltar; confira .
3. Encerre atividades em andamento e reinicie pelo procedimento do equipamento: .
4. Confira rede e serviços após o retorno, valide com a operação e registre horário e resultado.

## Troca ou configuração de PC

1. Identifique o posto, cabo ou Wi-Fi, programas e periféricos: .
2. Preserve os dados locais necessários conforme .
3. Configure sistema, licenças, programas e acesso à rede: . Não há ingresso em domínio AD.
4. Configure UltraVNC e demais acessos necessários sem registrar segredos; .
5. Teste os serviços do posto e periféricos; atualize o inventário e combine .

## Configuração de impressora em rede

1. Identifique impressora, posto e rede de destino: .
2. Confira alimentação e conexão; configure o endereço conforme .
3. Instale o driver e configure a impressão no PC ou sistema: .
4. Faça impressão de teste, valide o uso real com a operação e registre endereço, modelo e configuração no inventário.

## Configuração de PDV

1. Identifique a maquininha entre as 30 do ERP e o posto: .
2. Conecte somente à rede fechada de PDV: ; nunca use a rede aberta do parque.
3. Confirme a saída pela Eldorado com IP público autorizado no MultiClubes.
4. Configure ou vincule o posto com a fornecedora: .
5. Execute , valide com a operação e atualize o inventário.

## Configuração de Raspberry Pi

1. Confirme sua função e dependências antes de intervir: .
2. Registre a configuração atual e preserve o necessário: .
3. Configure sistema, rede e serviços conforme .
4. Teste os serviços e o retorno após reinício conforme ; atualize o inventário e a referência de recuperação.

## Configuração de rede — Decos, rádios e avulsos

1. Identifique equipamento, rede atendida e ligação de entrada: .
2. Registre a configuração antes de alterar: .
3. Mantenha os 7 Decos e 4 avulsos em modo **router**, cada um com DHCP próprio; .
4. Nos 2 rádios Intelbras, preserve a separação entre redes abertas do parque e redes fechadas de PDV: . O antigo ponto StarLink distribui a rede do ISP atual.
5. Teste conexão, entrega de endereços e acesso ao ERP pela Eldorado; registre a mudança na topologia e no inventário. Não mudar o modo dos roteadores sem revisar o impacto na faixa 88.

## Backup e restauração do que é nosso

1. Identifique o equipamento, serviço ou dados locais a recuperar: . Não existe rotina de backup on-prem; ERP e seu backup são da fornecedora.
2. Confira . Para o roteador, consulte [backup da configuração do MikroTik](03-mikrotik.md).
3. Para gerar uma cópia, siga ; não inclua segredos nos documentos.
4. Para restaurar, combine a janela e siga .
5. Valide rede e serviços com a operação e registre a cópia usada e o resultado; se for ERP, use o procedimento de solicitação à fornecedora acima.

## Abrir chamado com suporte externo

1. Identifique o responsável: MultiClubes para ERP/backup cloud, Eldorado para link e .
2. Registre horário, impacto, sintoma, mensagens e testes realizados; para bloqueio de ERP, informe o IP público de saída e a referência da white list.
3. Abra o chamado pelo canal , sem enviar senhas ou dados de pagamento.
4. Registre protocolo, prazo/SLA e próximo retorno: .
5. Acompanhe com a operação, valide a correção e registre o encerramento.

## 🧭 Notas do handover
