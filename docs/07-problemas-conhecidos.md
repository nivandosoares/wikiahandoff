# Problemas conhecidos
> Última atualização:  | Responsável: Nivando Soares

O bloqueio do ERP na mudança de link foi relatado. As linhas de PDV e DHCP registram situações a prevenir; não há ocorrência confirmada informada para elas. Trate causa provável como hipótese até validar.

| ID | Sistema | Sintoma | Causa provável | Workaround | Status |
| --- | --- | --- | --- | --- | --- |
| 01 | MultiClubes / internet | Perda de acesso ao ERP após mudança do IP público de saída, mesmo com internet disponível | Após o ataque no RJ, a fornecedora passou a aceitar só IPs autorizados; a saída StarLink não correspondia ao IP Eldorado cadastrado | Manter saída pela Eldorado; se seu IP mudar, solicitar atualização da white list. O antigo ponto StarLink virou distribuição | Incidente relatado; StarLink fora do failover e plano B de link para ERP pendente.  |
| 02 | PDV / rede |  | Conexão à rede aberta do parque, fora da rede fechada prevista para as 30 maquininhas | Reconectar à rede fechada correta e validar MultiClubes/TEF pela Eldorado | Regra preventiva;  |
| 03 | DHCP / Deco e avulsos | Possível aumento de dispositivos e solicitações de IP na faixa 88 ao retirar roteador do modo router | Perda da distribuição de DHCP feita de propósito nos Decos/avulsos; carga pode se concentrar no MikroTik | Manter modo router e DHCP próprio; se alterado, recuperar a configuração validada e conferir os clientes | Risco preventivo, sem sobrecarga confirmada informada;  |
|  |  |  |  |  |  |

A ausência de cofre corporativo é uma pendência confirmada; acompanhe em [pendências](10-pendencias.md).

## 
