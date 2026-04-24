---
title: Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign
url: https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html
source: The Hacker News
date: 2026-04-23
fetch_date: 2026-04-24T04:57:38.111929
---

# Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

# [Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html)

**Ravie Lakshmanan**Apr 23, 2026Supply Chain Attack / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3GuK50sJwMRH4ad8bcUVRSBm1Wk0X5Gj1dSalza49wWxFY9g3_E32271zOeqx6vsqrWY2SWAVnnXTKiJZvKbhxynk018zLTIlZpBNhFA_QVi6kzn7vATBe419m222ZMUcTToaSn19L4DgElrI9luwUv2EJk0efy5TLDIqIUyGcOnTvVU2KKZw9AMsMipz/s1700-e365/bitwarden.jpg)

[Bitwarden CLI](https://www.npmjs.com/package/%40bitwarden/cli?activeTab=versions) has been compromised as part of the newly discovered and ongoing [Checkmarx supply chain campaign](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html), according to new findings from JFrog and Socket.

"The affected package version appears to be [@bitwarden/cli@2026.4.0](https://socket.dev/npm/package/%40bitwarden/cli/overview/2026.4.0), and the malicious code was published in 'bw1.js,' a file included in the package contents," the application security company [said](https://socket.dev/blog/bitwarden-cli-compromised).

"The attack appears to have leveraged a compromised GitHub Action in Bitwarden's CI/CD pipeline, consistent with the pattern seen across other affected repositories in this campaign."

In a post on X, JFrog [said](https://x.com/JFrogSecurity/status/2047268576071991766) the rogue version of the package "steals GitHub/npm tokens, .ssh, .env, shell history, GitHub Actions and cloud secrets, then exfiltrates the data to private domains and as GitHub commits."

Specifically, the malicious code is [executed](https://research.jfrog.com/post/bitwarden-cli-hijack/) by means of a preinstall hook, resulting in the theft of local, CI, GitHub, and cloud secrets. The data is exfiltrated to the domain "audit.checkmarx[.]cx" and to a GitHub repository as a fallback if the primary method fails.

The entire series of actions is listed below -

* It launches a credential stealer that targets developer secrets, GitHub Actions environments, and artificial intelligence (AI) coding tool configurations, including Claude, Kiro, Cursor, Codex CLI, and Aider.
* The stolen data is encrypted with AES-256-GCM and exfiltrated to audit.checkmarx[.]cx, a domain impersonating Checkmarx.
* If GitHub tokens are found, the malware weaponizes them to inject malicious Actions workflows into repositories and extract CI/CD secrets.

"A single developer with @bitwarden/cli@2026.4.0 installed can become the entry point for a broader supply chain compromise, with the attacker gaining persistent workflow injection access to every CI/CD pipeline the developer’s token can reach," StepSecurity [said](https://www.stepsecurity.io/blog/bitwarden-cli-hijacked-on-npm-bun-staged-credential-stealer-targets-developers-github-actions-and-ai-tools).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

While the malicious version is no longer available for download from npm, Socket said the compromise follows the same GitHub Actions supply chain vector identified in the Checkmarx campaign.

As part of the effort, threat actors have been [found](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html) abusing stolen GitHub tokens to inject a new GitHub Actions workflow that captures secrets available to the workflow run, and uses harvested npm credentials to push malicious versions of the package to read the malware to downstream users.

According to security researcher Adnan Khan, the threat actor is said to have used a [malicious workflow](https://github.com/bitwarden/clients/blob/03df1ecd86132e06643d24c856d8976d1b497945/.github/workflows/publish-cli.yml) to publish the malicious bitwarden CLI. "I believe this is the first time a package using NPM trusted publishing has been compromised," Khan [added](https://x.com/adnanthekhan/status/2047276201429897679).

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7Djs-LF6-TUTPhW__KznM3E0FahhC8Ge3hRMmNCRmf3M0F89y8LQjEY3al6a8vPvT4vjrbTLVXJWzXWb3r68yi57taHpJdwAdd_thHvHsJcqi8lIUYCyuQGRsyjEv7dzegt1Ik5sCZoYkDl_pt_mMqOApcXJhFkXaq5f5ZrG-PyA9cOUTFrHU3KOYW3Go/s1700-e365/ox.jpg) |
| Bitwarden CLI Attack Chain | Source: OX Security |

It's suspected that the threat actor known as TeamPCP is behind the latest attack aimed at Checkmarx. As of writing, TeamPCP's [X account has been suspended](https://x.com/pcpcats/) for violating the platform's rules.

OX Security, in a breakdown of the attack, [said](https://www.ox.security/blog/shai-hulud-bitwarden-cli-supply-chain-attack/) it identified the string "Shai-Hulud: The Third Coming" in the package, suggesting this could likely be the next phase of the [supply chain attack campaign](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html) that came to light last year.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiDMclt2TvjTiNyzD2rqmFpktPvAn2G_8b7fSq1EzMwmQQGDiDnyc658CoQA1GLMrDBRZ5oHBsGyOPIm4-89s2Vl1mY_7NC2RJHWrvsRSYPDJvtwPmQJmJcpkcKrc1cJ8M2GziArqNrSpb1Ujaj09WLoBlueVKhGatmuMavoRxjABJOhyphenhyphenvnK8odJMkRPF8/s1700-e365/ox-2.jpg) |
| Reference to the "Shai-Hulud: The Third Coming" |

"The latest Shai Hulud incident is just the latest in a long chain of threats targeting developers around the world. User data is being publicly exfiltrated to GitHub, often going undetected because security tools typically don't flag data being sent there," Moshe Siman Tov Bustan, Security Research Team Lead at OX Security, said.

"This makes the risk significantly more dangerous: anyone searching GitHub can potentially find and access those credentials. At that point, sensitive data is no longer in the hands of a single threat actor – it’s exposed to anyone."

Like in the case of the Checkmarx incident, the stolen data is exfiltrated to public repositories created under victim accounts using a Dune-themed naming scheme in the same format "<word>-<word>-<3 digits>. "But in an interesting shift, the malware is also designed to quit execution on systems if their locale corresponds to Russia.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-...