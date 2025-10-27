---
title: HCM Nómina España: Utilización de la BAdI para ajuste de valores relacionados con entradas de infotipo
url: https://blogs.sap.com/2023/03/21/hcm-nomina-espana-utilizacion-de-la-badi-para-ajuste-de-valores-relacionados-con-entradas-de-infotipo/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:14:57.504456
---

# HCM Nómina España: Utilización de la BAdI para ajuste de valores relacionados con entradas de infotipo

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* HCM Nómina España: Utilización de la BAdI para aju...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51072&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HCM Nómina España: Utilización de la BAdI para ajuste de valores relacionados con entradas de infotipo](/t5/enterprise-resource-planning-blog-posts-by-sap/hcm-n%C3%B3mina-espa%C3%B1a-utilizaci%C3%B3n-de-la-badi-para-ajuste-de-valores/ba-p/13555179)

![former_member183497](https://avatars.profile.sap.com/former_member_small.jpeg "former_member183497")

[former\_member183497](https://community.sap.com/t5/user/viewprofilepage/user-id/183497)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51072)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51072)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555179)

‎2023 Mar 21
9:16 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51072/tab/all-users "Click here to see who gave kudos to this post.")

1,926

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

Al utilizar la **BAdI para ajuste de valores relacionados con entradas de infotipo** (HRPADES\_FIE\_BATCH\_INPUT), usted puede cambiar las instrucciones de *batch input* que el programa **Mensaje FIE** (RPU\_PADES\_FIE) genera cuando hace la comparación de los ficheros FIE con los datos maestros de los empleados. Por lo tanto, en este blog post usted encuentra ejemplos de utilización para cada uno de los métodos disponibles.

**Métodos para implementación obligatoria:**

*CHANGE\_SUBTY*

Este método le permite definir el tipo de absentismo, una vez que recibe como parámetro el seguimiento referente a la información utilizada en la generación de absentismo.

**Nota:**

Usted puede verificar los tipos de seguimiento en el manual MENSAJE DE I.N.S.S. EMPRESA (FIE).

**Ejemplo de código:**

method IF\_HRPADES\_FIE\_BATCH\_INPUT~CHANGE\_SUBTY.

IF is\_segment\_data-dit\_contingency\_type = '1'.

cv\_subty = '1000'. " Incapacidad Temporal

ELSEIF is\_segment\_data-dit\_contingency\_type = '3'.

cv\_subty = '2000'. " Accidente de trabajo

ENDIF.

endmethod.

*SET\_DELEGATED\_ABSENCE\_SUBTY*

Este método le permite cambiar el subtipo de un absentismo en lo cual se reporta un cambio para pago directo, o sea, su compañía empieza a pagar un valor diferente de contribución, mientras el empleado sigue incapacitado.

**Ejemplo de código:**

method IF\_HRPADES\_FIE\_BATCH\_INPUT~SET\_DELEGATED\_ABSENCE\_SUBTY.

"Determina cual el subtipo para el absentismo de pago directo baseado en el subtipo del absentismo original

IF is\_original\_absence-subty = '1000'.

cv\_subty = '9991'.

ELSEIF is\_original\_absence-subty = '2000'.

cv\_subty = '9992'.

ELSE.

cv\_subty = '9990'.

ENDIF.

endmethod.

**Métodos para implementación opcional:**

*UPDATE\_ABSENCE*

Este método recibe la información del absentismo que usted creará y le permite modificarlo de acuerdo con su necesidad, como las fechas del campo Inicio certificado de enfermedad de los absentismos, o algún otro campo nuevo en el infotipo **Absentismos** (IT2001).

**Ejemplo de código:**

method IF\_HRPADES\_FIE\_BATCH\_INPUT~UPDATE\_ABSENCE.

"si no hay una fecha de fin (ENDDA = 31.12.9999), rellénela con la fecha de fin estimada.

IF is\_segment\_data-dit\_estimated\_duration IS NOT INITIAL AND

cs\_absence-endda = '99991231'.

cs\_absence-endda = cs\_absence-begda + is\_segment\_data-dit\_estimated\_duration.

ENDIF.

endmethod.

*UPDATE\_BI\_SCRIPT*

Este método recibe el script de batch input y le permite cambiar las instrucciones generadas, de acuerdo con su necesidad. A partir de este método, es posible integrar la funcionalidad con otros programas o soluciones.

**Ejemplo de código:**

method IF\_HRPADES\_FIE\_BATCH\_INPUT~UPDATE\_BI\_SCRIPT.

FIELD-SYMBOLS <lt\_script> TYPE hrcm\_bi\_tab.

FIELD-SYMBOLS <ls\_script\_data> TYPE bdcdata.

DATA lt\_new\_script  TYPE if\_hrpades\_fie\_batch\_input=>ty\_t\_fie\_bi\_script.

DATA lv\_is\_delete   TYPE abap\_bool.

DATA lv\_is\_open\_end TYPE abap\_bool.

MOVE-CORRESPONDING ct\_script TO lt\_new\_script.

"Evita que las entradas sin fecha de fin (endda = 31.12.9999) sean borrados por el script de batch input

LOOP AT lt\_new\_script ASSIGNING <lt\_script>.

CLEAR lv\_is\_delete.

CLEAR lv\_is\_open\_end.

LOOP AT <lt\_script> ASSIGNING <ls\_script\_data>.

IF <ls\_script\_data>-fnam = 'BDC\_OKCODE' AND

<ls\_script\_data>-fval = '=DEL'.

lv\_is\_delete = abap\_true.

ENDIF.

IF <ls\_script\_data>-fnam = 'RP50G-ENDDA' AND

<ls\_script\_data>-fval = '31129999'.

lv\_is\_open\_end = abap\_true.

ENDIF.

ENDLOOP.

IF lv\_is\_open\_end = abap\_true AND

lv\_is\_delete   = abap\_true.

DELETE lt\_new\_script INDEX sy-tabix.

ENDIF.

ENDLOOP.

ct\_script = lt\_new\_script.

endmethod.

*UPDATE\_COLISION\_ABSTY*

Este método le permite definir cuáles son los tipos de absentismo que no se pueden colisionar con los subtipos creados internamente, a través del tipo relacionado (ABSTY) a cada absentismo.

**Ejemplo de código:**

method if\_hrpades\_fie\_batch\_input~update\_colision\_absty.

"Definindo que el absty debe ser considerado para colisiones

APPEND 'ZZ' TO ct\_absty.

endmethod.

*UPDATE\_COLISION\_ABSTP*

Este método le permite definir cuáles son los tipos de absentismo que no se pueden colisionar con los subtipos creados internamente, a través del tipo relacionado (ABSTP) a cada absentismo.

**Ejemplo de código:**

method if\_hrpades\_fie\_batch\_input~update\_colision\_abstp.

"Definindo que el abstp debe ser considerado para colisiones

APPEND 'Z' TO ct\_abstp.

endmethod.

*APPEND\_ABSENCE\_TABLE*

Este método le permite cambiar las entradas de absentismos, a partir del recibimiento de la tabla de ausencias. La ejecución del método apenas puede ser realizada después de todos los anteriores relacionados con el seguimiento procesado.

**Ejemplo de utilización:**

1. Cambiar el segmento LCL\_FIE\_SEGMENT\_PARSER.

2. Añadir una llamada del nuevo método de BAdI.

3. Añadir las entradas de absentismos a la tabla de procesamiento de FIE.

**Nota:**

Al añadirlas a la tabla, las llamadas de los métodos APPEND\_NEW\_ABSE...