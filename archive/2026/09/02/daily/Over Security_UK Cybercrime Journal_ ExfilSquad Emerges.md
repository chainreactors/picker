---
title: UK Cybercrime Journal: ExfilSquad Emerges
url: https://blog.bushidotoken.net/2026/09/uk-cybercrime-journal-exfilsquad-emerges.html
source: Over Security
date: 2026-09-02
fetch_date: 2026-09-03T07:02:49.279105
---

# UK Cybercrime Journal: ExfilSquad Emerges

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: ExfilSquad Emerges

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[September 02, 2026](https://blog.bushidotoken.net/2026/09/uk-cybercrime-journal-exfilsquad-emerges.html "permanent link")

**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlrnq_KDX8h9DtdBEtV8az1vw1ijUv1pHrzC7lG_sM65JmUzOIXvJjtSsgutZh6l7DglKNEixxN7bdavO4-ubs7ypGPIwznzkn7bgo2-eSKh4-h3sU6CeryF7fmcE6mmLCZABohjvGGbL9SprHsBbifOK0uSiO9cSnTP5aqCEHBlajq1Z0jpVMbII58i8K/w640-h386/98590c2f-6a4b-442a-b47c-868429223c43.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlrnq_KDX8h9DtdBEtV8az1vw1ijUv1pHrzC7lG_sM65JmUzOIXvJjtSsgutZh6l7DglKNEixxN7bdavO4-ubs7ypGPIwznzkn7bgo2-eSKh4-h3sU6CeryF7fmcE6mmLCZABohjvGGbL9SprHsBbifOK0uSiO9cSnTP5aqCEHBlajq1Z0jpVMbII58i8K/s1024/98590c2f-6a4b-442a-b47c-868429223c43.jpg)**

**What Happened**

* In mid-2026, an emerging cybercriminal group known as [ExfilSquad](https://www.ransomware.live/group/ExfilSquad) launched a high-profile extortion campaign targeting prominent UK organisations across the public sector, education, and law enforcement, as well as other firms worldwide.
* Unlike traditional ransomware groups, ExfilSquad does not deploy encryptors or destructive malware. Instead, they operate as a pure data extortion group, stealing data and threatening to publish it on their onion-based Data Leak Site (DLS) if a ransom is not paid.
* Several prominent UK entities have confirmed breaches linked to the group:

+ **UK Department for Education (DfE):** Approximately 600,000 records stolen from its Help Portal containing parent and staff contact details (names, emails, phone numbers, job titles), plus around 7,000 records from the Turing Portal.
+ **Police National Legal Database (PNLD):** Stole 1.9 GB of data (around 135,000 records) containing contact information for over 100,000 serving police officers, staff, and criminal justice professionals, alongside around 21,000 "Ask the Police" public inquiry records.
+ **Newcastle University:** Approximately 440,000 records compromised containing applicant and student contact information, personally identifiable information (PII), and admissions database records caused by a technical configuration flaw connecting to an admissions system.

* Analysis of the details left on the data leak site revealed that ExfilSquad's primary attack vector involves exploiting misconfigurations in cloud portals, customer relationship management (CRM) platforms, internal case management systems, as well as Microsoft Power Pages data tables left publicly accessible without proper authentication.
* To force compliance and prove their claims are real, ExfilSquad uploaded multi-gigabyte torrent files for each victim to their TOR leak site. Resecurity [noted](https://www.resecurity.com/blog/article/exfilsquad-targets-new-victims-shares-data-via-torrents) that ExfilSquad assigns a distinct Torrent Tracker and initial Web Seed per victim.

**Analyst Comment**

While ExfilSquad is a new group, they appear to be already experienced at running these types of attacks, suggesting they have a history of cybercrime. Plus, ExfilSquad’s recent campaign highlights the growing trend of transitioning from file-encrypting ransomware to extortion driven entirely by cloud and SaaS misconfigurations. Organisations that have invested in defending against endpoint-based threats are often leaving critical business application interfaces exposed.

SaaS platforms [continue](https://www.sans.org/blog/hunting-saas-threats-insights-for589-course-cybercriminal-campaigns) to be primary targets of English-speaking cybercrime communities. In recent years,  customers of major SaaS providers, such as Salesloft, Salesforce, and Snowflake have all been extorted. Microsoft Power Pages portals, CRM databases, and customer support helpdesks frequently hold vast repositories of sensitive contact data and interaction histories. When internet-facing API endpoints or data table permissions are left unauthenticated or unpatched, cybercriminals can systematically scrape massive volumes of data without ever needing to drop a payload or escalate privileges internally.

ExfilSquad’s reliance on torrent distribution further amplifies reputational and operational damage. While gangs like LockBit, Clop, and Akira have previously utilised torrents, ExfilSquad’s operational twist of assigning unique Torrent Trackers and dedicated Web Seeds to individual victims ensures that leaked files distribute rapidly across P2P networks, making it extremely difficult to perform a takedown.

While ExfilSquad’s breaches have largely compromised contact directories and administrative support records, the real-world risks remain significant. Exposing work emails, names, and organisational structures for over 100,000 police officers and civil servants poses distinct social engineering, spear-phishing, and physical security concerns that impacted institutions will have to manage long after the breach occurs.

**Defensive Takeaways**

* **Audit Microsoft Power Pages and Public SaaS Tables:** Regularly review public data table permissions, web API settings, and unauthenticated browser views across Microsoft Power Pages, CRMs, and customer support portals to ensure backend data tables are not exposed to the public internet.
* **Harden CRM and Case Management Integrations:** Treat external-facing admissions portals, helpdesks, and case management systems as high-risk platforms. Implement strict access controls, conduct routine configuration audits, and enforce proper API token security.
* **Deploy External Attack Surface Management (EASM):** Utilise continuous external attack surface scanning to detect newly exposed web endpoints, misconfigured database connectors, and publicly exposed storage buckets before malicious actors locate them.
* **Incorporate Pure Extortion into Incident Response Plans:** Security teams must adapt incident response playbooks for data-theft-only scenarios. Organisations may seek to establish protocols for monitoring peer-to-peer (P2P) networks and managing public disclosures when stolen data is distributed via torrents.

**Relevant Sources**

1. <https://www.computing.co.uk/news/2026/security/newcastle-university-data-breach-exfilsquad>
2. <https://www.thetimes.com/uk/crime/article/who-are-exfilsquad-hackers-cyberattacks-dtzhvvzgj>
3. <https://www.ncl.ac.uk/press/articles/latest/2026/07/statementonpotentialunauthoriseddataaccess/>
4. <https://www.bbc.co.uk/news/articles/cq6dmgrp21po>
5. <https://www.pnld.co.uk/article/?id=7ebf3c0e-598e-f111-8077-7ced8d3aa78f>

**Relevant CTI Sources**

1. <https://www.ransomware.live/group/ExfilSquad>
2. <https://www.resecurity.com/blog/article/exfilsquad-targets-new-victims-shares-data-via-torrents>
3. <https://socradar.io/blog/dark-web-profile-exfilsquad/>
4. <https://www.sans.org/blog/hunting-saas-threats-insights-for589-course-cybercriminal-campaigns>

[Cybercrime](https://blog.bushidotoken.net/search/label/Cybercrime)
[DfE](https://blog.bushidotoken.net/search/label/DfE)
[ExfilSquad](https://blog.bushidotoken.net/search/label/ExfilSquad)
[Extortion](https://blog.bushidotoken.net/search/label/Extortion)
[PNLD](https://blog.bushidotoken.net/search/label/PNLD)
[UK](https://blog.bushidotoken.net/search/label/UK)
[UK Cybercrime Journal](https://blog.bushidotoken.net/search/label/UK%20Cybercrime%20Journal)
[UK Police](https://blog.bushidotoken.net/search/label/UK%20Police)
[university](https://blog.bushidotoken.net/search/label/university)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### [Ransomware Tool Matrix Project Updates: May 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

-
[May 05, 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html "p...