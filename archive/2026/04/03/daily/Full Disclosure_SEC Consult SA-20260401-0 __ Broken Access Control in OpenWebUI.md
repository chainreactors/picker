---
title: SEC Consult SA-20260401-0 :: Broken Access Control in Open	WebUI
url: https://seclists.org/fulldisclosure/2026/Apr/4
source: Full Disclosure
date: 2026-04-03
fetch_date: 2026-04-04T04:17:51.635276
---

# SEC Consult SA-20260401-0 :: Broken Access Control in Open	WebUI

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260401-0 :: Broken Access Control in Open WebUI

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 1 Apr 2026 10:54:01 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260401-0 >
=======================================================================
              title: Broken Access Control
            product: Open WebUI
 vulnerable version: <v0.8.11
      fixed version: v0.8.11
         CVE number: CVE-2026-34222
             impact: high
           homepage:https://openwebui.com
              found: 2026-02-06
                 by: Timo Müller (Office Munich)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"The self-hosted AI interface.
Open WebUI is the platform for running AI on your own terms.
Connect to any model—local or cloud. Extend with Python.
Share what you build with 331K others. 270 million downloads and growing."

Source:https://openwebui.com/

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Broken Access Control in Tool Valves (CVE-2026-34222)
Open WebUI supports function calling through "Tools". Function calling allows
an LLM to reliably connect to external tools and interact with external APIs.
Exemplary use-cases include connecting to an internal knowledge base,
retrieving emails from an exchange server, or retrieving order data from a
shop backend.

These interactions often require the LLM to authenticate against backend
services using API keys specifically created for a technical (Open WebUI)
user.

To simplify configuration and secret handling, Open WebUI implements
"Valves" and "UserValves" that allow users and administrators to input
dynamic details like API keys or configuration options.

Valves have the following distinction:
* Valves: Configurable by admins only.
* UserValves: Configurable by any user.

The Tool Valves endpoint does not properly restrict read access to the
valve. This allows a low privileged user to access all data contained
within the valve. In the worst case, this gives a low privileged
"Member" user access to sensitive Tool data, such as API keys for
third-party systems.

Proof of concept:
-----------------
1) Broken Access Control in Tool Valves (CVE-2026-34222)
The following steps can be performed to reproduce the vulnerability.

1. An administrator creates an Open WebUI Tool with a configured Valve.
   <10_create_tool.png>
2. The administrator configures the API key within the Tool Valve.
   <20_valves.png>
3. A user with at least "Member" privileges logs into Open WebUI.

The following screenshot shows the user overview of the test instance:
<30_user_admin.png>

The following screenshot illustrates that the "lowpriv" user
doesn't have access to the tool:
<35_lowpriv.png>

4. The "lowpriv" user uses their Authorization token to retrieve the
API key from the Tool Valve.

In order to do so, the attacker needs to know the Tool ID. However, as
this ID is always the same for imported tools, and the tool IDs are
concatenated from the tool name, guessing tool IDs is trivial.
<50_get_valve.png>

As seen in the following code snippet, the vulnerability is present because
the Tool Valves route does not check if the requesting user
has administrative permissions.

Code
source:https://github.com/open-webui/open-webui/blob/2b26355002064228e9b671339f8f3fb9d1fafa73/backend/open_webui/routers/tools.py#L513-L531

```
@router.get("/id/{id}/valves", response_model=Optional[dict])
async def get_tools_valves_by_id(
    id: str, user=Depends(get_verified_user), db: Session = Depends(get_session)
):
    tools = Tools.get_tool_by_id(id, db=db)
    if tools:
        try:
            valves = Tools.get_tool_valves_by_id(id, db=db)
            return valves
[...]
)
```

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* v0.7.2

All versions below the fixed version v0.8.11 are affected.

Vendor contact timeline:
------------------------
2026-02-11: Contacting vendor through the Open WebUI GitHub security
            advisories page (github.com/open-webui/open-webui/security/advisories/GHSA-7429-hxcv-268m)
2026-02-11: GitHub security advisory was closed by the maintainer with the
            reasoning "Tools perm should NOT be given to an untrusted party."
2026-02-11: Closure of the advisory was contested by submitting additional proof
2026-02-18: Additional reminder to the vendor that we will disclose this issue.
2026-03-18: Additional reminder to the vendor that we will disclose this issue.
2026-03-24: Vendor re-evaluates the submitted advisory, requests additional details,
            and requests a validation of this issue on the development branch.
2026-03-24: Provided the additional details and confirmed that the issue is patched
            on the development branch.
2026-03-24: Vendor re-opens and confirms the submitted  advisory.
2026-03-27: Vendor confirms the CVSS score and requests a CVE through GitHub.
2026-03-27: GitHub has issued CVE-2026-34222 for this vulnerability.
2026-04-01: Vendor advisory published, SEC Consult release of advisory as well.

Solution:
---------
The vendor provides a patched version v0.8.11 which can be downloaded from their website:
https://github.com/open-webui/open-webui/releases

Fix commit:https://github.com/open-webui/open-webui/commit/f949d17db1e62e0b79aecbbcbcabe3d57d8d4af6

The vendor has also published the security report / advisory here:
https://github.com/open-webui/open-webui/security/advisories/GHSA-7429-hxcv-268m

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

Interested in improving your c...