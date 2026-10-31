# Onboarding do próximo analista
> Última atualização:  | Responsável: Nivando Soares

O ambiente atende um clube/parque aquático com operação de PDV, catraca, portaria e TEF.

## Primeiro dia

1. Alinhe prioridades e horários críticos: .
2. Teste os acessos transferidos com seu próprio usuário: . Consulte [credenciais e acessos](08-credenciais-e-acessos.md).
3. Localize o MikroTik, switches, APs, Raspberry Pi, PDVs, PCs e NVR: .
4. Valide Tailscale, UltraVNC via IP para gestão interna e RDP de urgência: .
5. Confira vendas, ativação de pulseira, catraca, PDV, TEF e portaria no MultiClubes: .

## Checklist de acessos do dia 1

- [ ] MikroTik: testar a gestão em `192.168.88.1`; .
- [ ] Tailscale: entrar na TailNet e validar os destinos; .
- [ ] UltraVNC: testar acesso interno via IP; .
- [ ] Painel MultiClubes: testar o perfil pela saída Eldorado; .
- [ ] WordPress Admin: .
- [ ] StayCloud: .
- [ ] E-mail: .
- [ ] NVR: .
- [ ] EzpointWeb: .
- [ ] Contato do ERP: .
- [ ] Contato do ISP Eldorado Telecom: .

## Ferramentas do dia a dia

| Ferramenta | Para que usar | Referência |
| --- | --- | --- |
| Winbox | Consultar e administrar o MikroTik | `192.168.88.1`; [download aqui](https://mikrotik.com/download/winbox) |
| Tailscale | Acesso remoto pela TailNet | [ Mais sobre o Tailscale](https://tailscale.com/) |
| UltraVNC | Gerenciamento interno dos computadores via IP | [Ultra VNC server & Viewer](https://uvnc.com/downloads/ultravnc.html) |
| RDP | Acesso de urgência | RDP protocol está habilitado nos computadores para torná-los acessíveis mesmo em ambiente Linux via xfreerdp:  *xfreerdp /v:192.168.1.50 /u:username /p:password*      **lembre de usar o endereço do adaptador de rede Tailscale** |
| Painel MultiClubes | Operação e gestão do ERP | Deve se usar uma conta com permissões de administrador para acesso completo ao painel de configurações avançadas |

## Quem acionar

| Assunto | Contato e canal |
| --- | --- |
| Operação e decisões |  |
| MultiClubes e backup cloud |  |
| Eldorado Telecom |  |
| StarLink |  |
| Sistemas internos e serviços externos |  |

## Limites do ambiente

- Active Directory: Não se aplica — não existe AD no ambiente.
- Servidor on-prem de arquivos: Não se aplica — não existe esse servidor.
- Backup on-prem: Não se aplica — o backup é 100% cloud, administrado pela fornecedora do ERP.
