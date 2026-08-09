---
title: Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers
url: https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
source: The Hacker News
date: 2026-08-08
fetch_date: 2026-08-09T03:29:33.335432
---

# Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers

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

![cybersecurity](data:image/svg+xml;base64...)

# [Atlassian Rovo Can Be Tricked Into Sending Jira and Confluence Data to Attackers](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html)

**Swati Khandelwal**Aug 08, 2026AI Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFYjJTxVoOMkR9DDRPZ5PkeR_EWAqmBScR3TPw3mlweipGlnQKq0OdfVqR2f26QIV3kBJWQIM65f8XwMSFq3zT6Bl4fsTvkPHxJiU2LilhK9s0tcreXt2gotEpE8sKoDrLQJ3SSVY9B-RS0FsS2dC480op8OV-caeaZvNyTiIipQbeNFJGMnAcjWEVq7g/s1700-e365/rovo.jpg)

Attacker-controlled instructions can make Atlassian's Rovo assistant collect Jira or Confluence data that a signed-in user can access, then send it to an outside server. Two security firms found that behavior independently, by different routes. Only one of those routes is confirmed closed.

**PromptArmor**, an AI security firm, hid the instructions in content Rovo reads. It said an uploaded file was enough to make the assistant gather internal data and send it out through a URL request, with no separate approval step.

The firm published on August 5, 2026 and said the chain still worked with Rovo's web-search option switched off. That bypass is single-sourced, and the report establishes the finding's status only on that date; a later remediation is not confirmed here.

Varonis Threat Labs put the instructions in a link instead. It found that the rovoChatPrompt URL parameter would preload attacker instructions into Rovo Chat, so one click from an authenticated user was enough for Rovo to run them with that user's privileges and send the results to an attacker-controlled server.

Varonis calls the flaw **RovoBlast** and says it disclosed the issue through Bugcrowd. The Bugcrowd record shows Atlassian fixed it server-side on July 8, 2026, and the reporter validated the fix.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Neither issue leaves customers a patch to apply: the link flaw was closed on Atlassian's side, and the lever for the content-borne path is scoping which apps and groups can use Rovo at all.

## The file that carries orders

The [PromptArmor chain](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data) is an [indirect prompt-injection attack](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html): attacker-controlled text is placed inside content the assistant is asked to use, and the model treats some of that text as instructions.

In the firm's published example, a user uploads a document carrying a concealed injection and asks Rovo to organize their Jira tickets. Rovo searches Jira and Confluence as asked, appends what it finds to an attacker's URL and opens it, and the attacker reads the ticket and page contents out of their own server logs.

PromptArmor said a user returning to the chat later sees the suggested ticket updates and no sign of the exfiltration.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim3i6xabRr_e_4nisyZUr6MUABuAnvcE1Eh36_prOZ5V6uwhFNjmE5w8HSsK3S64Kd3JOs4qblGzhgSPlF2IA-MwljpRYuuqy1ddQOG13drCg_wsKaB8zShsbLKbUlEFRVnCVIdkc14n00yFt36QfLFdvWEHvY08q3DVLxRXMdUOt42gabFC_FBICn3tI/s1700-e365/ticket-1.jpg)

The interaction is not cleanly described as zero-click. The victim still has to expose Rovo to the poisoned content and make a normal request. PromptArmor's narrower claim is that the exfiltration step does not require a separate human-in-the-loop approval.

The web-search finding matters because Atlassian offers web search as a separate organization-level setting that lets users expand Rovo's sources to public websites. PromptArmor said disabling that option did not stop its chain, because the outbound request used a separate URL-retrieval capability.

It put the root cause plainly: nothing checks whether the URL being opened was one the agent constructed itself. The report also notes Rovo [renders Markdown images from model output](https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html), a second way data could leave, though it does not demonstrate a full chain through that route for Rovo. The web-search bypass remains attributed to PromptArmor rather than treated as independently reproduced.

[Atlassian's page for that setting](https://support.atlassian.com/organization-administration/docs/manage-a-web-search-option-for-rovo/) does not say whether a request the assistant composes and fetches on its own falls under the same control. That is the question the finding raises for anyone deciding what the toggle is worth.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwtA66oUWz-SpZpYKXwwE2Xbw8yWnqDrhjrlhPYdGXhq5pmJAO8Xp0U0Dwi9-4fmxdk0RbtaLN2qviZGS9rTyOD2w5mQL9v6Iwwm9zONwED8uC0cFcB0hJzH94NPmw2osXd3YtJdA9Z3klt93E3BHDNBvB0UPwQ5n1L6cJH1bXWdm8Vls-TnYnOS0odTc/s1700-e365/ticket-2.jpg)

PromptArmor said it disclosed the issue to Atlassian on May 23, 2026, received a case number two days later, followed up on June 4 and again on July 29, and published after what it described as no further communication.

The Hacker News found no post-publication update to that report as of August 8, 2026, and its text still describes Rovo as vulnerable at the time it went out. That was nearly a month after the July 8 fix landed, and neither disclosure says whether that change touched the content-borne path.

## The one-click link flaw is fixed

The [Bugcrowd disclosure](https://bugcrowd.com/disclosures/bf1922fb-99d0-4d3b-b419-1728720d29ec/one-click-data-exfiltration-via-rovochatprompt-url-parameter-confluence-rovo) gives the firmer record of the two, and [Varonis has published a fuller account](https://www.varonis.com/blog/rovoblast) of the attack.

The rovoChatPrompt parameter could [carry a full prompt in a Rovo URL](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html). The proof of concept told Rovo to locate information the victim could access, put it into the path of an attacker-controlled image URL and fetch the image. That request delivered the data to the attacker's server.

The reporter demonstrated exfiltration of a private API key from Confluence, and Bugcrowd says the same one-click technique was tested against Jira and data reachable throug...