---
title: Novo layout 17 da EFD ICMS IPI
url: https://blogs.sap.com/2023/02/06/drc-brazil-tdf-novo-layout-17-da-efd-icms-ipi/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:17.131328
---

# Novo layout 17 da EFD ICMS IPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* Novo layout 17 da EFD ICMS IPI

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7990&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Novo layout 17 da EFD ICMS IPI](/t5/financial-management-blog-posts-by-sap/novo-layout-17-da-efd-icms-ipi/ba-p/13563926)

![former_member453011](https://avatars.profile.sap.com/former_member_small.jpeg "former_member453011")

[former\_member453011](https://community.sap.com/t5/user/viewprofilepage/user-id/453011)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7990)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7990)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563926)

‎2023 Feb 06
7:36 PM

[10
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7990/tab/all-users "Click here to see who gave kudos to this post.")

2,968

* SAP Managed Tags
* [SAP Tax Declaration Framework for Brazil](https://community.sap.com/t5/c-khhcw49343/SAP%2520Tax%2520Declaration%2520Framework%2520for%2520Brazil/pd-p/67838200100800006027)
* [SAP Document and Reporting Compliance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520and%2520Reporting%2520Compliance/pd-p/73554900100700003181)

* [SAP Tax Declaration Framework for Brazil

  SAP Tax Declaration Framework for Brazil](/t5/c-khhcw49343/SAP%2BTax%2BDeclaration%2BFramework%2Bfor%2BBrazil/pd-p/67838200100800006027)
* [SAP Document and Reporting Compliance

  Software Product](/t5/c-khhcw49343/SAP%2BDocument%2Band%2BReporting%2BCompliance/pd-p/73554900100700003181)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/02/Blog-post-images-1.jpg) Nota: A informação abaixo é válida para as soluções **SAP Document and Reporting Compliance** e **SAP Tax Declaration Framework**.

Olá pessoal!

Liberamos as SAP Notes [3239072](https://launchpad.support.sap.com/#/notes/3239072) e [3284842](https://launchpad.support.sap.com/#/notes/3284842), que contém as mudanças relacionadas à versão 3.1.1 do Guia Prático da EFD ICMS IPI.

Veja abaixo as alterações entregues para atender o novo layout:

* Nova versão do layout 17, com validade a partir de 01/01/2023.

* Descontinuação dos códigos 04 e 05 da tabela **4.1.2** **Tabela de situação de documentos,** à partir de 31/12/2022. Com isso não será mais possível reportar documentos que tenham o campo *COD\_SIT* preenchido com os valores **04 – Denegado** e **05 – Numeração inutilizada**.

* Inclusão do registro **0221 - Correlação entre códigos de itens comercializados**. Para ser reportado, o registro deve atender os seguintes requisitos:

  1. Deverá existir um registro de nota fiscal com o *COD\_ITEM* para o período e filial.

  2. Deverá ser tipo de mercadoria para revenda (“00”).

  3. Será reportado o que estiver na lista técnica.

* Inclusão dos registros **C855, C857, C895** e **C897**.

* Aumento do tamanho (de 15 para 60 caracteres) do campo **Identificação do processo ou ato concessório** (NUM\_PROC) nos registros C111, E112, E116, E230, E250, E312, E316, 1922, 1926.

  1. Atenção no registro 1922: foi necessária a substituição da tabela **/TMF/D\_SA\_INFAJU** (que foi obsoletada) pela **/TMF/D\_SA\_INF\_AJ**.

  2. Nos demais registros, houve apenas aumento de campo. O processo de reportar permanece o mesmo

* Registro K010: O campo **Indicador do tipo de leiaute** (IND\_TP\_LEIAUTE) tem um novo indicador de opção.

  1. Foi adicionado na tela de execução da EFD ICMS IPI o novo campo de filtro **Layout Type**. O campo é obrigatório para o layout 17 e é opcional para a versão 16 e anteriores.

  2. Foi adicionado o campo **Layout Type** ao WebService /TMF/II\_TMFEFDREPORT\_RUN.

  3. Em um cenário de **IND\_TP\_LEIAUTE = “0” Simplificado** que tenha ocorrido consumo apenas para o K235, não será gerado o K230.

  4. Em um cenário de **IND\_TP\_LEIAUTE = “2” Restrito aos saldos de estoque**, são reportados os registros K001, K010, K100, K200 e K280. O entendimento é que o K280 deve fazer parte dos registros apresentados nesse cenário.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-34.png)

Novo campo disponível para reportar os diferentes layouts do bloco K.

* Nesta versão do manual foi divulgado mais informações sobre os novos registros do bloco D (D700, D730, D731, D735, D737, D750, D760 e D761), os quais devem entregues em 2023. Você pode acompanhar as datas planejadas de entrega no app **Announcement of Legal Change** (disponível no **SAP ONE Support Launchpad**).

Gostaríamos muito de receber o seu feedback. Deixe seu comentário abaixo caso tenha alguma dúvida ou sugestão para um próximo post.

Além dos comentários, você pode entrar em contato conosco através da plataforma [Customer Influence](https://influence.sap.com/sap/ino/#/campaign/2079). Lá, você pode propor ideias para melhorar nosso produto, votar em outras ideias já lançadas e acompanhar ideias em implementação.

Também não se esqueça de seguir a tag [SAP Tax Declaration Framework for Brazil](https://blogs.sap.com/tags/67838200100800006027/) e [SAP Document and Reporting Compliance](https://blogs.sap.com/tags/8a7d73f3-61df-4cdf-9688-8a28ae4dd8b6/) aqui na SAP Community para ficar ligado nas últimas notícias.

Até a próxima,

Time de desenvolvimento TDF e DRC Brazil.

Labels

* [Product Updates](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap/label-name/product%20updates)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ffinancial-management-blog-posts-by-sap%2Fnovo-layout-17-da-efd-icms-ipi%2Fba-p%2F13563926%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Understanding the Context of Brazil’s Tax Reform](/t5/financial-management-blog-posts-by-members/understanding-the-context-of-brazil-s-tax-reform/ba-p/14159547)
  in [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)  2025 Jul 23
* [SAP TDF: SP17 – What’s New](/t5/financial-management-blog-posts-by-sap/sap-tdf-sp17-what-s-new/ba-p/13523830)
  in [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)  2022 Sep 22
* [MM: Exclusão do ICMS da base do PIS e do COFINS](/t5/financial-management-q-a/mm-exclus%C3%A3o-do-icms-da-base-do-pis-e-do-cofins/qaq-p/12560713)
  in [Financial Management Q&A](/t5/financial-management-q-a/qa-p/financial-management-questions)  2022 Jun 09
* [TDF: Novo layout 16 da EFD ICMS IPI](/t5/financial-management-blog-posts-by-sap/tdf-novo-layout-16-da-efd-icms-ipi/ba-p/13528114)
  in [Financial Management Blog Pos...