---
title: OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector
url: https://any.run/cybersecurity-blog/oauth-device-code-phishing/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-10
fetch_date: 2026-03-11T04:05:14.139784
---

# OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector](/cybersecurity-blog/wp-content/uploads/2026/03/M365-Accounts-Under-Attack.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector

March 10, 2026

[Add comment](#comments-18987)
6 views
10 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/03/M365-Accounts-Under-Attack-1024x497.png)

  #### OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector

  6
  0](/cybersecurity-blog/oauth-device-code-phishing/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/Threat-coverage-updates-1024x497.png)

  #### Threat Coverage Digest: New Malware Reports and 2,400+ Detection Rules

  150
  0](/cybersecurity-blog/threat-coverage-digest-february-2026/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/5-Major-Cyber-Attacks-in-February-2026_cover-1024x497.png)

  #### Major Cyber Attacks in February 2026: BQTLock, Thread-Hijack Phishing, and MFA Bypass Evolution

  359
  0](/cybersecurity-blog/february-26-attacks/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

OAuth Device Code Phishing: A New Microsoft 365 Account Breach Vector

ANY.RUN’s analysts are observing a sharp increase in phishing activity abusing Microsoft’s OAuth Device Code flow, with more than 180 phishing URLs detected in just one week.

This technique represents a shift from credential [phishing](https://any.run/phishing/) to token-based account takeover, making detection significantly harder for many SOC teams.

## Key Takeaways

* **OAuth Device Code phishing is rising rapidly.**Campaigns abusing Microsoft’s Device Authorization Grant are increasing, with hundreds of phishing URLs appearing in short timeframes.

* **Account takeover can occur without credential theft.**Victims authenticate on legitimate Microsoft pages, yet attackers still receive OAuth tokens that grant account access.

* **The attack abuses legitimate authentication flows.**Threat actors initiate the device authorization process themselves and trick victims into approving it.

* **Token abuse replaces password theft.**Access tokens and refresh tokens allow attackers to operate within Microsoft 365 without needing stolen credentials.

* **Encrypted HTTPS traffic hides attack signals.**Because activity happens on legitimate domains and encrypted channels, detection using traditional indicators becomes harder.

* **Automatic SSL decryption improves detection speed.**ANY.RUN Sandbox extracts SSL keys from process memory to decrypt HTTPS traffic, revealing hidden scripts and network activity that enable faster investigations and reduced MTTD and MTTR.

## How the Attack Works

In this campaign, attackers abuse Microsoft’s **device login process**, which is normally used to sign in on devices that cannot display a full login page.

The attacker first initiates a login request with Microsoft. This generates two values:

* **user\_code** — a short, human-readable code (e.g., EL4BGRHUZ) displayed on the fake page as a “verification code;”

* **device\_code** — an internal session identifier held only by the attacker, never shown to the victim. This is the ‘claim ticket’ the attacker uses to poll Microsoft’s token endpoint.

The victim is then shown the **user\_code** on a phishing page, often disguised as a document verification step (for example, a fake DocuSign notification). The page instructs the user to copy the code and enter it at **microsoft[.]com/devicelogin**.

From the user’s perspective, everything appears legitimate. They are redirected to a real Microsoft page, where they enter their credentials and complete MFA.

However, by entering the verification code, the user is unknowingly approving a login request that was initiated by the attacker. While the victim sees only the **user\_code**, the attacker uses the associated **device\_code** to collect authentication tokens from Microsoft once the approval is completed.

Microsoft then issues **access tokens** to the attacker’s session, allowing them to access the victim’s Microsoft 365 account. Because the login happens through legitimate Microsoft infrastructure, no credentials are stolen on the phishing page and no fake login form is required.

## Why This Attack Poses a Critical Risk and Is Harder for SOC Teams to Detect

OAuth Device Code phishing changes how account compromise happens. This campaign represents a structural shift:

* The victim interacts with legitimate Microsoft domains;

* Credentials and MFA are entered on authentic pages;

* The attack runs entirely over encrypted HTTPS;

* Traditional phishing indicators may not trigger.

As a result, token abuse replaces password theft. Detection relies heavily on visibility into encrypted network traffic and behavioral artifacts rather than domain reputation alone.

For SOC teams, this means:

* **Delayed detection**: Account compromise may only be noticed after suspicious activity appears.

* **Longer investigations**: Analysts must reconstruct token-based access rather than analyze credential theft.

* **Higher incident impact**: Attackers can operate inside Microsoft 365 immediately after token issuance.

**For organizations, this creates a critical risk**: attackers can immediately access corporate email, internal documents, and shared resources, impersonate employees in business email compromise schemes, and potentially maintain persistent access through refresh tokens, turning a single phishing interaction into **data exposure, financial fraud, or broader account compromise**.

## OAuth Device Code...