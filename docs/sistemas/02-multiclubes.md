# MultiClubes
> Última atualização:  | Responsável: Nivando Soares

## 1. O que é

ERP principal da operação, ponta a ponta: vendas online, gestão de sócios, pulseira, catraca, portaria, PDV e TEF. Administração, atualização e backup do ERP são responsabilidade da fornecedora, em cloud.

## 2. Para que usamos aqui

- Cadastro de sócios/clientes e emissão/ativação de pulseiras.
- Vendas online e vínculo das operações de entrada, saída e consumo com o cliente.

## 3. Como acessar

- Onde fica: .
- Com quem está: .
- Referência: [credenciais e acessos](../08-credenciais-e-acessos.md).

## 4. Dependências de rede

- O ERP usa white list de IP público. A saída autorizada é a da Eldorado Telecom: .
- Internet funcionando por outro IP não garante acesso ao ERP. Antes de mudar link ou IP público, alinhar a autorização com a fornecedora e validar o acesso.
- StarLink não é mais failover; o antigo ponto distribui a rede do ISP atual. Ainda falta um plano B de link autorizado para o ERP.
- Detalhes e responsabilidades: [ERP central e white list](../04-erp-multiclubes.md).

## 5. Operações do dia a dia

## 6. Integrações com outros sistemas

- [MultiVendas PDV](03-multivendas-pdv.md) e TEF: consumo no PDV e pagamentos por crédito/débito.
- [MultiVendas Retaguarda](01-multivendas-retaguarda.md): retaguarda financeira; .
- Id Control: controle de entrada/saída pela catraca e portaria, relacionado à pulseira NFC.
- O código de barras da pulseira vincula cliente, cartão de consumo e operações. Veja [fluxo da operação](../01b-fluxo-operacao.md).

## 7. Fornecedor / suporte

| Quem chamar | Como chamar | SLA |
| --- | --- | --- |
|  |  |  |

Backup e restauração do ERP ficam com a fornecedora: .

## 8. Problemas conhecidos

- Saída por IP público não autorizado bloqueia o acesso ao ERP, mesmo com internet disponível. Esse problema ocorreu quando a saída mudava para StarLink.
- Se a pulseira não lê, o fluxo operacional trava: .
- Referência: [problemas conhecidos](../07-problemas-conhecidos.md).

## 9. Procedimentos específicos

1. Em falha, registrar horário, sintoma, mensagem e áreas afetadas: .
2. Conferir conectividade local e saída pelo IP Eldorado autorizado. Se o IP mudou, confirmar a white list com a fornecedora.
3. Abrir chamado e registrar protocolo: .
4. Validar os fluxos afetados com a operação após a correção: .

Procedimentos gerais: [procedimentos](../06-procedimentos.md). Rotinas de cadastro e pulseira: .

## 🧭 Notas do handover
