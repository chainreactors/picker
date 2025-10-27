---
title: Critical Unpatched Flaws Disclosed in Popular Gogs Open-Source Git Service
url: https://thehackernews.com/2024/07/critical-vulnerabilities-disclosed-in.html
source: The Hacker News
date: 2024-07-09
fetch_date: 2025-10-06T17:47:33.078878
---

# Critical Unpatched Flaws Disclosed in Popular Gogs Open-Source Git Service

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Critical Unpatched Flaws Disclosed in Popular Gogs Open-Source Git Service](https://thehackernews.com/2024/07/critical-vulnerabilities-disclosed-in.html)

**Jul 08, 2024**Ravie LakshmananVulnerability / Software Security

[![Gogs Open-Source Git Service](data:image/png;base64... "Gogs Open-Source Git Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZSlSdNUZX8YGmOyBqpQdzdGlCvZVE4Tmtxeq9sP_mypbYT50IPItTus60WQ0rwcChxQ1QLnb3ltlAVHrRa-szpXkLk_EBn-A-eeXVy6m3N2U11sVbnzEN9maptC4OR5I1DUlddajxc_0HjaitPQuNyM-iihLYIwlpwYEa7cvlL9aoQTUmYfz5sUMHxn-B/s790-rw-e365/gogs.png)

Four unpatched security flaws, including three critical ones, have been disclosed in the [Gogs](https://gogs.io/) open-source, self-hosted Git service that could enable an authenticated attacker to breach susceptible instances, steal or wipe source code, and even plant backdoors.

The vulnerabilities, according to SonarSource researchers Thomas Chauchefoin and Paul Gerste, are listed below -

* **CVE-2024-39930** (CVSS score: 9.9) - Argument injection in the built-in SSH server
* **CVE-2024-39931** (CVSS score: 9.9) - Deletion of internal files
* **CVE-2024-39932** (CVSS score: 9.9) - Argument injection during changes preview
* **CVE-2024-39933** (CVSS score: 7.7) - Argument injection when tagging new releases

Successful exploitation of the first three shortcomings could permit an attacker to execute arbitrary commands on the Gogs server, while the fourth flaw allows attackers to read arbitrary files such as source code, and configuration secrets.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In other words, by abusing the issues, a threat actor could read source code on the instance, modify any code, delete all code, target internal hosts reachable from the Gogs server, and impersonate other users and gain more privileges.

That said, all four vulnerabilities require that the attacker be authenticated. Furthermore, triggering CVE-2024-39930 necessitates that the built-in SSH server is enabled, the version of the env binary used, and the threat actor is in possession of a valid SSH private key.

"If the Gogs instance has registration enabled, the attacker can simply create an account and register their SSH key," the researchers [said](https://www.sonarsource.com/blog/securing-developer-tools-unpatched-code-vulnerabilities-in-gogs-1/). "Otherwise, they would have to compromise another account or steal a user's SSH private key."

Gogs instances running on Windows are not exploitable, as is the Docker image. However, those running on Debian and Ubuntu are vulnerable due to the fact that the env binary supports the "--split-string" option.

[![Gogs Open-Source Git Service](data:image/png;base64... "Gogs Open-Source Git Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyZBwedZ_Y3e3uJmctmg7RkVXZqsfOAWskI4ski5NWnETsJ1TB39BBAwxCaDgOnV4ElyfJL_xwd4Susy_KXShCwTOeGgkIJGbf0hQHDvLAPRxD6Qi54m36ngvLuGSpxzfGTdSEdiucfi1t5i63nQxu2WeEo4fEk2LZs_NutclEJZgukM4bKyfuK7_tiQre/s790-rw-e365/shodan.jpg)

According to data available on Shodan, around 7,300 Gogs instances are publicly accessible over the internet, with nearly 60% of them located in China, followed by the U.S., Germany, Russia, and Hong Kong.

It's currently not clear how many of these exposed servers are vulnerable to the aforementioned flaws. SonarSource said it does not have any visibility into whether these issues are being exploited in the wild.

The Swiss cybersecurity firm also pointed out that the project maintainers "did not implement fixes and stopped communicating" after accepting its initial report on April 28, 2023.

In the absence of an update, users are recommended to disable the built-in SSH server, turn off user registration to prevent mass exploitation, and consider switching to Gitea. SonarSource has also [released a patch](https://gist.githubusercontent.com/paul-gerste-sonarsource/207f5dc79f59bb256a0bfccda4e3e92b/raw/Gogs-security-fixes-by-Sonar.patch) that users can apply, but noted it hasn't been extensively tested.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as cloud security firm Aqua discovered that sensitive information such as access tokens and passwords once hard-coded could remain permanently exposed even after removal from Git-based source code management (SCM) systems.

Dubbed phantom secrets, the issue stems from the fact that they cannot be discovered by any of the conventional scanning methods – most of which look for secrets using the "git clone" command – and that certain secrets are accessible only via "git clone --mirror" or cached views of SCM platforms, highlighting the blind spots that such scanning tools may miss.

"Commits remain accessible through 'cache views' on the SCM," security researchers Yakir Kadkoda and Ilay Goldman [said](https://www.aquasec.com/blog/undetected-hard-code-secrets-expose-corporations/). "Essentially, the SCM saves the commit content forever."

"This means that even if a secret containing commit is removed from both the cloned and mirrored versions of your repository, it can still be accessed if someone knows the commit hash. They can retrieve the commit content through the SCM platform's GUI and access the leaked secret."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share...