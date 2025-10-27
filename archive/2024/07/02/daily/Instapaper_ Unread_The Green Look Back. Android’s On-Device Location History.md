---
title: The Green Look Back. Android’s On-Device Location History
url: https://thebinaryhick.blog/2024/06/28/the-green-look-back-androids-on-device-location-history/
source: Instapaper: Unread
date: 2024-07-02
fetch_date: 2025-10-06T17:50:05.833038
---

# The Green Look Back. Android’s On-Device Location History

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

# The Green Look Back. Android’s On-Device Location History

[Binary Hick](https://thebinaryhick.blog/author/binaryhick/ "Posts by Binary Hick")

[Android](https://thebinaryhick.blog/category/android/), [Locations](https://thebinaryhick.blog/category/locations/), [Mobile](https://thebinaryhick.blog/category/mobile/)

2024-06-28
11 Minutes

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/image.gif?resize=479%2C270&ssl=1)

We’re at now, now.

Back in December of 2023 [Google announced a change](https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/) to Android’s Location History feature that got quite a bit of attention. Prior to the announcement, users could view their location history via the Google Maps application *and* any web browser where they were signed in. That meant the data was stored by and likely accessible to Google, which made anyone who was privacy-minded nervous. Google’s December announcement changed all of that. According to the announcement Location History was getting a new name in the Google Maps UI, “Timeline,” the data it contained would be stored locally on the device instead of their servers, and the default retention time of location data was shortened from 18 months to 3. The announcement went on to say these changes were being done in the name of privacy and control, and they would happen gradually in 2024.

This post is going to be one of my shorter ones. There is not too much to look at; it’s location data, after all. However, the trick comes in validating both its accuracy *and* reliability. Is the data an accurate representation of a device being in a specific place at a specific time, or is it data that that is cached and more generalized that is used by the device for other purposes? These are the questions examiners need to answer when evaluating the value of location data.

There were five devices used for testing: a Galaxy S22, Galaxy S23, Pixel 5a, Pixel 6a, and a Pixel 8a. Four of the devices had an account had been migrated to this new location data paradigm. The Pixel 5a used the same account as the Galaxy S22 because I wanted to see how multiple devices on the same account may interact with each other.

## Finally

Right after the new year I started keeping a lookout for when this data landed on my test Androids, and for months there was nothing that stood out as location data. As it turns out, Google was not exaggerating about that gradual rollout. It was not until May that I got the email for my first account.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-1.jpg?resize=1024%2C1024&ssl=1)

Figure 1. The email.

I was already in the process of extracting test data from my devices due to a potential [upcoming speaking engagement](https://www.sans.org/cyber-security-training-events/digital-forensics-summit-2024/), and after each extraction I would look for this location data, and, initially, I wasn’t seeing anything obvious. The problem was I was looking in the wrong location in the file system. Because Timeline was accessed via Google Maps I had been looking in **/data/data/com.google.android.apps.maps/**. However, *Timeline is a Google account-level feature*. As it turns out, the data is in **/data/data/com.google.android.gms/**. The first file of interest tells an examiner if the account has migrated, and whether or not the feature is on or off. The file is **ULR\_USER\_PREFS.xml**, and it resides in the **~/shared\_prefs** folder. See Figure 2.

[![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-2.png?resize=1024%2C497&ssl=1)](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-2.png?ssl=1)

Figure 2. ULR\_USER\_PREFS.xml with Timeline turned off.

(Note: It’s refreshing to see non-Binary XML (ABX) for once. :-)) There are two entries in this file that are important. The first entry, in the blue box, lets you know if the account has migrated to storing location history on device. I suspect “Odlh” is “On-device Location History,” but that is purely speculation on my part. Here, the value is “true” as this account had already migrated to storing location data locally. I checked previous versions of this file from other extractions that pre-dated my receiving the email from Google, and this value was set to “false.” In those previous extractions, I still found location in the artifacts discussed later in this post even though I had not yet received the email from Google.

The entry in the red box is important. The value associated with the XML tag “**historyEnabled\_Account**” is based on whether or not a user has turned on Timeline for their Google account. Figure 2 showed how **ULR\_USER\_PREFS.xml** looks while Timeline is turned off. Figure 2-1 shows how it looks with it turned on.

[![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-2-1.png?resize=1024%2C476&ssl=1)](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-2-1.png?ssl=1)

Figure 2-1. ULR\_USER\_PREFS.xml with Timeline turned on.

To adjust the setting a user can go through a web browser or adjust it via Google Maps. Figures 3, 4, and 5 show how the Google Maps flow would look to a user.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-3.png?resize=461%2C1024&ssl=1)

Figure 3. Settings menu within Maps app.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-4.png?resize=461%2C1024&ssl=1)

Figure 4. Timeline settings within Maps.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-5.png?resize=461%2C1024&ssl=1)

Figure 5. Timeline on/off setting.

Getting back to the red box in Figures 2 and 2-1, if **historyEnabled\_Account** is set to false, an examiner can expect to find little or no data in the following artifacts discussed in this article depending on two factors. First, Timeline is not enabled by default, so if you are hunting for location data from Timeline, make sure you check this setting first because there is a good chance a user never turned it on. Second, if a user has Timeline on and later opts to turn it off, they are given two options: to turn Timeline off, or to turn Timeline off *and* delete any existing data. See Figure 6.

![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/06/Figure-6.jpg?resize=473%2C1024&ssl=1)

Figure 6. Choices.

One of the XML tags in this file has a timestamp associated with it: “**serverMillis\_Account**.” During testing I found that changing the Timeline on/off setting would cause this timestamp to update; however, I found other extractions where I did not adjust this setting (and its predecessor) and the timestamp would update. So, just know that this timestamp *is not* indicative of when the setting was last changed.

A couple of notes with regards to the settings and multi-device accounts. First, if an account has more than one device associated with it, turning Timeline off on one device affects all devices on the account. Again, this is an account-level setting. Second, based on my testing, if a user turns Timeline off on one device and opts to delete the data, that only affects the device on which that happens. The historical data on the other devices (should it be there) remains. Again, this is how it was during testing, and Google could always change that.

## The Good Stuff…?

...