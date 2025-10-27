---
title: 18 Popular Code Packages Hacked, Rigged to Steal Crypto
url: https://krebsonsecurity.com/2025/09/18-popular-code-packages-hacked-rigged-to-steal-crypto/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-09
fetch_date: 2025-10-02T19:51:17.752500
---

# 18 Popular Code Packages Hacked, Rigged to Steal Crypto

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# 18 Popular Code Packages Hacked, Rigged to Steal Crypto

September 8, 2025

[11 Comments](https://krebsonsecurity.com/2025/09/18-popular-code-packages-hacked-rigged-to-steal-crypto/#comments)

At least 18 popular JavaScript code packages that are collectively downloaded more than two billion times each week were briefly compromised with malicious software today, after a developer involved in maintaining the projects was phished. The attack appears to have been quickly contained and was narrowly focused on stealing cryptocurrency. But experts warn that a similar attack with a slightly more nefarious payload could lead to a disruptive malware outbreak that is far more difficult to detect and restrain.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/npmjshelp.png)

**Aikido** is a security firm in Belgium that monitors new code updates to major open-source code repositories, scanning any code updates for suspicious and malicious code. In a blog post published today, Aikido said its systems found malicious code had been added to at least 18 widely-used code libraries available on [**NPM**](https://www.npmjs.com/) (short for) “Node Package Manager,” which acts as a central hub for JavaScript development and the latest updates to widely-used JavaScript components.

JavaScript is a powerful web-based scripting language used by countless websites to build a more interactive experience with users, such as entering data into a form. But there’s no need for each website developer to build a program from scratch for entering data into a form when they can just reuse already existing packages of code at NPM that are specifically designed for that purpose.

Unfortunately, if cybercriminals manage to phish NPM credentials from developers, they can introduce malicious code that allows attackers to fundamentally control what people see in their web browser when they visit a website that uses one of the affected code libraries.

According to Aikido, the attackers injected a piece of code that silently intercepts cryptocurrency activity in the browser, “manipulates wallet interactions, and rewrites payment destinations so that funds and approvals are redirected to attacker-controlled accounts without any obvious signs to the user.”

“This malware is essentially a browser-based interceptor that hijacks both network traffic and application APIs,” Aikido researcher **Charlie Eriksen** [wrote](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised). “What makes it dangerous is that it operates at multiple layers: Altering content shown on websites, tampering with API calls, and manipulating what users’ apps believe they are signing. Even if the interface looks correct, the underlying transaction can be redirected in the background.”

Aikido said it used the social network Bsky to notify the affected developer, **Josh Junon**, who quickly replied that he was aware of having just been phished. The phishing email that Junon fell for was part of a larger campaign that spoofed NPM and told recipients they were required to update their two-factor authentication (2FA) credentials. The phishing site mimicked NPM’s login page, and intercepted Junon’s credentials and 2FA token. Once logged in, the phishers then changed the email address on file for Junon’s NPM account, temporarily locking him out.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/junon-bsky.png)

Junon also issued a mea culpa [on HackerNews](https://news.ycombinator.com/item?id=45169794), telling the community’s coder-heavy readership, “Hi, yep I got pwned.”

“It looks and feels a bit like a targeted attack,” Junon wrote. “Sorry everyone, very embarrassing.”

**Philippe Caturegli**, “chief hacking officer” at the security consultancy [Seralys](https://seralys.com), observed that the attackers appear to have registered their spoofed website — npmjs[.]help — just two days before sending the phishing email. The spoofed website used services from dnsexit[.]com, a “dynamic DNS” company that also offers “100% free” domain names that can instantly be pointed at any IP address controlled by the user.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/junon-hn.png)

Caturegli said it’s remarkable that the attackers in this case were not more ambitious or malicious with their code modifications.

“The crazy part is they compromised billions of websites and apps just to target a couple of cryptocurrency things,” he said. “This was a supply chain attack, and it could easily have been something much worse than crypto harvesting.”

Aikido’s Eriksen agreed, saying countless websites dodged a bullet because this incident was handled in a matter of hours. As an example of how these supply-chain attacks can escalate quickly, Eriksen pointed to [another compromise of an NPM developer in late August](https://www.aikido.dev/blog/popular-nx-packages-compromised-on-npm) that added malware to “**nx**,” an open-source code development toolkit with as many as six million weekly downloads.

In the nx compromise, the attackers introduced code that scoured the user’s device for authentication tokens from programmer destinations like GitHub and NPM, as well as SSH and API keys. But instead of sending those stolen credentials to a central server controlled by the attackers, the malicious code created a new public repository in the victim’s GitHub account, and published the stolen data there for all the world to see and download.

Eriksen said coding platforms like GitHub and NPM should be doing more to ensure that any new code commits for broadly-used packages require a higher level of attestation that confirms the code in question was in fact submitted by the person who owns the account, and not just by that person’s account.

“More popular packages should require attestation that it came through trusted provenance and not just randomly from some location on the Internet,” Eriksen said. “Where does the package get uploaded from, by GitHub in response to a new pull request into the main branch, or somewhere else? In this case, they didn’t compromise the target’s GitHub account. They didn’t touch that. They just uploaded a modified version that didn’t come where it’s expected to come from.”

Eriksen said code repository compromises can be devastating for developers, many of whom end up abandoning their projects entirely after such an incident.

“It’s unfortunate because one thing we’ve seen is people have their projects get compromised and they say, ‘You know what, I don’t have the energy for this and I’m just going to deprecate the whole package,'” Eriksen said.

**Kevin Beaumont**, a frequently quoted security expert who writes about security incidents at the blog doublepulsar.com, has been following this story closely today in frequent updates to [his account on Mastodon](https://infosec.exchange/%40GossiTheDog%40cyberplace.social). Beaumont said the incident is a reminder that much of the planet still depends on code that is ultimately maintained by an exceedingly small number of people who are mostly overburdened and under-resourced.

“For about the past 15 years every business ha...