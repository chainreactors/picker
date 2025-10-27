---
title: Document and Report Compliance México: Reporte de retención de impuestos y DIOT
url: https://blogs.sap.com/2023/02/13/document-and-report-compliance-mexico-reporte-de-retencion-de-impuestos-y-diot/
source: SAP Blogs
date: 2023-02-14
fetch_date: 2025-10-04T06:31:48.261046
---

# Document and Report Compliance México: Reporte de retención de impuestos y DIOT

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Document and Report Compliance México: Reporte de ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163750&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Document and Report Compliance México: Reporte de retención de impuestos y DIOT](/t5/technology-blog-posts-by-sap/document-and-report-compliance-m%C3%A9xico-reporte-de-retenci%C3%B3n-de-impuestos-y/ba-p/13567903)

![AndrewCaus](https://avatars.profile.sap.com/8/7/id87e471f367467cb1f35c3555b1385f4613266c0d55a1b23ed5b1107d840e07ab_small.jpeg "AndrewCaus")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AndrewCaus](https://community.sap.com/t5/user/viewprofilepage/user-id/122076)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163750)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163750)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567903)

‎2023 Feb 13
8:36 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163750/tab/all-users "Click here to see who gave kudos to this post.")

4,171

* SAP Managed Tags
* [SAP Document and Reporting Compliance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520and%2520Reporting%2520Compliance/pd-p/73554900100700003181)

* [SAP Document and Reporting Compliance

  Software Product](/t5/c-khhcw49343/SAP%2BDocument%2Band%2BReporting%2BCompliance/pd-p/73554900100700003181)

View products (1)

![](/legacyfs/online/storage/blog_attachments/2023/02/imagem-blog-post-CORRETA-.jpg)

 *Document and Reporting Compliance México: Reporte de retención de impuestos y DIOT*

Read this post in English: Click [here.](https://blogs.sap.com/2023/02/07/document-and-reporting-compliance-mexico-reporting-withholding-tax-amount-with-diot-report/)

¡Hola a todos!

Este blog contiene información acerca de cómo reportar correctamente la información de retención de impuestos utilizando el informe DIOT de Document and Report Compliance. Analizaremos los siguientes temas:

* Información de fondo.

* Cómo configurar el informe.

### **Información de fondo**

El informe DIOT solo refleja la retención de impuestos que se considera al momento del pago.

Mientras que una factura también genera un Importe de retención, no se supone que este importe aparezca en el reporte. Dado que el Servicio de Administración Tributaria (SAT) de México solo tiene en cuenta el importe pagado.

### **¿Cómo puedo configurarlo?**

Para declarar el importe de retención de impuestos con el reporte DIOT del CDI, se debe configurar la retención de impuestos para el proveedor al momento del pago.

1. Actualice la vista V\_T059PP en la transacción SM30 para el país MX.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture-WTax-Type.png)

 L*a imagen muestra una captura de pantalla del sistema SAP en la transacción SM30. Se resalta el tipo de retención de impuestos "4% IVA (IVA) para proveedor de México", en la columna Nombre.*

2. Abra la opción Socio comercial (Business Partner) en proveedor.

![](/legacyfs/online/storage/blog_attachments/2023/02/BP-Role.png)

 *La imagen muestra una captura de pantalla del sistema SAP en la transacción SM30. El campo Interlocutor comercial está en blanco y el campo Visualizar en rol IC se completa con la opción Proveedor FI FLVN00.*

3. Fije la retención de impuestos relevante.

![](/legacyfs/online/storage/blog_attachments/2023/02/WHT.png)

*La imagen muestra una captura de pantalla de la pestaña Proveedor: Retención de impuestos. A continuación, se muestra la sección Tipos de retención de impuestos con dos artículos en la columna Tipo de retención de impuestos: M1 y M2. En la columna Descripción de tipo de retención de impuestos, aparece una descripción breve para cada uno: M1, Retención de impuestos ISR y M2, Retención de IVA. Ambos tienen el mismo indicador de retención, A1.*

Después de seguir los pasos anteriores, ejecute el reporte DIOT del CDI y el importe correcto para la retención de impuestos se mostrará.

Ahora, cuando contabiliza una compensación o un pago parcial, el pago tendrá el importe  de retención de impuestos necesario para mostrar en el reporte DIOT Document and Report Compliance, el monto proporcional al importe pagado. Además, no se mostrará ningún importe de retención en la factura.

### **Más información:**

* Más información sobre informes legales para México: Haga clic aquí.

* ¿Tiene preguntas sobre la declaración del IVA para México? Consulte nuestra [nota de preguntas frecuentes](https://launchpad.support.sap.com/#/notes/2986139) para el reporte de IVA.

* Haga clic [aquí](https://launchpad.support.sap.com/#/notes/3169254) para ver la nota SAP 3169254.

* SAP S/4HANA Cloud: [VAT Declaration | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ce12687340f040afb02c3a9d01039a4c/29df758a77184f4784a7b4b3e240f29d.html?version=latest)

* Siga la página del tema SAP Document and Reporting Compliance y márquelo para mantenerse al día con las nuevas publicaciones de blog.

Hasta la próxima,

Andrew Caus

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [DRC mexico](/t5/tag/DRC%20mexico/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fdocument-and-report-compliance-m%25C3%25A9xico-reporte-de-retenci%25C3%25B3n-de-impuestos-y%2Fba-p%2F13567903%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  7 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Secure Your Digital Journey with SAP CIAM](/t5/technology-blog-posts-by-sap/secure-your-digital-journey-with-sap-ciam/ba-p/14232983)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procurement-lessons-from-our-s-4hana-mm/qaq-p/14233251)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [Top Reasons to Modernize with SAP HANA Cloud – Blog #5 in the Series](/...