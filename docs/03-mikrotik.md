# MikroTik RB750Gr3
> Última atualização:  | Responsável: Nivando Soares

É o roteador central da rede. O acesso por SSH foi confirmado em `admin@192.168.88.1`; sistema RouterOS **7.24.4 stable**. Responsável: .

**É o coração da rede, mas boa parte do DHCP foi distribuída de propósito:** os 7 Decos e 4 roteadores avulsos ficam em modo router, cada um com DHCP próprio, para manter a faixa 88 administrativa enxuta. As 30 maquininhas do ERP ficam em redes fechadas.

**StarLink não é mais failover.** O antigo ponto distribui a rede do ISP atual. O MultiClubes só aceita nosso IP público autorizado da Eldorado; as referências antigas a backup abaixo são configurações encontradas, não uma contingência disponível. Veja [a mudança na topologia](01-topologia.md).

Informações consultadas em **08/10/2026, por volta de 09:55 (UTC−03)**. Nada foi alterado. As observações mostram o estado naquele momento; a troca de link e a recuperação de backup não foram testadas.

## Interfaces — onde os cabos entram

- `ether2`, nome “ELDORADO TELECOM”: entrada do link principal, com conexão ativa.
- `ether3`, nome “ACARAJE E ACAI”: faz parte da rede interna e estava ativa. O comentário antigo menciona StarLink; .
- `ether1`, identificada como “CAMERAS”: estava sem conexão de cabo detectada; conferir o caminho até o NVR/câmeras.
- `ether4`, “OUTRO LADO DO PARQUE”, e `ether5`, “SETOR ADMINISTRATIVO”: conexões ativas.
- Para consultar: Winbox **Interfaces** ou `/interface print detail`.

## Bridge — como as portas são agrupadas

- O grupo `bridge` reúne a rede interna pelas portas `ether3`, `ether4` e `ether5`.
- O grupo `Cameras` usa somente `ether1`, que estava sem conexão detectada.
- Na lista usada pelas regras de internet, só Eldorado aparece como saída. O antigo ponto StarLink participa da distribuição interna, não como segunda saída de internet.
- Para consultar: Winbox **Bridge → Ports** ou `/interface bridge port print detail`.

## IP/DHCP — endereços da rede

- Rede interna: `192.168.88.0/24`; roteador `192.168.88.1`; faixa automática configurada `192.168.88.2–192.168.88.254`. Na operação atual, o MikroTik atende DHCP só na 88; Decos/avulsos atendem suas próprias redes.
- Câmeras: `192.168.200.0/24`; roteador `192.168.200.1`. A coleta também encontrou DHCP configurado nessa faixa, incluindo o IP do roteador; .
- Eldorado entregou ao roteador o endereço `192.168.255.254`, com saída por `192.168.255.1`; esse endereço é automático e pode mudar.
- Há cadastro de `192.168.100.0/24` sem porta/endereço correspondente encontrado. .
- Para consultar: Winbox **IP → Addresses / DHCP Server / Pool** ou `/ip address print detail` e `/ip dhcp-server network print detail`.

## Firewall — regras de acesso

- Existem regras para proteger o roteador e controlar conexões vindas da internet, mas vários blocos estão repetidos.
- Há liberações para VPN e para o endereço `177.101.158.185`, identificado nos comentários como ERP, além da faixa `10.200.0.0/24`.
- O comentário “ERP ONLY” não garante, por si só, que o acesso fique restrito ao ERP. .
- Há regras de aceleração (FastTrack) e antigas regras de divisão entre links; conferir dependências antes de limpar. O ERP exige saída pelo IP público Eldorado autorizado; .
- Para consultar: Winbox **IP → Firewall → Filter Rules / Mangle** ou `/ip firewall filter print stats`.

## NAT — saída das redes para a internet

- A regra `WAN-MASQ-CLEAN` permite saída pela lista de internet, que hoje contém somente Eldorado.
- Existem outras regras de saída repetidas para redes internas e VPNs; várias regras antigas de StarLink/Eldorado estão desativadas.
- Duas regras iguais tratam o acesso da VPN `10.99.0.0/24` ao endereço do ERP pela Eldorado.

- Para consultar: Winbox **IP → Firewall → NAT** ou `/ip firewall nat print detail`.

## Rotas — saída atual e configurações antigas

- A saída pela Eldorado (`192.168.255.1`) estava ativa. É o link cujo IP público está autorizado no MultiClubes; `192.168.255.1` é o gateway local, não o IP público da white list.
- A antiga rota de backup (`192.168.1.1`) estava **inativa**. StarLink deixou de ser failover porque a mudança de IP público bloqueava o ERP.
- Existem antigas configurações de divisão entre Eldorado e StarLink, sem caminhos preenchidos na consulta. Não usá-las como indicação de redundância funcional.
- Duas rotinas estavam habilitadas a cada minuto: `wan-quality-failover` e `run-network-watchdog`. .
- Para consultar: Winbox **IP → Routes / System → Scheduler** ou `/ip route print detail`.

## Queues — controle de velocidade

- Existe uma regra chamada `Monitor Multivendas`, ligada ao endereço `177.101.158.185`, com limites configurados muito altos.
- Não foi confirmado se ela serve apenas para acompanhamento ou para limitar velocidade. .
- Para consultar: Winbox **Queues → Simple Queues** ou `/queue simple print stats`.

## VPN — conexões remotas

- Além do Tailscale informado, há duas conexões WireGuard no roteador: `wg-gcp` e `wg-remote`.
- `wg-gcp`: endereço local `10.10.10.2`, destino `8.231.170.59:51820`. `wg-remote`: endereço local `10.99.0.1`, comentário “TEST - ERP REMOTE”.
- Ambas estavam habilitadas, mas sem tráfego e sem registro de conexão estabelecida apresentado. **Habilitada não significa funcionando.** .
- Tailscale para acesso remoto, UltraVNC via IP para gestão interna e RDP de urgência: .
- Para consultar: Winbox **WireGuard** ou `/interface wireguard peers print detail proplist=interface,name,last-handshake,rx,tx` (sem mostrar chaves).

## Port forward — encaminhamento de acesso

- Foi encontrada a regra antiga “Acesso Web Starlink”, apontando para `192.168.1.1`, sem limitar porta, protocolo ou origem; a StarLink não é mais saída de failover.
- Nenhuma regra específica de encaminhamento para RDP foi encontrada. .
- Para consultar: Winbox **IP → Firewall → NAT** ou `/ip firewall nat print detail where chain=dstnat`.

## Logs — registros e alertas

- Os principais registros ficam na memória do roteador, com limite de 1000 linhas; não foi confirmada guarda externa contínua.
- Há envio configurado de eventos das portas para `sidvandoni@gmail.com`. .
- A consulta de eventos das portas não retornou registros naquele momento; isso não comprova ausência de falhas.
- Para consultar: Winbox **Log / System → Logging** ou `/log print`.

## Backup da config — recuperar o roteador

- Foi encontrado `flash/auto-before-reset.backup`. A data gravada é de 2106, portanto não dá para saber sua idade com segurança; a recuperação não foi testada.
- . Esse backup é separado do backup cloud do ERP.
- Para criar uma cópia: Winbox **Files → Backup**, com senha guardada fora deste documento e **Don't Encrypt** desmarcado. Nenhuma cópia foi criada durante a coleta.
- Para consultar a configuração em texto: `/export`, sem `show-sensitive`; revise comentários e scripts antes de compartilhar. Referência: [documentação MikroTik](https://manual.mikrotik.com/docs/getting-started/configuration-management/).

