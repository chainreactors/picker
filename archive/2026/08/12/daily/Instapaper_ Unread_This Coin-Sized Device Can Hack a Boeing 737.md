---
title: This Coin-Sized Device Can Hack a Boeing 737
url: https://www.wired.com/story/this-coin-sized-device-can-hack-a-boeing-737/
source: Instapaper: Unread
date: 2026-08-12
fetch_date: 2026-08-13T04:05:26.126622
---

# This Coin-Sized Device Can Hack a Boeing 737

[Skip to main content](#main-content)

Menu

[WIRED](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[WIRED](/)

Account

Account

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Podcasts](/podcasts/)

[Video](/video/)

[Livestreams](https://www.wired.com/livestreams)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Andy Greenberg](/author/andy-greenberg/)

[Security](/category/security)

Aug 12, 2026 8:00 AM

# This Coin-Sized Device Can Hack a Boeing 737

Security researchers found that in less than 60 seconds, they could open a hatch on a plane’s exterior, plug in a tiny device, and redirect the aircraft’s autopilot or sabotage its flight plan.

![This CoinSized Device Can Hack a Boeing 737](https://media.wired.com/photos/6a7b869fe7d5fc6f31658f9b/master/w_2560%2Cc_limit/Security_60SecondsofAccessandThisCoin-SizedDevice-02.gif)

Photo-Illustration: Jobanny Cabrera; Getty Images

Comment

Loader

Save StorySave this story

Comment

Loader

Save StorySave this story

Even as the digital components of so many life-critical systems have proven susceptible to cybersabotage—[cars](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/), [medical devices](https://www.wired.com/story/defcon-medical-device-village-hacking-hospital/), even [water utilities](https://www.wired.com/story/a-leaked-memo-ties-cyberattacks-on-minnesota-water-utilities-to-iran/) and [power grids](https://www.wired.com/story/russian-hackers-attack-ukraine/)—the computer systems of airplanes have, thankfully, remained uniquely inaccessible to hackers. But one group of academic researchers has spent years testing a different, devious approach to aviation cybersecurity. Perhaps, they suggest, a plane could be hacked the same way that spies and saboteurs have targeted other high-value, offline computers: by surreptitiously gaining physical access to one and plugging in a device designed to silently run the attackers' malicious code.

Tomorrow at the Usenix Cybersecurity Conference, researchers from the University of California at San Diego and Oberlin College will present a hacking technique capable of commandeering the autopilot of a Boeing 737 to redirect its navigation or silently altering key values in the plane's takeoff and fuel calculations while spoofing the results on the pilot's screen—subtle changes the researchers say could potentially cause anything from runway overruns on takeoff to diversions to a different country's airspace to catastrophic crashes.

To carry out that hacking, they've built a roughly coin-sized, Wi-Fi-enabled prototype device that costs less than $100. In less than a minute, that hardware implant can be fitted into a port accessible via a hatch on the exterior of the plane, one that's routinely within reach of maintenance workers or other airport and airline staff between flights. Once it's in place, the device can send electrical signals on one of the 737's internal networks to spoof commands to sensitive computer systems that guide its autopilot and show the pilot variables like the plane's total weight and outside air temperature, which play a critical role in a 737's takeoff calculations.

![The researchers' hacking device next to a quarter for scale.](https://media.wired.com/photos/6a7b87f036c0a5326b1c65a3/master/w_1600%2Cc_limit/signal-2026-08-11-14-53-13-177_002.jpg)

The researchers' hacking device, next to a quarter for scale.

Photograph Courtesy of UCSD

By proving the viability of that technique, the result of a process that stretched over more than a decade and entailed buying tens of thousands of dollars’ worth of plane components for testing, they hope to show that this sort of physical access hacking represents a practical threat in the hands of well-resourced saboteurs and a significant blind spot in aircraft security. Compared to the traditional threat of simply planting a bomb on a plane, they argue, it's also an approach that would offer an attacker more control, stealth, and deniability.

“If you could get 60 seconds with an airplane, what could you do?” asks Stefan Savage, one of the UCSD computer science professors who led the project, describing the question that first motivated their line of research. “Well, it turns out there’s a port that’s externally accessible. You can get to it with no special tools in about 15 seconds. And you can shove in a piece of electronics a little bigger than a quarter that lets you basically tell the autopilot what to do and lie to the pilot about changes to the flight plan.”

![The hacking device  next to the connector it fits into on a Boeing 737 one that can be found inside a port thats...](https://media.wired.com/photos/6a7b88d57516787394c3eaaa/master/w_1600%2Cc_limit/signal-2026-08-11-14-54-42-248_002.jpg)

The hacking device (bottom) next to the connector it fits into on a Boeing 737, one that can be found inside a port that’s accessible from a hatch on the plane’s exterior.

Photograph Courtesy of UCSD

The researchers aren't revealing which port they targeted on the 737, nor are they releasing some details of how their hacking device is able to spoof commands to the plane's computers. They've worked closely with Boeing to share their findings, first disclosing elements of their research to the company more than six years ago, and going so far as to test out and demonstrate their attack in a Boeing facility's test lab.

When WIRED reached out to Boeing about the researchers' work, it responded in a statement that it had carried out its own review of its components' designs, installations, and interfaces in response to the researchers' findings. But it downplayed the practical risk of their physical-access hacking technique. “Our technical experts are confident that the layers of protection in place on the airplane, including within the system design and the operating environment, provide sufficient mitigation to significantly limit the feasibility and risk of real-world attacks,” the statement reads.

For their part, the researchers say, Boeing hasn't told them about any technical fix for the vulnerabilities they've discovered—and they speculate that the company may not in fact implement any such update to their systems for years to come, given how rarely commercial airplanes are redesigned.

That lack of an immediate security update for planes shouldn't be cause for panic or grounding aircraft, they [write in their paper](https://cseweb.ucsd.edu/~savage/papers/UsenixSec26-429.pdf). “All of the authors of this paper routinely travel on Boeing 737 aircraft and expect to continue doing so,” the introduction of the paper reads.

Savage argues, though, that the research has demonstrated the need for long-term changes in both the cybersecurity of airplane components and, perhaps more immediately, the operational security measures that determine who can access a plane while it's on the ground. Their simplest fix suggestion: Plug the port with epoxy, or remove it altogether.

“This is something the aviation industry will want to plan to defend against,” Savage says. “I would not sleep on this one.”

## **Building a Plane, Then Breaking It**

This particular team of researchers' interest in hacking a plane originated nearly a decade and a half ago, when some of them discovered and demonstrated the first successful over...