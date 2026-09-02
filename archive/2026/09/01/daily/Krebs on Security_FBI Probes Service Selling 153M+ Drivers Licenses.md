---
title: FBI Probes Service Selling 153M+ Drivers Licenses
url: https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/
source: Krebs on Security
date: 2026-09-01
fetch_date: 2026-09-02T06:41:49.833216
---

# FBI Probes Service Selling 153M+ Drivers Licenses

Advertisement

[![](/b-gartner/11.png)](https://www.gartner.com/en/conferences/na/symposium-us/sessions?utm_medium=display&utm_campaign=EVT_NA_2026_SYM36_PD_BN1_STAYAHEAD&utm_term=krebs)

Advertisement

[![](/b-doppel/19.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# FBI Probes Service Selling 153M+ Drivers Licenses

September 1, 2026

[10 Comments](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/#comments)

A new identity theft service launched on the dark web this week is selling digital scans of more than 153 million drivers licenses from people in the United States and Canada. Based on interviews with individuals whose licenses are available for purchase on this service, it appears to be siphoning images collected by a widely-used identity verification company based in Louisiana. KrebsOnSecurity also has learned that the New Orleans field office of the **Federal Bureau of Investigation** (FBI) today launched an official inquiry into the source of the images.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/nexus-phegseth.png)

A record available at this identity theft service that includes the drivers license for U.S. Defense Secretary Pete Hegseth, who is one of several high-ranking U.S. government officials whose drivers licenses can be found for sale.

On Monday, Aug. 31, a source alerted KrebsOnSecurity to a service advertised by a new user on the Russian cybercrime forum **Exploit**, offering access to digital scans of identity documents on more than 170 million people in North America. The source brought it to my attention because the proprietor of this identity theft service offered my Virginia drivers license as a free sample in their initial sales thread on Exploit.

The service, dubbed **Nexus**, claims to have more than 153 million drivers licenses for people in the United States and Canada, as well as more than 10 million identification cards; more than three million travel documents and/or international IDs; and at least 579,000 medical cards.

A quick look around Nexus finds they are likely not exaggerating about that 153 million number: Running a blank search in Nexus (with no search parameters entered) returns approximately 11.5 million pages of results, with roughly 15 results displayed per page. It includes documents from people in both Canada and the United States, but the bulk of these records are on Americans: searching for just Canadian drivers licenses returns approximately 1.1 million results, with the largest concentration from Ontario (473,673 records).

Curiously, the identity records include not only drivers licenses but also marijuana dispensary cards. Some of the records list their “source” as “CDL,” presumably short for “commercial drivers license.” Other records carry the source notation of “CAC,” which may refer to Common Access Cards, government issued identity cards that grant physical access to government buildings and secure rooms.

The people behind Nexus claim the license images are coming from an active breach at “a major identity verification company” whose customers include multiple Fortune 500 companies.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/nexus-totals.png)

The record totals listed by the Nexus identity theft service. The number of drivers license records increased by nearly 400,000 in the span of just 24 hours.

“We have been continuously exfiltrating new data for over a year into our private database,” the service enthused in its introductory post on Exploit. “Records are available to preview before purchase with pertinent information redacted. Customer photos are displayed if available.”

Indeed, over the past 24 hours, the number of drivers license records listed as available in Nexus has increased by nearly 400,000, suggesting that freshly stolen license data is being harvested and uploaded to this service on a semi-regular basis.

The record that features my drivers license includes six image files — three pairs of photos of the license’s front and back — a basic image scan — as well as infrared and ultraviolet versions of the same images. A date and timestamp is appended to each image file, and the timestamp on my license scan corresponds to a date in June 2025 when I took a flight to the midwest United States to attend a family funeral.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/nexus-bk.png)

Some of the 153 million+ license scans — including mine — feature six image files with date and timestamps appended to the filenames. Not all records include photos, and some that do feature photos do not display the associated filenames.

Intent on discovering the source of this data, KrebsOnSecurity asked more than a dozen friends and family members for permission to search for their licenses in this service. Each person whose license could be found (nine of them) confirmed having traveled on or very close to the dates in the timestamps attached to their images. It is unclear what timezone these timestamps are in, but from reviewing car rental records shared by several people who helped with this research, it appears the timezone is set to Greenwich Mean Time (GMT).

At first, I thought the source of the data might have something to do with airports. However, that theory went out the window when it became apparent there were no passports in this data set. Also, only some of those who helped with this research said they showed their drivers license at the airport on the day of their travel. One person whose license was in Nexus hadn’t flown at all recently, but was renting a car from **Hertz** for several months around the date of their timestamp.

Two of those who agreed to help are federal employees who said they shared other forms of government identification when passing through airport security. However, those individuals each said they shared their state-issued drivers licenses later that day when renting vehicles at their respective destinations, and that both rented their cars from Hertz.

After finding a note in my calendar for the day of my June 2025 flight reminding me to bring my passport, I remembered that I also never actually shared my drivers license when I went through security at Reagan National Airport on that day because I did not yet have a Real ID, a security-enhanced drivers license that is now required by the Transportation Security Administration (TSA) for all domestic travel. Instead, I showed the TSA agent my government-issued U.S. passport.

Here’s where it gets interesting: I was able to find my mother’s drivers license in this service as well, and the timestamps for her images are just a few seconds apart from mine. That’s notable because we both handed our licenses to the Hertz rental car representative at the same time.

According to my mom, the only place she gave her drivers license to that day was the rental car company, and if memory serves that is also true for me. I don’t recall if the rental car representative inserted our licenses into any kind of machine, but I remember they held onto them for several minutes behind the counter while we were signing various forms. KrebsOnSecurity sought comment from Hertz and will update this story in the event they reply.

**Zach Edwards** is a well-known security and privacy researcher who recently launched a service called [DecryptAds](https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out/) to help people better understand how online advertisers are tracking them. A scan of...