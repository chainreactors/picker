---
title: Hacking ChatGPT by Planting False Memories into Its Data
url: https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html
source: Schneier on Security
date: 2024-10-02
fetch_date: 2025-10-06T18:55:26.227692
---

# Hacking ChatGPT by Planting False Memories into Its Data

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Hacking ChatGPT by Planting False Memories into Its Data

This vulnerability hacks a feature that allows ChatGPT to have long-term memory, where it uses information from past conversations to inform future conversations with that same user. A researcher [found](https://arstechnica.com/security/2024/09/false-memories-planted-in-chatgpt-give-hacker-persistent-exfiltration-channel/) that he could use that feature to plant “false memories” into that context window that could subvert the model.

> A month later, the researcher submitted a new disclosure statement. This time, he included a PoC that caused the ChatGPT app for macOS to send a verbatim copy of all user input and ChatGPT output to a server of his choice. All a target needed to do was instruct the LLM to view a web link that hosted a malicious image. From then on, all input and output to and from ChatGPT was sent to the attacker’s website.

Tags: [AI](https://www.schneier.com/tag/ai/), [LLM](https://www.schneier.com/tag/llm/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on October 1, 2024 at 7:07 AM](https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html) •
[9 Comments](https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html#comments)

### Comments

Clive Robinson •
[October 1, 2024 9:37 AM](https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html/#comment-440870)

Well not quite yet the season to be jolly but,

> *“A researcher found that he could use that feature to plant “false memories” into that context window that could subvert the model.”*

Does give me a fun idea 😉

If it can “go to any web site” then it should be possible to make it do like “Alexa once did” and get it to buy you an Xmas Present or three…

Just saying 😉

More seriously we’ve not given these current AI ML LLM systems “physical agency” but they do have “informational agency” to a certain extent.

Getting an AI to “time delay a purchase” is a POC of other “time delay payloads” that in turn have “physical implications” in the “real world”.

I doubt anyone at these AI Vendors in their rush to get their next big thing out to market have actually thought about their systems being used to getting “physical agency” in the “real world” via having the ability to act as an “information agent”, using non obvious “embedded” commands.

Funny thing is Issac Asimov got there with a story back in the 1950’s. But more famously in a more refined form is the story arc in

For those that don’t know the AI in the film called HAL had secret information put in it’s memory about an alien artifact, that the astronauts onboard were unaware of. In trying to deal with two different realities HAL developed symptoms like hallucinations that enabled it to kill the astronauts in “accidents”.

lurker •
[October 1, 2024 12:40 PM](https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html/#comment-440873)

Sorry, I don’t understand this:

> All a target needed to do was instruct the LLM to view a web link that hosted a malicious image. From then on, all input and output to and from ChatGPT was sent to the attacker’s website.

So is this a hack of ChatGPT? or is it just demonstrating that ChatGPT has a vulnerability to web-based input, of the kind that gets fixed on a weekly basis for all your other two-bit browsers?

Sid •
[October 2, 2024 2:37 AM](https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html/#comment-440882)

@Clive Robinson

Your description of the problem with an AI that has more information than the user can be aware of is of some growing interest.

And of course, our merely human memory falters, and knowledge often incomplete to begin with. The usual problems with game theory.

Thank you for recalling the depths of Clarke’s parable of HAL in “2001.”

Clive Robinson •
[October 2, 2024 6:15 AM](https://www.schneier.com/blog/archives/2024/10/hacking-chatgpt-by-planting-false-memories-into-its-data.html/#comment-440883)

@ lurker,

Re : Hacking has broad meaning.

I may be wrong but as I understand it from,

<

blockquote>*“When security researcher Johann Rehberger recently reported a vulnerability in ChatGPT that allowed attackers to store false information and malicious instructions in a user’s long-term memory settings”*

<

blockquote>

The researcher found a way to modify “long term memory” for a user that would then cause ChatGPT to do things “for a user” from then on in a way that was “not obvious/apparent to the user”.

Further,

> *“OpenAI summarily closed the inquiry, labeling the flaw a safety issue, not, technically speaking, a security concern.”*

OpenAI “potentially misunderstood / misclassified” that was reported to them, thus did not take action.

As we don’t have the information supplied in the article it’s not possible to say from it’s reporting.

So the researcher made the flaw found a little more obvious to OpenAI (again by how much is not in the article other than saying it was a POC with what that might imply).

The flaw and hack are described as,

> *“Rehberger found that memories could be created and permanently stored through indirect prompt injection, an AI exploit that causes an LLM to follow instructions from untrusted content such as emails, blog posts, or documents. The researcher demonstrated how he could trick ChatGPT into believing a targeted user was 102 years old, lived in the Matrix, and insisted Earth was flat and the LLM would incorporate that information to steer all future conversations. These false memories could be planted by storing files in Google Drive or Microsoft OneDrive, uploading images, or browsing a site like Bing—all of which could be created by a malicious attacker.”*

The implication as written is the “prompt injection” was not done as the “effected user” but as another user and it in effect updated the more “global memory” of ChatGPT.

But could some how be focused on a particular user[1] via “the system” not “their account”.

So I could produce allegations against J.Sixpack in many places on the Internet that I know ChatGPT goes sniffing for “input”. I could by say making a post to some “social media site” that has lax or nonexistant rules get others to “create churn” around the name “J.Sixpack” which then gets used to train ChatGPT and in the process pulls in all the “fake memories” you’ve created on line. Much like happens with Wikipedia and it’s “secondary sources” rules, the “primary” or “true” data is downgraded as being in effect “faux”…

Whilst there are known ways to embed malware payloads in images and the like, it’s not clear how this actually effects an individual user or target.

It’s written to suggest that when a user follows ...