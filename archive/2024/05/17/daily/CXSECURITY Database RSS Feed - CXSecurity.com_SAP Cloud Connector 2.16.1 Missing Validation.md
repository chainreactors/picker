---
title: SAP Cloud Connector 2.16.1 Missing Validation
url: https://cxsecurity.com/issue/WLB-2024050047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-17
fetch_date: 2025-10-06T17:13:41.076719
---

# SAP Cloud Connector 2.16.1 Missing Validation

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
|  |  | |  | | --- | | **SAP Cloud Connector 2.16.1 Missing Validation** **2024.05.16**  Credit:  **[Mingshuo Li](https://cxsecurity.com/author/Mingshuo%2BLi/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-25642](https://cxsecurity.com/cveshow/CVE-2024-25642/ "Click to see CVE-2024-25642")**  CWE: **[CWE-295](https://cxsecurity.com/cwe/CWE-295 "CWE-295")** | |

SEC Consult Vulnerability Lab Security Advisory < 20240513-0 >
=======================================================================
title: Tolerating Self-Signed Certificates
product: SAP® Cloud Connector
vulnerable version: 2.15.0 - 2.16.1 (Portable and Installer)
fixed version: 2.16.2 (Portable and Installer)
CVE number: CVE-2024-25642
impact: high
homepage: https://www.sap.com/about.html
found: 2023-11-13
by: Mingshuo Li (Office Munich)
Fabian Hagg
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"The Cloud Connector is an optional on-premise component that is needed to
integrate on-demand applications with customer backend services and is the
counterpart of SAP Connectivity service."
Source: https://tools.hana.ondemand.com/#cloud
Business recommendation:
------------------------
SEC Consult recommends to implement the security note 3424610, where the
documented issue is fixed in version 2.16.2 according to the vendor. We
advise installing the correction as a matter of priority to keep
business-critical data secured.
Source: https://support.sap.com/en/my-support/knowledge-base/security-notes-news/february-2024.html
Vulnerability overview/description:
-----------------------------------
1) Tolerating Self-Signed Certificates (CVE-2024-25642)
As per vendor documentation, the authentication between SCC and SAP BTP is guaranteed
mutually:
"The tunnel itself is using TLS with strong encryption of the communication,
and mutual authentication of both communication sides, the client side
(Cloud Connector) and the server side (SAP BTP)."
Source: https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/inbound-connectivity#tls-tunnel
It was however discovered that the SCC trusts self-signed X.509 server certificates
for transport security to establish outbound connections with cloud-related
endpoints. Thus, an attacker can impersonate the genuine servers to interact
with the SCC, hence breaking the mutual authentication promise. Our analysis shows
furthermore that the product does not implement Certificate Pinning for the
trusted endpoints.
The security impact of this vulnerability is rated high due to the trust put
into self-signed certificates, SCC is unable to distinguish between genuine and
malicious SAP BTP endpoints, rendering trivial adversary-in-the-middle attacks
possible.
Proof of concept:
-----------------
1) Tolerating Self-Signed Certificates (CVE-2024-25642)
A "tunnel" established between a subaccount of SAP BTP and SCC represents a
long-lived bi-directional WebSocket over TLS customized by the vendor.
Such a tunnel is initiated by the SCC, known as reverse invoke approach,
to give the administrator full control of the tunnel.
Two tunnels established by SCC are protected by TLS with respect to encrypted
communication. However, SCC does not verify the authenticity of the
certification authority, hence allowing an attacker to impersonate the target
server, using self-signed certificates.
In particular, the attack is targeted at the following two endpoints, but not
limited to the region host us10.
- connectivitynotification.cf.us10.hana.ondemand.com
- connectivity.us10.trial.applicationstudio.cloud.sap
Note that the following endpoint, which is used for the initial certificate
signing request by SCC and to receive the BTP subaccount credentials, is
not susceptible to this issue.
- connectivitycertsigning.cf.us10.hana.ondemand.com
Nonetheless, it suffices to silently eavesdrop and manipulate network traffic
between SCC and SAP BTP by impersonating the two vulnerable endpoints above.
Without loss of generality, the first endpoint is taken as example to
demonstrate the issue by the following steps:
1. Add an entry in /etc/hosts of the SCC host as below to resolve the host name
to an attacker-controlled IP address:
192.168.1.100 connectivitynotification.cf.us10.hana.ondemand.com
2. Generate a self-signed certificate with the spoofed hostname as common name
```
$ openssl req -x509 -newkey rsa:4096 -keyout conn-noti-key.pem -out conn-noti-cert.pem -sha256 -days 3650 -nodes -subj "/C=DE/ST=Baden-Wuerttemberg/L=Walldorf/O=SAP
SE/OU=ITSecurity/CN=connectivitynotification.cf.us10.hana.ondemand.com"
```
3. Start an HTTPS server on the attacker machine to receive the connection from
SCC, using the self-signed certificate created in step 2
The following Python script can be used to start the HTTPS server:
```
$ cat https-dummy-server.py
import http.server
import ssl
server\_address = ("192.168.1.100", 443)
httpd = http.server.HTTPServer(server\_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap\_socket(httpd.socket,
server\_side=True,
certfile="self-signed-cert/conn-noti-cert.pem",
keyfile="self-signed-cert/conn-noti-key.pem",
ssl\_version=ssl.PROTOCOL\_TLS)
httpd.serve\_forever()
```
4. Connect to a subaccount of BTP, for example US East AWS, in the SCC
Administration UI
As soon as the connection is launched, the dummy web server will receive the
request as shown below:
```
$ python3 https-dummy-server.py
192.168.1.200 - - [10/Nov/2023 12:00:00] "GET /connectivity HTTP/1.1" 200 -
```
This observation confirms that the TLS connection between SCC and the spoofed
BTP endpoint operated on the attacker's machine has been successfully established
although the server presented a self-signed certificate. No security warning
message is being displayed in the Administration UI, making the attack
surreptitious.
Vulnerable / tested versions:
-----------------------------
The following versions have been tested which were the...