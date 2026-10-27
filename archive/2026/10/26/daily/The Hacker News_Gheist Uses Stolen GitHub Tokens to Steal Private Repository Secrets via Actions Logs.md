---
title: Gheist Uses Stolen GitHub Tokens to Steal Private Repository Secrets via Actions Logs
url: https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html
source: The Hacker News
date: 2026-10-26
fetch_date: 2026-10-27T07:05:44.341066
---

# Gheist Uses Stolen GitHub Tokens to Steal Private Repository Secrets via Actions Logs

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Gheist Uses Stolen GitHub Tokens to Steal Private Repository Secrets via Actions Logs](https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html)

**Swati Khandelwal**Oct 26, 2026Cyber Attack / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipCbP2hnS9ddXqMz9cNIAMEQZWy2qX45MZnYfIuO_Zszamhl_FS7ViRp4CZcjHS6uu6A4jR_S4vBzHzoMNtAb0CbaGxHxj2F07wuKWHfSbsFUov-4dsQWUNJZwfGbnfThW1sAQZ61y5ibqyhlW1iBmbWeSwE1gKHsigRRXaql9P96aFANb3al6vno7fuA/s1700-nu-rw-lo-l85-e365/github-secrets.jpg)

An automated campaign is using stolen GitHub tokens to plant workflows that print a repository's secrets into its GitHub Actions logs, which the attackers then download before deleting the runs. The attacks have succeeded in private repositories and GitHub Enterprise environments, according to an analysis by cloud security company Wiz.

A [GitHub safeguard](https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval/) that pauses suspicious workflow runs stopped every public-repository run Wiz checked, but it does not cover private repositories or GitHub Enterprise Server.

Each workflow sits on a new branch named ci-sync- followed by six random characters. Deleting a branch, or the run it started, does not undo the exposure. Every secret the repository could read should be rotated, and the token that pushed the branch revoked.

Wiz has tracked the campaign since September 15 and calls it [Gheist](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles), after the user agent gheist that the attackers' tool sends with GitHub API requests.

Wiz has recovered more than 13,500 planted branches from more than 850 compromised accounts, from personal projects to the private repositories of enterprise organizations. Wiz's analysis does not say how many organizations had secrets exposed.

In private repositories and on GitHub Enterprise Server, GitHub audit logs show runs on the planted branches finishing and then being deleted by the gheist user agent. AWS CloudTrail logs show the organization's own workflows also running on those branches and assuming AWS roles, a sign that GitHub Actions ran there without approval.

In enterprise organizations, the tool cycled through tokens from several users and automation accounts within minutes and cloned private repositories before planting the workflow. Hours later, cloud credentials from the same organization were used to enumerate AWS Secrets Manager. Wiz's analysis does not say where those credentials came from or who used them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

As of October 24, the campaign was still running and changing. About two-thirds of the accounts involved were no longer available on GitHub. Wiz reported the activity to GitHub and says their disappearance likely reflects a response.

Anyone with write access to a GitHub repository can read every secret configured in it, according to [GitHub's documentation](https://docs.github.com/en/actions/reference/security/secure-use). A stolen token with that access is enough.

For each repository a token can reach, the tool creates a ci-sync- branch and commits one file, .github/workflows/sync-check.yml, with the message ci: sync config. The commit is unsigned and includes the token owner's name; pushing it starts the workflow.

The workflow prints the job's environment and every secret the job can read, encoded in base32. GitHub masks secrets in logs, but its documentation says this is not guaranteed once a value has been encoded or otherwise changed. Wiz says the base32 text no longer matches the original secret, so it prints in full.

The workflow sets an empty permissions block. That limits the job's GITHUB\_TOKEN, which the attackers do not need, and does not stop the job from reading secrets.

One version of the tool also runs a job for each deployment environment in the repository, so secrets limited to those environments print too. These are often production credentials, according to Wiz.

The tool then downloads the log through GitHub's API and deletes the run seconds later. Because the secrets leave through GitHub itself, there is no attacker server or outbound connection to block.

Since July 28, GitHub has held workflow runs it identifies as potentially malicious until a collaborator with write access approves them. GitHub says the hold "currently applies to public repositories on github.com only" and that GitHub Enterprise Server does not have it at this time.

Every public Gheist run Wiz checked, across all versions of the tool, was still waiting for approval, so its payload never ran.

The hold only catches runs that GitHub flags. A new variant of [GhostAction](https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html), a separate campaign, ran in public repositories until GitHub began blocking it on October 9, according to [research from security company GitGuardian](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/). Wiz says Gheist is distinct from GhostAction, which uses different workflow files.

Around October 19, one version of the tool began pushing a second job meant for self-hosted runners, the machines organizations run themselves to process GitHub Actions jobs. It appears to target only repositories that have such a runner registered.

The job is written to search the runner machine for credentials, including 31 types of tokens: private keys, process environments, AWS instance role credentials, runner credential files, and the Kubernetes service account token. Wiz describes the job as buggy, and its analysis reports no successful run.

The sources Wiz could trace for the stolen tokens include infostealer logs and tokens exposed in earlier supply-chain attacks, such as the [March compromise of the Trivy vulnerability scanner](https://thehackernews.com/20...