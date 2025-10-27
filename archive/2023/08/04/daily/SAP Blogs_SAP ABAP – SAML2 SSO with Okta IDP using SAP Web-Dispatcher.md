---
title: SAP ABAP – SAML2 SSO with Okta IDP using SAP Web-Dispatcher
url: https://blogs.sap.com/2023/08/03/sap-abap-saml2-sso-with-okta-idp-using-sap-web-dispatcher/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:36.644380
---

# SAP ABAP – SAML2 SSO with Okta IDP using SAP Web-Dispatcher

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP ABAP – SAML2 SSO with Okta IDP using SAP Web-D...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163935&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP ABAP – SAML2 SSO with Okta IDP using SAP Web-Dispatcher](/t5/technology-blog-posts-by-members/sap-abap-saml2-sso-with-okta-idp-using-sap-web-dispatcher/ba-p/13572704)

![ashishv610](https://avatars.profile.sap.com/d/f/iddf01e3b4ddde438e29156bea7f5a4284619d6d5e9eb6662a2a2d1af2215ee511_small.jpeg "ashishv610")

[ashishv610](https://community.sap.com/t5/user/viewprofilepage/user-id/684246)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163935)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163935)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572704)

‎2023 Aug 03
7:38 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163935/tab/all-users "Click here to see who gave kudos to this post.")

6,005

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP enhancement package for SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520enhancement%2520package%2520for%2520SAP%2520ERP/pd-p/01200615320800000693)
* [SAP NetWeaver Application Server](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server/pd-p/01200615320800000352)

* [SAP enhancement package for SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2Benhancement%2Bpackage%2Bfor%2BSAP%2BERP/pd-p/01200615320800000693)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP NetWeaver Application Server

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer/pd-p/01200615320800000352)

View products (3)

We have seen several blogs or documentations from IDP providers which does not help us to understand SAML2 SSO setup using SAP Web-Dispatchers. In my recent case, I came across SAML2 SSO authentication with Okta Identity Provider using SAP Web-Dispatcher with Logon ID and not from AD.

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-1-2.png)

**SAP GUI Settings** -

Below settings are important for launching Web-URLs using SAML2 SSO –

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-2.png)

For using Microsoft Edge seamlessly, SAP recommends deploying WebView.

* Deployed WebView to enable Edge for proper functioning using below SAP notes or Microsoft URL.

* You will have to work with Client’s IT service desk to send this setting across all users. Otherwise, they will face challenge in Web-based URLS like BRF+, SAML2, NWBC, WebGUI, or any Z-SICF, etc.

**2901278** - SAP GUI HTML Control based on Chromium Edge: Legacy HTML does not work (correctly) / present limitations

**2796898** - New and changed features in SAP GUI for Windows 7.70

**3043532** - Web Dynpro application opens always in Internet Explorer (IE11) when called from SAPGUI

<https://learn.microsoft.com/en-us/microsoft-edge/webview2/>

Below blog will help you with all the necessary information to setup SAML2 SSO authentication with Okta IDP using SAP Web-Dispatcher –

* **Case-1**: **SAP Systems with one MANDT (or SAP Client) used.**

1. Make sure you use only one authentication method – SAML2 or SPNEGO. SAP strongly recommends using one authentication at the same time.

2. In Web-dispatcher, maintain backend systems and make sure to include mysapsso2 cookie because all Web-URLs / Okta tiles uses myssocntl sicf.

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-21.png)

3. Go to Tx – SPNEGO and Disable/Deactivate spnego or remove complete settings.

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-3-1.png)

4. Maintain web-dispatcher entries in table – HTTPURLLOC in Tx – SE16 within Customer MANDT/Client other than 000.

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-4.png)

5. In Tx – SICF, go to service name – SAML2 and maintain Logon Procedure with Priority-1 for SAML2 LOGON.

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-5.png)

6. Apply Okta related settings.

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-6.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-901.png)

|
 **Validation Required** |

|
 Check Parameters |

|
 \* login/ticket\_only\_by\_https = 1    login/accept\_sso2\_ticket = 1    login/create\_sso2\_ticket = 2 or 3 |

|
 Check Services |

|
 \* SYSTEMLOGINJS (activate the service) |

|
 \* saml2 (Change priority of SAML) |

|
 \* /default\_host/sap/bc/webdynpro/sap  /sap/public/bc/icf/systemloginjs  /sap/public/bc/pictograms  /sap/public/bc/ur  /sap/public/bc/icons  /sap/public/bc/webdynpro  /sap/public/bc/webicons  /sap/public/icf\_info/icr\_groups  /sap/public/icf\_info/icr\_urlprefix  /sap/public/bc/ping  /sap/public/myssocntl  /sap/bc/bsp/sap/system\_test  /sap/bc/webdynpro/sap/configure\_application |

|
 Check Tcodes |

|
 \* SPNEGO |

|
 \* SMLG |

|
 \* RZ12 |

|
 \* STRUST / SSO2 |

|
 \* SNC |

|
 Check Tables from SE16 |

|
 \* HTTPURLLOC |

You may encounter an issue where SAML2 screen using web-dispatcher URL for backend system shows blank. Applied below SAP Note fix to get the next screen.

**3037454** - ESI - "Logon is being prepared" when accessing SOAMANAGER

7. Ask your Okta administrator to maintain below endpoint URL in Okta Relay mapping as –

<https://<Public-ALB>:<port>/sap/saml2/sp/acs/123>
or

<https://<Web-Dispatcher> hostname>:<port>/sap/saml2/sp/acs/123

**where 123 is an arbitrary Customer’s MANDT/Client for their backend SAP system.**

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-101.png)

* **Case 2**: **SAP Systems with multiple MANDT (or SAP Clients) used.**

Our customer faced an issue where SAML2 SSO works only for one client out of three clients. As a solution, apply Okta certificate in all three clients after every activation. Please follow below SAP Note for more details and fix -

**3095581** - SAML2.0 ABAP: SAML authentication only works in one client despite SAML is configured in multiple clients

* **Case 3**: Within Hub/Embedded Fiori, first level authentication through SAML2 SSO works but when it points to another Fiori URL internally it asks for Username and password, and SSO does not works. Please follow below SAP Note for more details and fix -

**2051210** - Fragments in HTTP URLS are not handled after SAML 2.0 authentication

![](/legacyfs/online/storage/blog_attachments/2023/07/AV-12.png)

Finally, SAML2 SSO setup is completed using Okta IDP with Web-dispatcher.

Best Regards,

Ashish Verma

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreaso...