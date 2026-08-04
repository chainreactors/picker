---
title: Snowflake Volunteer, an Android app to help people bypass censorship
url: https://blog.torproject.org/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/
source: Tor Project blog
date: 2026-08-03
fetch_date: 2026-08-04T05:01:34.247232
---

# Snowflake Volunteer, an Android app to help people bypass censorship

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Snowflake Volunteer, an Android app to help people bypass censorship

by [pavel](/author/pavel)
| August 3, 2026

![](/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/lead.png)

Bypassing censorship comes down to two challenges: disguising internet traffic from censors while making an open network easy to reach. [Snowflake](https://snowflake.torproject.org) is particularly effective at tackling both of these challenges. It disguises a user's traffic to look like a video call and routes it through volunteer-run proxies using short-lived connections, making the traffic harder to detect and block.

**That's why it's important to have a large and healthy pool of volunteers always available. To achieve that, Snowflake has to be easy to use and deploy, ideally on the devices and with the services they already use.**

Up until this point, volunteers could use browser extensions, a website embed, a command-line tool for desktop, and on Android they can use Orbot's *[Kindness Mode](https://orbot.app/en/kindness/)*. During the first half of 2026, the Snowflake broker saw an average of approximately 146,000 unique volunteer proxy IP addresses checking in each day[1](#fn-nested). Roughly a third of those were associated with Orbot's Kindness Mode. Kindness Mode also makes volunteering tangible by showing users how many connections their proxy has supported.

Seeing how much capacity that feature contributed, [Bloco](https://www.bloco.io/), an Android app studio in Portugal became curious if a standalone app, focused just on volunteering proxies, could reach even more helpers. They reached out to Tor's anti-censorship team which had plans to work on a similar project, but had not yet had the capacity to develop it, yet. So, Bloco took on the task of building such an app.

The motivation grew out of the team's work with [OONI (Open Observatory of Network Interference)](https://ooni.org/), where they saw how NGOs and activists rely on anti-censorship tools to stay safe and connected. After discovering how easy it was to volunteer a Snowflake proxy, the team members wanted to contribute their skills and expertise to an open-source project they cared about.

## A dedicated app for Snowflake volunteers

The Bloco team built on the foundations already developed by the [Guardian Project](https://guardianproject.info) for the mobile Tor ecosystem, including [IPtProxy](https://github.com/tladesignz/IPtProxy). It's an easy-to-use library that brings together the tools and ongoing pluggable transport work needed to integrate Tor into mobile apps, making it easier to keep censorship-circumvention technology current and reuse it across new apps.

With these libraries already in place, that make it easy to build Tor apps for mobile, Bloco was able to focus their effort on:

* Making sure the app runs successfully in the background for as long as possible, while using as little battery as possible.
* Getting the user experience right, so everyone understands what the app is for, and can configure it correctly and according to their internet setup and capabilities.
* Keep volunteers motivated by showing statistics of how much they're helping across time.

![Image features overview](/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/features-overview.png)

The result is Snowflake Volunteer, a single-purpose app that gives volunteers control over when and how they contribute. Users can allow it to run in the background, restrict it to unmetered networks such as Wi-Fi, choose to run it only while the device is charging, and set a limit on how many people it can help simultaneously. Once enabled, the app automatically connects with people seeking a Snowflake proxy and helps route their connection to the Tor network.

After an initial round of testing and feedback with the Tor community, Snowflake Volunteer was launched publicly in April. In May, we saw an average of approximately 1,300 daily unique proxy IP addresses. By June that had risen to approximately 1,700 per dayâan increase of 29% in one month. During this initial period, activity reached a high of more than 2,100 daily proxies. This suggests that a dedicated app can bring additional volunteers into the Snowflake community.

## Become a Snowflake volunteer by downloading Snowflake Volunteer

Snowflake Volunteer is available on [F-Droid](https://f-droid.org/en/packages/io.bloco.snowflake/) and [Google Play](https://play.google.com/store/apps/details?id=io.bloco.snowflake). For those who want to tinker with the app, [you can also build it from the source code](https://github.com/blocoio/snowflake). Helping people bypass internet censorship [takes a global community](https://blog.torproject.org/fighting-censorship-with-webtunnel/). Tell a friend about this new tool or share this post so more people can learn about this app and [provide feedback](https://github.com/blocoio/snowflake/issues/new).

We also would like to thank our community of localizers. Thanks to their efforts, the app is already available in 8 languages (Chinese, English, French, German, Japanese, Portuguese, Turkish and Vietnamese). If you want to expand access to Snowflake Volunteer, consider contributing translations into more languages. Localization is how we reach this global community. Learn [more about the process](https://community.torproject.org/localization/), and [get started](https://hosted.weblate.org/projects/snowflake-volunteers/).

---

1. We analyzed 180 available daily Snowflake broker reports covering January 1 through June 30, 2026. Snowflake broker statistics are published as aggregated snowflake-stats descriptors through [Tor Metricsâ CollecTor archive](https://metrics.torproject.org/collector/archive/snowflakes/)[↩](#fnref-nested)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/&text=There%20are%20many%20ways%20to%20help%20people%20bypass%20censorship%20with%20Snowflake%E2%80%93a%20browser%20extension%2C%20using%20Orbot%20or%20Tor%20Browser%2C%20website%20embedding%20etc.%20We%20set%20out%20to%20experiment%20with%20a%20new%20mechanism%20and%20test%20an%20Android%20app%20called%20Snowflake%20Volunteer%20for%20those%20willing%20to%20help%20people%20reach%20the%20Tor%20network%20and%20circumvent%20censorship%20from%20their%20mobile%20devices.%20It%20was%20built%20open-source%20by%20Bloco%2C%20an%20Android%20app%20studio%20from%20Portugal.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/snowflake-volunteer-standalone-app-to-help-people-bypass-censorship/&text=There%20are%20many%20ways%20to%20help%20people%20bypass%20censorship%20with%20Snowflake%E2%80%93a%20browser%20extension%2C%20using%20Orbot%20or%20Tor%20Browser%2C%20website%20embedding%20etc.%20We%20set%20out%20to%20experiment%20with%20a%20new%20mechanism%20and%20test%20an%20Android%20app%20called%20Snowflake%20Volunteer%20for%20those%20willing%20to%20help%20people%20reach%20the%20Tor%20network%20and%20circumvent%20censorship%20from%20their%20mobile%20devices.%20It%20was%20built%20open-source%20by%20Bloco%2C%20an%20Android%20app%20studio%20from%20Portugal.)
[Bluesky](https://bsky.app/intent/compose?text=There%20are%20many%20ways%20to%20help%20people%20bypass%20censorship%20with%20Snowflake%E2%80%93a%20browser%20extension%2C%20using%20Orbot%20or%20Tor%20Browser%2C%20website%20embedding%20etc.%20We%20set%20out%20to%20experiment%20with%20a%20new%20mechanism%20and%20test%20...