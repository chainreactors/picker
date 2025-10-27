---
title: HCM Nómina España: Escenarios de utilización del Mensaje FIE
url: https://blogs.sap.com/2022/10/17/hcm-nomina-espana-como-ejecutar-el-mensaje-fie-para-un-empleado-2/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:06:58.798924
---

# HCM Nómina España: Escenarios de utilización del Mensaje FIE

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* HCM Nómina España: Escenarios de utilización del M...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/49720&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HCM Nómina España: Escenarios de utilización del Mensaje FIE](/t5/enterprise-resource-planning-blog-posts-by-sap/hcm-n%C3%B3mina-espa%C3%B1a-escenarios-de-utilizaci%C3%B3n-del-mensaje-fie/ba-p/13545345)

![former_member183497](https://avatars.profile.sap.com/former_member_small.jpeg "former_member183497")

[former\_member183497](https://community.sap.com/t5/user/viewprofilepage/user-id/183497)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=49720)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/49720)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13545345)

‎2022 Oct 17
9:22 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/49720/tab/all-users "Click here to see who gave kudos to this post.")

3,676

* SAP Managed Tags
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)
* [HCM Payroll](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll/pd-p/372556673030062693282256213775139)
* [HCM Payroll Spain](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll%2520Spain/pd-p/306843521589030681976078829712463)

* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [HCM Payroll

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll/pd-p/372556673030062693282256213775139)
* [HCM Payroll Spain

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll%2BSpain/pd-p/306843521589030681976078829712463)

View products (3)

(Scroll down for the English version)

Hola todos,

En el [último blog post](https://blogs.sap.com/2022/10/05/hcm-nomina-espana-como-ejecutar-el-mensaje-fie-para-un-empleado/), hablamos acerca del reporte **Mensaje FIE**, cómo ejecutarlo y tratar los absentismos de los empleados y la configuración necesaria para utilizar sus funcionalidades. Por lo tanto, en este blog post usted encuentra ejemplos de los siguientes escenarios:

* Creación de un absentismo

* Cuándo un absentismo es cerrado

* Colisión de absentismos

* Absentismo con diferente tipología

* Anulación de un parte en un absentismo guardado

* Recaída de un absentismo

* Absentismo existente con diferente fecha de fin

* Absentismo de pago directo

* Utilización de la BAdI para ajuste de valores relacionados con entradas de infotipo

**Prerrequisitos**

Usted ha implementado la siguientes SAP Notes:

* [3110425 - FIE: Absence comparison improvements and fixes](https://launchpad.support.sap.com/#/notes/3110425)

* [3082939 - FIE: Comparison between file and infotype absences](https://launchpad.support.sap.com/#/notes/3082939)

* [3224750 - FIE: Allow multiple absences for each file segment (APPEND\_ABSENCE\_TABLE BAdI method)](https://launchpad.support.sap.com/#/notes/3224750)

**Creación de un nuevo absentismo**

Al ejecutar el reporte, se nota que el fichero contiene un absentismo que todavía no existe en el sistema. Entonces, se sugiere la creación de un nuevo absentismo a través del ícono de adición.![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-1.png)

Al ejecutar el script generado, se creará el absentismo en el infotipo **Absentismos** (IT2001).

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-2.png)

**Un absentismo es cerrado**

Hay un absentismo guardado en el sistema sin fecha de fin, pero al ejecutar el reporte para el fichero, el sistema indica una fecha. Por lo tanto, es necesario que se cierre el absentismo con la fecha indicada en el fichero y el sistema lo sugiere a través de ícono de edición.

Al ejecutar el script generado, se modificará el absentismo en el infotipo **Absentismos** (IT2001) poniendo la nueva fecha de fin.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-4.png)

**Colisión de absentismos**

La colisión de absentismos ocurre cuando hay un absentismo guardado en el sistema, al mismo tiempo que el fichero reporta otra entrada cuyas fechas se colisionan. En el ejemplo abajo, hay un absentismo guardado con la fecha de 1 hasta 11 de febrero, pero el fichero contiene una entrada diferente con las fechas de 10 hasta 21 de febrero.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-5.png)

El sistema verifica si el absentismo guardado puede coexistir con el reportado en el fichero. Caso no sea posible, el log del reporte lo exhibe como un absentismo ya existente y con diferencias.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-6.png)

**Absentismo con diferente tipología**

Al ejecutar el reporte **Mensaje FIE** (RPU\_PADES\_FIE), el sistema le retorna un absentismo con una tipología diferente. O sea, el fichero reporta los datos de absentismo como accidente laboral, por ejemplo, mientras el absentismo esta guardado como una enfermedad común. El absentismo es lo mismo, pero su subtipo es diferente.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-7.png)

Es posible elegir si el sistema deberá considerar la colisión, bloquear o borrar la entrada original. Por lo tanto, usted define cómo el sistema tratará la colisión de información a través de la actividad de customización **Cálculo de la nómina** > **Cálculo de nómina: España** > **Evaluaciones para la Seguridad Social** > **Mensaje FIE** > **Indicar tratamiento de cambio de contingencia para el FIE**.

Suponga que usted elige la opción 0, el sistema mantendrá el absentismo como coexistente con diferencias.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-8.png)

Si usted elige la opción 1, el sistema le sugiere el bloqueo del absentismo existente y la creación de un nuevo con el misto subtipo reportado en el fichero.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-9.png)

Entonces, al ejecutar el script, el sistema bloquea el absentismo original y crea un nuevo para sustituirlo.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-10.png)

Si usted elige la opción 2, el sistema le sugiere que usted borre el absentismo existente para entonces crear un otro nuevo con el misto subtipo reportado en el fichero.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-11.png)

Entonces, al ejecutar el script, el sistema borra el absentismo original y crea un nuevo para sustituirlo.

![](/legacyfs/online/storage/blog_attachments/2022/10/8.-blog-post-image-12.png)

**Anulación de un parte en un absentismo guardado**

Al ejecutar el reporte **Mensaje FIE** (RPU\_PADES\_FIE) para un empleado con absentismo, un parte ha sido anulado por la Seguridad Social, necesitando, por lo tanto, anular la entrada del absentismo o actualizarla en ...