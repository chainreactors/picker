---
title: HCM Brasil: Nova configuração disponível para ambientes de qualidade no eSocial
url: https://blogs.sap.com/2022/10/14/hcm-brasil-nova-configuracao-disponivel-para-ambientes-de-qualidade-no-esocial/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:15.206202
---

# HCM Brasil: Nova configuração disponível para ambientes de qualidade no eSocial

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* HCM Brasil: Nova configuração disponível para ambi...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/49486&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HCM Brasil: Nova configuração disponível para ambientes de qualidade no eSocial](/t5/enterprise-resource-planning-blog-posts-by-sap/hcm-brasil-nova-configura%C3%A7%C3%A3o-dispon%C3%ADvel-para-ambientes-de-qualidade-no/ba-p/13543472)

![former_member691429](https://avatars.profile.sap.com/former_member_small.jpeg "former_member691429")

[former\_member691429](https://community.sap.com/t5/user/viewprofilepage/user-id/691429)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=49486)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/49486)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543472)

‎2022 Oct 14
9:39 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/49486/tab/all-users "Click here to see who gave kudos to this post.")

1,478

* SAP Managed Tags
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)
* [HCM Payroll](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll/pd-p/372556673030062693282256213775139)
* [HCM Payroll Brazil](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll%2520Brazil/pd-p/517106488272734260515465412269325)

* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [HCM Payroll

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll/pd-p/372556673030062693282256213775139)
* [HCM Payroll Brazil

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll%2BBrazil/pd-p/517106488272734260515465412269325)

View products (3)

![](/legacyfs/online/storage/blog_attachments/2022/10/banner-4.png)

eSocial - Nova configuração disponível para ambientes de qualidade

Olá pessoal!

Como todos já devem estar cientes, o layout S-1.1 do eSocial já está publicado e seguimos entregando as alterações no nosso produto.

Conforme o layout S-1.1 do eSocial, algumas validações do eSocial começarão a valer somente a partir de março de 2023, como é o caso dos Rendimentos Recebidos Acumuladamente (RRA).

Para permitir que sistemas de testes validem tais informações no ambiente de produção restrita do governo, criamos o parâmetro **PROD\_R\_VALIDITY** (Data para validar preenchimento de campos em produção restrita).

Nesse blog post serão encontradas as seguintes informações:

* Caso de uso do **PROD\_R\_VALIDITY**

* Configurando o **PROD\_R\_VALIDITY**

* Referências

**Caso de uso do parâmetro PROD\_R\_VALIDITY**

No layout S-1.1 do eSocial, as seguintes informações são validadas a partir de 2023-03.

* Evento S-1200, campo *indRRA*

* Evento S-1210, campo *paisResidExt*

* Evento S-2299, campo *indRRA*

* Evento S-2399, campo *indRRA*

Entretanto, sistemas de pré-produção do governo não seguem essa mesma data.

Por conta disso, a partir do eSocial S-1.1 permitiremos que você configure em sistemas de qualidade uma data diferente de 2023-03 através do parâmetro PROD\_R\_VALIDITY.

Dessa forma, você poderá gerar e enviar as informações listadas acima para o ambiente de produção restrita do eSocial a fim de validar seus eventos.

**Configurando o parâmetro PROD\_R\_VALIDITY**

O novo parâmetro está disponível na visão **Atualizar parâmetros configuração do sistema para o eSocial** (V\_T7BREFD\_CONFIG).

Para configurá-lo, acesse a transação SM30 e edite o objeto V\_T7BREFD\_CONFIG.

![](/legacyfs/online/storage/blog_attachments/2022/10/SM30-1.png)

Manutenção da visão V\_T7BREFD\_CONFIG

Feito isso, crie uma entrada nova.

Na coluna "Configuração do eSocial", digite PROD\_R\_VALIDITY. Se preferir, você também pode apertar F4 e então selecionar o parâmetro.

Na coluna "Empresa", digite para qual empresa a configuração irá valer ou então digite "\*" caso o parâmetro seja aplicável a todas empresas.

No campo valor digite uma data, no formato aaaammdd.

![](/legacyfs/online/storage/blog_attachments/2022/10/parameter_saved.png)

Parâmetro PROD\_R\_VALIDITY

Salve suas alterações.

Pronto! O parâmetro está salvo e será utilizado pelo eSocial.

**Referências**

SAP Note [3246764 - eSocial S-1.1 - Configuration parameter to enable restricted production](https://launchpad.support.sap.com/#/notes/3246764)

Fique ligado para acompanhar as atualizações do sistema para atender o layout S-1.1 do eSocial.

Gostou desse post? Dê um Like e compartilhe o conteúdo com seus colegas.

Fique à vontade para deixar um feedback, comentário ou pergunta no espaço abaixo. E não esqueçam de seguir a tag HCM Payroll Brazil na SAP Community para ficarem ligados nas últimas notícias.

Um abraço,

Eduardo Pedersetti José

Time de HCM Brasil

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [esocial](/t5/tag/esocial/tg-p/board-id/erp-blog-sap)
* [hcm brasil](/t5/tag/hcm%20brasil/tg-p/board-id/erp-blog-sap)
* [HCMBR](/t5/tag/HCMBR/tg-p/board-id/erp-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhcm-brasil-nova-configura%25C3%25A7%25C3%25A3o-dispon%25C3%25ADvel-para-ambientes-de-qualidade-no%2Fba-p%2F13543472%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [5 pontos essenciais para o fechamento da fase REALIZE em projetos SAP S/4HANA Cloud Private Edition](/t5/enterprise-resource-planning-blog-posts-by-sap/5-pontos-essenciais-para-o-fechamento-da-fase-realize-em-projetos-sap-s/ba-p/14232344)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [5 pontos essenciais para o fechamento da fase EXPLORE em projetos SAP S/4HANA Cloud Private Edition](/t5/enterprise-resource-planning-blog-posts-by-sap/5-pontos-essenciais-para-o-fechamento-da-fase-explore-em-projetos-sap-s/ba-p/14226164)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  a week ago
* [5 pontos essenciais para um bom fechamento da fase PREPARE em projetos SAP S/4HANA Cloud Private](/t5/enterprise-resource-planning-blog-posts-by-sap/5-pontos-essenciais-para-um-bom-fechamento-da-fase-prepare-em-projetos-sap/ba-p/14219239)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [EFD REINF Erro MS0038](/t5/enterprise-resource-planning-q-a/efd-reinf-erro-ms0038/qaq-p/...