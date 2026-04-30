---
title: SEC Consult SA-20260421-0 :: Broken Access Control in Config Endpoint in LiteLLM
url: https://seclists.org/fulldisclosure/2026/Apr/17
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:38.360437
---

# SEC Consult SA-20260421-0 :: Broken Access Control in Config Endpoint in LiteLLM

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260421-0 :: Broken Access Control in Config Endpoint in LiteLLM

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 21 Apr 2026 11:15:23 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260421-0 >
=======================================================================
              title: Broken Access Control in Config Endpoint
            product: LiteLLM
 vulnerable version: <=v1.83.0
      fixed version: v1.83.0-nightly
         CVE number: CVE-2026-35029
             impact: high
           homepage:https://www.litellm.ai/
              found: 2026-02-24
                 by: Timo Müller (Office Munich)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"AI Gateway to provide model access, fallbacks and spend tracking across 100+
LLMs. All in the OpenAI format."

Source:https://www.litellm.ai/

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Broken Access Control in Config Endpoint (CVE-2026-35029)
LiteLLM exposes a /config/update API endpoint that allows administrators to
make configuration changes to the instance. Due to a missing authorization
check, low-privileged users can access this endpoint without restriction.
An attacker with a low-privileged account can exploit this to exfiltrate
environment variables and read arbitrary files within the context of the
LiteLLM application.

Proof of concept:
-----------------
1) Broken Access Control in Config Endpoint (CVE-2026-35029)
The vulnerability exists because the update_config function, which handles the
/config/update route, does not check whether the requesting user has
administrative permissions.

The vulnerable function can be seen
here:https://github.com/BerriAI/litellm/blob/47c24ef8ae1b6c77827491437b3e3ed143c1e77f/litellm/proxy/proxy_server.py#L11337-L11481

The following screenshot illustrates a request sent by a regular user without
administrative privileges. The exploit leverages "Pass Through Endpoints",
which allow administrators to route requests from the LiteLLM proxy to
any external API.

Pass Through Endpoints:https://docs.litellm.ai/docs/proxy/pass_through

The request contains the following parameters:

* path - defines the path under which the pass through endpoint is created
* target - the attacker-controlled server to which requests are routed
           (i.e. the exfiltration server receiving sensitive data)
* headers - a list of headers containing the exfiltrated data, populated by
            LiteLLM before routing the request to the attacker-controlled server

The "X-DB-URL" header retrieves the DATABASE_URL environment variable from the
LiteLLM environment. The LANGFUSE* headers are used to exfiltrate files from
the LiteLLM host system. Specifically, these headers are chosen because LiteLLM
base64-encodes any values passed to them.

LANGFUSE* header
encoding:https://github.com/BerriAI/litellm/blob/47c24ef8ae1b6c77827491437b3e3ed143c1e77f/litellm/proxy/pass_through_endpoints/pass_through_endpoints.py#L100-L115

<10_exploit.png>

Once the configuration is set, the pass through route update can take several
minutes. After this wait time, the attacker triggers exfiltration by calling the
endpoint. The exfiltration request is shown in the following screenshot.
Please note that the LiteLLM response contains the response data from the
exfiltration server.

<20_exfil.png>

The following screenshot illustrates the successful exploitation of this issue,
showing the request received by the attacker-controlled server from the
LiteLLM instance. The DATABASE_URL environment variable is visible highlighted
within the server header, and the contents of /etc/passwd are included in
base64-encoded form within the Authorization header.

<30_content.png>

Decoding the base64-encoded Authorization header reveals the contents of
the /etc/passwd file from the LiteLLM host system:

<40_decoded.png>

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* 1.81.12

Vendor contact timeline:
------------------------
2026-02-26: Contacting vendor throughsupport () berri ai.
2026-03-10: Inquiry sent to verify whether the vendor has
            received and analysed the advisory.
2026-03-10: BerriAI confirms receipt of the advisory and
            loops in engineers for vulnerability analysis.
2026-04-01: A security patch for the reported vulnerability
            is released on the nightly build.
2026-04-01: Vendor contacted for additional details
            to coordinate advisory disclosure.
2026-04-03: A CVE is assigned to the vulnerability and it is disclosed
            without further coordination through the GitHub
            security page of LiteLLM.
2026-04-07: A draft version of the advisory is sent to the vendor
            in preparation of the advisory release.
2026-04-14: The vendor is informed that the advisory will be released
            the upcoming week.
2026-04-14: The vendor validates the submitted draft advisory
            and confirms the planned release.
2026-04-21: Coordinated release of advisory.

Solution:
---------
The vendor provides a patched version v1.83.0-nightly which can be
downloaded from their website:
https://github.com/BerriAI/litellm/releases

Fix commit:https://github.com/BerriAI/litellm/commit/57c05459ae9b4e607bfb35228ec13a3ee8586ce4

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Atos business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your applicationhttps://sec-consult.com/career/

Interested in improving your cyber security with the experts of SEC Consult?
Contact our local officeshttps://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...