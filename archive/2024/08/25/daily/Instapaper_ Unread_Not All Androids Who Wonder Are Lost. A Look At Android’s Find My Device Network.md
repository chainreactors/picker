---
title: Not All Androids Who Wonder Are Lost. A Look At Android’s Find My Device Network
url: https://thebinaryhick.blog/2024/08/23/not-all-androids-who-wonder-are-lost-a-look-at-androids-find-my-device-network/
source: Instapaper: Unread
date: 2024-08-25
fetch_date: 2025-10-06T18:02:49.526154
---

# Not All Androids Who Wonder Are Lost. A Look At Android’s Find My Device Network

[Skip to content](#content)

[![](https://secure.gravatar.com/avatar/30a89971088a09252b6d39339ea487072e9352a20f7a711253ed149206bc4794?s=80&d=identicon&r=g)](https://thebinaryhick.blog/)

[The Binary Hick](https://thebinaryhick.blog/)

Thoughts From a Digital Forensic Practitioner

Menu

* [Public Images](https://thebinaryhick.blog/public_images/)
* [Contact](https://thebinaryhick.blog/contact/)
* [Bluesky](https://bsky.app/profile/thebinaryhick.blog)
* [Mastodon](https://infosec.exchange/%40joshua_hickman1)
* [X (Twitter)](https://x.com/josh_hickman1)

# Not All Androids Who Wander Are Lost. A Look At Android’s Find My Device Network

[Binary Hick](https://thebinaryhick.blog/author/binaryhick/ "Posts by Binary Hick")

[Android](https://thebinaryhick.blog/category/android/), [Locations](https://thebinaryhick.blog/category/locations/), [Mobile](https://thebinaryhick.blog/category/mobile/), [Trackers](https://thebinaryhick.blog/category/trackers/)

2024-08-232024-08-24
24 Minutes

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/image.gif?resize=500%2C257&ssl=1)

Where am I???

*NOTE: portions of this post appeared in my presentation at the 2024 SANS DFIR Summit.*

Where did the summer go? August is almost behind us, but it seems like yesterday the kids got out of school here in the U.S. Conferences, work and vacations have a way of making the time fly.

Back in May of this year Google finally starting sending emails to users about a new feature on Android’s Find My Device (FMD) network: allowing Bluetooth trackers to be located using the milions of Android phones out in the wild. This was after announcing plans to do so at I/O 2023. So what took long? After the privacy and safety issues that arose from the arrival of AirTags, Google and Apple decided it would be best to collaborate in order to ensure users of Android and iOS had a way to detect unwanted FMD trackers. This collaboration included the [creation of a formalized specification on Bluetooth trackers](https://datatracker.ietf.org/doc/draft-detecting-unwanted-location-trackers/01/). When iOS 17.5 was ready to be released, Google flipped the switch and more Bluetooth trackers were now available in the wild.

It doesn’t take much work to find articles about how individuals with malicious intent use AirTags for nefarious purposes. Stalking and ancillary offenses are not new. However, the near-ubiquitous availability of the technology and the low price-point makes it really easy and convenient for individuals who would otherwise not be inclined to do such things to do so from the comfort of their homes. Just before I left for the SANS DFIR Summit I had a 4-pack of AirTags shipped to my home in a matter of hours by Amazon for $70 USD. I could have easily driven to my local Target store to get the same thing much sooner. While there are not many FMD-compatible trackers on the market *yet*, they are coming, and the mass availability and cost will be the same.

Considering all of this, I decided to take a look at FMD from both an owner’s perspective and from a target’s (i.e., a victim). As forensic examiners, it will only be a matter of time before a phone comes across our benches involving FMD and these trackers. This is going to be one of my longer posts, so buckle up.

For testing, I had several devices that were used over a 2 and half month period:

* Pixel 5a (Android 14, May, June, July SPLs)
* Pixel 8a (Android 14, May, June, July SPLs)
* Pixel Tablet (Android 14, May, June, July SPLs)
* Chromebook
* Galaxy S22 (One UI 6, May, June, July updates)
* Galaxy S23 (One UI 6, May, June, July updates)
* iPhone 14 (iOS 17.5.1)
* iPhone 14 Pro (iOS 17.5.1 & 17.6, and 17.6.1)

The Pixel devices (5a, 8a, Tablet) and Chromebook were all on the same Google account. The Galaxy devices each had their own Google account. The iPhones had no Google accounts associated with them, but, because we are also talking about unwanted trackers, they were included in the testing because both could be “victims.”

I will go ahead and remove the suspense around the Chromebook – it never appeared in my FMD data. It is quite possible my particular hardware model was not compatible, but you will not see it again in the rest of this post.

## The Trackers

As of the time of this post there are only two OEMs that make Bluetooth trackers that are compatible with the FMD network: Chipolo and Pebblebee. For testing, I chose the latter OEM. Specifically, I used the Pebblebee Clip.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Clip_Front.jpeg?resize=1024%2C768&ssl=1)

The front of the Pebblebee Clip.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Clip_Back.jpeg?resize=1024%2C768&ssl=1)

The back of the Pebblebee Clip.

Pebblebee makes FMD trackers in other form factors, so keep that in mind while reading this post. The first picture shows the front of the trackers; note the Pebblebee logo in the middle. There is a physical button underneath the logo, and different press-sequences caused the trackers to do certain things. Depending on the OEM, there may or may not be a button, and the hardware functionality will likely be different.

The second picture shows the back of the tracker. Note there is a serial number (left) and MAC address (right) on the bottom portion of the tracker. These will not be seen again in the rest of this post as I never found them in any of the data I examined, so pairing a physical tracker back to its owner is going to require help from Google. More on that later.

## Setup and Enrollment

Being able to pair FMD trackers to a phone assumes that the user is already participating or is willing to participate in FMD. Users, like myself, were sent emails from Google when their accounts were eligible to start participating in FMD. At the time of this post, using trackers on FMD is only available to users in North America, with the rest of the world getting the capabilities in the future. Additionally, users will need a device running Android 6 or higher and be running the Google Services update from May 2024 or later. In order for a phone to detect and report locations about seen items back to FMD, it needs to be running Android 9 or higher.

When enrolling a phone in the FMD network a user has to decide *how* they want to participate in FMD in regards to detecting other people’s stuff. A user has two options:

1. With Network in High-Traffic Areas Only. This setting means a user’s device will only report seen trackers to FMD while located in areas with a lot of other Android users. Think of being in a busy shopping mall/office complex, an airport, a traffic jam on a major highway, or major event where there are a lot of other people. This setting also enforces what Google calls “aggregated detection.” Basically, more than one Android device has to detect the tracker/thing being located in these high traffic areas before its location is reported back to FMD.
2. With Network in All Areas. This setting basically removes to the two caveats in the other setting. A single Android that detects a tracker/thing will report its location back to FMD regardless of where the Android is.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-1.jpg?resize=473%2C1024&ssl=1)

Figure 1. Participation options.

The default setting here is “With Network in High-Traffic Areas Only.” Google states this is done for privacy reasons, which I get; however, it does cause performance issues with FMD. A quick Google search will find several articles and Reddit posts that complain about how bad tracking performance is on FMD, and this setting seems to contribute to the poor performance. One example can be found [here](https://9to5google.com/2024/07/07/android-find-my-device-airtag-mail-comparison/). Google recommends that users change the setting to “With Network in All Areas” to help with the performance (why isn’t this default then?), and state they are impl...