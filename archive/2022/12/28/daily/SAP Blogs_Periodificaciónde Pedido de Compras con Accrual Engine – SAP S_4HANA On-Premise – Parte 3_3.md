---
title: Periodificaciónde Pedido de Compras con Accrual Engine – SAP S/4HANA On-Premise – Parte 3/3
url: https://blogs.sap.com/2022/12/27/periodificacionde-pedido-de-compras-con-accrual-engine-sap-s-4hana-on-premise-parte-3-3/
source: SAP Blogs
date: 2022-12-28
fetch_date: 2025-10-04T02:35:53.639098
---

# Periodificaciónde Pedido de Compras con Accrual Engine – SAP S/4HANA On-Premise – Parte 3/3

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Periodificaciónde Pedido de Compras con Accrual E...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51742&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Periodificaciónde Pedido de Compras con Accrual Engine – SAP S/4HANA On-Premise – Parte 3/3](/t5/enterprise-resource-planning-blog-posts-by-sap/periodificaci%C3%B3n-de-pedido-de-compras-con-accrual-engine-sap-s-4hana-on/ba-p/13559461)

![cguedes](https://avatars.profile.sap.com/d/f/iddf16d4de1334092384d948fbe63314d73ac8936fc9db7cda14829b71604484ad_small.jpeg "cguedes")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[cguedes](https://community.sap.com/t5/user/viewprofilepage/user-id/633)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51742)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51742)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559461)

‎2022 Dec 27
4:27 PM

0
Kudos

1,709

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

# **Contabilizaciones de utilización**

El Accrual Engine admite el proceso de que la contabilización de costes reales, como la contabilización de una factura de proveedor o una entrada de mercancías, reduzca las periodificaciones contabilizadas anteriormente.

Este proceso se denomina *Utilización* *de* *periodificación (Accrual Utilization)*.

– Se utiliza el término *Utilización*: Este término enfatiza más claramente que las  periodificaciones se reducen en este proceso.

Las contabilizaciones *de* *utilización* *de* *periodificación* son partidas individuales en asientos contables que se pueden identificar como utilización de periodificación.

– El campo *Código de* *tipo* *de* *partida* *individual* *específico* *de* *libro* *auxiliar*, ACDOCA-SLALITTYPE, por ejemplo, se puede evaluar para este fin.

En combinación con los conceptos de *la* *Fecha* *de valor de* *periodificación* y *la* *Frecuencia* *de* *cierre* *de las* *periodificaciones*, el proceso de utilización se puede personalizar de forma flexible. Simplemente hablando:

– La *Fecha* *de valor de* *periodificación* permite definir qué contabilizaciones de periodificación se pueden utilizar en una contabilización de costes reales

– La *Frecuencia* *de* *cierre* *de las* *periodificaciones* permite diferenciar entre las utilizaciones del último ejercicio y las periodificaciones del ejercicio actual.

La utilización de periodificación se puede personalizar para que tenga lugar

– En línea, es decir, durante la contabilización de los costes reales y/o

– Sin conexión, es decir, al final del período mediante la ejecución de contabilización de periodificación periódica.

El indicador correspondiente en el Customizing se llama *Periódicamente* en lugar de *Offline*.

# **Contabilizaciones de utilización:** **Partidas individuales adicionales en factura y entrada de mercancías**

Para lograr que durante la factura o la entrada de mercancías las periodificaciones se reduzcan directamente durante esta contabilización,

– en *la* *actividad* *IMG* ***Asignar* *tipos**de* *posición* *de* *periodificación* *a* *tipos* *de asiento* *contable* *y* *esquemas* *de* *contabilización***, el tipo de transacción UP debe asignarse a un esquema de contabilización y

– se debe fijar el indicador Contabilizar online.

La partida individual adicional se añadirá automáticamente al asiento contable de la factura o de la entrada de mercancías: abonan la cuenta de costes y cargan la cuenta de periodificación.

Tenga en cuenta que puede fijar ambos indicadores, *Contabilizar* *online* y *Contabilizar* *periódicamente*.

– Esto no perjudica. En este caso, la ejecución de periodificación periódica no contabilizará la contabilización UP dos veces.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_15-55-03-scaled.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_15-59-38.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_16-25-11.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_16-26-55-scaled.jpg)

# **Contabilizaciones de utilización: Utilización parcial**

Si el importe de periodificación es menor que los costes contabilizados por la factura o la entrada de mercancías, solo el importe parcial correspondiente de los costes se contabilizará como contabilización de utilización. El resto se contabiliza como costes.

– Técnicamente hablando: el mínimo de periodificaciones y costes existentes contabilizados por la factura o la entrada de mercancías se contabiliza como contabilización de utilización.

# **Frecuencia de contabilización y período contable**

***Los* *períodos* *contables*** en el libro mayor se definen mediante la variante de ejercicio fiscal de la combinación de sociedad y ledger.

El accrual engine es más flexible en comparación con el libro mayor:

El accrual engine también admite frecuencias de contabilización que no sean períodos definidos por la variante de ejercicio.

En la actividad IMG *Definir* *clases* *de* *posición* *de* *periodificación* puede introducir una ***Frecuencia*** ***de*** ***contabilización***.

– Por defecto, esta frecuencia es ***Por*** ***período*** ***contable***, lo que significa que es el período contable como en el libro mayor.

– Esta también es la recomendación: Utilice el período contable, es decir, introduzca como frecuencia el valor *Por* *período* *contable*.

– Pero también puede introducir una frecuencia diferente como *Diario* o *Trimestral*, por ejemplo.

Por este motivo, el término *Período* en el contexto del Accrual Engine significa el período definido por la frecuencia de contabilización del tipo de posición de periodificación:

El período en el Accrual Engine se denomina ***Período*** ***de*** ***contabilización*** ***de*** ***periodificación*** para enfatizar que este período (diario, período contable, trimestral...) puede ser diferente del período del libro mayor (siempre = período contable).

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_16-40-11.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_16-42-57-scaled.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-27_16-43-42.jpg)

# **Contabilizaciones de utilización:** **Se utilizan periodificaciones de períodos contables anteriores**

La contabilización de costes reales (por ejemplo, factura) solo puede utilizar periodificaciones que se han contabilizado en el período de contabilización de *periodificación* **anterior**.

La contabilización de costes reales **no** **puede** utilizar periodificaciones que se hayan contabilizado en el mismo período contable de periodificación o en uno futuro.

– En su lugar, cuando la ejecución de contabilización de periodificación periódica...