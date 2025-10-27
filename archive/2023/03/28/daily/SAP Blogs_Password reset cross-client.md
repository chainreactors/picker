---
title: Password reset cross-client
url: https://blogs.sap.com/2023/03/27/password-reset-cross-client/
source: SAP Blogs
date: 2023-03-28
fetch_date: 2025-10-04T10:51:12.719897
---

# Password reset cross-client

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Password reset cross-client

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47061&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Password reset cross-client](/t5/application-development-and-automation-blog-posts/password-reset-cross-client/ba-p/13560916)

![marcobuescher](https://avatars.profile.sap.com/0/7/id077d51d5442f0306cf560b3fcdf8241d8773aca7d99d7de3094c89834541547f_small.jpeg "marcobuescher")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[marcobuescher](https://community.sap.com/t5/user/viewprofilepage/user-id/169)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47061)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47061)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560916)

‎2023 Mar 27
5:18 PM

[2
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47061/tab/all-users "Click here to see who gave kudos to this post.")

3,021

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

Hello,

I had a request that a client requested a client copy. Unfortunately the passwords of the users SAP\* and DDIC in client 000 could not be found anymore. So that the system copy could still be performed I decided to perform the following workaround. The program for this was a find from the net, the source is mentioned.

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild2-5.png) |
 REPORT ZPWDDEL.  \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  \* \*  \* Dieses Programm setzt die Paßworthistorie \*  \* zurück, so daß ein User sein altes Paßwort \*  \* weiter benutzen kann. \*  \* \*  \* 21.09.05 \*  \* Ergänzung für ein verlorenes Passwort \*  \* Mandant = Mandant, wo das Passwort verändert \*  \* werden soll. \*  \* Modify = Hier ein X setzen, wenn verändert \*  \* werden soll. \*  \* Hexpass = Verschlüsseltes Passwort des gleichen\*  \* Users aus einem anderen System \*  \*------------------------------------------------\*  \* gefunden im Netz \*  \* Original von:IMRE KABAI \*  \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  TABLES: USR02.  PARAMETERS: USER LIKE USR02-BNAME,  Mandant LIKE USR02-MANDT,  Modify(1) type c,  HexPass LIKE USR02-BCODE.SELECT \* FROM USR02 client specified WHERE BNAME = USER  and Mandt = Mandant.  ENDSELECT.IF SY-SUBRC = 0.  if Modify = 'X'.  usr02-bcode = Hexpass.  usr02-uflag = '0'.  update usr02 client specified.  write: / 'Passwort geändert.'.  else.  USR02-OCOD1 = USR02-OCOD2 = USR02-OCOD3 =  USR02-OCOD4 = USR02-OCOD5 = USR02-BCODE.  usr02-bcda1 = usr02-bcda2 = usr02-bcda3 =  usr02-bcda4 = usr02-bcda5 = usr02-erdat.  MODIFY USR02.  write: / 'Paßworthistorie erfolgreich zurückgesetzt!'.  endif.  ELSE.  WRITE: / 'Benutzer nicht vorhanden!'.  ENDIF. |

|
 At first you need this Program. |
 Program code. |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild2.2.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild3-4.png) |

|
 Client 100: SE16N - Table USR02 - Read HEX value. Open the table USR02, where you will find the initial password of the user encrypted as HEX value. |
 Client 100 - Change DDIC password |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild4-4-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild1-21.png) |

|
 Client 100 control HEX value was new and overwritten |
 Client 100 - open Programm ZPWDDEL,  Enter User, Mandant, Set Flag X as explained in the Program code. HEX value - Save |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild6-4.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild7-3.png) |

|
 Information, that the PW is set |
 Client 000 Login (Possibly set new password, since 90 days have passed) |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild8-3.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild9-2.png) |

|
 Logon works fine in Test System. Transport in Prod... |
 Transport is running.. |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild10-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild11-1.png) |

|
 Transport is done. |
 Program imported into productive system |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild12-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild13-1.png) |

|
 SE16N Initial password read from DDIC. Password is hexadecimal encrypted. |
 Login to client 100 with DDIC and new password |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild14-1-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild15-1.png) |

|
 Assign new password (90 days policy) |
 Set the password in the ZPWDEL program and execute the program. Save. |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild16-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild17-1.png) |

|
 PW changed. |
 Logon to client 000 with user DDIC and new password. |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild19.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild18.png) |

|
 Successful registration. |
 Successful registration. |

```
REPORT ZPWDDEL.

**************************************************

* *

* Dieses Programm setzt die Paßworthistorie *

* zurück, so daß ein User sein altes Paßwort *

* weiter benutzen kann. *

* *

* 21.09.05 *

* Ergänzung für ein verlorenes Passwort *

* Mandant = Mandant, wo das Passwort verändert *

* werden soll. *

* Modify = Hier ein X setzen, wenn verändert *

* werden soll. *

* Hexpass = Verschlüsseltes Passwort des gleichen*

* Users aus einem anderen System *

*------------------------------------------------*

* gefunden im Netz *

* Original von:IMRE KABAI *

**************************************************

TABLES: USR02.

PARAMETERS: USER LIKE USR02-BNAME,

Mandant LIKE USR02-MANDT,

Modify(1) type c,

HexPass LIKE USR02-BCODE.SELECT * FROM USR02 client specified WHERE BNAME = USER

and Mandt = Mandant.

ENDSELECT.IF SY-SUBRC = 0.

if Modify = 'X'.

usr02-bcode = Hexpass.

usr02-uflag = '0'.

update usr02 client specified.

write: / 'Passwort geändert.'.

...