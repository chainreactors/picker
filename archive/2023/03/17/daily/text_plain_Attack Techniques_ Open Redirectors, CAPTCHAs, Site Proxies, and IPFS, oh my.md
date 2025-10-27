---
title: Attack Techniques: Open Redirectors, CAPTCHAs, Site Proxies, and IPFS, oh my
url: https://textslashplain.com/2023/03/16/attack-techniques-open-redirectors-captchas-site-proxies-and-ipfs-oh-my/
source: text/plain
date: 2023-03-17
fetch_date: 2025-10-04T09:51:29.569358
---

# Attack Techniques: Open Redirectors, CAPTCHAs, Site Proxies, and IPFS, oh my

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Open Redirectors, CAPTCHAs, Site Proxies, and IPFS, oh my

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-03-162023-04-06](https://textslashplain.com/2023/03/16/attack-techniques-open-redirectors-captchas-site-proxies-and-ipfs-oh-my/)Posted in[security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [phishing](https://textslashplain.com/tag/phishing/), [security](https://textslashplain.com/tag/security/), [SmartScreen](https://textslashplain.com/tag/smartscreen/)

The average phishing site doesn’t live very long– think *hours* rather than days or weeks. **Attackers** use a variety of techniques to try to keep ahead of the **Defenders** who work tirelessly to break their attack chains and protect the public.

Defenders have several opportunities to interfere with attackers:

* Email scanners can detect **Lure** emails and either block them entirely, or warn the user (e.g. Microsoft SafeLinks) if they click on a link in an email that leads to a malicious site. These email scanners might check embedded URLs by directly checking URL Reputation Services, or they might use **Detonators**, automated bots which try to navigate a virtual machine to the URLs contained within a Lure email to determine whether the user will end up on a malicious site.

* Browsers themselves use URL Reputation Services (Microsoft SmartScreen, Google SafeBrowsing) to block navigations to URLs that have been reported as maliciously **Request**ing the victim’s credentials and/or **Record**ing those stolen credentials.
* Browser extensions (e.g. NetCraft, Suspicious Site Reporter) can warn the user if the site they’re visiting is *suspicious* in some way (newly, bad reputation, hosted in a “dodgy neighborhood”, etc).
* Defenders can work with Certificate Authorities to revoke the HTTPS certificates of malicious sites (alas, this [no longer works very well](https://textslashplain.com/2022/08/01/certificate-revocation-in-microsoft-edge/))
* Defenders and Authorities work with web infrastructure providers (hosting companies, CDNs, domain registration authorities, etc) to take down malicious sites.

Each of these represents a weak link for attackers, and they can improve their odds by avoiding them as much as possible. For example, phishers can try to avoid URL Reputation services’ blocking entirely by sending Lures that trick users into completing their [victimization over the phone](https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/). Or, they can try to limit their exposure to URL Reputation services by using the Lure to serve the credential **Request** [from the victim’s own computer](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/), so that only the url that **Record**s the stolen credentials is a candidate for blocking.

To make their Lure emails’ URLs less suspicious to mail scanners, some phishers will not include a URL that points directly at the credential Request page, instead pointing at a **Redirect** URL. In some cases, that redirector is provided by a legitimate service, like Google or LinkedIn:

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-25.png?w=489)](https://textslashplain.com/wp-content/uploads/2023/03/image-25.png)

That first Redirect URL might itself link to another Redirect service; in some cases, a **Cloaking Redirector** might be used which tries to determine whether the visitor is a real person (potential victim) or a security scanning bot (Defender). If the Cloaking Redirector believes they’ve got a real bite, they’ll send them to the Credential Request page, but if not, they’ll instead send the bot to some innocuous other page (Google and Microsoft homepages are common choices).

Redirectors can also complicate the [phish-reporting process](https://textslashplain.com/2023/01/19/defense-techniques-reporting-phish/): a user reporting a phishing site might not report the original URL, so when the credential **Request** page starts getting blocked, the attacker can just update the Redirect URL used in their lure to point to a *new* **Request** page.

Before showing the user the credential Request, an attacker might ask the user to complete a [CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA). Now, you might naturally wonder “*Why would an attacker ever put a hurdle in the way of the victim on their merry way to give up their secrets?”* And the answer is simple: While CAPTCHAs make things slightly harder for human victims, they make things significantly harder for the Defender’s **Detonators** — if an automated security scanner can’t get to the final URL, it cannot evaluate its phishyness.

After the user has been successfully lured to a credential collection page, the attacker bears some risk: the would-be victim might [report the phish](https://textslashplain.com/2023/01/19/defense-techniques-reporting-phish/) to URL reputation services. To mitigate that risk, the attacker might rely on *[cloaking](https://textslashplain.com/2023/01/19/defense-techniques-reporting-phish/#:~:text=Attacker%20Technique%3A%20Cloaking%20from%20Graders)* techniques, so that graders cannot “see” the phishing attack when they check the false negative report.

Similarly, the would-be victim might themselves report the URL directly to the phisher’s web host, who often has no idea that they’re facilitating a criminal enterprise.

To avoid getting their sites taken offline by hosting providers, attackers may split their attack across multiple servers, with the credential **Request** happening at one URL, and the user’s stolen data sent to be **Record**ed on another domain entirely. That way, if only **Request** URL is taken down, the attacker can still collect their plunder from the other domain.

### Proxy-Type Services

An attack I saw today utilized several of these techniques all at once. The attacker sent a lure with a URL pointing to a Google-owned **translate.goog** domain. That URL was itself just acting as a *proxy* for a Cloudflare **IPFS** gateway. [IPFS is a new-ish technology](https://en.wikipedia.org/wiki/InterPlanetary_File_System) that’s not supported by most browsers yet, but it has a *huge* benefit to attackers in that Authorities have no good way to “take down” content served via IPFS, although there’s a [bad bits list](https://badbits.dwebops.pub/).

To enable the attack page to be reachable by normal users’ browsers (which don’t natively support IPFS), the attackers supply a URL to a Cloudflare IPFS gateway, a special webservice that allows browsers to retrieve IPFS content using plain-old HTTPS. In this case, neither Google nor Cloudflare recognizes that they’re facilitating the attack, as neither of them is really acting as a “Web server” in any traditional sense.

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-22.png?w=1002)](https://textslashplain.com/wp-content/uploads/2023/03/image-22.png)

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-23.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/03/image-23.png)

Even if Google Translate and Cloudflare eventually *do* block the malicious URLs, the attacker can easily pick a different proxy service and a different IPFS gateway, without even having to republish their attack elsewhere on IPFS. The design of IPFS makes it harder to ever discover who’s behind the malicious page.

Now, *storing* data back to IPFS is a somewhat harder challenge for attackers, so this phishing site uses a different server for that purpose. The “KikiCard” URL used by the attackers receives POST requests with victims’ credentials, stores those credentials into a database...