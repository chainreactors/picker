---
title: Falha de handshake TLS com o ambiente de Homologação de NF-e da SEFAZ-SP
url: https://blogs.sap.com/2023/03/09/falha-de-handshake-tls-com-o-ambiente-de-homologacao-de-nf-e-da-sefaz-sp/
source: SAP Blogs
date: 2023-03-10
fetch_date: 2025-10-04T09:08:17.580509
---

# Falha de handshake TLS com o ambiente de Homologação de NF-e da SEFAZ-SP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Falha de handshake TLS com o ambiente de Homologaç...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162999&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Falha de handshake TLS com o ambiente de Homologação de NF-e da SEFAZ-SP](/t5/technology-blog-posts-by-members/falha-de-handshake-tls-com-o-ambiente-de-homologa%C3%A7%C3%A3o-de-nf-e-da-sefaz-sp/ba-p/13566969)

![andrelamonteiro](https://avatars.profile.sap.com/0/9/id090799f88149fa73d873b1836b8c56717db98a4ea515d4e863cbc6bda5b70953_small.jpeg "andrelamonteiro")

[andrelamonteiro](https://community.sap.com/t5/user/viewprofilepage/user-id/127711)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162999)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162999)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566969)

‎2023 Mar 09
9:35 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162999/tab/all-users "Click here to see who gave kudos to this post.")

3,578

* SAP Managed Tags
* [SAP NetWeaver Process Integration, adapters](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Process%2520Integration%252C%2520adapters/pd-p/01200615320800001376)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP NetWeaver Process Integration, adapters

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BProcess%2BIntegration%25252C%2Badapters/pd-p/01200615320800001376)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (2)

## Introdução

Entre 08/02/2023 e 09/02/2023, a SEFAZ-SP fez algumas alterações de segurança nos webservices de NF-e do ambiente de Homologação. Infelizmente estas mudanças não foram publicadas pela SEFAZ-SP, e desde então nossos ambientes GRC NF-e não têm conseguido se conectar aos serviços para que possamos executar testes, impactando diversos projetos relacionados à NF-e aqui na empresa. Felizmente, o problema está restrito ao ambiente de Homologação, não tendo sido feita nenhuma modificação pela SEFAZ-SP no ambiente de Produção até este momento.

O objetivo deste blog é mostrar a análise do problema, identificação da causa raiz e solução implementada.

## O Problema

Dependendo do nosso ambiente interno de GRC NF-e (DEV, Pre-QA ou QA), entre 08/02/2023 e 09/02/2023, a consulta de status de serviço na SEFAZ-SP de Homologação começou a retornar erro:

![](/legacyfs/online/storage/blog_attachments/2023/03/StatusServico.png)

Status de Serviço

Inicialmente achei que era uma intermitência temporária, e como o SVC está configurado em todos os ambientes, as Notas Fiscais continuaram sendo processadas em ambiente de Homologação, com exceção do serviço de Inutilização que não existe no SVC.

Na semana seguinte, em conversa com outras empresas, recebi a confirmação que o problema que estávamos enfrentando também estava ocorrendo em outras empresas, porém confirmei também que outras empresas não estava sofrendo nenhuma indisponibilidade de serviço. Coincidentemente - e isto acabou desviando o foco da análise - as empresas que estavam enfrentando problemas possuem seus servidores GRC NF-e fora do país. Por causa disto, minha primeira suspeita é que a SEFAZ-SP passou a bloquear também em ambiente de Homologação as conexões provenientes de fora do país.

Para confirmar isto, solicitei ao time de Basis para fazer um traceroute a partir de um dos servidores afetados até o endereço homologacao.nfe.fazenda.sp.gov.br:

![](/legacyfs/online/storage/blog_attachments/2023/03/traceroute.png)

Traceroute

Para complicar as coisas, aparentemente o traceroute falhava ao tentar sair da rede interna. Então o que inicialmente parecia ser um problema externo de repente se tornou um problema de infraestrutura interna.

Acionei o time de redes e de firewall para analisar o motivo pelo qual o tráfego não saía da rede interna. Depois de vários dias de troubleshooting e análises, o veredito veio através da utilização da ferramenta TCP Gateway, disponível na Nota SAP [856597](https://launchpad.support.sap.com/#/notes/856597). Basicamente o teste que fiz em casa foi instalar o TCP Gateway em duas máquinas: a primeira o meu laptop de trabalho, conectado à rede da empresa via VPN e acessível pelo GRC NF-e, e a segunda uma máquina pessoal sem nenhuma restrição de firewall e acessando a SEFAZ-SP sem nenhum bloqueio. Apontei o Canal de Comunicação da consulta de status de serviço no GRC NF-e para o TCP Gateway da primeira máquina, e o TCP Gateway da primeira máquina para o TCP Gateway da segunda máquina que, por fim, estava apontando para o WebService da SEFAZ. Ao disparar a comunicação pelo GRC NF-e, pude ver que o tráfego estava normal, passando por ambos os TCP Gateways, e mesmo assim não havia uma comunicação efetiva com a SEFAZ-SP.

Uma vez descartado um possível bloqueio de firewall e também um possível bloqueio de IPs de fora do Brasil pela SEFAZ-SP em Homologação, e considerando que havia empresas em que a counicação estava ocorrendo sem problemas, ficou evidente que era agum problema específico do GRC NF-e, porém causado por algo que havia mudado na SEFAZ-SP, uma vez que não houve nenhuma modificação implementada nos ambientes GRC NF-e recentemente.

## A Causa Raiz

Ativei o trace do Canal de Comunicação através da ferramenta XPI Inspector (vide Nota SAP [1514898](https://launchpad.support.sap.com/#/notes/1514898)). Ao rodar a interface de Consulta de Status de Serviço com o XPI Inspector ativado, o seguinte trecho do log chamou a minha atenção:

```
Begin IAIK Debug:

ssl_debug(7821): Starting handshake (iSaSiLk 5.104)...

ssl_debug(7821): Sending v3 client_hello message to homologacao.nfe.fazenda.sp.gov.br:443, requesting version 3.3...

ssl_debug(7821): Sending extensions: renegotiation_info (65281), signature_algorithms (13)

ssl_debug(7821): IOException while handshaking: Connection reset

ssl_debug(7821): Sending alert: Alert Fatal: handshake failure

ssl_debug(7821): Exception sending message: java.net.SocketException: errno: 32 (Broken pipe), error: Write failed (local port 29780 to address 10.38.175.201 (***********.jnj.com), remote host unknown)

ssl_debug(7821): Shutting down SSL layer...

ssl_debug(7821): Closing transport...

End IAIK Debug.
```

A análise de certificados, tanto interno quando da SEFAZ-SP, não retornou nenhum erro, porém ainda assim ocorria erro de handshake TLS. Um trecho importante do log é a frase "remote host unknown", mostrando que  durante o handshake não foi possível identificar o servidor de destino. Baseado nestas informações, algumas pesquisas na internet me apontaram para uma possível causa do problema, que posteriormente se confirmaram como sendo efetivamente a causa raiz: Cipher Suites.

Em resumo, todas vez que um serviço se conecta a um servidor utilizando um protocolo seguro, tal como o HTTPS utilizado pelos webse...