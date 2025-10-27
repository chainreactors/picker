---
title: Napkin Ideas Around What Changes to Expect Post-ChatGPT
url: https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt/
source: Daniel Miessler
date: 2022-12-05
fetch_date: 2025-10-04T00:31:40.357843
---

# Napkin Ideas Around What Changes to Expect Post-ChatGPT

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Napkin Ideas Around What Changes to Expect Post-ChatGPT

December 4, 2022

[#ai](/archives/?tag=ai) [#business](/archives/?tag=business) [#creativity](/archives/?tag=creativity) [#cybersecurity](/archives/?tag=cybersecurity) [#ethics](/archives/?tag=ethics) [#future](/archives/?tag=future) [#innovation](/archives/?tag=innovation) [#productivity](/archives/?tag=productivity) [#society](/archives/?tag=society) [#technology](/archives/?tag=technology) [#top](/archives/?tag=top)

![gptbot-insanity](/images/fa3dc9b7-2ae5-402f-8a4d-f21158e1a92b-gptbot-insanity.png)

1. [Work Replacement](#work) >
2. [Talent Magnification](#talent) >
3. [Solopreneuers](#smallbusiness) >

1. [AI Specialists](#specialists) >
2. [Idea Dominance](#ideas) >
3. [Use Cases](#usecases) >
4. [Random Thoughts](#thoughts) >

If you’re reading this you already know the internet is on fire over [the new  GPTChatBot from OpenAI](https://chat.openai.com/chat?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >. There are people using it to [create full virtual machines](https://www.engraved.blog/building-a-virtual-machine-inside/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >, to be [their personal writing coach](https://andrewmayneblog.wordpress.com/2022/11/30/collaborative-creative-writing-with-openais-chatgpt/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >, to write terraform, to [take an SAT](https://twitter.com/davidtsong/status/1598767389390573569?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >, [generate Pokemon-like characters](https://share.danielmiessler.com/i/WU4fXm?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >, and a thousand other things.

Hat tips to [@sasazdelar](https://twitter.com/sasazdjelar?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >, [@jhaddix](https://twitter.com/jhaddix?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) >, and [@clintgibler](https://twitter.com/clintgibler?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt) > for some of these conversations.

I’ve had lots of conversations with friends about, "oh, that means this will be possible!", or "oh, think about this that might happen!", so I wanted to capture a few things we’ve come up with here. Please note that some of these are horribly negative in terms of impact to society, and others are possible ways to harvest positivity out of the situation.

## 1. The startup engine is about to point its sights at human work

There are about to be a ton of new startups—as well as established consulting companies like McKinsey and KPMG and the like—that will build frameworks that leverage GPT (and its competitors) to replace human work. I feel bad about this, but like I mentioned in my [Companies as Alaskan Fishing Boats](https://danielmiessler.com/blog/companies-as-alaskan-fishing-boats/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt&last_resource_guid=Post%3Ad1fae494-fb81-4fee-b2bc-19752d46ab4b) > article, businesses aren’t there to employ people. They’re there to get work done.

I’m sure KPMG would love to let its AI take your "boring" work off your hands.

I also had it recreate a customer report it took me personally 2 hours to create. It nailed it in 10 seconds.

Feeling bad about it, I decided to point the weapon at myself. I had it emulate the dozens of hours of work I do every week for [my own newsletter](https://danielmiessler.com/newsletter/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=napkin-ideas-around-what-changes-to-expect-post-chatgpt&last_resource_guid=Post%3Ad1fae494-fb81-4fee-b2bc-19752d46ab4b) >. With some very simple prompting and some good examples it produced a decent facimile of what I do.

Well, *shit*.

![ul-newsletter-attempt-miessler](/images/558f820c-caf5-4221-9002-c1b7fa7d5ead-ul-newsletter-attempt-miessler-479x650.png)

It created these analysis headlines in 10 seconds

And soon the Bobs will be largely replaced by AI as well.

These companies will walk into businesses like Bob2 and figure out who is doing what, how long it takes them, and figure out how to use their new AI Framework to eliminate the need for human workers. Of course it’ll be called optimization or enhancement or some shit, but we all know what it is.

Looking at what the chatbot can do, we expect the biggest disruption in (obviously) repeatable work. But most work we do is repetitive. Some likely high-impact areas:

### Reviewing updates and looking for interesting nuggets or patterns

🤖 For all messages in this Slack channel, extract the most important updates and send them to company leaders in a report with the following sections and tables, including a prioritized list of recommended actions given our stated company goals and current OKRs.

### Conducting muti-step follow-ups to analysis

Also, for security issues do the same for re-opening tickets when the fixed condition goes away.

🤖 For all open Jira tickets look in the history for evidence of what completed would look like, check for that condition, and close the ticket using that evidence as the reason.

### Continuous monitoring for security or operational purposes

🤖 For all PR’s, evaluate the code submitted for coding errors that can place data at risk. Create and deliver a message to the developer that gives them the problem, it’s location in the code, the implications of doing it that way, and give 1-3 recommendations on doing it better. If there is a company-recommended way of doing it, give that as the singular recommendation.

🤖 Find all instances of sensitive data or tokens being posted in chat and email the poster and their manager pointing them to the company policy and the link to documentation on how to do it securely.

🤖 Using the AWS API below, monitor the authentication configuration for all admins on these accounts. Alert if any of those accounts ever have too much authority or have an authentication level below our company standard.

I think anyone not using GPTBot-like tech to do these tasks in the next few months will be on the path to being replaced by those who are. I don’t imagine this will result in some massive layoff. It’ll be more like a steady trend towards non-replacement as people naturally leave companies. Which will still result in companies needing far fewer people.

## 2. The talent gap will massively expand

![tech-separation-miessler](/images/62e74a8f-31c0-4d5f-85c1-b1fc9284723c-tech-separation-miessler-650x650.png)

Now I can draw better because I’m better at prompt engineering

And keep in mind this is Day 0 for this tech. Like a few days ago this thing was making pretty pictures.

You know how there’s a wide gap in income and status between the most talented and competent people and those who are less so? Well now imagine those super smart people armed—yes, armed—with AI. For them, AI will be like multiplying their brains and having them work continuously. Or like hiring a giant staff just for them.

This will magnify even further because the best AI will be the most expensive.

So now the lucky people who picked great parents, great genes, a great environment, and great education won’t just have the best opportunities and jobs. No...