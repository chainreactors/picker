---
title: OSINT & The Intelligence Cycle Part III: Processing Raw Intelligence
url: https://www.secjuice.com/osint-intelligence-cycle-part-iii-processing-raw-intelligence/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-13
fetch_date: 2025-10-07T00:48:30.415988
---

# OSINT & The Intelligence Cycle Part III: Processing Raw Intelligence

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[OSINT](/tag/osint/)

# OSINT & The Intelligence Cycle Part III: Processing Raw Intelligence

This OSINT part 3 post explains how to take the raw intelligence and refines it into forms better suited for exploitation and analysis.

* [![Sinwindie](/content/images/size/w100/2020/04/sinlogo.png)](/author/sinwindie/)

#### [Sinwindie](/author/sinwindie/)

Aug 10, 2025
• 3 min read

![OSINT & The Intelligence Cycle Part III: Processing Raw Intelligence](/content/images/size/w2000/2020/09/60ec9b833186c1bc377936eb7e47737f-1.png)

Once enough raw intelligence is gathered from the [collection](https://www.secjuice.com/osint-and-the-intelligence-cycle-part-ii-collection/) phase, the next step is processing. This phase of the intelligence cycle takes the raw intelligence and refines it into forms better suited for exploitation and analysis. Processing keeps the analyst from having to reinspect every piece of raw intelligence (unless they choose to) while also ensuring the data is in a usable format (whether by language or filetype, for the analyst to further exploit). Although not the most exciting phase, processing can significantly cut down the overall time needed for analysis. Some of these tips and recommendations may overlap with the analysis and production phase, particularly if the same staff is responsible for both portions of the OSINT intelligence cycle. Whether I’m processing raw intelligence for myself or another analyst, my usual procedures include the following steps:

## Transcribe, Translate and Decode

If an analyst cannot search, read, or understand the collected information, it poses no value for their analysis. Collected data should be translated, decrypted, or decoded into a human-readable format that the analyst understands. For videos or other media, have the content transcribed so that the analyst can scan for names, keywords, etc. without listening to the entire video or audio clip. If necessary, convert information stored in uncommon filetypes into those that the analysts are more likely to have the correct software to view and exploit. Be sure to also check for any relevant metadata or embedded text that might be overlooked.

## **Consolidate and Reduce**

One purpose of the processing phase is to reduce the amount of raw information handed over to the analyst as not everything that was initially collected will be useful come time for analysis. A csv or pdf of 10,000 tweets from a target may only have 10-20 relevant tweets. When possible, extract only the relevant intelligence and omit any noise. Grouping similar or related intelligence together in one PDF or spreadsheet will also reduce the number of files or sources the analyst has to filter through. This allows an investigator to run analyses without having to find and open up multiple documents or sift through a sea of unrelated information surrounding relevant intelligence.

## Organize and Retain Raw Intelligence

Just because the raw intelligence is filtered out by relevance does not mean the rest of the data can be deleted. Analysts may wish to view the raw collected intelligence, and it should remain available to them should they have any questions or want to confirm correct translation and transcription. Be sure to use informative naming schemes for files and folder structures to aid later searches. I often organize folder directories by platform and then by username with the individual filenames related to notable findings they contain. Organizing the collected data helps reduce the time an analyst spends looking for the right piece of raw data should they need to circle back.

## Generate a Timeline

Intelligence gathered in the collection phase may contain time or date information that allows it to be mapped out on a timeline. Placing relevant intelligence in a timeline aids with tracking major events and may assist in showcasing overall activity and the relationships between events that would otherwise not be discernible due to intelligence gaps. By cross-checking the known sequence of events, a timeline also helps approximate a time and date for other events that might not have initially included such information.

## Leverage Spreadsheets

Spreadsheets are one of the most versatile ways to view, sort, and manipulate raw data. They are also often accepted input types in various analysis and visualization tools such as Maltego and I2. Converting raw data into spreadsheet format allows analysts to quickly run different types of functions on the data, or convert it into charts and graphs to supplement their analyses, and get a high-level view of the overall data.

## Conclusion

The OSINT intelligence cycle's processing phase takes the raw data gathered from the collection phase and refines it in preparation for analysis. Processing raw intelligence helps mitigate data overload for analysts and streamlines the next phase, analysis, and production, which takes this processed data and begins shaping it into an intelligence product.

![](https://www.secjuice.com/content/images/2020/09/60ec9b833186c1bc377936eb7e47737f.png)

The awesome image in this post is called "[Dogs illustration doodles](https://dribbble.com/shots/10148488-Dogs-illustration-doodles?ref=secjuice.com)" by [Monstroman](https://dribbble.com/monstroman?ref=secjuice.com)

## Sign up for more like this.

[Enter your email

Subscribe](#/portal)

[![Rethinking Anonymity: Why Privacy Browsers Fall Short](/content/images/size/w600/2025/08/AdobeStock_1265650796-1.jpeg)](/anonymous-browser-browsing-anonymously/)

[## Rethinking Anonymity: Why Privacy Browsers Fall Short

Blocking trackers or using privacy browsers no longer guarantees true anonymity. As surveillance grows more sophisticated, traditional privacy browsers, while helpful, often fall short in protecting users' privacy.](/anonymous-browser-browsing-anonymously/)

Aug 12, 2025
3 min read

[![The OSINT Intelligence Cycle Part 1: Planning and Direction](/content/images/size/w600/2020/08/ghostbusters.png)](/osint-intelligence-cycle-part-i-planning-and-direction/)

[## The OSINT Intelligence Cycle Part 1: Planning and Direction

My advice for those wishing to improve their OSINT skills is to go back to the basics, namely the intelligence cycle.](/osint-intelligence-cycle-part-i-planning-and-direction/)

Aug 12, 2025
3 min read

[![OSINT & The Intelligence Cycle Part II: Lets Talk About Collection](/content/images/size/w600/2020/09/4-1.jpg)](/osint-intelligence-cycle-part-ii-collection/)

[## OSINT & The Intelligence Cycle Part II: Lets Talk About Collection

Part two of my guide to the OSINT intelligence cycle. Once you mapped out your planning and direction phase, the next step is collection.](/osint-intelligence-cycle-part-ii-collection/)

Aug 11, 2025
3 min read

[Secjuice](https://www.secjuice.com) © 2025

* [Dog Friendly Hotels](https://rochdog.com)
* [Dog Friendly Community](https://rochsociety.com)
* [Dog Friendly Directory](https://rochdog.com)
* [Donate](https://opencollective.com/secjuice)

[Powered by Ghost](https://ghost.org/)