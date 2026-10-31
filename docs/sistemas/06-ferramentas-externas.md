# Ferramentas Externas de Acesso e Suporte
> Responsável: Nivando Soares

## 1. Tailscale (TailNet)

### O que é

Ferramenta de conectividade entre os equipamentos autorizados na TailNet, usada para acesso remoto pós criação de white list para IP de saída.

### Para que usamos

Acesso remoto padrão da operação em computadores externos a rede local (contabilidade e gerenciamento de escitório externo na FAI). e contingência em casos de emergência sem suporte local.

### Como acessar

- Faça login em [tailscale.com](https://tailscale.com/) e prossiga ao console -- você deve receber uma solicitação para entrar na rede como novo usuário

### Cuidados / limitações

- Tailscale mantém os dispositivos operando como se estivessem em LAN física, portanto todo o tráfego pode ser redirecionado ao exit node, que é o computador do servidor de acesso 

- Transferência de administração e remoção dos acessos de quem sai: .

## 2. RDP

### O que é

Recurso de acesso à área de trabalho de um computador remoto.

### Para que usamos

Acesso de urgência via computador remoto.  **Atenção: é necessário estar devidamente logado na rede TailNet**

### Como acessar

- Referência: [credenciais e acessos](../08-credenciais-e-acessos.md).

### Quem tem acesso

### Cuidados / limitações

- Registrar a intervenção e encerrar a sessão conforme [procedimentos](../06-procedimentos.md).

## 3. AnyDesk

### O que é

Ferramenta de acesso remoto e suporte a computadores.

### Para que usamos

### Como acessar

### Quem tem acesso

### Cuidados / limitações

## 4. UltraVNC

### O que é

Ferramenta de acesso remoto à tela de computadores.

### Para que usamos

Gerenciamento interno via IP.

### Como acessar

- Destino: .

- Referência: [credenciais e acessos](../08-credenciais-e-acessos.md).

### Quem tem acesso

### Cuidados / limitações

- Destinos e parâmetros precisam corresponder ao [inventário](../09-inventario.md).

## 🧭 Notas do handover
