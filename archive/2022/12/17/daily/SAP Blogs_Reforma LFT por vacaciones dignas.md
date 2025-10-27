---
title: Reforma LFT por vacaciones dignas
url: https://blogs.sap.com/2022/12/16/reforma-lft-por-vacaciones-dignas/
source: SAP Blogs
date: 2022-12-17
fetch_date: 2025-10-04T01:46:03.547773
---

# Reforma LFT por vacaciones dignas

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Reforma LFT por vacaciones dignas

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50836&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Reforma LFT por vacaciones dignas](/t5/enterprise-resource-planning-blog-posts-by-sap/reforma-lft-por-vacaciones-dignas/ba-p/13553569)

![HugoRodriguez](https://avatars.profile.sap.com/3/c/id3cd9bc8981ed388873fd8e52f9642b8053b0272c75af86e8306a5d0a7384f07a_small.jpeg "HugoRodriguez")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[HugoRodriguez](https://community.sap.com/t5/user/viewprofilepage/user-id/53000)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50836)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50836)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553569)

‎2022 Dec 16
10:39 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50836/tab/all-users "Click here to see who gave kudos to this post.")

245,745

* SAP Managed Tags
* [HCM Payroll Mexico](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll%2520Mexico/pd-p/8570744770985579072506591679151)

* [HCM Payroll Mexico

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll%2BMexico/pd-p/8570744770985579072506591679151)

View products (1)

Como seguramente es de su conocimiento, el Senado de la República Mexicana aprobó las reformas en materia de Vacaciones Dignas.

Les comparto información relevante al respecto.

### **Cambio Legal**:

Esta reforma considera cambios en los Artículos 76 y 78 de la Ley Federal del Trabajo para elevar de 6 a 12 días el periodo vacacional anual para los trabajadores. Además, establece que se sumen dos días por cada año trabajado y a partir del sexto año se aumenten dos días por cada cinco años.

A partir del 2023, la nueva tabla de días de vacaciones por años laborados, quedará así:

![](/legacyfs/online/storage/blog_attachments/2022/12/VacacionesDignas.jpg)

Tabla Vacaciones Dignas

La reforma fue remitida al Ejecutivo para su publicación en el Diario Oficial de la Federación (DOF) para que sea aplicable a partir del 2023.

Como consecuencia de esta reforma, también se modifican el pago de la Prima Vacacional correspondiente (25% de las Vacaciones) y el factor mínimo de integración al salario (actualmente es igual a 1.0452 que corresponde a 15 días de aguinaldo + 1.5 días de pima vacacional entre 365).

### **Funcionalidad actual en Nómina Mexicana SAP**:

En HCM/PY de SAP el derecho a días de vacaciones y a la prima vacacional se configuran en la tabla T559E.

En cuanto al factor mínimo de integración, tenemos dos constantes en la tabla T511K. Estas son: “SFINT” y “SFMIN”.

Actualmente, tenemos las siguientes entradas modelo de SAP en la tabla T559E:

![](/legacyfs/online/storage/blog_attachments/2022/12/T559E_01.png)

T559E selección

![](/legacyfs/online/storage/blog_attachments/2022/12/T559E_02.png)

T559E salida

Donde TpCAb es el ‘Tipo de Contingente de Absentismo’ y tenemos, como modelo, los valores ‘1’ para Vacaciones y ‘2’ para Prima Vacacional.

Esta tabla, T559E, es una tabla tipo “C”. Esto significa que dicha tabla debería ser actualizada sólo el cliente y no por SAP. Así, cada cliente de SAP es responsable de mantener, en esa tabla, las entradas y los valores que apliquen para sus requerimientos particulares de negocio (que pueden ser iguales o mayores a los mínimos que señala la Ley).

En cuanto a las constantes citadas de la tabla T511K, éstas sí se encuentran en el rango de claves reservadas para SAP (sólo deberían ser actualizadas por SAP).

Ahora con la reforma a la LFT, en la tabla T559E deberán registrarse las entradas que correspondan a los requerimientos particulares de cada negocio, pero que no podrán ser menores a los que ahora señala la Ley reformada. Aquí es muy importante que cada empresa defina claramente cuántos días concederán de vacaciones a sus colaboradores para cumplir con los cambios aprobados a la Ley.

Hoy en día, algunas empresas ya conceden más días de los que se aprobaron con la reforma. Así que deberán decidir si aumentarán días a su tabla de vacaciones actual, cuántos días y en cuáles rangos de antigüedad. Las empresas que están en los valores mínimos, definitivamente deberán incrementar los derechos de vacaciones. Sea lo que decida cada empresa, en todo caso, insisto, los días de vacaciones no podrán ser menores a lo establecido por la nueva Ley. Pero la decisión deberá tomarla cada empresa en lo específico. Una vez definido lo anterior, se deberán configurar las entradas que correspondan en la tabla referida: T559E.

Es de esperarse, por supuesto, que no todos nuestros clientes tienen, ni tendrán, la misma tabla de vacaciones; y también que no todos coinciden, ni coincidirán, con la tabla modelo provista de fábrica por parte de SAP.

### **Funcionalidad nueva en Nómina Mexicana SAP**:

En SAP estamos analizando qué podemos hacer al respecto. Como ya mencioné en la sección anterior: la tabla donde se configuran los derechos de vacaciones y de prima vacacional es una tabla que debería ser configurada sólo por los clientes y no por SAP. Además, como ya también expuse, no todos nuestros clientes tienen los mismos valores propuestos como modelo de SAP.

Uno de los principales inconvenientes que vemos de entregar algo es que, si los clientes ya tienen configurados sus propios valores en las mismas entradas modelo de SAP (campos llave que aparecen en color azul en la imagen de arriba); entonces, la entrega de SAP sobrescribirá los valores que el cliente ya ha configurado ahí. Esto puede generar escenarios no deseados por nuestros clientes.

### **Aplicación práctica de los nuevos derechos de vacaciones**:

Por último, les comparto lo que algunos de nuestros clientes están decidiendo con respecto a cómo llevar a la práctica esta reforma: planean configurar la tabla T559E con los nuevos derechos de vacaciones (decididos internamente en su empresa). No van a sobrescribir entradas, sino a crear nuevas entradas (a partir del 01.01.2023) y delimitar la vigencia de las actuales.

Luego, van a generar los nuevos contingentes a partir del siguiente aniversario de cada trabajador en el 2023. Esto significa que cada trabajador recibirá el incremento en los días de vacaciones no a partir del 01.01.2023, sino a partir de su siguiente aniversario en el 2023. Para generar los nuevos contingentes con la nueva configuración de la nueva Ley se puede utilizar el reporte estándar RPTQTA00 (transacción PT\_QTA00).

Por ejemplo, un trabajador cumple años de servicio el 17 de Marzo. Supongamos que en el 2023 cumplirá tres años de antigüedad. Con lo mencionado en el párrafo anterior, el trabajador adquirió el derecho a 8 días de vacaciones (con 2.0 días de prima) el 17.03.2022 (Ley anterior). Ese derecho se conservará al iniciar el año 2023 y no se incrementará a partir del 1 de Enero. Pero, en el siguiente aniversario, es decir el 17.03.2023, el trab...