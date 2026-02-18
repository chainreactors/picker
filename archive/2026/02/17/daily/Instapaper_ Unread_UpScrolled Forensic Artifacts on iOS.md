---
title: UpScrolled Forensic Artifacts on iOS
url: https://dig-fo4-6.blogspot.com/2026/02/upscrolled-forensic-artifacts-on-ios.html
source: Instapaper: Unread
date: 2026-02-17
fetch_date: 2026-02-18T04:16:29.605414
---

# UpScrolled Forensic Artifacts on iOS

[Skip to main content](#main)

### Search This Blog

# [HK\_Dig4nsics](https://dig-fo4-6.blogspot.com/)

### UpScrolled Forensic Artifacts on iOS

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[February 15, 2026](https://dig-fo4-6.blogspot.com/2026/02/upscrolled-forensic-artifacts-on-ios.html "permanent link")

## **Introduction**

UpScrolled is an emerging social media platform that continues to gain rapid adoption. As with any social media application, it presents potential evidentiary value in digital forensic investigations. This research documents the identification and structure of UpScrolled chat artifacts recovered from an iOS device using an iTunes-style logical backup extraction.

## **Application Data**

Application artifacts were successfully recovered via a standard iTunes backup extraction. A preliminary review of the extracted data revealed that UpScrolled application data can be found in the following path within the iOS filesystem:

*/private/var/mobile/Containers/Data/Application/{UUID}*

Within this location, user-generated content and application data were stored in the *Documents*directory:

*/private/var/mobile/Containers/Data/Application/{UUID}/**Documents*

## **Chat Database**

UpScrolled stores chat data in a SQLite database named using the format: db\_{UserID}.sqlite

This naming convention indicates chat data is segregated by user account. Such a design enables multiple accounts to coexist on the same device without data commingling, while also providing a direct mapping between database files and specific user identities.

All tables within the database were accessible using standard SQLite forensic tools and could be parsed without encryption or obfuscation.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/a/AVvXsEjClwrmk7xlePazkq4FteX1BSPVf7PtnH1B9YAUjSTVuhfItdm3Hpv2_jii8-6m6wPYUiHZXM7Ja3aGlP_An7Asy5isiP9I9fYw6GOZJOaFFPA3gEJnpJFFTa5FiLHYODXRfuHMPP152VmH-GIuTQx0AVJT0wwcHxFUAmxbxwEHtoG4yfqb26YvUnRSqvg=w241-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEjClwrmk7xlePazkq4FteX1BSPVf7PtnH1B9YAUjSTVuhfItdm3Hpv2_jii8-6m6wPYUiHZXM7Ja3aGlP_An7Asy5isiP9I9fYw6GOZJOaFFPA3gEJnpJFFTa5FiLHYODXRfuHMPP152VmH-GIuTQx0AVJT0wwcHxFUAmxbxwEHtoG4yfqb26YvUnRSqvg) |
| Figure 1. SQLite database schema overview |

## Database Structure and Forensic Significance

Several tables within the database contained artifacts of high evidentiary value, particularly those associated with user identity, message content, communication timelines, and user interaction states.

### connection\_events Table

The *connection\_events* table contains metadata associated with the authenticated user. Of particular forensic value is the *own\_user* column, which stores a BLOB object containing:

* User ID
* Account name
* Username
* Visibility status
* Number of unread messages
* Active status
* Verification status

### members Table

The *members* table identifies all participants associated with chat channels, including the local user account. The *extra\_data* column contains structured metadata describing each participant’s role within the conversation (Figure 2). This table is useful for reconstructing communication relationships and identifying involved parties.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/a/AVvXsEhcfF0zwOs4AMB1GqF_WzQOHhYwV6aJA0VYZ4aNcpLY145q9eJnQBYZzbPpbNkuVgQECVAd8bPVEEBDfEfYX8CcchFRG176G7WnRNnsYOm3bdEPM0MQvBsX7zJN502ykO0wc0PalLd9CTSsmRF3XK75o73S3H1b-U_vHop_FMxtTuL-ORtpe7aBX9Oukns=w640-h88)](https://blogger.googleusercontent.com/img/a/AVvXsEhcfF0zwOs4AMB1GqF_WzQOHhYwV6aJA0VYZ4aNcpLY145q9eJnQBYZzbPpbNkuVgQECVAd8bPVEEBDfEfYX8CcchFRG176G7WnRNnsYOm3bdEPM0MQvBsX7zJN502ykO0wc0PalLd9CTSsmRF3XK75o73S3H1b-U_vHop_FMxtTuL-ORtpe7aBX9Oukns) |
| Figure 2. Members table showing channel participants and metadata |

### messages Table

The *messages* table is the primary source of evidentiary communication content. It contains both message bodies and associated metadata required to reconstruct conversations.

Relevant columns include:

* **message\_text**
  Contains the plaintext content of chat messages.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/a/AVvXsEjEvRrRMYEmFvi_9wI_zeh8D9EohaEbB80KFUoM3hDOfTzQxYVUf2S7KSQktpTFiMXRD-U6csRFRnIlUujm4fFkWqzFOLV092WAgYLftlpTT3fUnLLCzYi4sG2gJmQflqffYQr1OTQHbuLpEOa6Ak8hcNaw7p385gv9fG29dcGI_L8yxYWsp3xikx6ZC_Q=w640-h208)](https://blogger.googleusercontent.com/img/a/AVvXsEjEvRrRMYEmFvi_9wI_zeh8D9EohaEbB80KFUoM3hDOfTzQxYVUf2S7KSQktpTFiMXRD-U6csRFRnIlUujm4fFkWqzFOLV092WAgYLftlpTT3fUnLLCzYi4sG2gJmQflqffYQr1OTQHbuLpEOa6Ak8hcNaw7p385gv9fG29dcGI_L8yxYWsp3xikx6ZC_Q) |
| Figure 3. Message content stored in message\_text column |

* **local\_created\_at**
  Records the timestamp when a message was created by the local device user.
* **remote\_created\_at**
  Records the timestamp associated with message creation across all participants. This field provides a consistent timeline of communication regardless of sender.
* **user\_id**
  Identifies the sender of the message.
* **channel\_cid**
  Represents the unique identifier of a chat channel.
* **extra\_data**
  Contains a BLOB object storing metadata related to the message and channel. This field includes important forensic indicators such as:

  + is\_invitation: Indicates the message represents the initial chat invitation
  + is\_invitation\_acceptance: Indicates acceptance of the chat invitation

  |  |
  | --- |
  | [![](https://blogger.googleusercontent.com/img/a/AVvXsEhmV7yxyD44bnLimE6r8I6FjIYLyzCq1orTfg5B8z_0Sz3ed6_QfBXYOokEHZ50OKu2nIIySSqM1inXvsqcd_M6WKDuLefuhRuqRY6XNoTs32GUJiRCZwxD7JDKseaSeFjC2HrEnd4W-r463-n3ukk463YC6iU0xJn6HG7NZC_vfrer8RkfhEveN3WPspc=w572-h80)](https://blogger.googleusercontent.com/img/a/AVvXsEhmV7yxyD44bnLimE6r8I6FjIYLyzCq1orTfg5B8z_0Sz3ed6_QfBXYOokEHZ50OKu2nIIySSqM1inXvsqcd_M6WKDuLefuhRuqRY6XNoTs32GUJiRCZwxD7JDKseaSeFjC2HrEnd4W-r463-n3ukk463YC6iU0xJn6HG7NZC_vfrer8RkfhEveN3WPspc) |
  | Figure 4. extra\_data column showing invitation indicator |

###

### reads Table

The *reads* table contains read-receipt artifacts for each participant. Specifically, it records:

* The user ID of the participant
* The last message ID viewed
* The timestamp associated with the read event

### users Table

The *users* table contains identity and account metadata for all users associated with chat channels, including the local user. One of the most significant forensic artifacts in this table is the *created\_at* column, which records the timestamp when the account was created.

## Conclusion

UpScrolled chat artifacts can be successfully recovered from iOS devices through logical extraction methods such as iTunes backups or other forensic tools with equivalent capabilities. These artifacts are stored in user-specific SQLite database files that can be examined using standard database forensic tools without requiring specialized decoding.

Analysis of these databases provides direct access to message content, participant identifiers, channel associations, and detailed timestamp information. Additionally, supporting tables contain account metadata, communication relationships, and read-receipt activity. These findings demonstrate that UpScrolled chat data can be reliably acquired and analyzed using standard mobile forensic methodologies.

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[Powered by Blogger](https://www.blogger.com)

Theme images by [Radius Images](http://www.offset.com/photos/225860)

### Archive

* [February 20261](https://dig-fo4-6.blogspot.com/2026/02/)
* [June 20231](https://dig-fo4-6.blogspot.com/2023/06/)
* [May 20231](https://dig-fo4-6.blogspot.com/2023/05/)
* [April 20231](https://dig-fo4-6.blogspot.com/2023/04/)