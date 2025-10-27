---
title: Nota Técnica 2022.003: atualização de campos e regras de validação da NF-e modelo 55
url: https://blogs.sap.com/2023/03/03/nota-tecnica-2022.003-atualizacao-de-campos-e-regras-de-validacao-da-nf-e-modelo-55/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:38.723282
---

# Nota Técnica 2022.003: atualização de campos e regras de validação da NF-e modelo 55

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Nota Técnica 2022.003: atualização de campos e reg...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52045&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Nota Técnica 2022.003: atualização de campos e regras de validação da NF-e modelo 55](/t5/enterprise-resource-planning-blog-posts-by-sap/nota-t%C3%A9cnica-2022-003-atualiza%C3%A7%C3%A3o-de-campos-e-regras-de-valida%C3%A7%C3%A3o-da-nf-e/ba-p/13561995)

![Luize_Boyen](https://avatars.profile.sap.com/3/5/id353948d94af654a2f8134e5dd3f8520e38aa358136ef23a0de8ad99a84bcbbe8_small.jpeg "Luize_Boyen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Luize\_Boyen](https://community.sap.com/t5/user/viewprofilepage/user-id/39112)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52045)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52045)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561995)

‎2023 Mar 03
9:44 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52045/tab/all-users "Click here to see who gave kudos to this post.")

17,483

* SAP Managed Tags
* [SAP S/4HANA Logistics for Brazil](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Logistics%2520for%2520Brazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization](https://community.sap.com/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

* [SAP S/4HANA Logistics for Brazil

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BLogistics%2Bfor%2BBrazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization

  Topic](/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/03/NF-e-Technical-Note-2022.003-1.png)

Olá, pessoal

O governo brasileiro publicou a nota técnica 2022.003 de NF-e, que disponibiliza novas regras de validação, além de alteração no grupo de documentos referenciados.

A nota técnica inclui um novo campo e regras de validação aplicáveis a este campo. Neste blog post abordaremos as atualizações relativas a essas alterações e SAP Notes relevantes para este requisito legal disponível para SAP S/4HANA e SAP ERP. Clique [aqui](https://blogs.sap.com/2023/03/03/technical-note-2022.003-updating-fields-and-validation-rules-for-nf-e-model-55/) para a versão em inglês.

## Alteração nos campos e regras de validação

O novo campo **Chave da NF-e com o Código Numérico Zerado** (refNFeSig) permite que o contribuinte referencie uma nota fiscal eletrônica informando a chave de acesso com o código numérico zerado (*random number*)*.* Isso restringe o acesso a informações da nota fiscal, permitindo manter o sigilo dos dados da NF-e referenciada. Há novas regras de validação que garantem a consistência da chave de acesso referenciada com o código numérico zerado e impedem que esta referência ocorra em uma NF-e com finalidade diferente de normal (finNFe=1).

A referência pela chave de acesso completa é ainda obrigatória em casos de nota fiscal de devolução e complementar ou quando exigido por regulamentos legais.

Uma das alterações está relacionada ao número de ocorrências do grupo de documentos fiscais referenciados que anteriormente tinham um máximo de 500 ocorrências e que agora podem ter 999 ocorrências. Essa alteração aborda situações em que mais de 500 documentos são referenciados na mesma nota fiscal.

## Nova tabela de documento referenciado

A tabela **Nota Fiscal Document Reference** (J\_1BNF\_DOCREF) está disponível no seu sistema, entregue de acordo com as especificações da nota técnica publicada pela Sefaz.

Você encontra a tabela nos seguintes objetos do seu sistema:

* Transações da **Nota Fiscal Writer** (J1B\*N), tabela **External** **NFe** **References** na aba **Additional Information** do documento

* **Additional Data for Nota Fiscal** (J\_1BNF\_ADD\_DATA) BAdI

* **Nota Fiscal System – Create Object from data** (BAPI\_J\_1B\_NF\_CREATEFROMDATA) BAPI

* **Nota Fiscal: List details of a Nota Fiscal** (BAPI\_J\_1B\_NF\_READDATA) BAPI

O campo **Document Reference Type** (DOCREF\_TYPE) define a confidencialidade do documento referenciado. Você pode selecionar entre os valores *Standard* ou *Confidencial* e o campo **44-Digit Access Key** (ACCESS\_KEY) armazena a chave de acesso do documento fiscal referenciado.

A nova tabela permite a referência para documentos fiscais externos (notas fiscais não existem no seu sistema). No caso de referência interna (quando os documentos estão armazenados no seu sistema), nada muda, pois continua sendo como antes.

Ao selecionar o valor *Standard*, informe a chave de acesso completa da nota fiscal. Caso a escolha seja o valor *Confidencial*, você pode informar a chave de acesso da nota fiscal com código numérico zerado (random number) para garantir a confidencialidade. Quando você insere uma referência como *Confidencial*, ela vai para o campo **refNFeSig** do XML, mas quando você insere uma referência como *Standard*, ela vai para o campo **refNFe**.

## SAP Notes relevantes para esse requisito legal

* SAP Note [3295909](https://launchpad.support.sap.com/#/notes/3295909) - NT 2022.003: Confidential Nota Fiscal References

* SAP Note [3288601](https://launchpad.support.sap.com/#/notes/3288601) - Prerequisite Objects for NT 2022.003: Confidential Nota Fiscal References

SAP Notes para NF-e estão previstas para o dia 08 de março.

**Atualização – 10 de março de 2023**

ERP NF-e:

* SAP Note [3308184](https://launchpad.support.sap.com/#/notes/3308184) - Outbound NF-e: Technical Note 2022.003

* SAP Note [3309134](https://launchpad.support.sap.com/#/notes/3309134) - Outbound NF-e: Prerequisite objects for SAP Note 3308184

Inbound GRC:

* SAP Note [3309145](https://launchpad.support.sap.com/#/notes/3309145) -  Inbound NF-e: Technical Note 2022.003

Inbound eDocuments:

* SAP Note [3309706](https://launchpad.support.sap.com/#/notes/3309706) - eDocument Brazil Inbound NF-e: Technical Note 2022.003

* SAP Note [3309710](https://launchpad.support.sap.com/#/notes/3309710) - eDocument Brazil Inbound NF-e: Prerequisite objects for SAP Note 3309706

GRC NF-e:

* SAP Note [3290276](https://launchpad.support.sap.com/#/notes/3290276) - NF-e NT2022.003

**Atualização – 22 de março de 2023**

* SAP Note [3310241](https://launchpad.support.sap.com/#/notes/3310241) - Prerequisite Objects for NT 2022.003: Confidential Nota Fiscal References BAPI

* SAP Note [3310242](https://launchpad.support.sap.com/#/notes/3310242) - NT 2022.003: Confidential Nota Fiscal References BAPI

Gostou desse post? Dê um *Like* e compartilhe o conteúdo com seus colegas. Fiquem à vontade para deixar um feedback, comentário ou pergunta no espaço abaixo.  E não esqueça de seguir a [*SAP S/4HANA Logistics for Brazil*](https://blogs.sap.com/tags/ad2381ac-617c-4639-ad63-251765718582/) na SAP Community para ficar ligado nas últimas notícias.

Um abra...