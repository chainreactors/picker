---
title: How to reset Passwords from SAP* and DDIC
url: https://blogs.sap.com/2023/05/20/how-to-reset-passwords-from-sap-and-ddic/
source: SAP Blogs
date: 2023-05-21
fetch_date: 2025-10-04T11:37:45.220470
---

# How to reset Passwords from SAP* and DDIC

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* How to reset Passwords from SAP\* and DDIC

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46717&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [How to reset Passwords from SAP\* and DDIC](/t5/application-development-and-automation-blog-posts/how-to-reset-passwords-from-sap-and-ddic/ba-p/13553620)

![marcobuescher](https://avatars.profile.sap.com/0/7/id077d51d5442f0306cf560b3fcdf8241d8773aca7d99d7de3094c89834541547f_small.jpeg "marcobuescher")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[marcobuescher](https://community.sap.com/t5/user/viewprofilepage/user-id/169)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46717)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46717)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553620)

‎2023 May 20
9:25 AM

0
Kudos

9,244

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

As an SAP consultant or administrator, you may be familiar with the DDIC user, which plays a key role in your SAP system. The DDIC user has extensive privileges and is responsible for managing the database and other important tasks. However, there may be times when you need to reset the password for the DDIC user, whether due to security concerns or simply because of a forgotten password.

In this blog post, we will give you a simple guide on how to reset the password for the DDIC user in your SAP system. We will go step by step and show you how to perform this important procedure safely and effectively.

However, before we dive into the details, it is important to note that resetting the password for the DDIC user is a sensitive task and requires appropriate precautions. Make sure you have the necessary permissions and that you understand the impact this operation will have on your SAP system.

Now that we've covered the basics, without further ado, let's dive into how to reset the password for the DDIC user in SAP. Just follow the steps we present and you will be able to restore access to your DDIC user in no time.

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild1-16.png) |
 REPORT ZPWDDEL.  \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  \* \*  \* Dieses Programm setzt die Paßworthistorie \*  \* zurück, so daß ein User sein altes Paßwort \*  \* weiter benutzen kann. \*  \* \*  \* 21.09.05 \*  \* Ergänzung für ein verlorenes Passwort \*  \* Mandant = Mandant, wo das Passwort verändert \*  \* werden soll. \*  \* Modify = Hier ein X setzen, wenn verändert \*  \* werden soll. \*  \* Hexpass = Verschlüsseltes Passwort des gleichen\*  \* Users aus einem anderen System \*  \*------------------------------------------------\*  \* gefunden im Netz \*  \* Original von:IMRE KABAI \*  \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  TABLES: USR02.  PARAMETERS: USER LIKE USR02-BNAME,  Mandant LIKE USR02-MANDT,  Modify(1) type c,  HexPass LIKE USR02-BCODE.SELECT \* FROM USR02 client specified WHERE BNAME = USER  and Mandt = Mandant.  ENDSELECT.IF SY-SUBRC = 0.  if Modify = 'X'.  usr02-bcode = Hexpass.  usr02-uflag = '0'.  update usr02 client specified.  write: / 'Passwort geändert.'.  else.  USR02-OCOD1 = USR02-OCOD2 = USR02-OCOD3 =  USR02-OCOD4 = USR02-OCOD5 = USR02-BCODE.  usr02-bcda1 = usr02-bcda2 = usr02-bcda3 =  usr02-bcda4 = usr02-bcda5 = usr02-erdat.  MODIFY USR02.  write: / 'Paßworthistorie erfolgreich zurückgesetzt!'.  endif.  ELSE.  WRITE: / 'Benutzer nicht vorhanden!'.  ENDIF. |

|
  |
  |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild2-2.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild3.png) |

|
 Client 800: SE16N - Table USR02 - Read HEX value |
 Client 800 - Change DDIC password |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild4.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild5.png) |

|
 Client 800 control HEX value was overwritten |
 Client 800 - Enter HEX value - Save |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild6.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild7.png) |

|
 PW set |
 Client 000 Login (Possibly set new password, since 90 days have passed) |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/03/Bild8.png) | |

|
  |
  |

* [abap](/t5/tag/abap/tg-p/board-id/application-developmentblog-board)
* [basis](/t5/tag/basis/tg-p/board-id/application-developmentblog-board)
* [sapbasis](/t5/tag/sapbasis/tg-p/board-id/application-developmentblog-board)

5 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin