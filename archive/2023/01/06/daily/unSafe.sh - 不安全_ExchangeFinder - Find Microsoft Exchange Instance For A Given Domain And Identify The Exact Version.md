---
title: ExchangeFinder - Find Microsoft Exchange Instance For A Given Domain And Identify The Exact Version
url: https://buaq.net/go-144313.html
source: unSafe.sh - 不安全
date: 2023-01-06
fetch_date: 2025-10-04T03:08:29.780272
---

# ExchangeFinder - Find Microsoft Exchange Instance For A Given Domain And Identify The Exact Version

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d3e28196ffe49c07e8f600a93467b234.jpg)

ExchangeFinder - Find Microsoft Exchange Instance For A Given Domain And Identify The Exact Version

ExchangeFinder is a simple and open-source tool that tries to find Micrsoft Exchange instanc
*2023-1-5 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-144313.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjwTlxzmChj02jbrRrLZSN2OCZeKgaPfY-4Sh4wxXk8phBwQMOIIVRH-ORJXQ5Kw4bWLYSbvcddqPxDqu-ZC05yoExNpsd2LBdubun47H-BcfNHggtDRpG2qC4BBT_LzJXoq5dGiSfBXmPIPag0n_k-aVdon6Yk0JCOWa0cstOz35Anx-lDauBbzAzJNA=w640-h284)](https://blogger.googleusercontent.com/img/a/AVvXsEjwTlxzmChj02jbrRrLZSN2OCZeKgaPfY-4Sh4wxXk8phBwQMOIIVRH-ORJXQ5Kw4bWLYSbvcddqPxDqu-ZC05yoExNpsd2LBdubun47H-BcfNHggtDRpG2qC4BBT_LzJXoq5dGiSfBXmPIPag0n_k-aVdon6Yk0JCOWa0cstOz35Anx-lDauBbzAzJNA)

ExchangeFinder is a simple and open-source tool that tries to find Micrsoft Exchange instance for a given domain based on the top common DNS names for [Microsoft](https://www.kitploit.com/search/label/Microsoft "Microsoft") Exchange.

ExchangeFinder can identify the exact version of Microsoft Exchange starting from `Microsoft Exchange 4.0` to `Microsoft Exchange Server 2019`.

ExchangeFinder will first try to resolve any [subdomain](https://www.kitploit.com/search/label/Subdomain "subdomain") that is commonly used for Exchange server, then it will send a couple of HTTP requests to parse the content of the response sent by the server to identify if it's using Microsoft Exchange or not.

Currently, the tool has a signature of every version from Microsoft Exchange starting from `Microsoft Exchange 4.0` to `Microsoft Exchange Server 2019`, and based on the build version sent by Exchange via the header `X-OWA-Version` we can identify the exact version.

If the tool found a [valid](https://www.kitploit.com/search/label/Valid "valid") Microsoft Exchange instance, it will return the following results:

* Domain name.
* Microsoft Exchange version.
* Login page.
* Web server version.

Clone the latest version of `ExchangeFinder` using the following command:

`git clone https://github.com/mhaskar/ExchangeFinder`

And then install all the [requirements](https://www.kitploit.com/search/label/Requirements "requirements") using the command `poetry install`.

```
┌──(kali㉿kali)-[~/Desktop/ExchangeFinder]
```

```
┌──(kali㉿kali)-[~/Desktop/ExchangeFinder]
└─$ python3 exchangefinder.py

______     __                           _______           __
   / ____/  __/ /_  ____ _____  ____ ____  / ____(_)___  ____/ /__  _____
  / __/ | |/_/ __ \/ __ `/ __ \/ __ `/ _ \/ /_  / / __ \/ __  / _ \/ ___/
 / /____>  </ / / / /_/ / / / / /_/ /  __/ __/ / / / / / /_/ /  __/ /
/_____/_/|_/_/ /_/\__,_/_/ /_/\__, /\___/_/   /_/_/ /_/\__,_/\___/_/
                             /____/

Find that Microsoft Exchange server ..

[-] Please use --domain or --domains option

┌──(kali&#129   27;kali)-[~/Desktop/ExchangeFinder]
└─$
```

You can use the option `-h` to show the help banner:

Scan single domain

To scan single domain you can use the option `--domain` like the following:

```
askar•/opt/redteaming/ExchangeFinder(main⚡)» python3 exchangefinder.py --domain dummyexchangetarget.com

______     __                           _______           __
   / ____/  __/ /_  ____ _____  ____ ____  / ____(_)___  ____/ /__  _____
  / __/ | |/_/ __ \/ __ `/ __ \/ __ `/ _ \/ /_  / / __ \/ __  / _ \/ ___/
 / /____>  </ / / / /_/ / / / / /_/ /  __/ __/ / / / / / /_/ /  __/ /
/_____/_/|_/_/ /_/\__,_/_/ /_/\__, /\___/_/   /_/_/ /_/\__,_/\___/_/
                             /____/

Find that Microsoft Exchange server ..

[!] Scanning domain dummyexch   angetarget.com
	[+] The following MX records found for the main domain
	10 mx01.dummyexchangetarget.com.

[!] 	Scanning host (mail.dummyexchangetarget.com)
[+] 	IIS server detected (https://mail.dummyexchangetarget.com)
[!] 	Potential Microsoft Exchange Identified
[+] 	Microsoft Exchange identified with the following details:

Domain Found : https://mail.dummyexchangetarget.com
	Exchange version : Exchange Server 2016 CU22 Nov21SU
	Login page : https://mail.dummyexchangetarget.com/owa/auth/logon.aspx?url=https%3a%2f%2fmail.dummyexchangetarget.com%2fowa%2f&reason=0
	IIS/Webserver version: Microsoft-IIS/10.0

[!] 	Scanning host (autodiscover.dummyexchangetarget.com)
[+] 	IIS server detected (https://autodiscover.dummyexchangetarget.com)
[!] 	Potential Microsoft Exchange Identified
[+] 	Microsoft Exchange identified with the following details:

Domain Found : https://autodiscover.dummyexchangetarget.com	Exchange version : Exchange Server 2016 CU22 Nov21SU
	Login page : https://autodiscover.dummyexchangetarget.com/owa/auth/logon.aspx?url=https%3a%2f%2fautodiscover.dummyexchangetarget.com%2fowa%2f&reason=0
	IIS/Webserver version: Microsoft-IIS/10.0

askar•/opt/redteaming/ExchangeFinder(main⚡)»
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjwTlxzmChj02jbrRrLZSN2OCZeKgaPfY-4Sh4wxXk8phBwQMOIIVRH-ORJXQ5Kw4bWLYSbvcddqPxDqu-ZC05yoExNpsd2LBdubun47H-BcfNHggtDRpG2qC4BBT_LzJXoq5dGiSfBXmPIPag0n_k-aVdon6Yk0JCOWa0cstOz35Anx-lDauBbzAzJNA=w640-h284)](https://blogger.googleusercontent.com/img/a/AVvXsEjwTlxzmChj02jbrRrLZSN2OCZeKgaPfY-4Sh4wxXk8phBwQMOIIVRH-ORJXQ5Kw4bWLYSbvcddqPxDqu-ZC05yoExNpsd2LBdubun47H-BcfNHggtDRpG2qC4BBT_LzJXoq5dGiSfBXmPIPag0n_k-aVdon6Yk0JCOWa0cstOz35Anx-lDauBbzAzJNA)

### Scan multiple domains

To scan multiple domains (targets) you can use the option `--domains` and choose a file like the following:

```
askar•/opt/redteaming/ExchangeFinder(main⚡)» python3 exchangefinder.py --domains domains.txt

______     __                           _______           __
   / ____/  __/ /_  ____ _____  ____ ____  / ____(_)___  ____/ /__  _____
  / __/ | |/_/ __ \/ __ `/ __ \/ __ `/ _ \/ /_  / / __ \/ __  / _ \/ ___/
 / /____>  </ / / / /_/ / / / / /_/ /  __/ __/ / / / / / /_/ /  __/ /
/_____/_/|_/_/ /_/\__,_/_/ /_/\__, /\___/_/   /_/_/ /_/\__,_/\___/_/
                             /____/

Find that Microsoft Exchange server ..

[+] Total domains to scan are 2 domains
[!] Scanning domain externalcompany.com
	[+] The following MX records f   ound for the main domain
	20 mx4.linfosyshosting.nl.
	10 mx3.linfosyshosting.nl.

[!] 	Scanning host (mail.externalcompany.com)
[+] 	IIS server detected (https://mail.externalcompany.com)
[!] 	Potential Microsoft Exchange Identified
[+] 	Microsoft Exchange identified with the following details:

Domain Found : https://mail.externalcompany.com
	Exchange version : Exchange Server 2016 CU22 Nov21SU
	Login page : https://mail.externalcompany.com/owa/auth/logon.aspx?url=https%3a%2f%2fmail.externalcompany.com%2fowa%2f&reason=0
	IIS/Webserver version: Microsoft-IIS/10.0

[!] Scanning domain o365.cloud
	[+] The following MX records found for the main domain
	10 mailstore1.secureserver.net.
	0 smtp.secureserver.net.

[!] 	Scanning host (mail.o365.cloud)
[+] 	IIS server detected (https://mail.o365.cloud)
[!] 	Potential Microsoft Exchange Identified
[+] 	Microsoft Exchange identified with the following    details:

Domain Found : https://mail.o365.cloud
	Exchange version : Exchange Server 2013 CU23 May22SU
	Login page : https://mail.o365.cloud/owa/auth/logon.aspx?url=https%3a%2f%2fmail.o365.cloud%2fowa%2f&reason=0
	IIS/Webserver version: Microsoft-IIS/8.5

askar•/opt/redteaming/ExchangeFinder(main⚡)»
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhR8WFYUgTreyfxL0rY3YTW0FNdGyOI2MzhRrq9OVryDkqh-TYkED5bEhmfPiYLe460FLo3moRYtcoYz75-zXw7ro654MxVwxfg4emhsizc7t-_yhFUBkcgpSKFiZmlpFPc1u_MqPBUe4xa8sG_Jq2WMt4DXMWwMzqk9GbZ0hkpCOm-p7Pot8uShAyPbw=w640-h382)](h...