---
title: Bunch of IoT CVEs
url: https://seclists.org/fulldisclosure/2024/Jul/14
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:14.853376
---

# Bunch of IoT CVEs

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Bunch of IoT CVEs

---

*From*: Willem Westerhof | Secura <Willem.Westerhof () secura com>
*Date*: Fri, 26 Jul 2024 13:11:06 +0000

---

```
Hi all,

A list of CVE’s in a bunch of IoT devices that never made it to the general public through other means, but have either
been fixed, or never will be fixed, since they are a couple of years old.
```

> ```
> [Suggested description]
> An issue was discovered in Siime Eye 14.1.00000001.3.330.0.0.3.14.
> By sending a specific request to the webserver, it is possible to
> enable the telnet interface on the device. The telnet interface can
> then be used to obtain access to the device with root privileges and a
> default password. This default telnet password is the same across all
> Siime Eye devices.
> In order for the attack to be exploited, an attacker must be physically
> close in order to connect to the device's Wi-Fi access point.
>
> ------------------------------------------
>
> [Additional Information]
> The vulnerability was first discovered by Pentest Partners, later on it was also discovered by Qbit as the issues
> remain unaddressed by the vendor.
>
> default telnet password is the same across all
> Siime Eye devices and possibly even across all devices created by this
> developer
>
> ------------------------------------------
>
> [Vulnerability Type]
> Incorrect Access Control
>
> ------------------------------------------
>
> [Vendor of Product]
> Svakom
>
> ------------------------------------------
>
> [Affected Product Code Base]
> Siime Eye - 14.1.00000001.3.330.0.0.3.14
>
> ------------------------------------------
>
> [Affected Component]
> Siime Eye device
>
> ------------------------------------------
>
> [Attack Type]
> Physical
>
> ------------------------------------------
>
> [Impact Code execution]
> true
>
> ------------------------------------------
>
> [Attack Vectors]
> An attacker must first obtain access to the Wi-Fi access point of the device, after which the exploit can be done
> using simple network commands.
>
> ------------------------------------------
>
> [Reference]
> https://www.pentestpartners.com/security-blog/vulnerable-wi-fi-dildo-camera-endoscope-yes-really/
> N/A
>
> ------------------------------------------
>
> [Has vendor confirmed or acknowledged the vulnerability?]
> true
>
> ------------------------------------------
>
> [Discoverer]
> Willem Westerhof, Jasper Nota, Edwin Gozeling from Qbit during an assignment for the Consumentenbond. Unknown
> personnel at pentest partners who did not request a CVE back then.
> ```

```
Use CVE-2020-11915.
```

> ```
> [Suggested description]
> An issue was discovered in Siime Eye 14.1.00000001.3.330.0.0.3.14.
> The password for the root user is hashed using an old and
> deprecated hashing technique. Because of this deprecated hashing,
> the success probability of an attacker in an offline cracking attack
> is greatly increased.
>
> ------------------------------------------
>
> [Vulnerability Type]
> Incorrect Access Control
>
> ------------------------------------------
>
> [Vendor of Product]
> Svakom
>
> ------------------------------------------
>
> [Affected Product Code Base]
> Siime Eye - 14.1.00000001.3.330.0.0.3.14
>
> ------------------------------------------
>
> [Affected Component]
> Siime Eye linux password hashes
>
> ------------------------------------------
>
> [Attack Type]
> Context-dependent
>
> ------------------------------------------
>
> [Impact Information Disclosure]
> true
>
> ------------------------------------------
>
> [Attack Vectors]
> The hash can be obtained using various techniques (e.g.) through command injection.
>
> ------------------------------------------
>
> [Reference]
> N/A
>
> ------------------------------------------
>
> [Discoverer]
> Willem Westerhof, Jasper Nota, Edwin Gozeling from Qbit in assignment of the Consumentenbond.
> ```

```
Use CVE-2020-11916.
```

> ```
> [Suggested description]
> An issue was discovered in Siime Eye 14.1.00000001.3.330.0.0.3.14.
> It uses a default SSID value, which makes it easier for remote attackers to
> discover the physical locations of many Siime Eye devices, violating the
> privacy of users who do not wish to disclose their ownership of this type of device.
> (Various resources such as wigle.net can be use for mapping of SSIDs to physical locations.)
>
> ------------------------------------------
>
> [Additional Information]
> The access point is only detectable when the device is turned on. As the device is turned on for limited times less
> devices are detected via Wigle then one might expect.
>
> Wigle.net is a site which maps SSIDs to physical locations. Using this
> site, it is possible to filter on specific SSIDs. When a filter is
> applied to find the default SSID of the Siime Eye, it is possible to
> find several devices across the globe. The map shown on wigle shows an
> approximate physical location for the device and hence makes physical
> or physical proximity attacks more likely.
>
> In addition it violates the user's privacy as everyone on the internet
> is capable of detecting where the devices are being used.
>
> ------------------------------------------
>
> [VulnerabilityType Other]
> Information disclosure
>
> ------------------------------------------
>
> [Vendor of Product]
> Svakom
>
> ------------------------------------------
>
> [Affected Product Code Base]
> Siime Eye - 14.1.00000001.3.330.0.0.3.14
>
> ------------------------------------------
>
> [Affected Component]
> Siime Eye Wi-Fi access point
>
> ------------------------------------------
>
> [Attack Type]
> Context-dependent
>
> ------------------------------------------
>
> [Impact Information Disclosure]
> true
>
> ------------------------------------------
>
> [Attack Vectors]
> In order to exploit this issue an attacker needs to simply search for the Siime Eye SSID on wigle.net
>
> ------------------------------------------
>
> [Reference]
> https://wigle.net
> N/A
>
> ------------------------------------------
>
> [Has vendor confirmed or acknowledged the vulnerability?]
> true
>
> ------------------------------------------
>
> [Discoverer]
> Willem Westerhof, Jasper Nota, Edwin gozeling from Qbit cyber security in assignment of the Consumentenbond.
> ```

```
Use CVE-2020-11917.
```

> ```
> [Suggested description]
> An issue was discovered in Siime Eye 14.1.00000001.3.330.0.0.3.14.
> When a backup file is created through the web interface, information on
> all users, including passwords, can be found in cleartext in the
> backup file. An attacker capable of accessing the web interface
> can create the backup file.
>
> ------------------------------------------
>
> [Additional Information]
> Note that this means the application passwords are also stored on the device in plain text, otherwise they could not
> be placed in the backup file in this manner.
>
> Note that during normal functional use, the backup file is
> not created.
>
> and then use other vulnerabilities
> to obtain access to the backup file, including the user's passwords.
>
> ------------------------------------------
>
> [Vulnerability Type]
> Incorrect Access Control
>
> ------------------------------------------
>
>...