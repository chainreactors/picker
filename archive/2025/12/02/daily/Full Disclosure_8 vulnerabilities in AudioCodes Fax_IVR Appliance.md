---
title: 8 vulnerabilities in AudioCodes Fax/IVR Appliance
url: https://seclists.org/fulldisclosure/2025/Dec/3
source: Full Disclosure
date: 2025-12-02
fetch_date: 2025-12-03T03:17:16.512764
---

# 8 vulnerabilities in AudioCodes Fax/IVR Appliance

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# 8 vulnerabilities in AudioCodes Fax/IVR Appliance

---

*From*: Pierre Kim <pierre.kim.sec () gmail com>
*Date*: Thu, 20 Nov 2025 07:10:53 -0500

---

```
Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "8 vulnerabilities in AudioCodes Fax/IVR Appliance"
is posted here:

https://pierrekim.github.io/blog/2025-11-20-audiocodes-fax-ivr-8-vulnerabilities.html

The text version is also posted here:
  https://pierrekim.github.io/advisories/2025-audiocodes-fax-ivr.txt

Best regards,

=== text-version of the advisory  ===

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

## Advisory Information

Title: 8 vulnerabilities in AudioCodes Fax/IVR Appliance
Advisory URL: https://pierrekim.github.io/advisories/2025-audiocodes-fax-ivr.txt
Blog URL: https://pierrekim.github.io/blog/2025-11-20-audiocodes-fax-ivr-8-vulnerabilities.html
Date published: 2025-11-20
Vendors contacted: Audiocodes
Release mode: Released
CVE: CVE-2025-34328, CVE-2025-34329, CVE-2025-34330, CVE-2025-34331,
CVE-2025-34332, CVE-2025-34333, CVE-2025-34334, CVE-2025-34335

## Product description
```

> ```
> AudioCodes' Fax Server (Fax to Mail and Mail to Fax) application is a powerful and flexible software
> application used to manage inbound fax calls and outbound mail-to-fax calls, delivering them
> efficiently to their correct destination.
>
> From https://www.audiocodes.com/media/14442/fax-server-and-auto-attendant-ivr-administrators-guide-ver-26x.pdf
> ```

```
## Vulnerabilities Summary

Vulnerable versions: all versions.

The summary of the vulnerabilities is:

1. CVE-2025-34328 - Pre-authenticated Remote Code Execution #1
2. CVE-2025-34329 - Pre-authenticated Remote Code Execution #2
3. CVE-2025-34330 - Pre-authenticated File upload vulnerability
4. CVE-2025-34331 - Pre-authenticated File read
5. CVE-2025-34332 - Local Privilege Escalation #1
6. CVE-2025-34333 - Local Privilege Escalation #2
7. CVE-2025-34334 - Post-authenticated Command Injection and Local
Privilege Escalation
8. CVE-2025-34335 - Post-authenticated Command Injection

_Miscellaneous notes_:

The critical vulnerabilities have been confirmed to be present in the
latest public version.

Other vulnerabilities I have also identified require authentication,
therefore the security risk is considered low to medium:

- - An attacker with admin privileges in the web interface can execute
commands as `NT AUTHORITY\SYSTEM` in several ways;
- - An attacker with a local account on the server will very quickly
gain `NT AUTHORITY\SYSTEM` privileges, as file and directory
permissions are insecure everywhere.

Vulnerabilities #1, #2 #3 and #4 were shared with Audiocodes PSIRT but
communication was almost nonexistent (see Report Timeline): AudioCodes
PSIRT never provided any information or feedback, even with my regular
follow-up emails. I also believe that this solution is EOL since
December 31, 2024.

Vulnerabilities #5, #7 and #8 were discovered during an audit of an
"unsupported" version of the AudioCodes Fax/IVR Appliance that was
incorrectly patched. New unsupported versions were found in the vendor
AWS S3 bucket that allows directory listing
(https://downloads-audiocodes.s3.eu-central-1.amazonaws.com/) - this
bucket is used by the vendor to distribute some of its solutions.
Surprisingly, the root causes were not addressed and the
vulnerabilities #1 through #4 were still present. Vulnerability #6 was
simply discovered during the creation of this security advisory to
illustrate insecure permissions.

I didn't spend much time analyzing this solution (installation took 10
minutes and the first pre-auth RCE was found in about 5 minutes), but
the existing PHP code presents a considerable attack surface.

Regarding the security status of this product, it is also quite
surprising to find no public CVEs. I assume this solution has never
been audited.

Unfortunately, the vendor has not followed their official security
vulnerability handling. AudioCode's PSIRT team has not responded, and
security advisories have not been published.

Additionally, It is also worth noting that Audiocodes Session Border
Controllers (SBCs) were quietly patched in 2024 to address the
misfortune cookie vulnerability (CVE-2014-9222). This exploit was
tested on the Median Virtual Edition and Mediant 800 SBCs.

    kali% curl -kv --header 'Cookie: C1012213=1' https:///192.168.0.2/
    -> /acBin/TPApp will segfault in the remote appliance/ARM device

- - firmware sbc-F7.40A.005.619 is vulnerable.
- - firmware sbc-F7.40A.500.781 is not vulnerable.

No security bulletins were found regarding this silently patched
vulnerability and it is recommended to use the latest firmware version
of Audiocodes Session Border Controllers.

_Impacts_

An attacker can compromise AudioCodes Fax/IVR Appliance without
authentication and move laterally in the telecom and IT
infrastructure.

An attacker can compromise outdated AudioCodes Session Border
Controllers with the misfortune cookie vulnerability.

_Recommendations_

Do not use AudioCodes Fax/IVR Appliance.

Do not expose the AudioCodes Fax/IVR Appliance to the network.

Use secure permissions.

Remove vulnerable webpages.

Update Audiocodes Session Border Controllers.

## Identification of the solution

The latest solution (AudioCodes Fax/IVR Appliance Installer, Version
2.6.230.000) can be found at:

- - https://downloads-audiocodes.s3.eu-central-1.amazonaws.com/Download/AC_FAX_IVR_IW.html
- - https://downloads-audiocodes.s3.eu-central-1.amazonaws.com/Fax_IVR/FaxAtt_Setup_2.6.230.000.zip

[please use the HTML version at
https://pierrekim.github.io/blog/2025-11-20-audiocodes-fax-ivr-8-vulnerabilities.html]

## Details - Pre-authenticated Remote Code Execution #1

The vulnerability is located in the
`C:\F2MAdmin\F2E\AudioCodes_files\utils\IVR\diagram\ajaxScript.php`
PHP file. This file allows an attacker to upload files without
authentication.

Content of `C:\F2MAdmin\F2E\AudioCodes_files\utils\IVR\diagram\ajaxScript.php`:

[code:php]
  1 <?php
  2 $dir  = dirname(dirname(__FILE__));
  3 require_once $dir.'/classes/SystemStatus.class.php';
  4
  5 //$scriptName = $_REQUEST['scriptName'];
  6 $action = isset($_REQUEST["action"]) ? $_REQUEST["action"] : "";
  7
  8 if(!empty($action)){
  9         if($action == 'getScripts'){
[...]
 26         }
 27         else if($action == 'saveScript'){
 28                 $scriptValue = $_POST['value']; // [1] -
attacker-controlled value
 29                 $scriptName = $_POST['name'];   // [2] -
attacker-controlled value
 30
 31                 $systemStatus = new SystemStatus();
 32                 $sysInfo = $systemStatus->GetSysInfo();
 33                 $path = $sysInfo[SystemStatus::SCRIPTS_DIR];
 34
 35                 $ok = 'false';
 36                 $ok = file_put_contents($path."/".$scriptName,
$scriptValue); // [3] - insecure file write with attacker-controlled
values
 37                 if($ok === true){
 38                         $ok = 'true';
 39                 }
 40                 ob_clean();
 41                 echo ($ok);
 42                 die;
 43         }
 44 }
[/code]

As shown in the source code, there is no authentication.

Without authentication, a remote attacker can acce...