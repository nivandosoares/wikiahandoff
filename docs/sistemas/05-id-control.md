# Id Control
> Última atualização:  | Responsável: Nivando Soares

## 1. O que é

Sistema de controle de acesso usado na catraca e na portaria, **Não está associado ao ambiente MultiClubes.**

## 2. Para que usamos aqui

- Controle de entrada e saída relacionado à pulseira NFC e ao cadastro no MultiClubes.

## 3. Como acessar

- Onde fica: .
- Com quem está: .

- Referência: [credenciais e acessos](../08-credenciais-e-acessos.md).

## 4. Dependências de rede

- O acesso ao ERP central depende do IP público Eldorado autorizado: veja [MultiClubes e white list](../04-erp-multiclubes.md).

- Referências: [topologia](../01-topologia.md) e [inventário](../09-inventario.md).

## 5. Operações do dia a dia

## 6. Integrações com outros sistemas

- [MultiClubes](02-multiclubes.md): cadastro do cliente e emissão/ativação da pulseira, relacionados ao controle de entrada e saída.
- Pulseira NFC: o código de barras vincula cliente, cartão de consumo e operações do dia. Veja [fluxo da operação](../01b-fluxo-operacao.md).

## 7. Fornecedor / suporte

| Quem chamar | Como chamar | SLA |
| --- | --- | --- |
|  |  |  |

## 8. Problemas conhecidos

- Se a pulseira não lê, o fluxo operacional trava: .

- Referências: [problemas conhecidos](../07-problemas-conhecidos.md) e [procedimentos](../06-procedimentos.md).

## 9. Procedimentos específicos

### Validar entrada e saída

### Tratar falha de leitura ou acesso recusado

### Tratar indisponibilidade

1. Registrar horário, posto, equipamento, sintoma e mensagem: .
2. Conferir conectividade local e, se o ERP estiver afetado, a saída pelo IP público autorizado.
3. Acionar o suporte: .
4. Após a correção, validar entrada e saída com a operação: .

## 🧭 Notas do handover
