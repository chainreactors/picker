---
title: One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens
url: https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html
source: The Hacker News
date: 2026-06-03
fetch_date: 2026-06-04T06:32:18.299184
---

# One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens](https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html)

**Ravie Lakshmanan**Jun 03, 2026Vulnerability / Software Development

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeHvqmNHvAhdxgoBLbfFWsFBMdvH5SbJovunxx8AYHRkq7HOQ2l6I_ZaJGi_PF5WHKOlHEQHK4HyPBhmzOpYNhPS4HJSna2uLVlEwUV9i2j5YuRqGOLUqgKIrhx2ndFm1OSME7usiLk_ohtIBYyR5Xpq5Pzc2eHAjCK0OA_89JwPNxVrrBVDbTDRVbRG6e/s1700-e365/github.jpg)

Cybersecurity researchers have disclosed a one-click attack via Microsoft Visual Studio Code (VS Code) that makes it possible to steal a user's GitHub token.

"Just by clicking a link, it's possible for an attacker to steal a GitHub token that can read and write to your repos, including private ones," security researcher Ammar Askar [said](https://blog.ammaraskar.com/github-token-stealing/).

GitHub supports a feature called [GitHub.dev](https://github.com/github/dev) that runs as a [lightweight web-based source code editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor) in the web browser's sandbox by launching a VS Code environment. It allows users to send pull requests and make commits.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"This functionality is achieved by github.com POSTing over an OAuth token to github.dev that allows it to interact with GitHub on your behalf," Askar said. "The token is not scoped to the particular repo you interacted with, meaning it has full access to every other repo that you have access to."

In a nutshell, the vulnerability allows attackers to install malicious VS Code extensions that steal GitHub OAuth tokens when they are passed to GitHub.dev by exploiting a [message-passing mechanism](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) between the main VS Code window and [webviews](https://code.visualstudio.com/api/extension-guides/webview). Webviews are used to render Markdown previews or edit Jupyter notebooks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvwh3V2izKKwTcZio2TXCLwYguXnmEBARQ2F9lsZOTAXj6qdB71X__WJOL8BsZvx05qEMO6J7Fuvfn35rGIy6akT9V32tgLRBdT9kBCoNljwIRVk0TjNFvn5EqjQFiWSGwJs-Jubttfxnwfd2k5MqmGpzNFq0ahugsB7WjMv4gFpqdRvSXHKEFyPJFtwU1/s1700-e365/git.png)

Specifically, the exploit runs malicious JavaScript inside an untrusted webview to simulate keypresses (aka keydown events) in the main editor window, open the Command Palette by triggering "Ctrl+Shift+P," and install an attacker-controlled extension that extracts the GitHub OAuth token sent to GitHub.dev and queries the GitHub API to enumerate all private repositories the victim can access.

It's worth noting the approach also leverages a VS Code feature called [local workspace extensions](https://code.visualstudio.com/updates/v1_89#_local-workspace-extensions) that allows an extension to be directly installed without presenting any additional [trust dialog prompt](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security#_extension-publisher-trust) as long as it's placed in the ".vscode/extensions" folder within that workspace, effectively bypassing the publisher trust check.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"This is just a small hiccup though, one of the things that extensions can do as part of their package.json is to contribute extra keybindings to VS Code," the researcher explained. "Since we can reliably trigger keybindings, we can just add a keybind for whatever VS Code command we want, such as installing an extension while skipping the trusted publisher check."

The researcher also noted GitHub was [notified](https://github.com/microsoft/vscode/issues/319593) of the vulnerability on June 2, 2026, an hour after which details of the issue were made public knowledge, citing Microsoft's [handling](https://blog.ammaraskar.com/vscode-rce/) of [VS Code-related bugs](https://starlabs.sg/blog/2025/05-breaking-out-of-restricted-mode-xss-to-rce-in-visual-studio-code/) in the past. As of writing, Microsoft has acknowledged the vulnerability and noted that it's working on a fix.

"To clarify, this issue does not affect VS Code Desktop," Alexandru Dima, a partner software engineering manager at Microsoft, said.

### Update

Following the publication of the story, Microsoft told The Hacker News that the vulnerability has been addressed. "This issue has been mitigated for our services and no customer action is required," a Microsoft spokesperson said.

*(The story was updated after publication to include a response from Microsoft.)*

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
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[browser security](https://thehackernews.com/search/label/browser%20security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Extension Security](https://thehackernews.com/search/label/Extension%20Security), [GitHub](https://thehackernews.com/search/label/GitHub), [Microsoft](https://thehackernews.com/search/label/Microsoft), [OAuth](https://thehackernews.com/search/label/OAuth), [Soft...