---
title: PeekList: How Brave’s Playlist bypassed FaceID Protection for Private Tabs
url: https://infosecwriteups.com/peeklist-how-braves-playlist-bypassed-faceid-protection-for-private-tabs-9d1691b077be?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-28
fetch_date: 2026-07-29T05:02:50.145394
---

# PeekList: How Brave’s Playlist bypassed FaceID Protection for Private Tabs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpeeklist-how-braves-playlist-bypassed-faceid-protection-for-private-tabs-9d1691b077be&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpeeklist-how-braves-playlist-bypassed-faceid-protection-for-private-tabs-9d1691b077be&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9d1691b077be---------------------------------------)

·

1. [TL;DR](/?source=post_page-----9d1691b077be---------------------------------------#48d4 "TL;DR")
2. [Background](/?source=post_page-----9d1691b077be---------------------------------------#0c7b "Background")
3. [Affected Environment](/?source=post_page-----9d1691b077be---------------------------------------#f777 "Affected Environment")
4. [Steps To Reproduce:](/?source=post_page-----9d1691b077be---------------------------------------#1988 "Steps To Reproduce:")
5. [Impact](/?source=post_page-----9d1691b077be---------------------------------------#84f5 "Impact")
6. [The Fix](/?source=post_page-----9d1691b077be---------------------------------------#8f08 "The Fix")
7. [Conclusion](/?source=post_page-----9d1691b077be---------------------------------------#5eb3 "Conclusion")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9d1691b077be---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# PeekList: How Brave’s Playlist bypassed FaceID Protection for Private Tabs

[![Aaron Thomas](https://miro.medium.com/v2/resize:fill:64:64/1*lIcoMRojFuqqmWHLmRms9Q@2x.png)](https://medium.com/%40aaront_60605?source=post_page---byline--9d1691b077be---------------------------------------)

[Aaron Thomas](https://medium.com/%40aaront_60605?source=post_page---byline--9d1691b077be---------------------------------------)

4 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9d1691b077be&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpeeklist-how-braves-playlist-bypassed-faceid-protection-for-private-tabs-9d1691b077be&source=---header_actions--9d1691b077be---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Brave Browser Logo

## TL;DR

Brave for iOS lets you lock Private Tabs behind Face ID or a device passcode. That protection can be completely bypassed using the built-in Brave Playlist feature. Adding any video or audio to your Playlist and then selecting “Open in a New Private Tab” from the long-press menu opens a Private Tab with zero authentication prompt even when Face ID/Passcode protection is enabled. This means an attacker with brief physical access to an unlocked device could view a victim’s Private Tab content without ever being asked to authenticate. The issue was reported to Brave via HackerOne and has since been addressed.

## Background

Brave’s Private Tabs on iOS include an optional setting that requires Face ID or a device passcode before the app will reveal any open Private Tab, particularly useful when “Keep Private Tabs” is enabled so that private browsing sessions persist between app launches. The entire point of this setting is to stop someone who picks up an already-unlocked phone from casually opening the browser and landing on private browsing content.

[Brave Playlist](https://brave.com/playlist/) is a separate feature that lets a user save audio or video (for example, a YouTube link) for offline-style playback inside the browser. Playlist items support a long-press context menu with several actions, one of which is “Open in a New Private Tab.” That action opens the link directly in a Private Tab, but it does so through a different code path than the normal Private Tab entry point, and that path does not check whether Face ID/Passcode protection is enabled.

## Affected Environment

* **App:** Brave Browser for iOS
* **Version tested:** 1.88
* **iOS version tested:** 26.4.2
* **Feature:** Brave Playlist → Private Tab Face ID/Passcode protection

## Steps To Reproduce:

Step 1: Enable FaceID Protection for Private Tabs and Keep Private Tabs in Brave Settings

## Get Aaron Thomas’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Step 2: Open Private Tabs and browse any websites

Step 3: Exit out of Private Tabs and add any song or audio to your Brave Playlist. (For this PoC, I used a Youtube video)

Step 4: Enter your Brave Playlist and go to the song you just added.

Step 5: Tap and hold the song until a dropdown menu appears.

Step 6: Tap on the option to “Open in a New Private Tab”

The Private Tab will now open immediately. No Face ID prompt or no passcode prompt, nothing standing between the attacker and the private session. A user would have the false sense of security that nobody can access the content of their private tabs session.

## Impact

An attacker with physical access to an unlocked iPhone running Brave may be able to use this Playlist bypass to gain access into the user’s Private Tabs, defeating the entire purpose of the Face ID/Passcode setting. This is exactly the kind of “shoulder surf” or “phone left on the table for thirty seconds” scenario the protection exists to prevent, and the Playlist menu quietly gives an attacker a way around it.

## The Fix

Brave’s patch wraps the Playlist’s “open in new tab” delegate so that, before a private tab is actually opened, it checks whether Private Tab lock is enabled and the user isn’t already in a private session — and if so, gates the tab open behind `askForLocalAuthentication` (Face ID/Passcode) before proceeding:

```
player: player,
      delegate: .init(
        openTabURL: { [weak browserController] url, isPrivate in
          guard let browserController else { return }
          let isPrivate = Preferences.Privacy.privateBrowsingOnly.value ? true : isPrivate
          let openTab: () -> Void = {
            browserController.dismiss(animated: true)
            browserController.openURLInNewTab(
              url,
              isPrivate: isPrivate,
              isPrivileged: false
            )
          }
          if isPrivate,
            !browserController.privateBrowsingManager.isPrivateBrowsing,
            Preferences.Privacy.privateBrowsingLock.value
          {
            browserController.askForLocalAuthentication { success, _ in
              if success {
                openTab()
              }
            }
          } else {
            openTab()
          }
        },
        ...