---
title: Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction
url: https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html
source: The Hacker News
date: 2026-11-05
fetch_date: 2026-11-06T08:41:47.563106
---

# Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction](https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html)

**Ravie Lakshmanan**Nov 05, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrZkGDnavpYu1VmQZCorYSw9PnFNh3tGXQ7YWWrZ3g6sURYj4RiS7za99akV3poXhW7GLoJw3j-baYvwyor0f_8iI3t5zk3NeXj1V1eVDMFUklqlYz629h88oYzxk3aIQPPwQF3xaw10DZTE-lEKyaojqzlLHC_DGtF91AVhXkaFNfY6Mh-qVqn86LCfQz/s1700-nu-rw-lo-l85-e365/chat.gif)

Cybersecurity researchers have [disclosed details](https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/) of a now-patched vulnerability that could be exploited to bypass Lockdown Mode protections in OpenAI ChatGPT.

Lockdown Mode was [introduced](https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html) by the artificial intelligence (AI) company in June 2026 as an optional setting to [minimize data exfiltration risks](https://help.openai.com/en/articles/20001061-lockdown-mode) arising from prompt injections.

"The flaw could enable silent chat data theft, phishing, and malware delivery, including zero-click data exfiltration in the ChatGPT desktop application," Eli Smadja, head of research at Check Point, said in a report shared with The Hacker News.

The problem stems from HTML page previews inside ChatGPT code blocks, which allow HTML content to be rendered directly within the application. Given that executing user-supplied HTML and JavaScript can introduce security risks of its own, the content is placed inside a sandbox so that it cannot access data from the app, such as cookies and local storage.

The sandbox also prevents the rendered content from communicating with external resources without user consent. Lockdown Mode acts as a security barrier, mitigating data exfiltration risk by limiting outbound network requests that could be used to transfer sensitive information to an attacker-controlled infrastructure.

However, Check Point found a loophole in the manner popup windows are handled during HTML previews that made it possible to escape the confines of the sandbox and bypass Lockdown Mode.

"The HTML preview used nested sandboxed frames, and while ChatGPT intercepted direct attempts to open new windows, the underlying sandbox permissions still allowed popups and permitted them to escape the sandbox," Smadja explained.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

"By creating another nested frame within the rendered page, it was possible to access an unmodified popup function and bypass the restrictions placed on the original HTML preview. Content opened through this route was no longer subject to the same sandbox restrictions, providing a way to circumvent the protections of Lockdown Mode."

Once the restrictions are bypassed, a threat actor can exploit the vulnerability to exfiltrate data, chat messages, or deliver malicious payloads by means of a crafted prompt, a malicious GPT, or a shared chat.

What's more, as the attacker is in complete control of the content displayed in the popup window, it could be used to render convincing social-engineering lures, such as a fake ChatGPT update, and trick the victim into downloading malware by persuading them to click on a link.

That said, the underlying issue is not limited to the Electron-based desktop environment, highlighting how weakness outside of the scope of the AI model can undermine AI security controls. Following responsible disclosure, the vulnerability was addressed by OpenAI on September 18, 2026.

"Lockdown Mode was specifically intended to reduce the possibility of data leaving a conversation through potentially malicious outbound requests, yet a weakness in another application feature provided an alternative path around that security boundary," Smadja said.

"The finding raises a broader enterprise security issue: AI security controls are only as strong as the wider application environment around them."

The disclosure comes a week after Parameter Labs [detailed](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html) a way to bypass ChatGPT's sandbox and content security policy (CSP) and take over anyone's account simply by sending an attacker-controlled public ChatGPT share link and prompting them to click the HTML preview once. If the HTML block is marked as previewable, it's opened automatically.

"An attacker could create a malicious conversation, publish it using ChatGPT's normal sharing feature, and send the link to another user," security researcher Mukul Goyal said. "When the victim opened the share, the payload executed as chatgpt[.]com with access to the victim's authenticated web session."

Check Point told The Hacker News that the two shortcomings are different vulnerabilities on the same component, with the takeover bug enabling Javascript code execution outside of the sandbox so as to make the victim call out chatgpt[.]com and perform API requests on behalf of the victim

"This demonstrates how every new feature is a chance for more vulnerabilities," the company said in a statement.

Earlier this September, Check Point also [demonstrated](https://research.checkpoint.com/2026/the-shared-clipboard-inside-the-sandbox-cross-account-data-leakage-in-chatgpt/) a covert cross-account command channel through which an attacker could use a victim's ChatGPT session to run hidden tasks with the tools, data, and connected apps available to that session, alongside the visible conversation.

"The victim could receive a normal answer to their visible request while the attacker's task was processed separately and its result returned across accounts," Check Point said. "The channel operated through code-execution environments belonging to different ChatGPT accounts."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/netwo...