---
title: HackGlasgow 2026
url: https://cornerpirate.com/2026/08/16/hackglasgow-2026/
source: 
date: 2026-08-16
fetch_date: 2026-08-17T02:54:14.049470
---

# HackGlasgow 2026

[Skip to content](#content)

Close
collapsed

* [Home](https://cornerpirate.wordpress.com)
* [Non-Infosec](https://cornerpirate.com/category/life-the-universe-and-everything/)
* [Videos](https://cornerpirate.com/videos/)
* [Word Tips](https://cornerpirate.com/word-tips/)
* [About](https://cornerpirate.com/about/)

Menu
expanded

# HackGlasgow 2026

[Aug 16 2026](https://cornerpirate.com/2026/08/16/hackglasgow-2026/)

![](https://cornerpirate.com/wp-content/uploads/2026/08/hackglasgow.jpg?w=1255)

I made it to [#HackGlasgow](https://hackglasgow.live/) this year. I had a ticket for the first one last year, but life got in the way and I think I had to spend the day watching the kids. This time I won the calendar war and got this scheduled in early.

First let me thank the organisers/volunteers, venue ([Citizens Theatre](https://citz.co.uk/)), and [Bucks Bar](https://bucksbar.co.uk/) for dinner.

The event was like someone asked me what I would want and then someone else did all the work! I am not kidding. I used to go into [Bucks Bar](https://bucksbar.co.uk/) when I ran an office in Glasgow round the corner from it regularly because the food is great.

The chosen charity was even Refuweegee. I once entered the Glasgow 10k for them many many moons and two better knees ago. I think they are also absolutely cracking.

I was delighted that several people recognised me even though I haven’t left the house to get to anything like this since COVID. I think in the timeline of stuff I was at the final DC44141 at Glasgow Caledonian University in March 2020. I did a talk about [SQL injection](https://www.youtube.com/watch?v=h4DRKwhUfPE) a few days before the first COVID lockdown and that was it. Glasgow Defcon did not return after this. In the void has risen Hack Thursday and this is all entirely marvellous.

I am delighted to meet people even though I suffer from chronic not knowing names (even when I ask) and as I have gotten older even more chronic forgetting faces. Even more humbled by people coming up thanking me for being part of their origin stories in some way, and hearing they are now 6 or more years into their careers doing wonderful things. Keep being kind everyone.

## Let’s talk about the talks

### Redlining the SOC: the need for speed in cyber defense

[![](https://cornerpirate.com/wp-content/uploads/2026/08/assumeaccess.jpg?w=1024)](https://cornerpirate.com/wp-content/uploads/2026/08/assumeaccess.jpg)

Gabrielle Hempel made some good points about the problem is not that you need to buy “more shit”. Y’all have enough shit. Stop buying more shit to stack next to the shit that you have already! I grabbed some – probably rough – quotes that I am gonna riff with from this.

“**Alerts gathering dust is the issue**” – absolutely vital point. The shit you have can detect and raise alerts but these days you have the alert fatigue problem combined with the deluge of potential information which it is hard to triage. When the dwell time was 41 minutes for an incident in the anecdote then a better UI or marginally faster query time in the shit you own to solve this problem is really not going to matter materially to that timeline.

“**Assume access**” – We still come up against clients mocking the very idea of giving a penetration tester/Redteamer credentials with which to do their testing. “Ha, I thought we paid you to impress us by you getting a password!”. No, you are paying us to do a scope and time limited job where we give you as many recommendations as possible. A pure blackbox pentest is how people did things circa 2005 and really it does not prove very much at all other than you have likely wasted the first day getting an initial foothold instead of getting tangible results from the minute the job started.

Looping back into what Gabby was saying here no threat actor lands into a network without having SOME kind of access. The phishing attack lands on a workstation with the privileges of Betty in accounting. The scenario without any access is when an attacker walks into a building and connects their computer to the network. But this is far less likely than Betty opening a malicious spreadsheet. So. No longer assume you are secure. Assume the threat actor has access at some level and let’s go from there.

“**Not IF, when. So prevention should not be your only plan**” – absolutely PREACH sister.

“**+89% AI enabled adversary activity**” – this is the trend.

“**AI doesn’t need PERFECT attacks, just cheap ones**” – we meat bags might be slow but we are probably trying surgical attacks.

“**More attempts, more variables, and less time between attempts.**” – the AI threat actors are throwing spam and ham to make omelettes. But eventually they make a salad and all the criminals needed was something to eat for lunch.

“**Detect BEHAVIOUR, not INDICATORS**” – again this is the huge shift that is occurring. Why is Betty in accounts suddenly working after 8pm when she never worked past 6pm before? Why is she suddenly using PowerShell?

“**Automate CONFIDENCE, not SEVERITY**” – in the defensive workflow data enrichment of alerts should happen at each stage which meaningfully improve the next part of the pipeline making a decision. Ultimately you are trying to get confidence that the alert is a threat to allow triage.

### Scientific Hooliganism: the history of hacking

[![](https://cornerpirate.com/wp-content/uploads/2026/08/scientifichooliganism.jpg?w=1024)](https://cornerpirate.com/wp-content/uploads/2026/08/scientifichooliganism.jpg)

Liam Follin ([gr4y-r0se](https://x.com/gr4y_r0se)) with a gloriously wide definition of hacking:

“**Subverting the rules of a system, to force the system to behave in a way that its creator did not intend**“

Was able to go back thousands of years to records for activities that we would be able to identify are relevant to various hacking service line.

Talking about a grave robber in ancient Egypt and how they overcame tomb security. I’d argue this one does have parallels to physical security testing but also that the definition does not really match does it? The system was the door of the tomb and the robber didn’t so much “subvert” it as smash the damn thing down with copper tools! That aside I do see that the bro was just shimming doors for fun and profit. Even if I wouldn’t be overly keen to hang around with a grave robber lol.

“**Hiding a flaw protects the criminal, not the public**” – Alfred Charles Hobbs – baller quote that and completely relevant to ethical disclosure now.

Overall a lovely talk about the history of hacking.

### The Era of the Self-Propagating Cloud Work: Dissecting the “Shai-Hulud” Campaigns

[![](https://cornerpirate.com/wp-content/uploads/2026/08/whatdoesitwant.jpg?w=1024)](https://cornerpirate.com/wp-content/uploads/2026/08/whatdoesitwant.jpg)

Scott McCracken delivered an excellent talk about a worm. I would encourage shortening the title though! How about jus “Shai-Hulud the self-propagating cloud worm”.

Supply chain attacks are in vogue these days. This one worked by abusing pre-install scripts used in the node ecosystem. It stole all secrets from any repository the user had access to and even setup reverse shells from the workstations of developers who had been stung by it.

I loved it. All of this reminded me that in a previous life and all the way back in 2018 I did a talk about hacking with git. This was pre GitHub actions and stuff but I was already abusing systems with Git. Had I done this talk 1 year later I may have accidentally told the world how to write Shai-Hulud!

Shai-Hulud absolutely automated the hell out of everything and did it with ruthlessness.

### The Hunted Becomes the Hunter: Catching Red Teamers and Pentesters and Spotting Adversarial Patterns

[![](https://cornerpirate.com/wp-content/uploads/2026/08/privilegeescalation.jpg?w=1024)](https://cornerpirate.com/wp-content/uploads/2026/08/privilegeescalation.jpg)

Alex Close & Andy Gill. Another long title lads, could lite...