---
title: SEC Consult SA-20260415-0 :: Exposed Private Key of X.509 Certificate in SAP HANA Cockpit & SAP HANA Database Explorer
url: https://seclists.org/fulldisclosure/2026/Apr/16
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:38.772480
---

# SEC Consult SA-20260415-0 :: Exposed Private Key of X.509 Certificate in SAP HANA Cockpit & SAP HANA Database Explorer

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260415-0 :: Exposed Private Key of X.509 Certificate in SAP HANA Cockpit & SAP HANA Database Explorer

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 15 Apr 2026 09:25:38 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260415-0 >
=======================================================================
              title: Exposed Private Key of X.509 Certificate
            product: SAP HANA Cockpit & SAP HANA Database Explorer
 vulnerable version: HANA Cockpit <2.18.2 (HRTT <2.16.254002)
      fixed version: HANA Cockpit 2.18.2 (HRTT 2.16.254002)
         CVE number: CVE-2026-34262
             impact: high
           homepage:https://www.sap.com/
              found: 2025-04-24
                 by: Ben Samtleben (Office Berlin)
                     Bernd Kaufmann (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"SAP is one of the world’s leading producers of software for the management
of business processes."

Source:https://www.sap.com/about/what-is-sap.html

"SAP HANA cockpit is the main administration tool for SAP HANA. The SAP HANA
cockpit provides tools for the administration and monitoring of SAP HANA
databases (databases), and for development capabilities through the SAP
HANA database explorer."

Source:https://help.sap.com/docs/SAP_HANA_COCKPIT/df02d156db744412ad1f9e887aba68ad/ab5d442cc8a340fea07c15ef6f8eb537.html

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately, see
SAP Security Note 3730639 (https://me.sap.com/notes/3730639.

This patch does not completely mitigate the risk that the private keys were
obtained by an attacker in the past. Therefore, SEC Consult strongly
recommends rotating the affected X.509 certificates and corresponding private
keys - even if this is currently not mentioned in the SAP Security Note.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Exposed Private Key of X.509 Certificate in SAP HANA Cockpit (CVE-2026-34262)
SAP HANA Cockpit users with access to the Database Explorer can obtain the
X.509 certificate issued to the application server and its corresponding
private key. This information can be used to impersonate the application server
on network level, allowing an attacker to obtain user credentials or other sensitive
data. The issue arises if mutual TLS (mTLS) is configured for communication with the SAP HANA database.

Proof of concept:
-----------------
1) Exposed Private Key of X.509 Certificate in SAP HANA Cockpit (CVE-2026-34262)
When accessing the Database Explorer via the SAP HANA Cockpit, the following
HTTP request is sent to the HRTT service in the background:

GET /hrtt-service/sap/hana/cst/api/v2/databases HTTP/1.1
Host: hana-cockpit-web-app.example.org:31033
Cookie: JSESSIONID=[...]
[...]

The server response contains a list of all available databases.

{
    "__count": 6,
    "d": {
        "results": [
            {
                "__metadata": {
                    "uri": "/sap/hana/cst/api/v2/databases('C123456789')",
                    "type": "database.Database"
                },
                "id": "C123456789",
                "group_id": 0,
                "catalog_name": "SID@SID",
                "type": "COCKPIT_RESOURCE",
                "disabled": false,
                "has_login": false,
                "cockpit_resource_id": 123456789,
                "database_product_name": "HANA",
                "options": {
                    "schema_filter": "[]"
                },
                "set_xs_applicationuser": true,
                "hdl_support_sof": false
            },
            // [... more entries here...]
        ]
    }
}

However, the response can vary - most likely depending on other HTTP requests
that have been sent. A more verbose response can be triggered by manually
interacting with the Database Explorer and then repeating the request.
(No database credentials are needed.) Then, the following information is returned:

{
    "__count": 6,
    "d": {
        "results": [
            {
                "__metadata": {
                    "uri": "/sap/hana/cst/api/v2/databases('C123456789')",
                    "type": "database.Database"
                },
                "id": "C123456789",
                "group_id": 0,
                "catalog_name": "SID@SID",
                "type": "COCKPIT_RESOURCE",
                "disabled": false,
                "has_login": false,
                "cockpit_resource_id": 123456789,
                "database_product_name": "HANA",
                "cockpit_resource_name": "SID@SID",
                "options": {
                    "hosts": [
                        {
                            "host": "isidhdb01.example.org",
                            "port": "31013"
                        }
                    ],
                    "databaseName": "SID",
                    "encrypt": true,
                    "ca": [
                        "-----BEGIN CERTIFICATE-----\nMII[... certificate removed ...]zg==\n-----END
CERTIFICATE-----\n",
                        "-----BEGIN CERTIFICATE-----\nMII[... certificate removed ...]c4=\n-----END CERTIFICATE-----\n",
                    ],
                    "sslValidateCertificate": true,
                    "key": [
                        "-----BEGIN PRIVATE KEY-----MII[... private key removed ...]8tQ==-----END PRIVATE KEY-----"
                    ],
                    "cert": [
                        "-----BEGIN CERTIFICATE-----MII[... certificate removed ...]QHvC-----END CERTIFICATE----------BEGIN
CERTIFICATE-----MII[...]yotP-----END CERTIFICATE-----"
                    ],
                    "schema_filter": "[]"
                },
                "set_xs_applicationuser": true,
                "hdl_support_sof": false
            }
            // [... more entries here...]
        ]
    }
}

The HTTP response does not only leak additional metadata, but most importantly an X.509
certificate chain and the private key of the leaf certificate. This certificate is issued
to the application server hosting the SAP HANA Cockpit, not to the database server.

The vulnerability can be reproduced with the Cockpit Administrator and the Cockpit User role,
so it does not require administrative privileges.

Vulnerable / tested versions:
-----------------------------
The following versions are affected:
* SAP HANA Cockpit versions prior to 2.18.2 (SAP HANA Runtime Tools prior to 2.16.254002)

Vendor contact timeline:
------------------------
2025-07-01: Contacting vendor through vulnerability submission web form, receiving
            automatic confirmation.
2025-10-13: R...