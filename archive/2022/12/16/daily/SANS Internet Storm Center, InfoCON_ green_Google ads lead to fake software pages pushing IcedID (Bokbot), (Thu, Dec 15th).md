---
title: Google ads lead to fake software pages pushing IcedID (Bokbot), (Thu, Dec 15th)
url: https://isc.sans.edu/diary/rss/29344
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-16
fetch_date: 2025-10-04T01:42:06.108489
---

# Google ads lead to fake software pages pushing IcedID (Bokbot), (Thu, Dec 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29338)
* [next](/diary/29350)

# [Google ads lead to fake software pages pushing IcedID (Bokbot)](/forums/diary/Google%2Bads%2Blead%2Bto%2Bfake%2Bsoftware%2Bpages%2Bpushing%2BIcedID%2BBokbot/29344/)

**Published**: 2022-12-15. **Last Updated**: 2022-12-15 09:07:35 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/Google%2Bads%2Blead%2Bto%2Bfake%2Bsoftware%2Bpages%2Bpushing%2BIcedID%2BBokbot/29344/#comments)

Introduction

Fake sites for popular software have occasionally been used by cyber criminal groups to push malware.  Campaigns pushing IcedID malware (also known as Bokbot) also [use this method](https://www.binarydefense.com/threat_watch/icedid-malware-distributed-from-fake-zoom-installation-website/) as a distribution technique (we also commonly see IcedID sent through email).

This week, a new round of reports appeared about Google Ads leading to a new sites pushing IcedID.

* [https://infosec.exchange/@bencrypted/109508166164779496](https://infosec.exchange/%40bencrypted/109508166164779496)
* [https://infosec.exchange/@th3\_protoCOL/109513090531163473](https://infosec.exchange/%40th3_protoCOL/109513090531163473)

Based on these reports, on Wednesday 2022-12-14, I fired up my lab environment and did a Google search for AnyDesk and got a Google ad as my top result.  Although the Google ad showed a legitimate AnyDesk URL, it led to a fake site after I clicked the ad.

Today's diary reviews my IcedID infection from this fake AnyDesk site.

***Details***

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-01.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-01.jpg)
*Shown above:  Search results when I did a quick Google search for AnyDesk.*

Search Engine Optimization (SEO) is a technique that websites use to increase their visibility for search engines like Google.  Cyber criminals occasionally use SEO to direct search traffic to malicious advertisement links.  These ads redirect users to fake software sites based on specific search terms.  I've heard this technique referred to as "SEO poisoning."

The above image shows the top search results after I typed ***anydesk*** into Google search.  The top result is a Google ad for AnyDesk, which shows a legitimate URL for the official AnyDesk site.

I clicked on the ad, and it generated the following Google Ad Services URL:

hxxps://www.googleadservices[.]com/pagead/aclk?sa=L&ai=DChcSEwjh1bP\_3\_n7AhXbFdQBHdF9AqwYABAAGgJvYQ&ohost=www.google.com&cid=CAASJeRovgWCSOUdKVM\_De2wE7MnzlxJnzH8vREdVT\_40LhQhbz-Lks&sig=AOD64\_3NZNQWkb8O\_B18hKIs9Q3klfDfBw&q&adurl&ved=2ahUKEwjHl6v\_3\_n7AhVrkmoFHdIpAG4Q0Qx6BAgDEAE&nis=8

That generated the following URL:

hxxps://clickserve.dartsearch[.]net/link/click?&ds\_dest\_url=https://oferialerkal[.]online/81HqPxz2?https://anydesk.com/en/features/unattended-access&id=4&gclid=EAIaIQobChMI4dWz\_9\_5-wIV2xXUAR3RfQKsEAAYASAAEgLqA\_D\_BwE

This led to a URL from a malicious traffic distribution system (TDS) domain ***oferialerkal[.]online***.  These malicious TDS domains frequenty change multiple times each day.  The above URL generated HTTPS traffic to ***oferialerkal[.]online***, which then led to the following fake AnyDesk URL:

hxxps://wwwanydesk[.]top/en/downloads/windows

This is a fake AnyDesk page, with a button to download a malicious zip archive hosted on a Google Firebase Storage URL at:

hxxps://firebasestorage.googleapis[.]com/v0/b/our-audio-370812.appspot.com/o/wnitFn4RCG%2FSetup\_Win\_14-12-2022\_18-36-29.zip?alt=media&token=3ef517f1-eb72-46bc-ac4b-3fb41f92d373

As I wrote this diary, the above URL still worked, and it delivered a the malicious zip archive.

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-02.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-02.jpg)
*Shown above:  Fake AnyDesk site delivering the malicious zip archive.*

The zip archive contained a Microsoft Installer (.msi) file.  Double-clicking the .msi file on a vulnerable Windows host caused it to drop and run a DLL to install IcedID on the victim's system.

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-03.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-03.jpg)
*Shown above:  Downloaded zip archive and extracted .msi file.*

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-04.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-04.jpg)
*Shown above:  The installer DLL for IcedID.*

***Traffic from the infected Windows host***

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-05.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-05.jpg)
*Shown above:  Traffic from the infection filtered in Wireshark, part 1.*

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-06.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-06.jpg)
*Shown above:  Traffic from the infection filtered in Wireshark, part 2.*

[![](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-07.jpg)](https://isc.sans.edu/diaryimages/images/2022-12-15-ISC-diary-image-07.jpg)
*Shown above:  Traffic from the infection filtered in Wireshark, part 3.*

***Indicators of Compromise***

Traffic generated by IcedID installer DLL for gzip binary:

* 143.198.92[.]88 port 80 - klepdrafooip[.]com - GET / HTTP/1.1

IcedID post-infection C2 traffic:

* 94.140.114[.]40 port 443 - primsenetwolk[.]com - HTTPS traffic
* 94.140.114[.]40 port 443 - onyxinnov[.]lol - HTTPS traffic
* 158.255.211[.]126 port 443 - trashast[.]wiki - HTTPS traffic

IcedID backchannel traffic with VNC:

* 51.195.169[.]87 port 8080

First Cobalt Strike:

* 176.105.202[.]212 port 80 - 176.105.202[.]212 - GET /adcs4
* 172.67.130[.]194 port 443 - kingoflake[.]com - HTTPS traffic

Second Cobalt Strike:

* 199.127.62[.]132 port 80 - 199.127.62[.]132 - GET /download/h.exe
* 108.177.235[.]187 port 443 - bukifide[.]com - HTTPS traffic

Sliver and/or DonutLoader:

* 190.61.121[.]35 port 443 - 190.61.121[.]35:443 - GET /static/ZillaSlab-Bold.subset.e96c15f68c68.woff/CEx6\_0FDJn4RWxBZcsquwwUk57-n7pCuR5k24zUnBepPlxY9gqn968ZXnXAtC2GwTONSpEx3Pnz\_lvqz2c2E5B\_7n2lMU3wZ7Yeqb9yK9OFsqEQnybJ3THr\_uiJpi3X5yQI3puCyecatd8A8KWDsL6euQz1J\_U-MxD8EcfWPoPWF8lqYiHLRDP1rKGIpBbW
* 46.4.182[.]102 port 80 - post-infection TLSv1.3 HTTPS traffic

Associated malware:

Downloaded zip and extracted .msi file:

SHA256 hash: [19265aac471f7d72fcddb133e652e04c03a547727b6f98a80760dcbf43f95627](https://www.virustotal.com/gui/file/19265aac471f7d72fcddb133e652e04c03a547727b6f98a80760dcbf43f95627)
File size: 1,108,416 bytes
File name: Setup\_Win\_14-12-2022\_18-36-29.zip

SHA256 hash: [63a7d98369925d6e98994cdb5937bd896506665be9f80dc55de7eb6df00f7607](https://www.virustotal.com/gui/file/63a7d98369925d6e98994cdb5937bd896506665be9f80dc55de7eb6df00f7607)
File size: 1,966,080 bytes
File name: Setup\_Win\_14-12-2022\_18-36-29.msi

IcedID files from an infected Windows host:

SHA256 hash: [7e5da5fcda0da494da85cdc76384b3b08f135f09f20e582e049486e8ae2f168e](https://www.virustotal.com/gui/file/7e5da5fcda0da494da85cdc76384b3b08f135f09f20e582e049486e8ae2f168e)
File size: 1,503,408 bytes
File location: C:\Users\[username]\AppData\Local\MSI5da0ddad.mst
File description: 64-bit DLL to install IcedID dropped by above .msi file
Run method: rundll32.exe [filename],init

SHA256 hash: [53639070024366d23c3de5ba1d074cbd1d8b9e78d46f75c32ef02fc20c279fc3](https://www.virustotal.com/gui/file/53639070024366d23c3de5ba1d074cbd1d8b9e78d46f75c32ef02fc20c279fc3)
File size: 1,503,408 bytes
File location: hxxp://klepdrafooip[.]com/
File description: gzip binary from klepdrafooip[.]com retrieved by IcedID ins...