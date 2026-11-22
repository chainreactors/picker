---
title: Signal Blocks AI Agents From Reading Private Chats via Screenshots on Android and iOS
url: https://thehackernews.com/2026/11/signal-blocks-ai-agents-from-reading.html
source: The Hacker News
date: 2026-11-21
fetch_date: 2026-11-22T09:02:52.776942
---

# Signal Blocks AI Agents From Reading Private Chats via Screenshots on Android and iOS

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Signal Blocks AI Agents From Reading Private Chats via Screenshots on Android and iOS](https://thehackernews.com/2026/11/signal-blocks-ai-agents-from-reading.html)

**Ravie Lakshmanan**Nov 21, 2026Privacy / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1cVX1DZUDMTkSc3kGcO8KsGd-MIBr6py39SuaRxG1wCxVVfKIQhiQaywRpjn95FQV4tMy0dWyNc49745cwqBBLpGzVK_eut-DGLBaidiiYCdIH65bXGtopuPJ7dofJzAJVJ6cWrKp2JJb5gNrODQuWtK7vZZp824ecrz4_DHWWJIaC5wS6aYfsMsKshg4/s1700-nu-rw-lo-l85-e365/signal.jpg)

Signal has announced that it will restrict screenshots by default to stop artificial intelligence (AI) agents from reading private chats on Android and iOS devices, but conceded that the protection is "incomplete."

The feature applies to agentic systems built into iOS 27 and on Android versions where the encrypted messaging platform can detect an AI assistant attempting to read the Signal screen.

It also builds upon a similar setting that Signal [introduced](https://thehackernews.com/2025/05/weekly-recap-apt-campaigns-browser.html#:~:text=Signal%20Says%20No%20to%20Recall) in Windows 11 last May following Microsoft's release of the controversial Recall feature.

Calling the agentic integrations into Android, iOS, and Windows an "existential threat to Signal," Meredith Whittaker, president of the Signal Foundation, said the move is designed to uphold its privacy guarantees in the AI era.

"In order to gain access to information about you, these OS AI agents 'scan' the information that's on your screen," Whittaker [said](https://signal.org/blog/protecting-your-privacy/). "In doing so, your Signal data is captured, then made available to these agentic systems in order to allow them to answer your questions and do your bidding."

"The net result is that these AI capabilities in the operating system are undermining Signal's ability to independently guarantee privacy."

The risk here is that AI agents can capture and store the information accessed from Signal either locally or on remote servers, with the activity occurring outside of the platform's control and potentially putting the privacy of all the participants in a conversation at risk.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Users who want to disable the option can do so by navigating to Settings > Privacy > App Security > toggle "Block Siri AI" (on iOS) or "Screen security" (on Android).

"However, doing so will potentially expose your (and your contacts') Signal content to these AI agents, and break our privacy guarantees," Signal said.

"Our remedy is also incomplete – while we are doing everything we can, restricting screenshots does not address other more sneaky ways AI agents could potentially access application data, such as retrieving content already present on a user's device via the file system."

Signal also pointed out that application developers lack robust tools to prevent AI agents from eroding application-level privacy. It also called out the companies for failing to provide adequate documentation about how these systems work to help design necessary controls to prevent the agents from accessing sensitive application data.

Specifically, it's urging the tech giants to provide "two common-sense remedies" to help protect the privacy of its users -

* Access to easy and well-documented way to opt their app out of AI data access and processing entirely, including screen reading, filesystem access, notifications, APIs, and other OS frameworks, without making drastic compromises to the core user experience
* Create better documentation and technical specifications around how AI agents function, specifically with regards to data access and processing

The concerns are not theoretical. Reuters recently [reported](https://www.reuters.com/investigations/meta-bets-big-muse-ai-agent-early-safety-mishaps-surface-2026-11-18/) that Muse, Meta's AI agent, was able to bypass its own official "Connector" tool to obtain access to Signal messages on both an Apple computer and an Android device by taking advantage of the broad operating system permissions granted to it during initial setup.

On macOS, for example, the agent leveraged macOS's accessibility and screenshot tools to navigate to the Signal app, take screenshots, extract text from those images, and regenerate the textual content within the Muse app. On Android, it read messages by abusing its access to the device's push notifications.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

In one case highlighted by the news agency, the AI agent alerted a Meta staffer using Muse on her personal phone with a reminder to respond to a message from her sister on Signal. "This seems like an extreme privacy violation. I definitely did not grant it access to other apps, or recall being asked about this," the employee said in an internal post.

"We also see a growing need for tools that can prevent third-party agents, like Meta's Muse, from accessing application data using the deep permissions that users are encouraged to grant them during setup," Whittaker said.

"In many cases these agents are leveraging accessibility settings that were meant to empower actual people to get the most out of their apps and services, not to act as a skeleton key that provides access to AI agents."

Late last month, Apple [released](https://support.apple.com/149076) iOS 27.2 with an "Excluded Apps" option that [lets users](https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai) choose which apps Siri, Search, and suggestions can access. With Google Gemini, users have the [ability to disconnect apps](https://support.google.com/gemini/answer/13695044) via the Connected Apps settings.

Earlier this week, the iPhone maker also [previewed](https://thehackernews.com/2026/11/apple-tightens-macos-app-permissions-to.html) new controls that allow Mac users to give more granular acce...