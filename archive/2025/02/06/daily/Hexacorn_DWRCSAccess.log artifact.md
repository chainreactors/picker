---
title: DWRCSAccess.log artifact
url: https://www.hexacorn.com/blog/2025/02/05/dwrcsaccess-log-artifact/
source: Hexacorn
date: 2025-02-06
fetch_date: 2025-10-06T20:35:14.674863
---

# DWRCSAccess.log artifact

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2025/01/31/9839/)
[Next →](https://www.hexacorn.com/blog/2025/02/21/the-rapidly-changing-geopolitics-and-its-inevitable-effect-on-cyber/)

# DWRCSAccess.log artifact

Posted on [2025-02-05](https://www.hexacorn.com/blog/2025/02/05/dwrcsaccess-log-artifact/ "11:29 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I learned about DameWare’s *DWRCSAccess.log* log file from this [blog post](https://rt-solar.ru/solar-4rays/blog/5202/). Then, when I searched this file name on Google I only got a very small number of [results](https://www.google.com/search?q="DWRCSAccess.log"). Obviously, it immediately piqued my interest and I decided to describe the content of the file here.

The content of this file is just a plain text, with parts of it often localized, and it looks like it contains the info about subsequent logging in events that are appended to the log file.

The parts that are localized are language-specific ‘messages’ that describe the reason why the metadata has been logged in a first place, and includes entries like these:

* The following user has connected via remote control.
* The following user has disconnected from remote control.
* Disconnected due to a time-out while waiting for a response for a shared session request.
  Server closed the connection.
* Authentication Failed: Using Smart Card Logon. Please check previous event log entries for possible cause.
* Authentication Failed: Using Encrypted Windows Logon.
* Der folgende Benutzer ist durch Fernzugriff verbunden. (The following user is connected remotely.)
* Die Anmeldeerlaubnis wurde Ihnen nicht erteilt. Benutzer getrennt. (You have not been granted permission to log in. User disconnected.)
* etc.

Then comes the actual metadata, which seems to be always stored in English and usually includes a set of the following, mostly self-explanatory fields:

```
Date:
Computer Name:
User ID:
Logon As ID:
Domain:
Desktop User ID:
Desktop Name:
System Settings Using:
Desktop State:
Permission Required:
Access Approved By:
Access Declined By:
Access Request Timeout:
Access Request Disconnected:
OS Product ID:
OS Registered Owner:
OS Registered Organization:
Host Name from Peer:
IP Address(es) from Peer:
Peer Host Name:
Peer IP Address:
Protocol Version - DWRCC.EXE:
Protocol Version - DWRCS.EXE:
Product Version - DWRCS.EXE:
Product Version - DWRCC.EXE:
Proxy Host Used:
Proxy Host:
Proxy Destination Host:
Proxy Destination Port:
Proxy Callback Port:
Authentication Type:
Last Error Code:
Last Error Code (WSA):
Host Port Number:
Host IP Address:
Host Name:
Absolute timeout setting:
Connect/Logon timeout setting:
Access Check:
Registered:
WTS Session:
Used RSA Public-Key Key Exchange (1024 bit keys).
Encryption IDs:
Hashing IDs:
Used Shared Secret:
Registration:
```

Some of these may be containing a crucial information about the attackers that may not be present anywhere else.

This entry was posted in [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/), [New Forensic Artifacts](https://www.hexacorn.com/blog/category/new-forensic-artifacts/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/02/05/dwrcsaccess-log-artifact/ "Permalink to DWRCSAccess.log artifact").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")