---
title: iOS Telegram Forensics. Part II Artifacts, Secret Chats, Cache, Deleted Messages
url: https://belkasoft.com/ios-telegram-forensics-artifacts
source: Instapaper: Unread
date: 2025-11-18
fetch_date: 2025-11-19T03:14:52.820446
---

# iOS Telegram Forensics. Part II Artifacts, Secret Chats, Cache, Deleted Messages

* +1 (650) 272-0384
* [Sign in](/signin)

* Solutions

  [For Business

  Boost cyber incident response, eDiscovery and forensics capacity of your organization.](/corporate)
  [For Law Enforcement

  Acquire, examine and report digital evidence in a forensically sound way.](/law-enforcement)
  [For Academia

  Learn the art of digital forensics and cyber incident response with Belkasoft's training.](/academic)
* Products

  [Belkasoft X Forensic

  For law enforcement: Acquire, examine and analyze evidence from mobile, computer, drones, cars and cloud
  sources.](/x)
  [Belkasoft X Corporate

  For corporate customers: Carry out forensic examinations, conduct investigations into cyber incidents, and provide incident response.](/corporate)
  [Belkasoft Remote Acquisition

  A part of Belkasoft X Corporate for remotely acquiring data and evidence from computers and mobile devices
  around the world.](/r)
  [Belkasoft Incident Investigations

  A part of Belkasoft X Corporate for identifying infiltration points of malicious code and originating attack
  vectors to harden your cybersecurity.](/n)
  [Belkasoft Triage

  Instantly perform effective triage analysis of Windows devices in the
  field on scene.](/t)

  [Belkasoft Live RAM Capturer

  A tiny free forensic tool that allows to reliably extract the entire
  contents of computer’s volatile memory.](/ram-capturer)
* [Training](/training)
* Resources

  [Blog](/articles#blog)
  [Articles](/articles#article)
  [Whitepapers](/whitepapers)
  [Webinars](/webinar)
  [BelkaTalk](/belkatalk)
  [Tutorials](/tutorials)
  [Newsroom](/news)
  [Product Releases](/new)
  [Testimonials](/testimonials)
  [Case Studies](/case_studies)
  [BelkaCTF](/ctf)
  [User Guide](/help)
* Company

  [About](/company)
  [News](/news)
  [Customers](/customers)
  [Partners](/partners)
  [Contact Us](/contact)
* [![Get started](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/73846a5e-e69a-4352-8c78-bd41126272e8.png)](https://hubspot-cta-redirect-eu1-prod.s3.amazonaws.com/cta/redirect/26836331/73846a5e-e69a-4352-8c78-bd41126272e8)

[#article](/articles#article)

# iOS Telegram Forensics. Part II: Artifacts, Secret Chats, Cache, Deleted Messages

![](/images/blog/ios-telegram-forensics-2-cover.jpg)

[Manual decoding of the iOS Telegram database](/ios-telegram-forensics-acquisition-and-database-analysis) is undeniably a tedious task, and with a large number of records, it can take a very long time. For this kind of application, a digital forensic tool becomes indispensable.

In this article, we will explore how [Belkasoft X](/x) can help you streamline iOS Telegram forensic analysis and look into the pitfalls to avoid when interpreting Telegram data. Here is what we will cover:

* [Analyzing iOS Telegram artifacts](#Analyzing)
* [Working with Telegram secret chats](#Working)
* [Dealing with cached data](#Dealing)
* [Recovering deleted and edited messages from the iOS Telegram database](#Recovering)

## Analyzing iOS Telegram with Belkasoft X

When you add an iOS device image as a data source to a case in Belkasoft X, you can set up the analysis options to only examine Telegram data:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-01-analyze-telegram.png)

*Figure 1: iOS Telegram profile selected for analysis in Belkasoft X*

After the tool analyzes the files in Telegram folders, it presents extracted findings in the **Artifacts** window. In the **Structure** tab, the **Chats** → **Telegram** profile displays the account owner’s name and numeric ID in the database. The middle pane reveals the user’s sent and received messages in the bubble chat view:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-02-telegram-profile.png)

*Figure 2: The Artifacts window displaying Telegram messages in the bubble chat view*

You can select a message and then inspect its details in the **Properties** pane. If you want to view the source binary data record from which the message originates, you can find it highlighted in the **Tools** pane **→ Hex viewer** tab.

### Filters

To narrow your search, you can switch to the grid view and apply various filters. For example, you can select a date range of the messages to display:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-03-filter.png)

*Figure 3: Telegram messages filtered by a date range in the grid view*

### Attachments

While analyzing a Telegram database, Belkasoft X identifies the types of data exchanged in the messages and marks the records accordingly. Messages with attachments may include pictures, audio and video files, and other types of documents. You can view their details in the **Properties** pane and access shared files in the **Tools** pane → **Attachments** tab.

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-04-attachments.png)

*Figure 4: Telegram message attachments displayed in the Artifacts window*

Note that some attachment files may not be available if they had been cleared from the application cache before you acquired the device image.

### Chats

By default, the **Artifacts** window displays messages from all user’s Telegram chats in one window. If you want to look into each available chat individually, in the **Structure** tab, right-click the **Telegram** profile and select **Show contacts**:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-05-show-contacts.png)

*Figure 5: Configuring the Telegram profile to show individual chats*

The tool then displays the conversations available in the database. Channels and group chats are marked by the corresponding tags, while one-to-one chats and bots are displayed together with associated names if they are available:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-06-conversations.png)

*Figure 6: Viewing Telegram user’s chats individually*

The chat nodes that do not include user details are typically either secret chats or chats with deleted accounts.

One notable chat to explore when analyzing Telegram data is the user’s chat with themselves (typically marked in the iOS Telegram app as “Saved Messages”). In Belkasoft X, you can spot it by the same number as the numeric ID of the Telegram profile:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-07-saved-messages.png)

*Figure 7: A Telegram user’s “Saved Messages” chat presented in Belkasoft X*

For Telegram users, this chat often serves as a storage for important messages, files, links, and more, so it may contain valuable information for the investigation.

[![REQUEST A TRIAL OF BELKASOFT X](https://hubspot-no-cache-eu1-prod.s3.amazonaws.com/cta/default/26836331/interactive-301409908937.png)](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLKjuf6EGExkSXjRDN3b00cp1yG30Vd3mSY8H6EzVfQNri2J9ZE5cSn4NqT485XkRcXySVCPYuTi2jdGV5Dghi27JNk3aMzcKem67ftYlSjrZSgBxueuUoSIt9UUACya5vk0VyuVBClrTxNmz7qwZEhLyp5szfMxbfR6Oor2Sg%3D%3D&webInteractiveContentId=301409908937&portalId=26836331)

## Working with Telegram secret chats

Telegram secret chats are only available on the devices where they were initiated. Such chats are end-to-end encrypted while in transit between devices; however, devices store them in an unencrypted form.

Telegram database keeps each secret chat under a separate ID number. In Belkasoft X, they look essentially the same as other one-to-one chats, with the only difference being that the details of the sender do not display in the tree view. When analyzing such secret chats, Belkasoft X identifies the name of the sender and displays it in the chat view:

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-08-secret-chat.png)

*Figure 8: A message in a Telegram secret chat*

## Dealing with cached Telegram data

Telegram has a "global search" function that enables users to discover other users or groups and channels within the platform.

![](/images/articles/ios-telegram-forensics-artifacts/ios-tg-09-global-...