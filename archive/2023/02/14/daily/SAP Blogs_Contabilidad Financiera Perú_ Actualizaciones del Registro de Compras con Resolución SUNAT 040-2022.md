---
title: Contabilidad Financiera Perú: Actualizaciones del Registro de Compras con Resolución SUNAT 040-2022
url: https://blogs.sap.com/2023/02/13/contabilidad-financiera-peru-actualizaciones-del-registro-de-compras-con-resolucion-sunat-040-2022/
source: SAP Blogs
date: 2023-02-14
fetch_date: 2025-10-04T06:31:53.537767
---

# Contabilidad Financiera Perú: Actualizaciones del Registro de Compras con Resolución SUNAT 040-2022

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Contabilidad Financiera Perú: Actualizaciones del ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53294&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Contabilidad Financiera Perú: Actualizaciones del Registro de Compras con Resolución SUNAT 040-2022](/t5/enterprise-resource-planning-blog-posts-by-sap/contabilidad-financiera-per%C3%BA-actualizaciones-del-registro-de-compras-con/ba-p/13569626)

![BarnabasKirk](https://avatars.profile.sap.com/d/1/idd1578ae940af54f2732324180a256ca04e1910354c0ae6fadb006d2e018cd2d5_small.jpeg "BarnabasKirk")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[BarnabasKirk](https://community.sap.com/t5/user/viewprofilepage/user-id/12122)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53294)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53294)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569626)

‎2023 Feb 13
6:37 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53294/tab/all-users "Click here to see who gave kudos to this post.")

1,748

* SAP Managed Tags
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/02/Peru_FI_040-2022_ES.png)

Contabilidad Financiera Perú

Me complace presentar las actualizaciones recientes del reporte **Registro de Compras** de Perú para **SAP ERP Central Component** (SAP ECC). Estos cambios se implementaron para cumplir con los requisitos legales especificados por la Superintendencia Nacional de Aduanas y de Administración Tributaria (SUNAT) en la Resolución 040-2022.

* Para obtener detalles legales sobre la Resolución 040-2022 de la SUNAT, consulte el [sitio web de la SUNAT](https://cpe.sunat.gob.pe/node/141#item-2).

* Para obtener detalles de la implementación técnica de su solución SAP, consulte la [SAP Note 3239158](https://launchpad.support.sap.com/#/notes/3239158).

En este blog enumeraré las actualizaciones claves del reporte Registro de Compras (RFCLLIB04\_PE) y explicaré cómo puede aprovechar al máximo las nuevas funcionalidades.

El reporte desarrollado corresponde al Anexo N° 11, “Estructura y reglas para elaborar el archivo plano que permita la comparación con la propuesta del RCE o reemplazar esta última”.

**1. Generar archivos TXT**

Ahora tiene la opción de generar un archivo en el formato TXT obligatorio por SUNAT, que puede descargar y enviar electrónicamente a la Autoridad Fiscal Peruana.  Si prefiere no generar un archivo TXT, puede previsualizar la salida del informe con el ABAP List Viewer (ALV).

Generar su archivo TXT no podría ser más fácil, simplemente seleccione la casilla de verificación "Create File" al completar la información del informe.

**2. Especifique la ubicación del archivo TXT**

Para generar un archivo en formato TXT, primero debe especificar la vía de acceso del archivo y el nombre del archivo.

Antes de ejecutar el reporte Registro de Compras, ejecute la transacción FILE y configure la siguiente información:

**2.1.** Vía de acceso del archivo: FI\_PE\_PURCHASE\_LEDGER

**2.2.** Nombre del archivo: FI\_PE\_ARCHIVE\_PL\_FILE

**3. Nuevas actividades de configuración**

Hay dos nuevas actividades de configuración que debe completar para ejecutar el reporte Registro de Compras:

**3.1.** Group Tax Balances (V\_T007L)

**3.2.** Group Tax Base Balances (V\_T007K)

Para obtener documentación sobre las rutas SPRO para estas actividades de configuración, consulte la versión más reciente de la documentación de SAP Help Portal: [Documentación de SAP Help Portal para Perú FI](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/fccf2ded571b4269ba14877b195df45a/fc346f2f7e6740e48cf19844fb73d3a5.html?locale=en-US,301).

Para obtener documentación sobre cómo generar estas actividades de configuración y para que los números de grupo se introduzcan en cada actividad, seleccione el ícono “Documento” en su entorno de configuración:

![](/legacyfs/online/storage/blog_attachments/2023/02/Peru_Configuration_Documentation-1.png)

El ícono Documento aparece junto al icono Ejecutar.

**4. Estructura de Balance**

Para generar el Registro de Compras Perú, ahora puede configurar la Estructura de Balance para compras nacionales. Para completar esta actividad, debe realizar dos tareas:

**4.1.** Cree una Estructura de Balance para "Clasificación de mercaderías y servicios para el registro de compras nacionales (080400)".

**4.2.** Asigne sus cuentas de mayor a la estructura de balance/ganancias y pérdidas que ha creado en el paso 4.1.

Para obtener una descripción completa de este proceso, acceda a la página de SAP Help Portal Libro de compras Perú: [Additional Configuration for Financial Statement Version.](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/fccf2ded571b4269ba14877b195df45a/cf9ebc4b79644de181de2b8e6c00bc96.html?locale=en-US,301) Allí encontrará una guía completa, paso a paso, para configurar su Estructura de Balance para compras nacionales:

![](/legacyfs/online/storage/blog_attachments/2023/02/Peru_FI_FSV-4.png)

SAP Help Portal

**Comentarios finales**

El reporte Registro de Compras ya está activo y listo para su uso. Si tiene más preguntas sobre este informe o cualquiera de estos cambios recientes, hágamelo saber en la casilla de comentarios.

Sus comentarios siempre son apreciados e incluso pueden ser el tema de mi próxima publicación en el blog.

Gracias y hasta la próxima,

Barnabas Kirk

#SAPGoGlobal #SAPLocalization

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [fi](/t5/tag/fi/tg-p/board-id/erp-blog-sap)
* [Legal Change](/t5/tag/Legal%20Change/tg-p/board-id/erp-blog-sap)
* [peru](/t5/tag/peru/tg-p/board-id/erp-blog-sap)
* [RCE](/t5/tag/RCE/tg-p/board-id/erp-blog-sap)
* [sap ecc](/t5/tag/sap%20ecc/tg-p/board-id/erp-blog-sap)
* [sunat](/t5/tag/sunat/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fcontabilidad-financiera-per%25C3%25BA-actualizaciones-del-registro-de-compras-con%2Fba-p%2F13569626%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39...