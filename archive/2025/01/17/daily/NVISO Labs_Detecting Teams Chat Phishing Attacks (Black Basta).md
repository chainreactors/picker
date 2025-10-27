---
title: Detecting Teams Chat Phishing Attacks (Black Basta)
url: https://blog.nviso.eu/2025/01/16/detecting-teams-chat-phishing-attacks-black-basta/
source: NVISO Labs
date: 2025-01-17
fetch_date: 2025-10-06T20:09:03.665600
---

# Detecting Teams Chat Phishing Attacks (Black Basta)

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Detecting Teams Chat Phishing Attacks (Black Basta)

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[SOC](https://blog.nviso.eu/category/soc/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [phishing](https://blog.nviso.eu/category/phishing/), [Sentinel](https://blog.nviso.eu/category/cloud-security/sentinel/), [Kusto Query Language](https://blog.nviso.eu/category/kusto-kql/), [SIEM](https://blog.nviso.eu/category/siem/)

January 16, 2025January 23, 2025
4 Minutes

## Attack Description

For quite a while now, there has been a new, ongoing threat campaign where the adversaries first bomb a user’s mailbox with spam emails and then pose as Help Desk or IT Support on Microsoft Teams to trick their potential victims into providing access. This social engineering tactic is being attributed to the ransomware group “Black Basta”. [1] [2]

![attack flow](https://blog.nviso.eu/wp-content/uploads/2025/01/Untitled-Diagram.drawio-1-1024x188.png)

The attack flow is as follows:

1. The adversary sets up a new M365 tenant to appear as a legitimate organization.
2. The adversary floods the user’s inbox with spam emails that are benign in nature, such as newsletter subscriptions.
3. The adversary initiates a chat with the user via Teams (typically OneOnOne), posing as Help Desk or IT support personnel and offering assistance regarding the spam email problem.
4. The adversary convinces the victim to provide access via RMM tools either native (Quick Assist) or third-party like AnyConnect.
5. The adversary uses the remote access to further expand his foothold, disable security controls, gather sensitive files or deploy malware.

## Detection Opportunities

The attack chain above offers many hunting and detection opportunities. To name a few:

1. Detecting spikes of incoming emails per user, whether classified as spam, phishing or malware.
2. Looking for suspicious keywords like “Help Desk” or “Support” of the member’s Display Name.
3. Hunting for RMM tools usage in your environment (refer to [3] by Stef Collart).
4. Specific IOCs (emails, dropped file names and hashes, domains or IPs contacted etc.) from previously identified campaigns, although that search is never ending.

For our hunt, we are going to focus on the first half of the attack chain and create a query that will detect a combination of email bombing to a user’s mailbox, followed by a Teams chat creation with that same user as a participant, within a 3-hour window from the beginning or end of the email bombing attack.

## KQL Query

```
// Set the threshold for identifying a high number of bad emails and the time window for chat creation
let bad_email_threshold = 100;
let chat_creation_time_diff_minutes = 180;
// Filter inbound emails that have threat types or specific email actions applied
EmailEvents
| where EmailDirection == "Inbound"
| where ThreatTypes != "" or EmailActionPolicy != ""
// Summarize the count of bad emails and the time range they were received, grouped by hour and recipient email address
| summarize
    BadEmailCount = count(),
    minTimeGenerated = min(TimeGenerated),
    maxTimeGenerated = max(TimeGenerated),
    Subjects = make_set(Subject, 100),
    SenderFromAddresses = make_set(SenderFromAddress, 100)
    by bin(TimeGenerated, 1h), RecipientEmailAddress
// Filter for recipients with a count of bad emails exceeding the threshold
| where BadEmailCount > bad_email_threshold
// Normalize the recipient email address to lowercase for consistent matching
| extend RecipientEmailAddress = tolower(RecipientEmailAddress)
// Further summarize the data by 3-hour bins to identify potential email bombing incidents
| summarize
    BadEmailCount = sum(BadEmailCount),
    EmailBombingTimeGeneratedStart = min(minTimeGenerated),
    EmailBombingTimeGeneratedEnd = max(maxTimeGenerated),
    Subjects = make_set(Subjects, 100),
    SenderFromAddresses = make_set(SenderFromAddresses, 100)
    by bin(TimeGenerated, 3h), RecipientEmailAddress
// Join with OfficeActivity data to find chat creation events related to the potentially bombed email addresses
| join kind=inner (
    OfficeActivity
    | where RecordType == "MicrosoftTeams"
    | where Operation == "ChatCreated"
    | where CommunicationType == "OneOnOne"
    // Normalize the user ID to lowercase for consistent matching
    | extend UserId = tolower(UserId)
    )
    on $left.RecipientEmailAddress == $right.UserId
// Extract details about the chat participants and the time the chat was created
| extend Member0DisplayName = Members[0].DisplayName
| extend Member0UPN = Members[0].UPN
| extend Member1DisplayName = Members[1].DisplayName
| extend Member1UPN = Members[1].UPN
| extend ChatCreationTimeGenerated = TimeGenerated1
// Calculate the time difference between the chat creation and the start/end of the email bombing period
| extend ChatCreationTimeDifferenceStart = datetime_diff('minute', ChatCreationTimeGenerated, EmailBombingTimeGeneratedStart)
| extend ChatCreationTimeDifferenceEnd = datetime_diff('minute', ChatCreationTimeGenerated, EmailBombingTimeGeneratedEnd)
// Filter chats that were created within the specified time window of the email bombing period
| where (ChatCreationTimeDifferenceStart >= 0 and ChatCreationTimeDifferenceStart <= chat_creation_time_diff_minutes) or (ChatCreationTimeDifferenceEnd >= 0 and ChatCreationTimeDifferenceEnd <= chat_creation_time_diff_minutes)
// Select the relevant fields to display in the final result
| project
    Operation,
    CommunicationType,
    ChatCreationTimeGenerated,
    EmailBombingTimeGeneratedStart,
    EmailBombingTimeGeneratedEnd,
    ChatCreationTimeDifferenceStart,
    ChatCreationTimeDifferenceEnd,
    Member0DisplayName,
    Member0UPN,
    Member1DisplayName,
    Member1UPN,
    RecipientEmailAddress,
    BadEmailCount,
    Subjects,
    SenderFromAddresses,
    UserId,
    ClientIP,
    Members,
    ExtraProperties
```

Kusto

The query will return any chat creations that occurred within a 3-hour window from an email bombing attack. In the results you will also be able to see the time difference of the chat creation from the start/end of the attack (ChatCreationTimeDifference<Start|End>), the members of the chat (Member<0|1>DisplayName), how many emails were sent to the user (BadEmailCount) as well as a sample of Subjects and Senders of...