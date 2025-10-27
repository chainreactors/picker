---
title: Esteja preparado para o RISE with SAP Private Cloud Edition
url: https://blogs.sap.com/2023/01/11/esteja-preparado-para-o-rise-with-sap-private-cloud-edition/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:16.890613
---

# Esteja preparado para o RISE with SAP Private Cloud Edition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Esteja preparado para o RISE with SAP Private Clou...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52772&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Esteja preparado para o RISE with SAP Private Cloud Edition](/t5/enterprise-resource-planning-blog-posts-by-sap/esteja-preparado-para-o-rise-with-sap-private-cloud-edition/ba-p/13565652)

![mcalgaroto](https://avatars.profile.sap.com/e/7/ide741b8e608296068baf67e29360dabcce79d9587f8475f33b51d0d311a659bd6_small.jpeg "mcalgaroto")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[mcalgaroto](https://community.sap.com/t5/user/viewprofilepage/user-id/145749)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52772)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52772)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565652)

‎2023 Jan 11
9:02 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52772/tab/all-users "Click here to see who gave kudos to this post.")

2,373

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)

View products (3)

Olá,

Neste blog trarei algumas dicas e tópicos de como estar preparado para o ***RISE with SAP*** com ‘*S/4HANA Cloud, private edition*’.

## **Estratégia Multinuvem**

O ***RISE with SAP*** faz parte da estratégia multinuvem, onde várias soluções SAP de suas nuvens estão embaixo do mesmo contrato e são utilizados pelo cliente de maneira integrada, afim de realizar os respectivos processos de negócio. O produto chave da oferta é o S/4HANA Cloud.

Quando o cliente opta pelo ***RISE with SAP*** com o *S/4HANA Cloud, private edition*, é criado um tenant dedicado para o cliente, também conhecido como nuvem gerenciada, que inclui todos os produtos ‘*private edition*’. Esta entrega é realizada pelo time SAP Enterprise Cloud Services (ECS). O ECS fica responsável por todas as atividades relacionadas à definição e construção da infraestrutura, instalação e configuração inicial, bem como a realização de diversas atividades relacionadas com o mantenimento e administração dos respectivos sistemas que estão sob sua responsabilidade.

![](/legacyfs/online/storage/blog_attachments/2023/01/Untitled.png)

Para a infraestrutura dessa nuvem gerenciada o cliente pode escolher um provedor de infraestrutura em uma região homologada. A escolha deve ocorrer para o *Data Center* primário e também para o *Data Center* secundário caso tenha optado por contratar *DR* de longa distância. O time de Engenharia do ECS elaborou – e mantém em processo de melhoria contínua – toda a arquitetura de referência para cada um dos provedores de infraestrutura, a fim de obter o máximo de disponibilidade e desempenho em seu ambiente SAP.

Os provedores de infraestrutura atualmente disponíveis são a própria SAP (com seus DCs) ou um dos três Hyperscalers (*IaaS*) líderes de mercado:

* Amazon Web Services (AWS)

* Microsoft Azure

* Google Cloud Platform (GCP).

A escolha da região dentre aquelas homologadas pelo ECS deve ser realizada com o suporte do CAA (*Cloud Architect & Advisor*) durante a pré-venda.

A matriz de Funções e Responsabilidades do ECS mapeia e classifica todas as atividades que podem ser demandadas durante o ciclo de vida dos sistemas que ficam nesta nuvem gerenciada:

[RISE with SAP S/4HANA Cloud, private edition and SAP ERP, PCE Roles and Responsibilities](https://www.sap.com/about/agreements/policies/hec-services.html?sort=latest_desc&search=RISE%20with%20SAP%20S%2F4HANA%20Cloud%2C%20private%20edition%20and%20SAP%20ERP%2C%20PCE%20Roles%20and%20Responsibilities&tag=language:portuguese-brazil)

## **Jornada do cliente ao *Private Edition***

A SAP demanda que o cliente forneça informações para realizar a construção da nuvem gerenciada do cliente, devido à natureza de sua arquitetura.

Se o cliente mapear em sua companhia os respectivos times responsáveis por prover cada um dos itens e distribuir as demandas antes da assinatura do contrato, irá agilizar a entrega destas informações dentro do prazo requisitado pela SAP. Assim permitirá que todo o ambiente seja entregue pela SAP na data de início do contrato, sem atrasos.

As informações estão detalhadas abaixo:

**➢ Credenciais do S-User:** necessário para que o time de operações do ECS possa instalar, suportar e gerenciar os sistemas pelo cliente. Quando o cliente adquire o ***RISE with SAP*** ele indica um membro de sua equipe para ser o Super Administrador da respectiva instalação. A partir deste usuário o cliente deve realizar a criação de um novo usuário dedicado para o time de operação, adicionando as permissões listadas no formulário enviado ao cliente.

**➢ Línguas a serem instaladas nos sistemas SAP (além do padrão - EN, DE):** (além do padrão - EN, DE): Indica o(s) idioma(s) adicional(is) a serem instalados, por exemplo: Português, Espanhol, Francês, etc. Relevante apenas para novas instalações (*Greenfield*).

**➢ Janela de manutenção planejada:** janela de indisponibilidade pré-aprovada de 4 horas para ser utilizada em caso de emergência. Deve ser definida dentro da janela de manutenção contratual, que é 24x5 (dias úteis) para sistemas não produtivos e 24x7 para sistemas produtivos.

**➢ 1 x subrede IPv4 (/22):** Um intervalo de IPs disponível (sem utilização) e exclusivamente reservado para os hosts e componentes que serão construídos na nuvem gerenciada.

Se o Hyperscaler escolhido for GCP, este intervalo deve fazer parte do endereçamento privado documentado na RFC 1918.

**➢ 1 x subrede IPv4 (/22) para DR**: um segundo intervalo de IPs deve ser provido caso haja recuperação de desastre (DR) de longa distância (em uma região distinta) no escopo.

**➢ Subdomínio de DNS interno do Cliente:** o cliente irá delegar um subdomínio embaixo do seu domínio de DNS interno e a SAP o utilizará em todos os componentes que serão construídos na nuvem gerenciada. Por exemplo: se o domínio de DNS interno do Cliente é ‘customer.corp’, o subdomínio será ‘sap.customer.corp’. Assim, as URLs utilizadas pelo usuário final estarão embaixo deste domínio. Importante: o cliente deverá prover certificados TLS/SSL para o subdomínio fornecido.

**➢ Endereço de IP dos servidores de DNS:** este...