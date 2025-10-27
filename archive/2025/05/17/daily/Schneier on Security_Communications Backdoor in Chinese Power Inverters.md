---
title: Communications Backdoor in Chinese Power Inverters
url: https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html
source: Schneier on Security
date: 2025-05-17
fetch_date: 2025-10-06T22:29:23.658883
---

# Communications Backdoor in Chinese Power Inverters

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

## Communications Backdoor in Chinese Power Inverters

This is a [weird story](https://www.msn.com/en-us/news/world/ar-AA1EMfHP):

> U.S. energy officials are reassessing the risk posed by Chinese-made devices that play a critical role in renewable energy infrastructure after unexplained communication equipment was found inside some of them, two people familiar with the matter said.
>
> […]
>
> Over the past nine months, undocumented communication devices, including cellular radios, have also been found in some batteries from multiple Chinese suppliers, one of them said.
>
> Reuters was unable to determine how many solar power inverters and batteries they have looked at.
>
> The rogue components provide additional, undocumented communication channels that could allow firewalls to be circumvented remotely, with potentially catastrophic consequences, the two people said.

The article is short on fact and long on innuendo. Both more details and credible named sources would help a lot here.

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [China](https://www.schneier.com/tag/china/), [infrastructure](https://www.schneier.com/tag/infrastructure/), [power](https://www.schneier.com/tag/power/)

[Posted on May 16, 2025 at 9:55 AM](https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html) •
[29 Comments](https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html#comments)

### Comments

Technotron •
[May 16, 2025 10:32 AM](https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html/#comment-445281)

The Israelis had planned explosives in pager batteries. Here we find radios. We need a complete architectural specification, approval and audit at the component level for everything we purchase for our critical infrastructure – from any nation.

Ray Dillinger •
[May 16, 2025 11:10 AM](https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html/#comment-445282)

See, this is the kind of thing that tariffs can and should be applied to. This is a foreign power, clearly setting up a capability to attack the infrastructure and communications of other nations and setting up a capability (which may be in use already) of exfiltrating data from other nations. From the POV of other nations, that’s behavior that ought to be avoided and discouraged in commerce.

Devices designed to bypass firewalls and security, capable of sending data via radio, cell phone, or satellite, PARTICULARLY if those devices are also typically used in communications or industrial infrastructure, and PARTICULARLY if those devices also contain cameras and/or microphones (including unauthorized, undocumented cameras and microphones), ought to be subject to a tariff.

To avoid market shocks, I’d start it out around ten percent, raise it by another ten percent every quarter such devices are found to still be manufactured, and lower it by one percent every quarter no new such devices are found.

Unfortunately, this would include virtually all cars and cell phones manufactured today, at least three-quarters of all IOT (Internet Of Targets) devices, many baby monitors and children’s toys, and a plethora of things sourced from third countries that knowingly or unknowingly used Chinese components in their manufacture.

SeattleSipper •
[May 16, 2025 12:14 PM](https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html/#comment-445284)

I am remember the days when people made fun of news reports that hidden snooping chips were being embedded in motherboards by Chinese manufacturers. They may have gotten the details wrong but the underlying strategy was reported correctly.

Clive Robinson •
[May 16, 2025 12:20 PM](https://www.schneier.com/blog/archives/2025/05/communications-backdoor-in-chinese-power-inverters.html/#comment-445285)

@ Bruce, ALL,

I would expect to find communications in “grid equipment” it is after all what US, UK and European politicians insisted happen for “Smart Grids” and why you will find such radios in “Smart Meters” as well.

Home Solar and Wind installations tend to have Bluetooth or 900Mhz ISM band radios in then to talk back to peoples Smart Phones and central control systems. Likewise city and suburban Smart Meters to a “lamp-post or pillar-box” in the street.

Why? Because it saves a lot of money in installation and maintenance of home systems. Remember the US UK and European Governments want “smart grids” and so the ability to control your house hold appliances like electric water heaters, fridges and freezers and obviously all those new shinny heat pumps they are trying to ram down peoples throats. Because domestic electrical demand is rising and nobody wants to pay to upgrade “the grid” to meet “peek capacity” thus by controling “the load” they can get as much as ten times the number of users on the same back spur just by time shifting when the appliance is on or off.

Look at it this way lets say 10 fridges draw 1 amp each about 2minutes in approximately a thirty minute period. If they are time synced and capped you know the total load will only be 1 amp running maximum and a peak of 5-10 times that for the start up which will be time phased apart.

This the I^2R “heating loss” in the back spur is kept down.

However if the fridges are not synced and capped then you can get all the fridges on at the same time hence 10 amp running load, but consider the peek startup load could be as high as 100amps or more if they cause the line voltage to brown out. This high “in rush” or “startup” current is a consiquence of the likes of DC or AC motors and most Switch Mode Power Supplies.

Switch mode power supplies and DC motors made with rare earth magnets are modern features of domestic appliances because their high efficiencies are the only way to meet “The Energy Star” ratings legislated

However Bluetooth and ISM band radios have a quite limited “reliable range” of maybe 25-100ft with both antennas at ground level.

Thus for larger systems 2G and later GSM radios are used which work in nearly all first world cities and urban areas and quite a few rural areas.

Now from a manufacturing perspective the way to add the plethora of radio communications including the newer LoRa systems is to use a “common chip” to cut inventory and development costs…

Such chips are known as “Systems on a Chip”(SoC) and they are so ubiquitous that they end up in even hand hair dryers and the irons you use for making your cloths look presentable. Oh and yes they have also been used in “sex toys” to do remote control from a mobile phone.

This is the promise of regulated Smart Grids and Smart Devices/appliances in “Smart Homes” on “Smart Grids” for governments and corporations. Oh and don’t forget all those “Internet of Things...