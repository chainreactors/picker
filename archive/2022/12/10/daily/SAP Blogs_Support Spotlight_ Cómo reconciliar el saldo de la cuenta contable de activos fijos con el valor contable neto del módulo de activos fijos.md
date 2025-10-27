---
title: Support Spotlight: Cómo reconciliar el saldo de la cuenta contable de activos fijos con el valor contable neto del módulo de activos fijos
url: https://blogs.sap.com/2022/12/09/support-spotlight-como-reconciliar-el-saldo-de-la-cuenta-contable-de-activos-fijos-con-el-valor-contable-neto-del-modulo-de-activos-fijos/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:06:02.238715
---

# Support Spotlight: Cómo reconciliar el saldo de la cuenta contable de activos fijos con el valor contable neto del módulo de activos fijos

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Support Spotlight: Cómo reconciliar el saldo de la...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53484&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Support Spotlight: Cómo reconciliar el saldo de la cuenta contable de activos fijos con el valor contable neto del módulo de activos fijos](/t5/enterprise-resource-planning-blog-posts-by-sap/support-spotlight-c%C3%B3mo-reconciliar-el-saldo-de-la-cuenta-contable-de/ba-p/13571414)

![mauricio_lopez3](https://avatars.profile.sap.com/a/6/ida686d88b1e7b0ad3714febf07bd3f770cdbf7dadef3b3d06cfa88d42694f99aa_small.jpeg "mauricio_lopez3")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[mauricio\_lopez3](https://community.sap.com/t5/user/viewprofilepage/user-id/461408)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53484)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53484)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571414)

‎2022 Dec 09
7:00 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53484/tab/all-users "Click here to see who gave kudos to this post.")

1,390

* SAP Managed Tags
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004775)

* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004775)

View products (2)

Este blog es una traducción del blog publicado por ivy.zhang en Abril 21 de 2017:

[How to Reconcile Fixed Assets Account Balance with Fixed Assets Net Book Value | SAP Blogs](https://blogs.sap.com/2017/04/21/how-to-reconcile-fixed-assets-account-balance-with-fixed-assets-net-book-value/)

Si usted usa la funcionalidad de activos fijos de SAP Business One y no sabe cómo verificar si el valor contable neto en el módulo de activos fijos coincide con los saldos de cuenta pertinentes, este artículo lo ayudará.

En SAP Business One, las cuentas contables utilizadas en las contabilizaciones de los activos fijos están definidas por la determinación de la cuenta asignada en la clase de activos. Los activos pertenecientes a la misma clase de activos utilizarán el mismo grupo de cuentas.

En SAP Business One, lo definido en la 'Contabilización de Depreciación' (Indirecta o Directa) para el Área de Valoración con el tipo 'Contabilizar en LM’ determina si la cuenta de depreciación acumulada será utilizada en las contabilizaciones de la ejecución de valoración. En consecuencia, determinará la manera de conciliar el saldo de la cuenta con el valor contable neto.

#### **Indirecta**

Si usted selecciona la contabilización indirecta de la depreciación, la cuenta de depreciación acumulada será usada para registrar la valoración en la ejecución de valoración. El valor contable neto debe calcularse con el saldo de la cuenta de balance de activos fijos y la cuenta de depreciación acumulada.

|
  |
 Cuadro AF |
  |
 Saldo de la cuenta |

|
 Cuenta de balance de activos fijos |
 Costo de adquisición y producción en fecha de inicio |
 <=> |
 saldo inicial del saldo acumulado (ML) |

|
 Costo de adquisición y producción en fecha final |
 <=> |
 Saldo final del saldo acumulado (ML) |

|
 Cuenta de depreciación acumulada |
 Depreciación acumulada en fecha de inicio |
 <=> |
 Saldo inicial del saldo acumulado (ML) |

|
 Depreciación en fecha final |
 <=> |
 Saldo final del saldo acumulado (ML) |

#### **Directa**

Si usted elige la contabilización directa de la depreciación, la cuenta de depreciación acumulada no será usada y usted puede reconciliar el saldo de la cuenta de balance de activos con el valor contable neto directamente.

|
  |
 Cuadro AF |
  |
 Saldo de la cuenta |

|
 Cuenta de balance de activos fijos |
 Valor contable neto en fecha de inicio |
 <=> |
 saldo inicial del saldo acumulado (ML) |

|
 Valor contable neto en fecha final |
 <=> |
 Saldo final del saldo acumulado (ML) |

### ***Nota***

* Recuerde seleccionar la cuenta de balance, área de valoración y clase de activo correctos cuando ejecute el reporte Cuadro AF.

* Asegúrese de seleccionar el mismo periodo cuando ejecute el Cuadro AF y cuando filtre las contabilizaciones en la ventana del saldo de la cuenta.

#### **Serie Support Spotlight**

Esperamos que esta lectura haya sido informativa y beneficiosa. Para obtener más blogs y consejos del equipo de soporte de SAP Business One, visite nuestro espacio en las comunidades: <https://blogs.sap.com/tag/b1-support-spotlight/>

Si tiene preguntas sobre SAP Business One, [envíela aquí](https://answers.sap.com/tags/01200615320800000816).

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [B1 support spotlight](/t5/tag/B1%20support%20spotlight/tg-p/board-id/erp-blog-sap)
* [B1\_Espanol](/t5/tag/B1_Espanol/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsupport-spotlight-c%25C3%25B3mo-reconciliar-el-saldo-de-la-cuenta-contable-de%2Fba-p%2F13571414%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Reconciliar Pago recibido con Factura de deudor](/t5/enterprise-resource-planning-q-a/reconciliar-pago-recibido-con-factura-de-deudor/qaq-p/11834058)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2016 Aug 10
* [Reconciliar Solicitud de anticipos de proveedor](/t5/enterprise-resource-planning-q-a/reconciliar-solicitud-de-anticipos-de-proveedor/qaq-p/7949950)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2011 Jun 10
* [Error en Reconciliacion Interna de Socio de Negocios](/t5/enterprise-resource-planning-q-a/error-en-reconciliacion-interna-de-socio-de-negocios/qaq-p/7179746)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2010 Sep 01
* [Reconciliar Via SDK](/t5/enterprise-resource-planning-q-a/reconciliar-via-sdk/qaq-p/4316181)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2008 Aug 28

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jp...