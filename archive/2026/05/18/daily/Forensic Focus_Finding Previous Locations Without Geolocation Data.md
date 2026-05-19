---
title: Finding Previous Locations Without Geolocation Data
url: https://www.forensicfocus.com/articles/finding-previous-locations-without-geolocation-data/
source: Forensic Focus
date: 2026-05-18
fetch_date: 2026-05-19T06:04:48.834306
---

# Finding Previous Locations Without Geolocation Data

[Skip to content](#content "Skip to content")

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/themes/generatepress_child/assets/images/logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

[Login](/sign-in/)
[Register](/sign-up/)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/uploads/2020/05/forensic-focus_logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

Menu

* [News](https://www.forensicfocus.com/news/)
* Community
  + [Forums](https://www.forensicfocus.com/forums/)
  + [Discord (Invite)](https://discord.gg/97zKvTXHeS)
* Resources
  + [Newsletter](https://www.forensicfocus.com/newsletter/)
  + [Articles](https://www.forensicfocus.com/articles/)
  + [Reviews](https://www.forensicfocus.com/reviews/)
  + [Webinars](https://www.forensicfocus.com/webinars/)
  + [Podcast](https://www.forensicfocus.com/podcast/)
  + [Interviews](https://www.forensicfocus.com/interviews/)
  + [Case Studies](https://www.forensicfocus.com/case-studies/)
  + [Well-Being](https://www.forensicfocus.com/well-being/)
  + [Guides](https://www.forensicfocus.com/guides/)
  + [Useful Links](https://www.forensicfocus.com/useful-links/)
  + [Digital Forensics Timeline](https://www.forensicfocus.com/digital-forensics-timeline/)
* Jobs & Careers
  + [View jobs](https://www.forensicfocus.com/jobs/)
  + [How To Start A Career In Digital Forensics](https://www.forensicfocus.com/articles/how-to-start-a-career-in-digital-forensics/)
* Education
  + [Course Listings](https://www.forensicfocus.com/education/)
  + [Education & Training Guide](https://www.forensicfocus.com/articles/digital-forensics-education-certification-and-training-guide/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](https://www.forensicfocus.com/event-info/)

Menu

* [News](https://www.forensicfocus.com/news/)
* Community
  + [Forums](https://www.forensicfocus.com/forums/)
  + [Discord (Invite)](https://discord.gg/97zKvTXHeS)
* Resources
  + [Newsletter](https://www.forensicfocus.com/newsletter/)
  + [Articles](https://www.forensicfocus.com/articles/)
  + [Reviews](https://www.forensicfocus.com/reviews/)
  + [Webinars](https://www.forensicfocus.com/webinars/)
  + [Podcast](https://www.forensicfocus.com/podcast/)
  + [Interviews](https://www.forensicfocus.com/interviews/)
  + [Case Studies](https://www.forensicfocus.com/case-studies/)
  + [Well-Being](https://www.forensicfocus.com/well-being/)
  + [Guides](https://www.forensicfocus.com/guides/)
  + [Useful Links](https://www.forensicfocus.com/useful-links/)
  + [Digital Forensics Timeline](https://www.forensicfocus.com/digital-forensics-timeline/)
* Jobs & Careers
  + [View jobs](https://www.forensicfocus.com/jobs/)
  + [How To Start A Career In Digital Forensics](https://www.forensicfocus.com/articles/how-to-start-a-career-in-digital-forensics/)
* Education
  + [Course Listings](https://www.forensicfocus.com/education/)
  + [Education & Training Guide](https://www.forensicfocus.com/articles/digital-forensics-education-certification-and-training-guide/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](https://www.forensicfocus.com/event-info/)

[Home](https://www.forensicfocus.com/) » [Articles](https://www.forensicfocus.com/articles/) » Finding Previous Locations Without Geolocation Data

# Finding Previous Locations Without Geolocation Data

18th May 202618th May 2026 by [Berla](https://www.forensicfocus.com/author/berla/ "View all posts by Berla")

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/05/0_hero-image.jpg)

Determining the previous locations a suspect or victim visited, and the roads traveled, is one of the main questions investigators use vehicle data to answer. When tracklogs, navigation points or other geo-tagged data is recovered, this is a pretty straightforward task. What happens when a vehicle does not record any of these? Can the question, “Where has this vehicle been?” still be answered?

Recently, in a missing persons case out of New Jersey, investigators were faced with this exact scenario. The recovered vehicle did not record any geolocation data. Despite this, investigators used other time-stamped, distance-based data to identify key areas of interest with a technique called reachability analysis. This ultimately led to the recovery of the victim’s body.

In this article, we are going to show you how to drive your investigations forward with non-geotagged vehicle data, reachability analysis and a few open-source tools to identify previous locations and areas of interest when traditional geolocation data is not an option.

To demonstrate how reachability analysis works, we asked our research team to drive a route from Berla Headquarters (HQ) to a local Park and Ride, simulating a vehicle being abandoned after a crime. The team chose a 2017 Jeep Grand Cherokee with a Uconnect system for this task. Uconnect systems sometimes record tracklogs, but not consistently. Since this is one of our research vehicles, the team already knew we would not get any geolocation data when we acquired the system data.

What the Uconnect system does provide, like many other vehicle systems, is reliable odometer events with timestamps. This allows us to determine both the distance traveled and the time it took. We acquired the data on-site at the Park and Ride and then returned to HQ to analyze it.

## Get The Latest DFIR News

### Join the Forensic Focus newsletter for the best DFIR articles in your inbox every month.

Unsubscribe any time. We respect your privacy - read our [privacy policy](/privacy-policy).

Leave this field empty if you're human:

## Establish Knowns

The process of identifying previous locations or areas of interest, starts with building a timeline of the vehicle’s movements. To do this, we will establish the knowns and identify the unknowns.
What we know is that the vehicle was driven between two known locations — Berla HQ as the starting point and the local ‘Park and Ride’ as the endpoint. What we don’t know is if the vehicle made any stops along the way. If it did, where did those stops occur?

We know the current odometer reading is 54088 miles; we noted it when we got into the vehicle at the Park and Ride to do the acquisition. We also found a receipt for a local gas station, conveniently left in the cup holder.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/05/1_Establish-Knowns-scaled.png)

Using the odometer reading we recorded at the Park and Ride, and the data we acquired from the vehicle, we know the vehicle arrived at the Park and Ride at 1:29:23 pm. Working backwards, we can see the vehicle left Berla HQ at 12:45:42 pm. The odometer events show that approximately 14 miles were traveled over a 43-minute period.

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/05/2_Entire-Trip-A-3-2-scaled.jpg)

Having driven the route, we know the actual trip is approximately 6.1 miles and takes about 12 minutes. This clearly indicates that the vehicle did not take the optimal path and must have deviated from the main route during its journey.

## Identify Unknowns

To identify unknown locations where stops were made, we will analyze the odometer events to determine whether the overall journey can be broken into independent trips. For each trip, we need to identify the start and stop location, distance traveled, and the time it took.

We are looking for patterns or a break in a pattern in the odometer events. We will focus on the timestamp of each event and the odometer reading. Consecutive events with increasing timestamps and increasing odometer values mean that the vehicle is on the move. Gaps in time between two events where the timestamp difference is greater than one minute and the odometer value does not change, indicate the vehicle stopped at a location and the engine was shut off. Consecutive events where the odometer value does not change and timestamps increase over several minutes indicate the v...