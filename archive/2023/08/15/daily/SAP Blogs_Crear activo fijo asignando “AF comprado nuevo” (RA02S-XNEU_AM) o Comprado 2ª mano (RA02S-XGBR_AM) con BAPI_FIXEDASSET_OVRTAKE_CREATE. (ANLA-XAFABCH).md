---
title: Crear activo fijo asignando “AF comprado nuevo” (RA02S-XNEU_AM) o Comprado 2ª mano (RA02S-XGBR_AM) con BAPI_FIXEDASSET_OVRTAKE_CREATE. (ANLA-XAFABCH)
url: https://blogs.sap.com/2023/08/14/crear-activo-fijo-asignando-af-comprado-nuevo-ra02s-xneu_am-o-comprado-2a-mano-ra02s-xgbr_am-con-bapi_fixedasset_ovrtake_create.-anla-xafabch/
source: SAP Blogs
date: 2023-08-15
fetch_date: 2025-10-04T12:01:49.064583
---

# Crear activo fijo asignando “AF comprado nuevo” (RA02S-XNEU_AM) o Comprado 2ª mano (RA02S-XGBR_AM) con BAPI_FIXEDASSET_OVRTAKE_CREATE. (ANLA-XAFABCH)

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Crear activo fijo asignando "AF comprado nuevo" (R...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47890&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Crear activo fijo asignando "AF comprado nuevo" (RA02S-XNEU\_AM) o Comprado 2ª mano (RA02S-XGBR\_AM) con BAPI\_FIXEDASSET\_OVRTAKE\_CREATE. (ANLA-XAFABCH)](/t5/application-development-and-automation-blog-posts/crear-activo-fijo-asignando-quot-af-comprado-nuevo-quot-ra02s-xneu-am-o/ba-p/13577969)

![mabace](https://avatars.profile.sap.com/e/c/idec4ab8741b99e34d673648e32ed3985d36573adbda2a02f5e5a178158ea08bee_small.jpeg "mabace")

[mabace](https://community.sap.com/t5/user/viewprofilepage/user-id/547182)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47890)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47890)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13577969)

‎2023 Aug 15
12:23 AM

0
Kudos

1,345

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

Tuve el reto de ajustar un programa para crear activos fijos asignándole el origen de la adquisición "nuevo" o "usado", con la BAPI *BAPI\_FIXEDASSET\_OVRTAKE\_CREATE*.

![](/legacyfs/online/storage/blog_attachments/2023/08/Transaccion-AS0x.png)

Al revisar la tabla *ANLA*, encontré el campo *XAFABCH* "Se ha adoptado el activo fijo usado" el cual tiene los posibles valores:

* X ► "Comprado 2ª mano"

* Y ► Indefinido

* <espacio> ► "AF comprado nuevo"

Al buscar en la pestaña Origen de la transacción AS01, AS02 y AS03 (programa *SAPLAIST* - dynpro *1181*) se indica la estructura *RA02S* para estos 2 checks:
> ```
> RA02S-XNEU_AM ► AF comprado nuevo
>
> RA02S-XGBR_AM ► Comprado 2ª mano
> ```

Los cuales se relacionan de la siguiente manera en el programa y dynpro arriba mencionado:
> ```
> CASE anla-xafabch.
>
> 	WHEN 'X'. " Asset acquired used
>
> 		ra02s-xgbr_am = 'X'.
>
> 		ra02s-xneu_am = space.
>
> 	WHEN space. " Asset acquired new
>
> 		ra02s-xgbr_am = space.
>
> 		ra02s-xneu_am ='X'.
>
> 	WHEN 'Y'. " Undefined
>
> 		ra02s-xgbr_am = space.
>
> 		ra02s-xneu_am = space.
>
> ENDCASE.
> ```

Yendo a la BAPI *BAPI\_FIXEDASSET\_OVRTAKE\_CREATE*, tiene el parámetro de entrada *ORIGIN* y *ORIGINx*, en cuya una estructura (*BAPI1022\_FEGLG009* y *BAPI1022\_FEGLG009X*, respectivamente) tienen el campo *PURCH\_NEW* "Indicador: El activo fijo ha sido comprado nuevo" el cual se debe llenar de la siguiente manera para marcar uno de los dos checks en la creación del activo fijo:

* AF comprado nuevo:

> ```
> BAPI1022_FEGLG009-PURCH_NEW = 'X'.
>
> BAPI1022_FEGLG009X-PURCH_NEW = 'X'.
> ```

* Comprado 2ª mano:

> ```
> BAPI1022_FEGLG009-PURCH_NEW = space.
>
> BAPI1022_FEGLG009X-PURCH_NEW = 'X'.
> ```

Si el campo *PURCH\_NEW* no se marca con *X* en la estructura *BAPI1022\_FEGLG009X*, el activo fijo se creará sin ninguno de los checks marcados:
> ```
> BAPI1022_FEGLG009-PURCH_NEW = space.
>
> BAPI1022_FEGLG009X-PURCH_NEW = space.
> ```

A continuación el ejemplo de cada caso:

![](/legacyfs/online/storage/blog_attachments/2023/08/Captura-de-pantalla-2023-08-10-133810.png)

Ejemplos de origen de Activos Fijos

Referencias:

* <https://answers.sap.com/questions/9721236/aa-master-tables.html>

* <https://answers.sap.com/questions/6924998/for-which-field-in-n-bapifixedassetovrtakecreate--.html>

* <https://userapps.support.sap.com/sap/support/knowledge/en/2401977>

* [ANLA-XAFABCH](/t5/tag/ANLA-XAFABCH/tg-p/board-id/application-developmentblog-board)
* [bapi\_fixedasset\_ovrtake\_create](/t5/tag/bapi_fixedasset_ovrtake_create/tg-p/board-id/application-developmentblog-board)
* [Origin](/t5/tag/Origin/tg-p/board-id/application-developmentblog-board)
* [RA02S-XGBR\_AM](/t5/tag/RA02S-XGBR_AM/tg-p/board-id/application-developmentblog-board)
* [RA02S-XNEU\_AM](/t5/tag/RA02S-XNEU_AM/tg-p/board-id/application-developmentblog-board)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin