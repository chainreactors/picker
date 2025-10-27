---
title: Nota Técnica 2023.001: tributação monofásica sobre combustíveis
url: https://blogs.sap.com/2023/03/30/nota-tecnica-2023.001-tributacao-monofasica-sobre-combustiveis/
source: SAP Blogs
date: 2023-03-31
fetch_date: 2025-10-04T11:14:24.374000
---

# Nota Técnica 2023.001: tributação monofásica sobre combustíveis

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Nota Técnica 2023.001: tributação monofásica sobre...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52594&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Nota Técnica 2023.001: tributação monofásica sobre combustíveis](/t5/enterprise-resource-planning-blog-posts-by-sap/nota-t%C3%A9cnica-2023-001-tributa%C3%A7%C3%A3o-monof%C3%A1sica-sobre-combust%C3%ADveis/ba-p/13564459)

![Luize_Boyen](https://avatars.profile.sap.com/3/5/id353948d94af654a2f8134e5dd3f8520e38aa358136ef23a0de8ad99a84bcbbe8_small.jpeg "Luize_Boyen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Luize\_Boyen](https://community.sap.com/t5/user/viewprofilepage/user-id/39112)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52594)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52594)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564459)

‎2023 Apr 28
3:41 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52594/tab/all-users "Click here to see who gave kudos to this post.")

11,513

* SAP Managed Tags
* [SAP S/4HANA Logistics for Brazil](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Logistics%2520for%2520Brazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)
* [Localization](https://community.sap.com/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)
* [SAP S/4HANA Logistics for Brazil

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BLogistics%2Bfor%2BBrazil/pd-p/ad2381ac-617c-4639-ad63-251765718582)
* [Localization

  Topic](/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

View products (3)

![](/legacyfs/online/storage/blog_attachments/2023/04/NT-2023.001.png)

Olá, pessoal

O governo brasileiro publicou a nota técnica 2023.001 de NF-e, que disponibiliza novos campos, novos grupos de ICMS, novas regras de validação e modificações nas regras de validação existentes para suportar a Lei Complementar 192 e o Convênio 199 de 2022 que define a nova tributação monofásica sobre combustíveis.

Neste blog post abordaremos as atualizações relativas a essas alterações e SAP Notes relevantes para este requisito legal disponível para SAP S/4HANA e SAP ERP.  Confira a versão em inglês [aqui](https://blogs.sap.com/2023/04/28/technical-note-2023.001-monophasic-taxation-on-fuels/).

## Novo campo para o índice de mistura do biodiesel

O campo **Biodiesel Mixing Index in Diesel B** (P\_BIO), disponível na tabela **Nota Fiscal: Fuel Details** (J\_1BNFFUEL), indica o índice de mistura do biodiesel (B100) no Diesel B em um valor decimal. Os valores permitidos nesse campo são de 0,0000 a 100,0000.

Você encontra o campo nos seguintes objetos do seu sistema:

* Transações da **Nota Fiscal Writer** (J1B\*N), abaixo da aba **Fuel** do documento

* **Additional Data for Nota Fiscal** (J\_1BNF\_ADD\_DATA) BAdI

* **Nota Fiscal System – Create Object from data** (BAPI\_J\_1B\_NF\_CREATEFROMDATA) BAPI

* **Nota Fiscal: List details of a Nota Fiscal** (BAPI\_J\_1B\_NF\_READDATA) BAPI

Na BAdI, você encontra o campo nos métodos **Fill additional fields in Nota Fiscal** (ADD\_DATA) e **Fill additional fields after J1B1N** (ADD\_DATA\_J1B1N), através do parâmetro **Fuel Details**(ET\_FUEL). Já em ambas as BAPIs o parâmetro é **Nota Fiscal: Fuel Details**(OBJ\_FUEL).

## Novos campos para novos grupos de ICMS

**ICMS** **15**

Há dois novos campos disponíveis para o grupo ICMS 15 que *trata do regime de tributação monofásica própria e com responsabilidade pela retenção do ICMS nas operações com combustíveis*. São eles os seguintes:

* O campo **ICMS ad rem percentage of reduction** (PREDADREM) informa o percentual de redução do valor da alíquota ad rem do ICMS, os valores permitidos são de 0,00 a 100,00.

* O campo **Reason for ad rem reduction** (MOTREDADREM) indica a razão para a redução do ICMS ad rem e permite os valores “1” para “transporte coletivo de passageiros” e “0” para “outros”. Esse campo só precisa ser preenchido quando o anterior também estiver preenchido.

**ICMS** **53**

Três novos campos foram disponibilizados para o grupo ICMS 53 que *trata do regime de tributação monofásica com recolhimento diferido do ICMS nas operações*.  São eles os seguintes:

* O campo **ICMS deferred value** (VICMSMONODIF) indica o valor do ICMS monofásico diferido. Esse valor é obtido pela multiplicação da alíquota ad rem pela quantidade do produto conforme unidade medida estabelecida.

* O campo **ICMS ad rem deferral percentage** (J\_1BNF\_ADREMICMSPDIF) indica a porcentagem de diferimento do ICMS ad rem.

* O campo **ICMS operation amount** (J\_1BNF\_VICMSMONOOP) indica o valor do ICMS obtido multiplicando a taxa de imposto ad rem pela quantidade do produto de acordo com a unidade de medida estabelecida pela legislação, como se não houvesse diferimento do imposto.

**Nota:** Os campos **Deferred taxed quantity** (QBCMONODIF) e **Tax rate ad rem of ICMS deferred established for the product** (JADREMICMSDIF) foram criados e se tornaram obsoletos devido a versão 1.2 da NT 2023.001.

**ICMS** **61**

Para o grupo 61 que *trata do regime de tributação monofásica sobre combustíveis com ICMS cobrado anteriormente* também foram disponibilizados três novos campos. São eles os seguintes:

* O campo **Tax rate ad rem of ICMS retained established for the product** (ADREMICMSRET) define a alíquota de imposto ad rem do ICMS retido anteriormente que está estabelecido para o produto em um valor decimal.

* O campo **ICMS retained value** (VICMSMONORET) refere-se ao valor do ICMS monofásico retido anteriormente.

* O campo **Retained taxed quantity** (QBCMONORET) define a quantidade tributada retida anteriormente em unidade de medida estabelecida pela legislação.

Todos os campos de ICMS mencionados estão disponíveis na tabela **Nota Fiscal Item Fields** (J\_1BNFLIN).

Você pode encontrar os campos relacionados aos grupos de ICMS nos seguintes objetos do seu sistema:

* Transações da **Nota Fiscal Writer** (J1B\*N), abaixo da aba **Taxes** em suas respectivas seções (ICMS 15, ICMS 53 e ICMS 61)

* **Additional Data for Nota Fiscal** (J\_1BNF\_ADD\_DATA) BAdI

* **Nota Fiscal System – Create Object from data** (BAPI\_J\_1B\_NF\_CREATEFROMDATA) BAPI

* **Nota Fiscal: List details of a Nota Fiscal** (BAPI\_J\_1B\_NF\_READDATA) BAPI

Na BAdI, você encontra o campo nos métodos **Fill additional fields in Nota Fiscal** (ADD\_DATA) e **Fill additional fields after J1B1N** (ADD\_DATA\_J1B1N) através do parâmetro **Additional Item Fields** (ET\_ITEM). Naz BAPIs **Nota Fiscal System – Create Object fr...