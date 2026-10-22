---
title: PHP says AI review of critical bugs first sparked alarm in August, but signs surfaced in 2024
url: https://therecord.media/php-foundation-statement-critical-vulnerabilities
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:22.980706
---

# PHP says AI review of critical bugs first sparked alarm in August, but signs surfaced in 2024

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![PHP loho](https://cms.therecord.media/uploads/large_php_logo_pexels_steve_a_johnson_132b80cbee.jpg)

[Jonathan Greig](/author/jonathan-greig)October 21st, 2026

# PHP says AI review of critical bugs first sparked alarm in August, but signs surfaced in 2024

The two PHP vulnerabilities causing worldwide alarm first drew serious attention in August after an outside review by AI companies, the PHP Foundation explained in a lengthy statement on Wednesday.

The organization said the history of one bug, CVE-2026-109618, dates back to 2024, when PHP underwent its first external security audit in several years, but officials took no action.

The issue caused controversy within PHP as engineers debated how to address it, with concerns ranging from “backward compatibility breaks, new denial-of-service potential, or requiring changes to many third-party extensions which seemed impossible to coordinate.”

“The PHP security team, operating on consensus, struggled to choose between these and feared the repercussions of shipping the wrong choice,” the nonprofit foundation [said](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/).

“Combined with the lack of a known path to remote code execution and the small team of core developers with the necessary deep knowledge of the engine occupied with many responsibilities, this decision process caused work on a fix to stall and restart repeatedly over months.”

Hundreds of websites were [taken offline](https://x.com/Rijkswaterstaat/status/2112919941846577654) on Wednesday by companies and [governments](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) as a result of CVE-2026-109618 and a related bug, CVE-2026-109619. Some are labeling them jointly as PHP2Shell.

Some estimates show that [more than 70%](http://wiz.io/blog/php2shell-php-rce) of all websites on the internet use PHP. Internet infrastructure company Cloudflare reported seeing attempted exploitation.

The PHP Foundation said both vulnerabilities “sit in parts of PHP that nearly every request touches.”

“Their central place in PHP is what made both vulnerabilities serious, and also so hard to fix without breaking compatibility, hurting performance, or forcing changes on the large ecosystem of third-party extensions,” they said.

The scope of the vulnerabilities has alarmed cybersecurity defenders and [governments](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching), with a [VirusTotal analysis](https://blog.virustotal.com/2026/10/sizing-php-exposure-window-for-cve-2026.html) showing 5.1 million IP addresses identified as running PHP. At least 758,000 IP addresses were disclosed as end-of-life PHP versions and 85,000 IP addresses were running the latest PHP releases available before developers issued emergency patches Wednesday morning.

These figures represent PHP's internet-facing footprint, not confirmed vulnerable systems. The patches only apply to versions dating back to PHP 8.2. Every version older than that no longer receives updates from the PHP Project.

Cisco Talos’ [released](https://blog.talosintelligence.com/two-critical-rces-in-php-core/) estimates suggesting roughly 50% of vulnerable PHP systems may not receive a patch.

## AI spotlights bugs

After deciding against taking any action in 2024, the PHP Foundation was confronted with the issues again with the emergence of powerful AI code review tools. Services from Anthropic and OpenAI were used earlier this year to scan PHP platforms and eventually a researcher at cybersecurity firm Calif [reported the bugs](https://calif.io/php2shell/) on August 11.

On social media, Calif also [credited](https://x.com/calif_io/status/2112914613297668583) another researcher with initially discovering the vulnerability and developing an exploit.

OpenAI and security companies Wiz and Trail of Bits also found the same vulnerabilities during audits of PHP.

The reports “made the full impact of the … problem clear, and from August 11th onward, fixing it became the top priority for all of the PHP Foundation's team working on security,” the foundation explained.

The PHP Foundation said its coordinated disclosure process was running smoothly until rumors of the bugs began to emerge on social media two days ago. They moved up their disclosure of the bugs by one day but argued that they could not have immediately released it because the fix was still being packaged.

They noted that Calif “mistakenly published a video” that showed their proof of concept working against a number of targets and revealed additional details about the vulnerabilities. [That video](https://x.com/silascutler/status/2112684895608652003/video/2), even after being deleted, began circulating and “accelerated development” of exploitation proof of concepts (PoCs).

PHP Foundation monitored [several of the PoCs](https://x.com/j4ck3lsyn/status/2112703096443097263) that began to circulate online throughout Tuesday evening but did not identify any functional exploits.

The blog notes that cybersecurity firm Chainguard unilaterally broke the embargo early on Wednesday and published images containing the fix.

“Like other distributors, Chainguard had received the patch in advance so its users could update the moment the vulnerabilities were disclosed,” the foundation said.

“Any attacker could now study the fix in binary form while every other PHP user was still waiting for the release. This disregarded weeks of work by many parties toward a coordinated disclosure.”

In response to the PHP Foundation's allegations, Chainguard CEO Dan Lorenc told Recorded Future News that he began to see exploitation attempts last night and made the judgement call to release the information.

"It's not us versus them here. It's all of us working together to minimize risk for the industry. These situations are always tough and require judgment calls. I think the PHP maintainers did a great job here," he said. "They put a lot of time into this patch. They responded to it well. There's going to be a lot more of these to come. We, as an industry, have to figure out how to get through them faster and more coordinated and better."

The PHP Foundation listed out dozens of changes to its internal structure that would not allow a similar situation to occur again and argued that “a serious vulnerability with a fix stuck on hard trade-offs would now reach the PHP Foundation leadership much sooner.”

*Editor's Note: Story updated 2:30 p.m. Eastern U.S. time with comment from Chainguard.*

* [Technology](/news/technology)
* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Industry](/)
* [Government](/news/government)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked acro...