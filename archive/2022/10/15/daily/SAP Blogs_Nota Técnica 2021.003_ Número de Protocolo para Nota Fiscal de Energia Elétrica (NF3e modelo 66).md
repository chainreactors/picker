---
title: Nota Técnica 2021.003: Número de Protocolo para Nota Fiscal de Energia Elétrica (NF3e modelo 66)
url: https://blogs.sap.com/2022/10/14/nota-tecnica-2021.003-numero-de-protocolo-para-nota-fiscal-de-energia-eletrica-nf3e-modelo-66/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:18.831795
---

# Nota Técnica 2021.003: Número de Protocolo para Nota Fiscal de Energia Elétrica (NF3e modelo 66)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Nota Técnica 2021.003: Número de Protocolo para No...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/47913&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Nota Técnica 2021.003: Número de Protocolo para Nota Fiscal de Energia Elétrica (NF3e modelo 66)](/t5/enterprise-resource-planning-blog-posts-by-sap/nota-t%C3%A9cnica-2021-003-n%C3%BAmero-de-protocolo-para-nota-fiscal-de-energia/ba-p/13535697)

![Luize_Boyen](https://avatars.profile.sap.com/3/5/id353948d94af654a2f8134e5dd3f8520e38aa358136ef23a0de8ad99a84bcbbe8_small.jpeg "Luize_Boyen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Luize\_Boyen](https://community.sap.com/t5/user/viewprofilepage/user-id/39112)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=47913)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/47913)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13535697)

‎2022 Oct 14
9:24 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/47913/tab/all-users "Click here to see who gave kudos to this post.")

9,834

* SAP Managed Tags
* [SAP S/4HANA Logistics for Brazil](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Logistics%2520for%2520Brazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization](https://community.sap.com/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

* [SAP S/4HANA Logistics for Brazil

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BLogistics%2Bfor%2BBrazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization

  Topic](/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2022/10/image.png)

Olá, pessoal!

O governo brasileiro publicou a nota técnica 2021.003-SEFAZ que divulga novas regras relacionadas ao número de protocolo da nota fiscal de energia elétrica NF3e modelo 66, que agora deve ter 16 dígitos.

As novas resoluções da NF3e incluem um novo número de controle nos documentos de número de série. Nesse blog post, abordaremos atualizações referentes ao campo relacionado ao número de protocolo e SAP Notes relevantes para esse requisito legal disponíveis para SAP S/4HANA e SAP ERP.

**Criação de um novo campo referente ao número de protocolo**

Para endereçar a nota técnica 2021.003-SEFAZ, o campo **Protocol Number** (J\_1BNFEAUTHCODE16) foi criado possibilitando o preenchimento de 16 dígitos no número de protocolo. O novo campo de 16 caracteres está disponível para ser preenchido durante a criação da NF3e modelo 66 via processo de compra ou criada manualmente. Os outros modelos de nota fiscal não são afetados por essa solução e continuam com o número de protocolo de 15 caracteres.

**Migração de dados**

Se você tem nota fiscal de energia elétrica modelo 66 nas tabelas **Nota Fiscal Header** (J\_1BNFDOC) e **Electronic Nota Fiscal: Actual Status** (J\_1BNFE\_ACTIVE), os valores do número do protocolo salvos no campo **Protocol Number** (AUTHCODE) migram para o campo **Protocol Number** (AUTHCODE16) após a execução da migração de dados. É importante seguir os passos de implementação das SAP Notes.

As alterações mencionadas neste blog post estão disponíveis nos seguintes objetos:

* Transações da **Nota Fiscal Writer** (J1B\*N)

* **Nota Fiscal System – Create Object from data** (BAPI\_J\_1B\_NF\_CREATEFROMDATA) BAPI

* **Nota Fiscal: List details of a Nota Fiscal** (BAPI\_J\_1B\_NF\_READDATA) BAPI

**SAP Notes relevantes para esse requisito legal**

Você pode instalar as seguintes SAP Notes para atualizar a sua solução, na seguinte ordem:

1. SAP Note [3240161](https://launchpad.support.sap.com/#/notes/3240161) – Prerequisite Objects for NT 2021.003: 16-Digit Protocol Number for Energy NF3e - Part 1

2. SAP Note [3240162](https://launchpad.support.sap.com/#/notes/3240162) – Prerequisite Objects for NT 2021.003: 16-Digit Protocol Number for Energy NF3e - Part 2

3. SAP Note [3232974](https://launchpad.support.sap.com/#/notes/3232974) – NT 2021.003: Enable 16-Digit Protocol Number for Energy NF3e

4. SAP Note [3234561](https://launchpad.support.sap.com/#/notes/3234561) – NT 2021.003: Complementary Changes for 16-Digit Protocol Number for Energy NF3e

5. Para migração de dados considere as seguintes SAP Notes:

   * **OP** **SAP S/4HANA:** SAP Note [3240163](https://launchpad.support.sap.com/#/notes/3240163) – NT 2021.003: Data Conversion - S/4HANA (XCLA) for 16-Digit Protocol Number for Energy NF3e

   * **SAP ERP:** SAP Note [3240164](https://launchpad.support.sap.com/#/notes/3240164) – NT 2021.003: Data Conversion - SAP\_APPL (XPRA) for 16-Digit Protocol Number for Energy NF3e

**Atualização – 04 de novembro de 2022**

A migração do campo **Protocol Number** (AUTHCODE) para o campo **Protocol Number** (AUTHCODE16) não estava sendo possível em alguns cenários para as releases **SAP ERP 618** e **SAP ERP 617**. Para resolver essa questão, é necessária a implementação da SAP Note [3264944](https://launchpad.support.sap.com/#/notes/3264944) – NT 2021.003: Data Conversion - SAP\_APPL (XPRA) for 16-digit Protocol Number with Missing Type.

**Atualização – 16 de novembro de 2022**

Para resolução de uma inconsistência na validação do **Protocol Number** ao criar ou modificar uma nota fiscal eletrônica, a SAP Note [3263831](https://launchpad.support.sap.com/#/notes/3263831) – Incorrect Validation of the Protocol Number When Creating or Modifying an Electronic Nota Fiscal foi disponibilizada para permitir a parametrização do preenchimento do campo como obrigatório.

**Atualização – 17 de novembro de 2022**

A SAP Note [3251073](https://launchpad.support.sap.com/#/notes/3251073) – [Fiori] NT 2021.003: Enable 16-Digit Protocol Number for Energy NF3e fornece ajustes no app **Verify Nota Fiscal** para exibir o campo **Protocol Number** com 16 dígitos.

Gostou desse post? Dê um *Like* e compartilhe o conteúdo com seus colegas. Fiquem à vontade para deixar um feedback, comentário ou pergunta no espaço abaixo.  E não esqueça de seguir a [*SAP S/4HANA Logistics for Brazil*](https://blogs.sap.com/tags/ad2381ac-617c-4639-ad63-251765718582/) na SAP Community para ficar ligado nas últimas notícias.

Um abraço,

Luize Boyen

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [Legal Change](/t5/tag/Legal%20Change/tg-p/board-id/erp-blog-sap)
* [legal change BR](/t5/tag/legal%20change%20BR/tg-p/board-id/erp-blog-sap)
* [materials management](/t5/tag/materials%20management/tg-p/board-id/erp-blog-sap)
* [sap s4hana](/t5/tag/sap%20s4hana/tg-p/board-id/erp-blog-sap)
* [SAPGoGlobal SAPLocalization](/t5/tag/SAPGoGlobal%20SAPLocalization/tg-p/board-id/erp-blog-sap)

36 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugi...