---
title: GitPhish – OAuth Device Code Phishing for GitHub Repos, Secrets, and CI/CD
url: https://www.darknet.org.uk/2025/06/gitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-21
fetch_date: 2025-10-06T22:54:59.356016
---

# GitPhish – OAuth Device Code Phishing for GitHub Repos, Secrets, and CI/CD

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# GitPhish – OAuth Device Code Phishing for GitHub Repos, Secrets, and CI/CD

June 20, 2025

Views: 689

GitPhish is an automated tool that exploits GitHub’s OAuth device code flow to gain unauthorised access to user accounts. Developed by Praetorian, it demonstrates how attackers can use legitimate GitHub functionality to trick users into granting access to repositories, secrets, and CI/CD pipelines.

![GitPhish - OAuth Device Code Phishing for GitHub Repos, Secrets, and CICD](data:image/svg+xml...)![GitPhish - OAuth Device Code Phishing for GitHub Repos, Secrets, and CICD](https://www.darknet.org.uk/wp-content/uploads/2025/06/GitPhish-OAuth-Device-Code-Phishing-for-GitHub-Repos-Secrets-and-CICD-640x427.jpg)

The attack does not rely on spoofed login pages. Instead, it generates real device codes through GitHub’s API, delivers them through custom GitHub Pages sites, and captures the resulting OAuth tokens once a user approves the request.

GitPhish will be publicly released on June 26, 2025.

## Overview

GitHub’s device code flow allows devices without a browser to authenticate users via a separate interface. Users are asked to go to `https://github.com/login/device` and enter a code to complete the login. This mechanism is designed for ease of use but introduces a phishing opportunity: if an attacker can convince a user to enter a malicious device code, they gain full access granted by that token.

GitPhish automates this attack chain.

## Key Features

* Generates GitHub OAuth2 device codes automatically
* Hosts phishing payloads on GitHub Pages
* Captures and stores valid OAuth tokens upon successful user authorisation
* Provides access to private repositories, secrets, GitHub Actions, and CI/CD integrations
* No need for password interception or fake login forms

## Security Implications

This technique is currently not preventable by GitHub organisation policies. The device flow cannot be globally disabled. Most developers will not recognise malicious code or a delivery URL if it appears to come from GitHub infrastructure.

Security teams should review GitHub OAuth usage, revoke unnecessary tokens, and regularly audit external application authorisations. Additional monitoring should be in place for unusual authorisation events.

## Installation and Usage

GitPhish is expected to be released under an open-source license on June 26. Installation will likely follow standard Python-based toolchain procedures. Based on the pre-release write-up, usage will follow a workflow similar to the one shown below.

# Clone the repository
git clone https://github.com/praetorian-inc/gitphish.git
cd gitphish
# Install dependencies
pip install -r requirements.txt
# Launch phishing server and generate new device code
python gitphish.py --start
# Monitor incoming OAuth tokens
tail -f logs/tokens.log

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | # Clone the repository  git clone https://github.com/praetorian-inc/gitphish.git  cd gitphish    # Install dependencies  pip install -r requirements.txt    # Launch phishing server and generate new device code  python gitphish.py --start    # Monitor incoming OAuth tokens  tail -f logs/tokens.log |

More detailed usage documentation will be available upon release.

## Mitigation Recommendations

* Enforce GitHub SSO wherever possible
* Regularly audit OAuth applications and tokens via the GitHub API
* Train developers to avoid authorising unsolicited device login requests
* Consider limiting developer GitHub access from unmanaged endpoints

You can read more here: [Introducing: GitHub Device Code Phishing](https://www.praetorian.com/blog/introducing-github-device-code-phishing/)

## Related Posts:

* [ChromeAlone - Chromium Browser C2 Implant for Red…](https://www.darknet.org.uk/2025/08/chromealone-chromium-browser-c2-implant-for-red-team-operations/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [TREVORspray - Credential Spray Toolkit for Azure,…](https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/)
* [evilreplay - Real-Time Browser Session Hijack…](https://www.darknet.org.uk/2025/07/evilreplay-real-time-browser-session-hijack-without-cookie-theft/)
* [Privacy Implications of Web 3.0 and Darknets](https://www.darknet.org.uk/2023/03/privacy-implications-of-web-3-0-and-darknets/)
* [thermoptic - Chrome-perfect HTTP Fingerprint…](https://www.darknet.org.uk/2025/09/thermoptic-chrome-perfect-http-fingerprint-cloaking-for-red-team-web-ops/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fgitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd%2F)

[Tweet](https://twitter.com/intent/tweet?text=GitPhish+-+OAuth+Device+Code+Phishing+for+GitHub+Repos%2C+Secrets%2C+and+CI%2FCD&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fgitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fgitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fgitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd%2F&text=GitPhish+-+OAuth+Device+Code+Phishing+for+GitHub+Repos%2C+Secrets%2C+and+CI%2FCD)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fgitphish-oauth-device-code-phishing-for-github-repos-secrets-and-ci-cd%2F)

[Email](/cdn-cgi/l/email-protection#f7c88482959d929483cab09e83a79f9e849fd2c5c7dad2c5c7b8b682839fd2c5c7b392819e9492d2c5c7b4989392d2c5c7a79f9e849f9e9990d2c5c7919885d2c5c7b09e83bf8295d2c5c7a592879884d2c5b4d2c5c7a4929485928384d2c5b4d2c5c7969993d2c5c7b4bed2c5b1b4b3d19598938ecab09e83a79f9e849fd2c5c79e84d2c5c79699d2c5c7968283989a96839293d2c5c78398989bd2c5c7839f9683d2c5c7928f879b989e8384d2c5c7b09e83bf8295d2c5c084d2c5c7b8b682839fd2c5c79392819e9492d2c5c794989392d2c5c7919b9880d2c5c78398d2c5c790969e99d2c5c782999682839f98859e8d9293d2c5c7969494928484d2c5c78398d2c5c785928798849e8398859e9284d2c5b4d2c5c784929485928384d2c5b4d2c5c7969993d2c5c7b4bed2c5b1b4b3d2c5c7848e8483929a84d9d2c5c7bb92968599d2c5c79f9880d2c5c79e83d2c5c78098859c84d2c5b4d2c5c79f9880d2c5c78398d2c5c7828492d2c5c79e83d2c5b4d2c5c7969993d2c5c79f9880d2c5c78398d2c5c79a9e839e90968392d2c5c7839f9e84d2c5c7929a9285909e9990d2c5c7879f9e849f9e9990d2c5c78392949f999e868292d9d2c7b3d2c7b6d2c7b3d2c7b6a5929693d7ba988592d7bf928592cdd7d2c5c79f83838784d2c4b6d2c5b1d2c5b1808080d99396859c999283d9988590d9829cd2c5b1c5c7c5c2d2c5b1c7c1d2c5b1909e83879f9e849fda989682839fda9392819e9492da94989392da879f9e849f9e9990da919885da909e839f8295da8592879884da84929485928384da969993da949eda9493d2c5b1)

Filed Under: [Secure Coding](https://www.darknet.org.uk/category/sec...