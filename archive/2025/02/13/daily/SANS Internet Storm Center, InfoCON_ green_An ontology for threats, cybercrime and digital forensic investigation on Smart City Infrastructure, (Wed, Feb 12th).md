---
title: An ontology for threats, cybercrime and digital forensic investigation on Smart City Infrastructure, (Wed, Feb 12th)
url: https://isc.sans.edu/diary/rss/31676
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-13
fetch_date: 2025-10-06T20:37:03.283921
---

# An ontology for threats, cybercrime and digital forensic investigation on Smart City Infrastructure, (Wed, Feb 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31674)
* [next](/diary/31680)

# [An ontology for threats, cybercrime and digital forensic investigation on Smart City Infrastructure](/forums/diary/An%2Bontology%2Bfor%2Bthreats%2Bcybercrime%2Band%2Bdigital%2Bforensic%2Binvestigation%2Bon%2BSmart%2BCity%2BInfrastructure/31676/)

**Published**: 2025-02-12. **Last Updated**: 2025-02-12 02:05:01 UTC
**by** [Yee Ching Tok](https://poppopretn.com/aboutme/) (Version: 1)

[0 comment(s)](/diary/An%2Bontology%2Bfor%2Bthreats%2Bcybercrime%2Band%2Bdigital%2Bforensic%2Binvestigation%2Bon%2BSmart%2BCity%2BInfrastructure/31676/#comments)

Blue teams have it hard – they maintain a watchful eye on whatever technology is deployed to detect threats, respond to incidents, perform digital forensics and reverse malware (or make malware happy!) when needed. Hopefully, no one has to handle all these roles alone since there is also the continuous learning aspect of getting up to speed with the latest threat vectors, vulnerabilities and exploit techniques. Adversaries only need one attack to succeed to gain actions on objective. In contrast, defenders have to detect and stop every attack to prevent adversaries from being successful. Let’s now extrapolate to an even bigger problem – what if this happens on emerging/future technologies and adversaries can get away with such crimes?

Multiple countries are gradually considering the concept of Smart Cities, a key consideration in the United Nations Development Programme (UNDP). As such technologies are implemented, the responsibility of defending this critical infrastructure again falls on the shoulders of blue teams. Smart Cities have yet to be fully implemented, but it does not mean we should not be proactive in preparing defenders to handle future problems. Current issues, even without Smart Cities in the fray, already cause blue team grief (e.g. different technology platforms, different contexts, information sharing, collaboration and tool interoperability). Given these complexities, an ontology would allow a shared understanding of vocabulary, facilitate data sharing, and even enable automated data reasoning.

Wanting to pre-emptively solve future issues of attacks and cybercrime on Smart City Infrastructure (SCI), I (along with my co-authors in the [SUTD ASSET Group](https://asset-group.github.io)) set out to create the Smart City Ontological Paradigm Expression (SCOPE). SCOPE was designed to be an ontology for threats, cybercrime and digital forensic investigation on SCI. We did not create the ontology from scratch but chose to adhere to ontology best practices and extended the venerable Unified Cyber Ontology (UCO) [1] and Cyber-investigation Analysis Standard Expression (CASE) [2]. UCO and CASE have gained some traction, and these ontologies have been experimentally adopted in forensic tools such as Cellebrite, Magnet Forensics, and MSAB XRY [3]. However, UCO and CASE did not have any SCI representation, and expecting overwhelmed blue teams to create them from scratch would most certainly be the straw that broke the camel’s back.

![](https://isc.sans.edu/diaryimages/images/Feb_2025_1_1.png)
**Figure 1:** Smart City Infrastructure Definition (reproduced with permission from the authors) [4]

We deliberated on several design factors. Firstly, we defined smart cities using a technology-agnostic approach while adhering to international standards (with reference to Figure 1) that adopted the United Nations (UN) Sustainable Development Goals (SDG) (this was done in a previous work) [4]. By doing so, we ensured that the evolution of technologies or vendors would not affect the fundamental principle of Smart Cities. Secondly, we identified possible threats, cybercrime, and digital forensic evidence sources from the Smart City, which were defined in the first step (also from the same previous work) [4]. Thirdly, we included MITRE ATT&CK techniques and MITRE CAPEC into SCOPE for analysts and investigators to provide additional context to forensic evidence. Finally, we followed the ontological style and design practices when creating SCOPE, an expansion profile from UCO and CASE.

We evaluated SCOPE via real-world attack scenarios attributed to publicly reported real-world incidents attributed to Advanced Persistent Threat (APT) groups. With reference to Figure 2, the evaluation process workflow is shown. We successfully represented the attack scenarios, cybercrime committed, incident details, evidence and attack patterns (to name a few).

![](https://isc.sans.edu/diaryimages/images/Feb_2025_1_2.png)
**Figure 2:** SCOPE Evaluation Process (reproduced with permission from the authors) [3]

Will SCOPE ever be helpful? Not yet. I hope it will come in handy in future for digital forensic investigators and law enforcement agencies when cybercrime on SCI becomes prevalent. As mentioned, SCOPE is technology-agnostic while adhering to several ISO standards. Additionally, it contains enough granularity to allow users to pinpoint key information while ensuring it can capture abstract definitions covering emerging technologies. We have made SCOPE publicly available to the digital forensic community to assist future smart city infrastructure investigations. SCOPE’s GitHub project link is <https://github.com/scopeProject>, and the official ontology website is <https://scopeontology.org>. If readers want to find out the complete details of SCOPE, you can find the full published paper in [Volume 52](https://www.sciencedirect.com/journal/forensic-science-international-digital-investigation/vol/52/suppl/C) of [Forensic Science International: Digital Investigation (FSIDI)](https://www.sciencedirect.com/journal/forensic-science-international-digital-investigation) or at <https://doi.org/10.1016/j.fsidi.2025.301883>.

**References:**
1. https://www.scopus.com/record/display.uri?eid=2-s2.0-85021968557&origin=inward
2. https://doi.org/10.1016/j.diin.2017.08.002
3. https://doi.org/10.1016/j.fsidi.2025.301883
4. https://doi.org/10.1016/j.fsidi.2023.301540

-----------
Yee Ching Tok, Ph.D., ISC Handler
[Personal Site](https://poppopretn.com)
[Mastodon](https://infosec.exchange/%40poppopretn)
[Twitter](https://twitter.com/poppopretn)

Keywords: [Smart City Ontological Paradigm Expression](/tag.html?tag=Smart City Ontological Paradigm Expression) [smart city infrastructure](/tag.html?tag=smart city infrastructure) [cybercrime](/tag.html?tag=cybercrime) [SCOPE](/tag.html?tag=SCOPE)

[0 comment(s)](/diary/An%2Bontology%2Bfor%2Bthreats%2Bcybercrime%2Band%2Bdigital%2Bforensic%2Binvestigation%2Bon%2BSmart%2BCity%2BInfrastructure/31676/#comments)

* [previous](/diary/31674)
* [next](/diary/31680)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [Abo...