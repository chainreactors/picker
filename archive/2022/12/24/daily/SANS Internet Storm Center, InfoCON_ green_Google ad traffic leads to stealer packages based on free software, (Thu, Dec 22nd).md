---
title: Google ad traffic leads to stealer packages based on free software, (Thu, Dec 22nd)
url: https://isc.sans.edu/diary/rss/29376
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-24
fetch_date: 2025-10-04T02:27:11.082483
---

# Google ad traffic leads to stealer packages based on free software, (Thu, Dec 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29374)
* [next](/diary/29380)

# [Google ad traffic leads to stealer packages based on free software](/forums/diary/Google%2Bad%2Btraffic%2Bleads%2Bto%2Bstealer%2Bpackages%2Bbased%2Bon%2Bfree%2Bsoftware/29376/)

**Published**: 2022-12-22. **Last Updated**: 2022-12-23 01:22:31 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[2 comment(s)](/diary/Google%2Bad%2Btraffic%2Bleads%2Bto%2Bstealer%2Bpackages%2Bbased%2Bon%2Bfree%2Bsoftware/29376/#comments)

***Introduction***

Earlier this month, I wrote a diary about [Google ad traffic leading to a fake AnyDesk page pushing IcedID malware](https://isc.sans.edu/diary/Google%2Bads%2Blead%2Bto%2Bfake%2Bsoftware%2Bpages%2Bpushing%2BIcedID%2BBokbot/29344/).  This week, the same type of ad traffic led to a fake TeamViewer page, and that page led to a different type of malware.  This week's infection involved a downloaded JavaScript (.js) file that led to Microsoft Installer packages (.msi files) containing other script that used free or open source programs.

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-01a.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-01.jpg)
*Shown above:  Flow of events from this infection chain.*

***Screenshots***

The following screenshots show a Google ad that led to the fake TeamViewer page.

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-02a.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-02b.jpg)
*Shown above:  Google ad that led to the fake TeamViewer page.*

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-03a.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-03b.jpg)
*Shown above:  Fake TeamViewer page provided a file named TeamViewer\_Setup.js.*

***Malicious ad traffic***

I recorded a packet capture (pcap) of the first run and used Google Cache Viewer to review the ad traffic from the Microsoft Edge browser cache.  However, data from the cache wasn't complete, so I recorded a second run using Telerik's Fiddler web debugging proxy tool.

I saved the Fiddler capture as a Session Archive Zip (.saz) file.  Examining the .saz file revealed the following Google Ad Services link:

* hxxps://www.googleadservices[.]com/pagead/aclk?sa=L&ai=DChcSEwi2nIKZuov8AhXnFtQBHYYZDcEYABAAGgJvYQ&ohost=www.google.com&cid=CAASJeRoMovfTxtBzHVlsj0LXMX3F-ME0fI0r0BXStL36GjWm1sw6Zk&sig=AOD64\_0nIv13ujTO6VuQgTMAQZ0H83315A&q&adurl&ved=2ahUKEwi3ivuYuov8AhVulWoFHZJGBuAQ0Qx6BAgJEAE&nis=8 HTTP/1.1

The above URL returned a ***HTTP/1.1 302 Found***, with a location of:

* hxxps://clickserve.dartsearch[.]net/link/click?&ds\_dest\_url=hxxps://baherlakerl[.]online/z7ND1tqY?https://status.teamviewer.com/&id=4&gclid=EAIaIQobChMItpyCmbqL\_AIV5xbUAR2GGQ3BEAAYASAAEgKMW\_D\_BwE

That ***clickserve.dartsearch.net*** URL redirected to a malicious URL from ***baherlaker[.]online.com***.  The ***baherlaker[.]online.com*** URL redirected to a fake TeamViewer page hosted on a compromised server at ***dogotungtam[.]com***.

The "Download Now" buttons on the fake TeamViewer page retrieved a malicious JavaScript (.js) file from the following URL:

* hxxps://coldcreekranch[.]com/z1/

The malicious ***.online*** domain changed multiple times each day.  The fake TeamViewer page and URL to download the ***.js*** file also change.  I generated the following traffic from fake TeamViewer infections this week:

Monday, 2022-12-19:

* Malicious domain for redirect traffic:  ***qweiaoer[.]online***
* Fake TeamViewer paged hosted on compromised server at:  ***hxxps://israelifrenchbulldogs[.]com/teamviewer***
* Malicious .js file hosted on compromised server at:  ***hxxps://acehphonnajaya[.]com/608E/***

Wednesday, 2022-12-21:

* Malicious domain for redirect traffic (first run):  ***ajerlakerl[.]online***
* Malicious domain for redirect traffic (second run):  ***baherlakerl[.]online***
* Fake TeamViewer paged hosted on compromised server at:  ***hxxps://dogotungtam[.]com/teamviewer***
* Malicious .js file hosted on compromised server at:  ***hxxps://coldcreekranch[.]com/z1/***

As shown above, the ***.online*** domains switched between my first and second infection runs on Wednesday.  They were approximately 3 hours apart.

***Running the downloaded .js file***

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-04.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-04.jpg)
*Shown above:  Downloaded **TeamViewer\_Setup.js** file opened in a text editor.*

Opening the downloaded file ***TeamViewer\_Setup.js*** revealed script with some slight obfuscation.  The script is designed to retrieve an ***.msi*** file from the following URL:

* hxxs://acehphonnajaya[.]com/csw/ke.msi

That URL will not return an ***.msi*** file, unless the HTTP request headers contain the following line:

* User-Agent: Windows Installer

Opening ***ke.msi*** in 7-Zip revealed the package contains a 262 byte Visual Basic Script (.vbs) named ***Terminal\_App\_Service.vbs*** as shown below.

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-14.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-14.jpg)
*Shown above:  Contents of the **ke.msi** file.*

The ***.vbs*** file was saved to ***C:\ProgramData\Cis\Terminal App Service.vbs*** and made persistent through a Windows shortcut under the Start Menu's Programs --> Startup directory.

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-12.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-12.jpg)
*Shown above:  Content of the **Terminal App Service.vbs** file.*

***Terminal App Service.vbs*** generated HTTP traffic to a Command and Control (C2) server at ***46.151.24[.]226***.

***Traffic from an infected Windows host***

HTTP GET requests to ***46.151.24[.]226*** occurred several times each minute.  Each HTTP request returned a ***404 Not Found*** until approximately 2 and 1/2 minutes later, when one of the HTTP GET requests returned a ***200 OK*** that provided another ***.msi*** package.  After receiving the ***.msi*** package, the infected host sent a screenshot of the desktop to the same C2 server at ***46.151.24[.]226***.

![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-05a.jpg)
*Shown above:  Initial traffic from the infected Windows host filtered in Wireshark.*

![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-06a.jpg)
*Shown above:  Wireshark showing a 200 OK that for the **.msi** file, and the screenshot post.*

This second ***.msi*** package contains two ***.js*** files and a Windows executable file (.exe) for [IrfanView](https://www.irfanview.com/).  IrfanView is a free graphic viewer and a legitimate program.  However, ***.js*** files in the ***.msi*** package use IrfanView to take a screenshot of the victim's desktop, and the ***.js*** script sends the image to the C2 server at ***46.151.24[.]226***.

[![](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-07a.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-23-ISC-diary-image-07.jpg)
*Shown above:  Traffic showing the **.msi** package, and 7-Zip revealing its contents.*

Approximately 6 minutes after the initial C2 traffic to ***46.151.24[.]226*** began, we see another ***200 OK***.  This returned a third .msi package used to install [AutoHotkey](https://www.autohotkey.com/).  AutoHotkey is an open-source scripting language for Windows, and it is also a legitimate program.  However, a script written to use AutoHotkey can perform malicious actions, which is the case here.  After downloading this ***.msi*** package, the infected host starts generating HTTP requests to a second C...