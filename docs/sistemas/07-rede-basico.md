# Rede — Básico para o Dia a Dia
> Última atualização:  | Responsável: Nivando Soares

## 1. IPs

O IP identifica o equipamento na rede. Para configurar ou localizar um equipamento, confira também a faixa, o gateway e a forma de atribuição do endereço no inventário.

| Rede ou equipamento | Referência | Observação |
| --- | --- | --- |
| Administrativa | Faixa 88.x, mantida enxuta de propósito | A [topologia](../01-topologia.md) registra `192.168.88.0/24`, confirmado na coleta anterior |
| Relógio de ponto | IP fixo terminado em `.200`;  | O final `.200` não indica a faixa; não confundir com a rede de câmeras |
| Câmeras | Faixa dedicada;  | A topologia registra `192.168.200.0/24` na coleta anterior |
| PDVs | Rede fechada por Deco;  | 30 maquininhas; não conectar às redes abertas do parque |
| Rádios Intelbras | Redes abertas ao parque;  | 2 rádios; manter a separação das redes de PDV |

Os 7 Decos e os 4 roteadores avulsos estão em modo **router**, cada um com DHCP próprio. DHCP é a distribuição automática de endereços aos equipamentos. Não mudar esse modo sem revisar o impacto na rede administrativa.

Tabela completa de equipamentos: [inventário](../09-inventario.md). Desenho da rede e referências de endereçamento: [topologia](../01-topologia.md).

## 2. Pasta pública

- Onde fica: .
- Quem acessa: .

### Como montar em um PC novo

### Cuidados

- Não há rotina de backup on-prem. 

## 3. Impressoras

- Modelos em uso: .
- Impressoras de rede: .
- Impressora compartilhada via pasta/servidor: .

### Como instalar em PC novo

1. Identificar a impressora do posto: .

4. Fazer uma impressão de teste e validar o uso com a operação: .

### Problemas comuns

- Procedimento geral: [configuração de impressora em rede](../06-procedimentos.md#configuração-de-impressora-em-rede).

## 4. Como conectar um PC novo na rede

1. Identificar o posto e a rede correta: .

5. Atualizar o [inventário](../09-inventario.md) com identificação, IP, MAC, local e responsável.

Não existe Active Directory; não há ingresso em domínio AD. Para programas, licenças e acesso remoto, seguir [troca ou configuração de PC](../06-procedimentos.md#troca-ou-configuração-de-pc).

Se o posto usa MultiClubes, conferir a saída pelo IP público Eldorado autorizado. Internet funcionando por outro IP pode deixar o ERP inacessível. Veja [ERP e white list](../04-erp-multiclubes.md).

## 🧭 Notas do handover
