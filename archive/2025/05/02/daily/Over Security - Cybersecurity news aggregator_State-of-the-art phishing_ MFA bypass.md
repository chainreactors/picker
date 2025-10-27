---
title: State-of-the-art phishing: MFA bypass
url: https://blog.talosintelligence.com/state-of-the-art-phishing-mfa-bypass/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-02
fetch_date: 2025-10-06T22:30:58.293321
---

# State-of-the-art phishing: MFA bypass

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# State-of-the-art phishing: MFA bypass

By
[Jaeson Schultz](https://blog.talosintelligence.com/author/jaeson-schultz/)

Thursday, May 1, 2025 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)
[phishing](https://blog.talosintelligence.com/category/phishing/)
[MFA](https://blog.talosintelligence.com/category/mfa/)

* Cybercriminals are bypassing multi-factor authentication (MFA) using adversary-in-the-middle (AiTM) attacks via reverse proxies, intercepting credentials and authentication cookies.
* The developers behind Phishing-as-a-Service (PhaaS) kits like Tycoon 2FA and Evilproxy have added features to make them easier to use and harder to detect.
* WebAuthn, a passwordless MFA solution using public key cryptography, prevents password transmission and nullifies server-side authentication databases, offering a robust defense against MFA bypass attacks.
* Despite its strong security benefits, WebAuthn has seen slow adoption. Cisco Talos recommends that organizations reassess their current MFA strategies in light of these evolving phishing threats.

---

For the past thirty years, phishing has been a staple in many cybercriminals' arsenals. All cybersecurity professionals are familiar with phishing attacks: Criminals impersonate a trusted site in an attempt to social engineer victims into divulging personal or private information such as account usernames and passwords. In the early days of phishing, it was often enough for cybercriminals to create fake landing pages matching the official site, harvest authentication credentials and use them to access victims’ accounts.

Since that time, network defenders have endeavored to prevent these types of attacks using a variety of techniques. Besides implementing strong anti-spam systems to filter phishing emails out of users’ inboxes, many organizations also conduct simulated phishing attacks on their own users to train them to recognize phishing emails. These techniques worked for a time, but as phishing attacks have become more sophisticated and more targeted, spam filters and user training have become less effective.

At the root of this problem is the fact that usernames are often easy to guess or discover, and people are generally [very bad at using strong passwords](https://blog.talosintelligence.com/threat-source-newsletter-may-2-2024/). People also tend to re-use the same weak passwords across many different sites. Cybercriminals, armed with a victim’s username and password, will often attempt credential stuffing attacks, and log into many different sites using the same username/password combination.

To prove that users are valid, authentication systems generally rely on at least one of three authentication methods or factors:

* Something you **know** (*ex. a username and password*)
* Something you **have** (*ex. a smartphone or USB key*)
* Something you **are** (*ex. your fingerprint or face recognition*)

In the presence of increasingly sophisticated phishing messages, using only one [authentication factor](https://blog.talosintelligence.com/what-might-authentication-attacks-look-like-in-a-phishing-resistant-future/), such as a username/password, is problematic. Many network defenders have responded by implementing MFA, which includes an additional factor, such as an SMS message or push notification, as an extra step to confirm a user’s identity when logging in. By including an additional factor in the authentication process, compromised usernames and passwords become much less valuable to cybercriminals. However, cybercriminals are a creative bunch, and they have devised a clever way around MFA. Enter the wild world of MFA bypass!

## How do attackers bypass MFA?

In order to bypass MFA, attackers insert themselves into the authentication process using an [adversary-in-the-middle (AiTM) attack](https://csrc.nist.gov/glossary/term/man_in_the_middle_attack).

Typically, this is done using a reverse proxy. A reverse proxy functions as an intermediary server, accepting requests from the client before forwarding them on to the actual web servers to which the client wishes to connect.

To bypass MFA the attacker sets up a reverse proxy and sends out phishing messages as normal. When the victim connects to the attacker’s reverse proxy, the attacker forwards the victim’s traffic onwards to the real site. From the perspective of the victim, the site they have connected to looks authentic — and it is! The victim is interacting with the legitimate website. The only difference perceptible to the victim is the location of the site in the web browser’s address bar.

By inserting themselves in the middle of this client-server communication the attacker is able to intercept the username and password as it is sent from the victim to the legitimate site. This completes the first stage of the attack and triggers an MFA request sent back to the victim from the legitimate site. When the expected MFA request is received and approved, an authentication cookie is returned to the victim through the attacker’s proxy server where it is intercepted by the attacker. The attacker now possesses both the victim’s username/password as well as an authentication cookie from the legitimate site.

![](https://blog.talosintelligence.com/content/images/2025/04/data-src-image-4cd00da6-7e8d-4009-893b-f577960d330e.jpeg)

**Figure 1. Flow diagram illustrating MFA bypass using a reverse proxy.**

## Phishing-as-a-Service (PhaaS) kits

Thanks to turnkey Phishing-as-a-Service (Phaas) toolkits, almost anyone can conduct these types of phishing attacks without knowing much about what is happening under the hood. Toolkits such as Tycoon 2FA, Rockstar 2FA, Evilproxy, [Greatness](https://blog.talosintelligence.com/new-phishing-as-a-service-tool-greatness-already-seen-in-the-wild/), Mamba 2FA and more...