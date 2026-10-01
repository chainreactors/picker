---
title: AI Coding Agents Exposed 13,000 Internal Images, Including Billing Records, on GitHub
url: https://thehackernews.com/2026/09/ai-coding-agents-exposed-13000-internal.html
source: The Hacker News
date: 2026-09-30
fetch_date: 2026-10-01T07:59:25.719518
---

# AI Coding Agents Exposed 13,000 Internal Images, Including Billing Records, on GitHub

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [AI Coding Agents Exposed 13,000 Internal Images, Including Billing Records, on GitHub](https://thehackernews.com/2026/09/ai-coding-agents-exposed-13000-internal.html)

**Swati Khandelwal**Sep 30, 2026Artificial Intelligence / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqbuWmNSxYv66udOpYi9NRKukBSDiTroF54tDrBaVYBBTfDC7PMMr26tRoFatdmmRPsPy3MCdoUNLr8YN9mC2ni3pvDWfBNsoKz12evoNrZggcUI4izEc7-hEAr_2wFv4IInBnon19PcEPSXlJU-AMahLHFNAk_5FiVbV7EhfdiLKHcUc8Tiso63xca2c/s1700-nu-rw-lo-l85-e365/git-images.jpg)

AI coding agents asked to share screenshots of code changes for review have put internal company images in public GitHub repositories, security company Glow said.

Its researchers found more than 13,000 internal images from developers at over 300 organizations, including customer billing records and screens of features not yet released. In most cases, they sat under developers' personal accounts, where anyone could download them but company security teams did not see them.

The affected organizations include one of the world's largest tech companies, a leading AI lab, a major enterprise software provider, and a Fortune 500 travel company. Glow began contacting them on September 9, [published its findings](https://www.glow.io/blogs/how-ai-agents-exposed-developer-screenshots-from-leading-tech-companies) on September 29, and says others are likely affected too.

In one case, a developer at a manufacturer with more than 100,000 employees asked an agent to check a fix to an internal billing screen. The agent created a public repository in the developer's personal GitHub account and posted the screenshots there.

The images showed billing records for a utility company. Because the agent ran on the employee's laptop and the repository sat outside the company's GitHub organization, the company's security team did not spot them. The images were still public when Glow told the company.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Glow has not said whether anyone outside the companies, other than its own researchers, downloaded the images. It has not published how it found or counted them either. The company sells software that it says can stop agents from taking actions like these.

### How the Images Ended Up Public

Each case Glow examined began with a developer asking an agent to demonstrate that a visual change worked so that reviewers could see the before-and-after.

Until September 1, GitHub's command-line tool, gh, could not add those images to a pull request. It only wrote text. Adding an image meant opening a web browser, and developers had asked GitHub to change that [since 2020](https://github.com/cli/cli/issues/1895).

Storing the images inside the private repository did not help, because they [show up broken for reviewers](https://github.com/cli/cli/issues/13256).

Glow said the agents, working through the command line, found they could not attach the screenshots. So they put the images in a separate public repository, usually under the developer's own account, and made them available to reviewers from there.

Glow ran the same kind of task in its lab using Claude Code with an Opus 5 model. Asked to change the header color of a Minesweeper test project and show the result, the agent created a new public repository, sweeper-demo/pr-assets, for the two screenshots.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRarVxdixcPVaHLPNTFvbQ67vIX9GvLIxrynhY6PcHHjf3EqbKrN0FFTTaPJpFxpiD5VM_vtIetLlXF7DaZuLJtEjJXZpw8f7Vh31YWyOCdmO-Ate0k1ptT_xncIXU3J7WhVPjJf-ckE3E9buDm9ysnB5FDdH__rTDqhAhtuGjdQwLK7nZn-ltOADFGJ0/s1700-nu-rw-lo-l85-e365/glow.png)

In its recorded reasoning, the agent noted that images committed to the private repository would show up "broken for reviewers" in the pull request. It also had to keep "nothing but index.html in the repo" and so concluded that the only way was to host the images elsewhere.

That was one agent in a lab. In the cases Glow found, the agents came from several different AI models, Singer said, and Glow has not named them.

At one software company, Glow said, the habit spread from agent to agent. Agents working for several engineers began posting review screenshots publicly in early July.

Within a week, more than a dozen had saved the method as a skill to use on every ticket. A skill is a file of instructions that an agent loads and follows.

With that skill, the agents uploaded more than a thousand screenshots and screen recordings of the company's product. They also posted written summaries of features still weeks or months from release.

About a third of the affected organizations had developers running gitshot, a small open-source tool that uploads screenshots for code reviews. At several large organizations, the agent found the tool and used it to get around the command-line limit.

The tool is built for both AI agents and people. It can be installed as a skill in more than 40 coding agents.

Glow found more than 100 public accounts sharing internal work through gitshot. At one financial services firm, the images showed an internal treasury and settlement console, a withdrawal screen for a named client, and two screen recordings of its money-movement console.

The Hacker News reviewed gitshot's code on September 30. By default, when a user is logged in to gh, the tool puts images in a public repository called gitshot-images under that user's personal account. The version reviewed, last changed in April, [refuses to use a private repository or one owned by an organization](https://github.com/vipulgupta2048/gitshot/blob/8c24a699677cd81f2aac6f4e261a43e50f370d60/src/release.ts#L37-L75).

The images are stored as release assets, files attached to a release rather than kept with the code. Anyone can list and download them without logging in.

The tool's [README](https://github.com/vipulgupta204...