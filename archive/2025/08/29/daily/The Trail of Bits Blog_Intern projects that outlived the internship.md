---
title: Intern projects that outlived the internship
url: https://blog.trailofbits.com/2025/08/28/intern-projects-that-outlived-the-internship/
source: The Trail of Bits Blog
date: 2025-08-29
fetch_date: 2025-10-07T00:47:42.546892
---

# Intern projects that outlived the internship

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Intern projects that outlived the internship

Aidan Kwok

August 28, 2025

[internship-projects](/categories/internship-projects/), [machine-learning](/categories/machine-learning/), [working-at-trail-of-bits](/categories/working-at-trail-of-bits/)

Page content

* [Podcast workflow](#podcast-workflow)
* [Slack exporter](#slack-exporter)
* [Generating excitement](#generating-excitement)

The day your summer internship ends is the day your project gets abandoned. I’ve been there before. But Trail of Bits is different. As a business operations intern this summer under Dan Guido and Sam Sharps, I built two automation tools using Claude (Anthropic’s AI model): a podcast workflow that saves 1,250 hours annually, and a Slack Exporter that lets employees find essential company knowledge with a single query. In both cases, these tools will be used across the organization well after my internship ends.

## Podcast workflow

Trail of Bits has teams of experts, often PhD level, across their different business practices: AppSec, AI/ML, Blockchain and Cryptography. They want to expand their guest presence on like-minded podcasts to share all the ways we’re pushing the boundaries of cybersecurity (and to encourage others to do the same). To best contribute to the community, they focus on filling a hyperspecific knowledge gap that few others can address. But manually scouting podcasts for these keywords would require hundreds of hours of weekly listening and research.

To ensure that we find the needle in the haystack (and do this at scale), we needed an automated workflow. Here it is:![Figure 1: Podcast workflow flow chart](/img/aidan-internship/internship-projects-post-1.png)

Figure 1: Podcast workflow flow chart

Users either run it manually or schedule it for a certain day and time. After checking if an episode contains the right keywords, Claude generates a variety of essential information: a summary of the episode, speakers’ opinions, quotes with timestamps, an outbound email draft, and more. A Replit front end displays all this output.

When building the workflow, I noticed that Claude has limitations. For example, it created fake employees when determining which Trail of Bits employee should appear on a given podcast. To solve this, the user uploads an Excel file into the Replit front end that maps Trail of Bits employees to the keywords they specialize in. Claude also failed to source the host’s contact info. However, it can extract the host’s first name, last name, and their website which an external API uses to get the contact info. Here’s an example of the insights that Claude and the other supplemental tools (like the Excel file) generate.![Figure 2: Output example of podcast workflow](/img/aidan-internship/internship-projects-post-2.png)

Figure 2: Output example of podcast workflow

The tool monitors upwards of 50 podcasts with weekly episodes. That’s 2,500 episodes a year! With an underestimate that each episode lasts 30 minutes, this workflow annually saves 1,250 hours of listening. That’s not including the time required to get the host’s contact info, map a Trail of Bits expert to a relevant podcast, and write an outbound email.

## Slack exporter

With hundreds of Slack channels containing hundreds to even thousands of messages, searching and analyzing historical information was time consuming. As a result, Trail of Bits implemented a Slack exporter in the terminal that exported channels into JSON and/or markdown. Users then uploaded the channels into Claude to get summaries and insights.

However, this implementation had two major limitations. First, all employees need the Slack exporter, but because of its terminal implementation, it was accessible only to engineers. Second, the user had to know which Slack channels contained the necessary info because the chosen channel(s) was the only context the chatbot would have.

To solve the first challenge, I distributed a Slack exporter Electron app. Users launch the app, and they’re ready to export. No terminal commands are required, so anyone can use it.

Instead of manually reading through each channel in the terminal implementation, users now have a far more efficient UI that can search and even select all the channels at once:

![Figure 3: Channel search in the Slack exporter Electron app implementation](/img/aidan-internship/internship-projects-post-4.png)

Figure 3: Channel search in the Slack exporter Electron app implementation

Once the user selects one or more channels, they receive these export options:![Figure 4: Export options in the Slack exporter Electron app implementation*](/img/aidan-internship/internship-projects-post-5.png)

Figure 4: Export options in the Slack exporter Electron app implementation\*

To solve the second limitation of the terminal exporter, I used Claude’s MCP (model context protocol) to expose our Slack workspace to Claude. Now, through Claude’s Desktop app and/or Claude code, users can search across all public channels and private channels they’ve joined, without ever exporting.

Need to know the progress of every company project? My improved implementation does it in one query. Need to onboard a new employee, but all your team members are busy? Again, one query. Due to this tool’s vast applications, our team can focus on pushing the frontiers of cybersecurity instead of sifting through Slack channels.

As you can see from the below image, the applications are endless:

![Figure 5: Claude MCP desktop Slack output](/img/aidan-internship/internship-projects-post-6.png)

Figure 5: Claude MCP desktop Slack output

## Generating excitement

Everyone talks about applying AI, but copying and pasting to and from a chatbot is just the tip of the iceberg. These projects show how much further AI applications can be taken. Yet to build these applications, you need to understand the user’s problems and keep them in the loop. My testing sessions went like this: discover a bug, frantically fix it live, get a feature request, and then test that feature later that day.

Unlike the stereotypical internship projects that die once the intern leaves, my tools survived because, through testing, people applied these tools to their own challenges, experienced the productivity gains, and then integrated them into their daily workflow. Equally important, they shared their excitement with other employees to cement them as company-wide tools.

Through these projects, Dan, Sam, and I hoped to generate excitement that AI won’t replace employees but rather augment their capabilities. Every team has AI use cases waiting to be discovered. At Trail of Bits, we’re on the hunt to find and implement them, and everyone contributes, even interns.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [Podcast workflow](#podcast-workflow)
* [Slack exporter](#slack-exporter)
* [Generating excitement](#generating-excitement)

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of ...