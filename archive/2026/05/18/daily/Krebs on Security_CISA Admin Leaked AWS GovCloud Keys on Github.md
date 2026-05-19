---
title: CISA Admin Leaked AWS GovCloud Keys on Github
url: https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/
source: Krebs on Security
date: 2026-05-18
fetch_date: 2026-05-19T06:05:14.306811
---

# CISA Admin Leaked AWS GovCloud Keys on Github

Advertisement

[![](/b-doppel/13.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

Advertisement

[![](/b-keeper/14.png)](https://www.keepersecurity.com/privileged-access-management/?utm_source=KrebsOnSecurity&utm_medium=Sponsored&utm_campaign=KrebsOnSecurity_020126&utm_id=Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# CISA Admin Leaked AWS GovCloud Keys on Github

May 18, 2026

[19 Comments](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/#comments)

Until this past weekend, a contractor for the **Cybersecurity & Infrastructure Security Agency** (CISA) maintained a public **GitHub** repository that exposed credentials to several highly privileged **AWS GovCloud** accounts and a large number of internal CISA systems. Security experts said the public archive included files detailing how CISA builds, tests and deploys software internally, and that it represents one of the most egregious government data leaks in recent history.

On May 15, KrebsOnSecurity heard from **Guillaume Valadon**, a researcher with the security firm **GitGuardian**. Valadon’s company constantly scans public code repositories at GitHub and elsewhere for exposed secrets, automatically alerting the offending accounts of any apparent sensitive data exposures. Valadon said he reached out because the owner in this case wasn’t responding and the information exposed was highly sensitive.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/05/privatecisa.png)](https://krebsonsecurity.com/wp-content/uploads/2026/05/privatecisa.png)

A redacted screenshot of the now-defunct “Private CISA” repository maintained by a CISA contractor.

The GitHub repository that Valadon flagged was named “**Private-CISA**,” and it harbored a vast number of internal CISA/DHS credentials and files, including cloud keys, tokens, plaintext passwords, logs and other sensitive CISA assets.

Valadon said the exposed CISA credentials represent a textbook example of poor security hygiene, noting that the commit logs in the offending GitHub account show that the CISA administrator disabled the default setting in GitHub that blocks users from publishing SSH keys or other secrets in public code repositories.

“Passwords stored in plain text in a csv, backups in git, explicit commands to disable GitHub secrets detection feature,” Valadon wrote in an email. “I honestly believed that it was all fake before analyzing the content deeper. This is indeed the worst leak that I’ve witnessed in my career. It is obviously an individual’s mistake, but I believe that it might reveal internal practices.”

One of the exposed files, titled “importantAWStokens,” included the administrative credentials to three Amazon AWS GovCloud servers. Another file exposed in their public GitHub repository — “AWS-Workspace-Firefox-Passwords.csv” — listed plaintext usernames and passwords for dozens of internal CISA systems. According to Caturegli, those system included one called “LZ-DSO,” which appears short for “Landing Zone DevSecOps,” the agency’s secure code development environment.

**Philippe Caturegli**, founder of the security consultancy **Seralys**, said he tested the AWS keys only to see whether they were still valid and to determine which internal systems the exposed accounts could access. Caturegli said the GitHub account that exposed the CISA secrets exhibits a pattern consistent with an individual operator using the repository as a working scratchpad or synchronization mechanism rather than a curated project repository.

“The use of both a CISA-associated email address and a personal email address suggests the repository may have been used across differently configured environments,” Caturegli observed. “The available Git metadata alone does not prove which endpoint or device was used.”

![](https://krebsonsecurity.com/wp-content/uploads/2026/05/privatecisa-filelist.png)

The Private CISA GitHub repo exposed dozens of plaintext credentials for important CISA GovCloud resources.

Caturegli said he validated that the exposed credentials could authenticate to three AWS GovCloud accounts at a high privilege level. He said the archive also includes plain text credentials to CISA’s internal “artifactory” — essentially a repository of all the code packages they are using to build software — and that this would represent a juicy target for malicious attackers looking for ways to maintain a persistent foothold in CISA systems.

“That would be a prime place to move laterally,” he said. “Backdoor in some software packages, and every time they build something new they deploy your backdoor left and right.”

In response to questions, a spokesperson for CISA said the agency is aware of the reported exposure and is continuing to investigate the situation.

“Currently, there is no indication that any sensitive data was compromised as a result of this incident,” the CISA spokesperson wrote. “While we hold our team members to the highest standards of integrity and operational awareness, we are working to ensure additional safeguards are implemented to prevent future occurrences.”

A review of the GitHub account and its exposed passwords show the “Private CISA” repository was maintained by an employee of **Nightwing**, a government contractor based in Dulles, Va. Nightwing declined to comment, directing inquiries to CISA.

CISA has not responded to questions about the potential duration of the data exposure, but Caturegli said the Private CISA repository was created on November 13, 2025. The contractor’s GitHub account was created back in September 2018.

The GitHub account that included the Private CISA repo was taken offline shortly after both KrebsOnSecurity and Seralys notified CISA about the exposure. But Caturegli said the exposed AWS keys inexplicably continued to remain valid for another 48 hours.

CISA is currently operating with only a fraction of its normal budget and staffing levels. The agency has [lost nearly a third of its workforce](https://www.cybersecuritydive.com/news/cisa-cybersecurity-division-reorganization/812155/) since the beginning of the second Trump administration, which forced a series of early retirements, buyouts, and resignations across the agency’s various divisions.

The now-defunct Private CISA repo showed the contractor also used easily-guessed passwords for a number of internal resources; for example, many of the credentials used a password consisting of each platform’s name followed by the current year. Caturegli said such practices would constitute a serious security threat for any organization even if those credentials were never exposed externally, noting that threat actors often use key credentials exposed on the internal network to expand their reach after establishing initial access to a targeted system.

“What I suspect happened is [the CISA contractor] was using this GitHub to synchronize files between a work laptop and a home computer, because he has regularly committed to this repo since November 2025,” Caturegli said. “This would be an embarrassing leak for any company, but it’s even more so in this case because it’s CISA.”

*This entry was posted on Monday 18th of May 2026 04:48 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[AWS GovCloud](https://krebsonsecurity.com/tag/aws-govcloud/) [Cybersecurity & Infrastructure Security Agency](https://k...