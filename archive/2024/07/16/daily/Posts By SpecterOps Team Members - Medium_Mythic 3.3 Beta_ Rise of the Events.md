---
title: Mythic 3.3 Beta: Rise of the Events
url: https://posts.specterops.io/mythic-3-3-beta-rise-of-the-events-6aeb84aa6fed?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-07-16
fetch_date: 2025-10-06T17:54:12.989267
---

# Mythic 3.3 Beta: Rise of the Events

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6aeb84aa6fed&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmythic-3-3-beta-rise-of-the-events-6aeb84aa6fed&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmythic-3-3-beta-rise-of-the-events-6aeb84aa6fed&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-6aeb84aa6fed---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-6aeb84aa6fed---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Mythic 3.3 Beta: Rise of the Events

[![Cody Thomas](https://miro.medium.com/v2/resize:fill:64:64/1*h8as9jCumXgD8d_EeWCtaw.png)](https://medium.com/%40its_a_feature_?source=post_page---byline--6aeb84aa6fed---------------------------------------)

[Cody Thomas](https://medium.com/%40its_a_feature_?source=post_page---byline--6aeb84aa6fed---------------------------------------)

7 min read

·

Jul 15, 2024

--

1

Listen

Share

A brief overview of Mythic 3.3’s new features

Press enter or click to view image in full size

![]()

Eventing Flows

## Mythic 3.3 Updates

Mythic 3.3 has too many updates to mention them all here, so if you want a deeper dive into the change log, please check it out on [GitHub](https://github.com/its-a-feature/Mythic/blob/Mythic3.3/CHANGELOG.MD#330-rc1---2024-07-09). Instead, we’re going to focus on the biggest changes and why you should care.

Because this Mythic update has so many bug fixes and new features, it is going into a public Beta phase for a few weeks first. To use this Mythic and any updated agents/profiles, be sure to use the `Mythic3.3` branches. When installing a C2 Profile or Payload Type with the `Mythic3.3` beta, you can use the following: `sudo ./mythic-cli install github [url] -b Mythic3.3 -f`

The following projects are updated with a `Mythic3.3` branch for experimentation: Mythic, Poseidon, Apollo, http, websocket, smb, httpx, basic\_webhook, basic\_logger, and example\_containers. You can also check out the [Mythic Overview](https://mythicmeta.github.io/overview/) page to see which installable services are updating.

tldr; what breaking changes are there and how do I update my existing components to work with Mythic 3.3? [Check here](https://docs.mythic-c2.net/updating/mythic-3.2-greater-than-3.3-updates).

## Eventing

Have you ever been on an assessment and thought any of the following:

* I wish I could run a series of tasks every time I get a new callback
* I wish I could automatically increase the sleep time of all my callbacks at the end of the workday and lower the sleep time at the beginning of my work
* I wish I could automatically create a bunch of payloads and feed them through various wrappers
* I wish I could send an alert from my agent to Mythic and trigger a series of actions (like dumping credentials when a new logon happens)
* I wish I could provide my own custom operation security checks across all tasks for all callbacks
* I wish I could intercept a task’s output and augment it before showing it to the user

Well, all of that and more is possible with Mythic’s new eventing system. The eventing system is configured via JSON/YAML/TOML files in a similar way to GitHub’s Actions. Clicking the play icon at the top of Mythic will open a new page where you can manage the eventing options for your operation. Mythic has a default set of action types you can take, but you can also implement your own eventing containers and call arbitrary functions within them. This, combined with access to per-event APITokens and Mythic’s Scripting means that you can do almost anything as an action.

Press enter or click to view image in full size

![]()

Mythic Eventing Example

Be sure to check out the [Mythic documentation](https://docs.mythic-c2.net/customizing/3.-consuming-containers/eventing) for more details on configurations.

## Command Augmentation

One of the more unique aspects of Mythic that everybody can create their own agents that all hook into the same one interface. However, this sometimes means that efforts are duplicated. For example, a few different agents have the capability to run Beacon Object Files (BOFs) in a generic way, but this still means that you need to know ahead of time which arguments each BOF takes, their order, and their types.

If you wanted to leverage Mythic’s unique command parameter functionalities (tab completion, parameter groups, named parameters, etc) for a BOF, then you’d need to create command files and load them up into each payload type and load them into each callback. That can be tedious, especially if some agents use Python and some use Go for their containers. Instead, what if we could build it once in a generic way and automatically “inject” these commands into new callbacks? That’s the idea for command augmentation.

Press enter or click to view image in full size

![]()

Loaded Commands in a Callback

Command Augmentation containers allow you to define everything about a Payload Type like normal, except there’s no build, wrapper, or C2 Profile aspects to worry about. Instead, you’re just defining your commands and general information about your Payload Type so that it can be easily identified in the UI (such as the screenshot above). Just like with normal Payload Types, you can control which callbacks your commands can be associated with. You can scope down your callbacks via Operating System type and even limit via specific agents!

Be sure to check out more details in the [documentation](https://docs.mythic-c2.net/customizing/4.-extending-agent-commands)!

## Auto Triage Tracking

Do you ever get into the swing of things in an assessment, triaging a bunch of file shares and downloading files, but then forget which files you’ve looked at after you’ve downloaded them? Mythic now automatically uses its tagging system to mark which files you downloaded or previewed and when.

Press enter or click to view image in full size

![]()

File Preview and File Downloaded tags in the File Search page

## Custom Authentication and Invites

Randomly generating passwords each time you stand up a Mythic instance or trying to remember your Mythic credentials in addition to so many other credentials can be tedious. If you already have Single Sign On (SSO) set up for your company, then it can be handy to simply use that for your operators instead. Mythic now offers “Auth” containers that allow you to extend Mythic’s authentication process into whatever best suits your environment. For example, you can hook into SAML and ADFS or prompt the user for additional information (like a MFA key) when authenticating. When your container is online and supports one of these me...