---
title: Mythic 3.3 — Out of Beta
url: https://posts.specterops.io/mythic-3-3-out-of-beta-9979e82660c3?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-08-29
fetch_date: 2025-10-06T18:05:51.232991
---

# Mythic 3.3 — Out of Beta

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9979e82660c3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmythic-3-3-out-of-beta-9979e82660c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmythic-3-3-out-of-beta-9979e82660c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-9979e82660c3---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-9979e82660c3---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Mythic 3.3 — Out of Beta

[![Cody Thomas](https://miro.medium.com/v2/resize:fill:64:64/1*h8as9jCumXgD8d_EeWCtaw.png)](https://medium.com/%40its_a_feature_?source=post_page---byline--9979e82660c3---------------------------------------)

[Cody Thomas](https://medium.com/%40its_a_feature_?source=post_page---byline--9979e82660c3---------------------------------------)

8 min read

·

Aug 28, 2024

--

Listen

Share

[Mythic 3.3](https://github.com/its-a-feature/Mythic) was released in a Beta six weeks ago, and since then there has been a bunch of feedback, not just about new Mythic 3.3 features but about the framework overall. Now that Mythic is exiting Beta and going to a full release, I wanted to take a moment and highlight some of these newer features that aren’t in the original [announcement post for Mythic 3.3](https://medium.com/specter-ops-posts/mythic-3-3-beta-rise-of-the-events-6aeb84aa6fed).

## File Rendering

When downloading files in Mythic 3.2, Mythic offered a series of buttons you could click to try to render the downloaded file in your browser or to preview the first 512KB of the file as strings or hex. Now, in Mythic 3.3, this view is updated to condense all that functionality into one solution. This also provides some contextual metadata about the file at the top. If the file is text, then Mythic will automatically try to determine the file syntax based on the file extension and automatically select the right syntax highlighter. The following screenshot shows the download of a Golang file with the new in-line media renderer:

Press enter or click to view image in full size

![]()

File Media Renderer

This functionality is available for [browser scripts](https://docs.mythic-c2.net/customizing/payload-type-development/browser-scripting#media) with the `media` field as well as in the file search page and file browser.

## File Browser

During assessments, operators might spend a large amount of time in Mythic’s file browser triaging multiple hosts and file shares to find that one special file that gives them the keys to the kingdom. Because of this, it’s important to have a workflow that minimizes operator friction. The new file browser in Mythic 3.3 has a lot of improvements to help with this:

Press enter or click to view image in full size

![]()

Mythic 3.3 File Browser Helpful Hints

The new file browser has a few more buttons in the top navigation pane to help movement feel more natural. There’s forward and backward icons to go through your traversal history as well as an up icon to go up a folder. If you get file browser data for a folder, Mythic will automatically infer that the parent folders must exist on the system, even though you haven’t explicitly listed them. To make this scenario clearer, Mythic now displays a message indicating that you don’t have data for this path explicitly and gives a helpful button to task an agent to list it.

On the right-hand side there’s a new button next to the file upload cloud. This is disabled by default, but when enabled, if you browse to a folder that has not yet been listed (such as in the screenshot above), then Mythic will automatically issue the list tasking for you. This allows you to quickly click through folders and have tasks kick off to fetch data without you explicitly clicking “list” each time.

If you try to list out the contents of a folder and get denied, Mythic will show a red exclamation point, but in Mythic 3.2 you wouldn’t get any additional context from the file browser itself. In Mythic 3.3, the file browser will change to show you the exact task that failed so you can see why (such as the access denied in the following screenshot):

Press enter or click to view image in full size

![]()

Access Denied in File Browser

## Situational Tracking

As you’re operating and you get many callbacks from your targets, it can be difficult to correlate which tab you’re interacting with and which callback that corresponds to. Similarly, when you’re browsing in the file browser, it can be easy to lose track of where you are in the tree view if you’re clicking through folders on the table view. To help with this, both the file browser and active callbacks table will auto scroll and highlight what you’re interacting with.

This means as you click between your active tabs, the corresponding callback is highlighted and scrolled into view if needed. In the screenshot below we have a file browser tab for callback 1757 selected and we can see the corresponding callback also highlighted at the top.

Press enter or click to view image in full size

![]()

Active Callback Highlighting

## Interactive Task Searching

One of the newer features of Mythic3.2 is the ability to perform “interactive” actions through your normal async communications channels. This can manifest in a variety of different ways in agents, but a common implementation is to allow an operator to drop into a pseudo terminal on the target and run commands. When doing this through `Poseidon`'s `pty` command, you drop into your specified terminal and get a full logon session, complete with the user’s environment, \*rc files, and history. This also means you can save environment variables and even run `sudo` normally (including providing a password).

While this is extremely helpful, it breaks one of Mythic’s normal flows — task and output tracking. You’re issuing new tasks to your agent (which are tracked), but all of the output is smashed together through the interactive tasking command. While you’re interacting with the task, this isn’t a huge issue, but when it comes time to search, there’s no more correlation. In Mythic 3.2, this meant you’d have to specifically search for the overarching interactive task and just browse through all the output to find what you’re looking for. In Mythic 3.3 though, we can approximate the responses from around the time that the task was issued and guess what the output might be. In the screenshot below we can see that we issued `whoami` to a `pty` task. We fetch the first five results from the agent after that task was issued and return that to the user with an indication of which `pty` task this belonged to....