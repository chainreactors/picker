---
title: macOS Extended Attributes: Case Study
url: https://dfir.ch/posts/macos_extended_attributes/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-17
fetch_date: 2025-10-06T20:35:21.905081
---

# macOS Extended Attributes: Case Study

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# macOS Extended Attributes: Case Study

15 Feb 2025

**Table of Contents**

* [Introduction](#introduction)
* [Inspecting Extended Attributes](#inspecting-extended-attributes)
* [Case Study](#case-study)
* [Removing the Quarantine Flag](#removing-the-quarantine-flag)
* [Conclusion](#conclusion)

## Introduction

`Extended attributes` (EAs) are a powerful and sometimes overlooked feature of macOS’s file system, storing additional metadata about files beyond what standard attributes like file name, size, and permissions allow. While these attributes are invisible in typical file interactions, they play a critical role in various macOS features and workflows.

## Inspecting Extended Attributes

macOS provides several tools for working with extended attributes. These include:

* The `ls` command (the `@` at the end of the permissions indicates extended attributes):
  `-rw-r--r--@ 1 malmoeb staff 202767345 Jan 6 13:29 Webex.dmg`
* The `xattr` command is the primary utility for managing extended attributes. It can list, read, write, and delete attributes.

  + **List Attributes**: `xattr filename`
  + **Read an Attribute**: `xattr -p attribute_name filename`
  + **Add or Modify an Attribute**: `xattr -w attribute_name "value" filename`
  + **Delete an Attribute**: `xattr -d attribute_name filename`

## Case Study

We download the fileÂ `Webex.dmg`Â from the official Webex website for testing purposes. Using `ls`, we can view its extended attributes, indicated by the `@` symbol at the end of the permissions

```
ls -l Webex.dmg
-rw-r--r--@ 1 malmoeb  staff  202767345 Jan  6 13:29 Webex.dmg
```

We see the list of extended attributes with the command `xattr`:

```
% xattr Webex.dmg
com.apple.metadata:kMDItemWhereFroms
com.apple.quarantine
```

The respective attributes can now be displayed with the parameter `-p attribute_name` to the `xattr` command, as in the following example, where we display the attribute `com.apple.metadata:kMDItemWhereFroms` (which describes where the file was obtained from):

```
% xattr -p com.apple.metadata:kMDItemWhereFroms Webex.dmg
bplist00?_>https://binaries.webex.com/webex-macos-apple-silicon/Webex.dmg_https://www.webex.com/
```

macOSâs quarantine feature sets a quarantine bit for files a user downloads to present a warning before running or opening the file.

```
% xattr -p com.apple.quarantine Webex.dmg | plutil -p -
{
  "0181" => "0181"
  "67794cd5" => "67794cd5"
  "Chrome" => "Chrome"
}
```

[Here](https://stackoverflow.com/questions/46198557/understanding-output-of-xattr-p-com-apple-quarantine) is a partial answer regarding the additional attributes in the output, but they are not particularly relevant to our case. Using the `mdfind` command with the search term `'kMDItemWhereFroms == "*"'`, we can identify additional downloaded files (excerpt from my computer):

```
% mdfind 'kMDItemWhereFroms == "*"'
/Users/malmoeb/Downloads/65cfa8debb157a91e0110fb7579f466e405d5b8aa9d53ff9339632bf4494b1cc.zip
/Users/malmoeb/Downloads/ToDesktop Builder Mac Installer (241204gvw4ijkij).zip
/Users/malmoeb/Downloads/Webex.dmg
```

The metadata of these files is stored in a special database that an Incident Responder can query to find a possible infection source. Use the following query on the command line to see all details:

```
sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'select LSQuarantineDataURLString from LSQuarantineEvent'
```

In addition to the URLs, an analyst can read out other metadata for a forensic investigation:

```
% sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV*
sqlite> .schema LSQuarantineEvent
...
LSQuarantineTimeStamp
LSQuarantineAgentBundleIdentifier
LSQuarantineAgentName
[..]
```

Or use the Velociraptor Hunt [MacOS.System.QuarantineEvents](https://docs.velociraptor.app/artifact_references/pages/macos.system.quarantineevents/) created by Wes Lambert ([@therealwlambert](https://x.com/therealwlambert)), where the parsing of the database fields is already done.

```
11LET QEventsDetails =
12    SELECT * FROM foreach(
13        row=QEvents,
14        query={ SELECT
15            timestamp(epoch=LSQuarantineTimeStamp + 978307200) AS DownloadTime,
16            LSQuarantineDataURLString AS DownloadURL,
17            LSQuarantineOriginURLString AS Origin,
18            LSQuarantineAgentName AS AgentName,
19            LSQuarantineAgentBundleIdentifier AS AgentBundle,
20            split(string=OSPath, sep='/')[2] AS User,
21            LSQuarantineEventIdentifier AS EventUUID
22           FROM scope()
23        }
24    )
```

## Removing the Quarantine Flag

As discussed, the quarantine flag is used to block programs downloaded from the Internet. In Figure 1, we see that `Aurora`, a tool to document Incident Response cases (created by my team colleague [Mathias Fuchs](https://www.linkedin.com/in/mathias-fuchs-99943465/)), was blocked on my computer (download Aurora [here](https://github.com/cyb3rfox/Aurora-Incident-Response)).

![TODO](/images/extended_attributes/Aurora_blocked.png "TODO")

Figure 1 : "Aurora" Not Opened

One option is to allow Aurora to run through the security settings (Figure 2).

![TODO](/images/extended_attributes/Open_Anyway.png "TODO")

Figure 2: Open Anyway

However, we can also achieve the same behavior if we delete the quarantine attribute:

```
% xattr Aurora.app
com.apple.provenance
com.apple.quarantine
% xattr -d com.apple.quarantine Aurora.app
% xattr Aurora.app
com.apple.provenance
```

After deleting the quarantine attribute, Aurora starts as expected.

## Conclusion

Extended attributes in macOS offer valuable metadata storage that enhances the functionality and security of the operating system. By examining a downloaded file like `Webex.dmg`, we observed how tools like `xattr` and `ls` help reveal important information, such as the file’s origin and quarantine status.

These attributes are not only essential for ensuring file integrity and security but can also play a key role in forensic investigations by providing insights into a fileâs history.

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).