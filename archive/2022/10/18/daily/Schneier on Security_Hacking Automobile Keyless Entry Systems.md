---
title: Hacking Automobile Keyless Entry Systems
url: https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html
source: Schneier on Security
date: 2022-10-18
fetch_date: 2025-10-03T20:09:43.822976
---

# Hacking Automobile Keyless Entry Systems

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

## Hacking Automobile Keyless Entry Systems

Suspected members of a European car-theft ring have been [arrested](https://www.europol.europa.eu/media-press/newsroom/news/31-arrested-for-stealing-cars-hacking-keyless-tech):

> The criminals targeted vehicles with keyless entry and start systems, exploiting the technology to get into the car and drive away.
>
> As a result of a coordinated action carried out on 10 October in the three countries involved, 31 suspects were arrested. A total of 22 locations were searched, and over EUR 1 098 500 in criminal assets seized.
>
> The criminals targeted keyless vehicles from two French car manufacturers. A fraudulent tool—marketed as an automotive diagnostic solution, was used to replace the original software of the vehicles, allowing the doors to be opened and the ignition to be started without the actual key fob.
>
> Among those arrested feature the software developers, its resellers and the car thieves who used this tool to steal vehicles.

The article doesn’t say how the hacking tool got installed into cars. Were there crooked auto mechanics, dealers, or something else?

Tags: [cars](https://www.schneier.com/tag/cars/), [hacking](https://www.schneier.com/tag/hacking/), [keys](https://www.schneier.com/tag/keys/), [law enforcement](https://www.schneier.com/tag/law-enforcement/), [theft](https://www.schneier.com/tag/theft/)

[Posted on October 17, 2022 at 10:07 AM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html) •
[12 Comments](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html#comments)

### Comments

Ollie Jones •
[October 17, 2022 11:14 AM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411205)

I wonder if this is confusion on the part of the press-release author? The whole thing would make more sense if the attack vector were some kind of code-stealing and replay gadget.

Austin •
[October 17, 2022 12:19 PM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411211)

per: <https://www.the420.in/europol-arrests-31-for-stealing-cars-by-hacking-keyless-technology/>

I wonder if this is like an OBD2 port diagnostic tool that can use either wifi or bluetooth to let you read data (and sometimes change) on your vehicle. There are several of these in the US market that they intend you to keep plugged in permanently for various reasons. Some are for diagnostics and your smartphone periodically collects data and sends to their servers where you can look up stats 1or get alerts. Some are “parental controls/monitoring” of your teenage driver, and many are from insurance providers for tracking your driving habits to ‘potentially’ lower your bill.

lurker •
[October 17, 2022 12:44 PM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411214)

Bleepingcomputer says they asked for more detail and haven’t yet got it.

PCMag says servers were seized that “had recorded over 53,000 connections.”

SpaceLifeForm •
[October 17, 2022 2:59 PM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411215)

Supply Chain attack comes to mind.

If the Diagtool is hacked at the creator side, then it could appear that when used by unwitting techs, it still provides the correct diagnostic info but silently creates the security hole.

SeanB •
[October 17, 2022 3:02 PM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411216)

Going to guess this was a common BT OBD plug, with slightly rewritten firmware, that allowed it to copy the CAN bus messages from the real fob, and allow them to be replayed, allowing the thieves to approach the parked vehicle, open the door and drive it off, as the system replayed the data from the original fob to the immobiliser, which them allowed start, and also allowed the doors to be unlocked on command. Then they can plug in the OBD port and, with the vehicle active, simply pair a new set of fobs to the immobiliser, and delete the originals, allowing them to move the vehicle and sell it in another country.

Going to say the devices were installed either by mechanics at dealerships, or by valets at hotels, or any place, like a car wash, where you leave your vehicle with other people unattended for a few minutes, as it takes little time to plug this small unit into the OBD connector, or with a little more time unscrew the existing OBD connector, and replace it with this device integrated into a short wire loom, with a socket to screw to the existing location, and a plug to plug into the original, so it does not appear to be there from cursory inspection. Common with things like car trackers used on those on “buy here pay here” places, or if you use the vehicle as surety for a loan, so they can recover the asset if it is needed.

Ted •
[October 17, 2022 10:32 PM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411229)

This is from a French article (translated):

“The thieves, experts in car hacking, bought from the organization tablets, software and connectors allowing them to “duplicate vehicle keys but also to program blank keys without having the original” and to “modify embedded systems fitted to many vehicles”, according to the gendarmerie .

These digital kits were sold on a website, hosted by several companies based in France, which recorded more than 53,000 connections “which could correspond to as many thefts or attempts to reprogram keys”.”

<https://www.20minutes.fr/faits_divers/4005516-20221014-vols-voitures-31-membres-organisation-criminelle-interpelles-france>

Here’s another article:

“The searches led to the seizure of more than one million euros in criminal assets, dozens of blank vehicle keys of all brands, as well as computer equipment.”

<https://www.bfmtv.com/police-justice/vols-de-voitures-31-membres-d-une-organisation-criminelle-interpelles-en-france_AD-202210140640.html>

Here’s also a tweet from the French National Gendarmerie with what looks like a picture of seized assets.

<https://twitter.com/gendarmerie/status/1581196341333864448>

Denton Scratch •
[October 18, 2022 7:15 AM](https://www.schneier.com/blog/archives/2022/10/hacking-automobile-keyless-entry-systems.html/#comment-411242)

That’s an odd report.

They re-programmed the car, so they could unlock the doors and start the engine?

How were they able to re-program the car, without first gaining access? Is this “automotive diagnostic solution” something like Intel’s ME, whereby the firmware can be re-blown remotely, even when the machine appears to be switched off?

I haven’t tinkered with a car for 30 years, and I haven’t owned one for 20. Time was when an ordinary person lik...