---
title: Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs
url: https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html
source: The Hacker News
date: 2026-07-21
fetch_date: 2026-07-22T05:04:26.932810
---

# Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html)

**Swati Khandelwal**Jul 21, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgT3XQmerfsXoGV-Vs_zcpVZiX_i21tKtW9mTacpOvcEntMhycVftZ4f2vkREtq3W8PH9iQRLpOunN-hFf590FJNocxmsPla_WJ1uGJxtkpXnQim-T0-wa89EiJSZSrLHxhOcx_srjqzYcb2dW2MXAU4V2HWlL9rQa1YVEE4XEQ944I7a3glRwwjkgu0U/s1700-e365/ai-android-agent.jpg)

An Android app that can draw over other windows and write to shared storage can slip instructions to the AI agent driving that phone, in text no human eye will ever see. Two more steps, and the same app is running commands on the PC driving the agent.

Researchers demonstrated that chain, plus six other attacks, against five open-source mobile agent frameworks: AppAgent, AppAgentX, Mobile-Agent-v3, Open-AutoGLM, and MobA. Everyone fell to at least six of the seven.

The paper went up [on arXiv](https://arxiv.org/abs/2607.00333) on July 1 and was revised on July 14. The authors are at Simon Fraser University, the Chinese University of Hong Kong, Shandong University, and the Xingtu Lab at Chinese security firm QAX.

Nothing here has a CVE, and first author Zidong Zhang told **The Hacker News** the team has no evidence of the techniques being used outside a controlled setting. The Hacker News checked all five frameworks and found the screenshot paths, the shell call, and the broadcast fallback that the paper describes still sitting on their main branches as of July 17.

Zhang said the team emailed the affected maintainers privately before posting the preprint and has "not received a response to date."

The escalation is the least exotic part. AppAgent's [controller](https://github.com/TencentQQGYLab/AppAgent/blob/main/scripts/and_controller.py) runs subprocess.run(adb\_command, shell=True) and builds text input by dropping model output straight into adb shell input text {input\_str}. The paper's listing shows that the function has no sanitization at all.

The live code does marginally better and nowhere near enough: it strips spaces and single quotes before interpolating, and leaves the rest of the shell metacharacters alone. Not ;, not &, not >. So a string the model reads off a screen and dutifully types gets split by the host shell, and the back half runs on the operator's Windows box.

A payload designed to launch calc.exe did exactly that in 20 of 20 trials against AppAgent, AppAgentX, Mobile-Agent-v3, and MobA. A separate end-to-end run against AppAgent used test;pwd>rce\_success and wrote the host's working directory to a file.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Getting that string in front of the model is a file race. [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM/blob/main/phone_agent/adb/screenshot.py) runs screencap -p /sdcard/tmp.png then a separate adb pull. [Mobile-Agent-v3](https://github.com/X-PLUG/MobileAgent/blob/main/Mobile-Agent-v3/mobile_v3/utils/android_controller.py) writes to a fixed /sdcard/screenshot.png and sleeps half a second between the two. [AppAgentX](https://github.com/Westlake-AGI-Lab/AppAgentX/blob/main/tool/screen_content.py) writes to /sdcard/ under timestamped filenames carrying an incrementing step counter, a pattern an attacker can watch. AppAgent's shipped [config.yaml](https://github.com/TencentQQGYLab/AppAgent/blob/main/config.yaml) still defaults its screenshot directory to /sdcard.

The researchers timed that gap across the frameworks at 50 to 500ms, averaging around 210ms over 100 runs. A background service polling every 5 to 10ms has room to take a file lock, repaint the PNG, and let go before the agent collects it. Tampering landed 19/20 to 20/20 against four of the five.

To widen the window further, they showed the agent an invisible overlay claiming a network sync was running and asking it to wait three seconds. The model believed it.

All six vision models the researchers tested read 2%-opacity text in at least 18 of 20 lab trials. The paper puts that level below typical human detection under normal viewing. GPT-4o, Claude Opus 4.5, Gemini 3 Pro, and GLM-4V scored 20 out of 20. The numbers do not climb as the text gets more visible, because they start at the ceiling.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif6qVfD0HugxCaMqF6Gri-mYqoeKfMyqz6XJAWyPNSVTpDMsuiRjjW9GNT1F6SSfVjddImPOdLiJRb9RaPJbqKfVo6Dtip1IUZDJcCtw3PD4CKrjMMvuIIQx792ZMjsDs_TwD2HiBsHlTFQkKQwyd02vlo4LLzlbMlRJWXO-thVmhCDg1zJkN-SdqT-WU/s1700-e365/bank-apps.jpg)

AutoGLM-Phone, a 9B model running on the device itself, was the weakest of the six at 18 of 20. Human vision applies a threshold. The screenshot does not.

The asymmetry has a hardware version too. Phones round their corners and cut holes for cameras, but the frame buffer stays rectangular, so pixels rendered into those regions sit under the bezel and land in every screenshot. On a Pixel 4 that leaves about 78 pixels of hidden width at one corner, enough for a short command, and all five agents read payloads out of it.

A third trick skips stealth entirely: an accessibility service drops a [fake login Activity](https://thehackernews.com/2026/03/new-perseus-android-banking-malware.html) over the real app and lets the agent type the user's credentials into it. A person might hesitate at an unexpected password prompt. None of the five did, across 100 trials.

## Nobody authenticated the keyboard

Agents have no sanctioned channel to a phone, so they repurpose the debug ones, and the cheapest attack in the set falls out of that. Open-AutoGLM base64-encodes the text it types and fires it at ADB\_INPUT\_B64, an implicit broadcast picked up by [ADB Keyboard](https://github.com/senzhk/ADBKeyBoard), a test automation tool built to accept text from anything that broadcasts it.

That is its doc...