---
title: 84 Streams Later, Part 2 Inside Apple Biome
url: https://blog.digital-forensics.it/2026/07/84-streams-later-part-2-inside-apple.html
source: Instapaper: Unread
date: 2026-07-28
fetch_date: 2026-07-29T05:04:45.465574
---

# 84 Streams Later, Part 2 Inside Apple Biome

[Skip to main content](#main)

### Search This Blog

# [ZENA FORENSICS](https://blog.digital-forensics.it/)

something about digital forensics and something not

### 84 Streams Later, Part 2: Inside Apple Biome

By

[Mattia Epifani](https://www.blogger.com/profile/05734345790174061166 "author profile")

-
[July 27, 2026](https://blog.digital-forensics.it/2026/07/84-streams-later-part-2-inside-apple.html "permanent link")

Following my previous article, [84 Streams Later: Exploring the Evolution of Apple Biome](https://blog.digital-forensics.it/2026/07/84-streams-later-exploring-evolution-of.html), this article takes a deeper look at the work performed during the analysis, with the goal of enabling further research into the various Biome streams identified throughout the investigation.

As described in the previous post, on iOS 17 and later systems, Biome streams are primarily stored in two locations:

1. /private/var/db/biome/streams/restricted/
2. /private/var/mobile/Library/Biome/streams/restricted/

The analysis of these folders across multiple devices—including personal devices, test devices, and real-world forensic acquisitions—allowed the identification of 84 streams containing information that may be of forensic interest.

Based on the observed content, I categorized the streams according to the type of information they contain. To simplify the analysis, I identified five categories of information:

* Device State (e.g., Airplane Mode on/off, device plugged in, battery level, and similar information)
* Connected Devices and Networks (e.g., Wi-Fi and Bluetooth)
* Device Geolocation
* Application Usage
* Application Data

The goal of this article is therefore to provide an overview, organized by category, of the most relevant streams identified and now processed by iLEAPP.

It is important to note that some streams may provide evidence relevant to more than one category. For example, **Safari.Navigations** represents both evidence of Safari usage and evidence of application data. Similarly, **Device.Wireless.WiFi** may provide evidence of both network connectivity and device geolocation.

For this reason, the analysis is organized according to the categories above while highlighting those streams that may have multiple forensic interpretations.

An additional note regarding timestamps is also necessary.

Each record stored in a SEGB file contains a write timestamp. This timestamp may be preserved even after the content of the record has been zeroed out. As a result, even when the actual record contents are no longer available, the existence of the record itself can sometimes provide useful information. For example, it may help determine whether a device was powered on and actively used at a particular point in time.

The write timestamp does not always correspond to the timestamp of the original event. Some streams contain internal timestamps that track the beginning and end of a specific device state or activity. A complete validation and interpretation of all timestamps, together with the forensic meaning of every field stored within each record, is outside the scope of this article. Such work requires dedicated testing and validation based on user activity and device configuration.

## Device State

The streams related to Device State represent one of the largest categories identified during the analysis.

A total of 11 relevant streams were identified within the db repository and 21 within the mobile repository. Some of these streams appear to be partially redundant, representing the same information in different formats or locations.

The relevant streams within the **db** folder are:

* \_DKEvent.Device.BatteryPercentage
* \_DKEvent.Device.IsPluggedIn
* Device.BootSession
* Device.Display.Backlight
* Device.KeybagLocked
* Device.Metadata
* Device.Power.BatteryLevel
* Device.Power.EnergyMode
* Device.Power.PluggedIn
* Device.ScreenLocked
* Device.SilentMode

The relevant streams within the **mobile** folder are:

* Audio.Route
* CameraCapture.AutoFocusROI
* CarPlay.Connected
* Device.Display.InterfaceOrientation
* Device.Power.LowPowerMode
* Device.Thermals.BatteryTemperature
* Device.Wireless.AirplaneMode
* Device.Wireless.Bluetooth
* Device.Wireless.CellularDataEnabled
* Device.Wireless.WiFi
* Discoverability.Signals
* OSAnalytics.Hardware.Reliability
* \_DKEvent.Audio.InputRoute
* \_DKEvent.Audio.OutputRoute
* \_DKEvent.CarPlay.IsConnected
* \_DKEvent.Device.LowPowerMode
* \_DKEvent.Display.Orientation
* \_DKEvent.Keybag.IsLocked
* \_DKEvent.Settings.DoNotDisturb
* \_DKEvent.System.AirplaneMode
* \_DKEvent.Wifi.Connection

It is worth noting that the \_DK acronym is generally understood to refer to Duet Knowledge (or CoreDuet Knowledge) and is associated with Apple's private CoreDuet framework, the component responsible for collecting and correlating information about user activities in order to provide device intelligence features such as Siri Suggestions, Spotlight recommendations, Shortcuts, Handoff, and related functionality.

A useful reference for understanding these events is:
https://bluecrewforensics.com/2025/06/03/ios-stream-names/

The following sections provide a detailed description of each stream, the fields identified within the parsed records, and the observed retention period of active (non-zeroed) records.

### \_DKEvent.Device.BatteryPercentage

* According to the “System Events” plist file: “Event capturing battery level”
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Time Start
+ Time End
+ Time Write
+ Battery Percentage
+ Action GUID

### \_DKEvent.Device.IsPluggedIn

* According to the “System Events” plist file: “Event capturing whether or not the device has charger plugged in”
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Time Start
+ Time End
+ Time Write
+ Status

- 0 = Not Plugged In
- 1 = Plugged In

+ Action GUID

NOTE: As mentioned by Ian Whiffin in the article "[KnowledgeC Complete(ish)](https://www.doubleblak.com/blogPost.php?k=knowledgec2)": “*A more appropriate term for this artifact may be “isCharging” as a record of this type is made whenever the device is charging, and this applies equally to being physically plugged in or placed onto a Wireless Charging device*”

### Device.BootSession

* Device Boot Sessions
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Session State

- 0 = Session End
- 1 = Session Start

### Device.Display.Backlight

* According to the “System Events” plist file: “Event capturing Backlight level”
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Timestamp
+ Status (0/1)

### Device.KeybagLocked

* Apparently similar to “\_DKEvent.Keybag.IsLocked”
* According to the “System Events” plist file: “Event capturing whether or not the keybag is locked”
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Timestamp
+ Value

- 0 = Unlocked
- 1 = Locked

### Device.Metadata

* Appears to contain iOS version information
* Exact retention is unknown, but in my tests I found up to 10 months of data
* Parsed values:

+ SEGB Timestamp
+ OS Build

### Device.Power.BatteryLevel

* Apparently similar to “\_DKEvent.Device.BatteryPercentage”
* According to the “System Events” plist file: “Event capturing battery level”.
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Battery level (%)

### Device.Power.EnergyMode

* Apparently similar to “\_DKEvent.Device.LowPowerMode” and “Device.Power.LowPowerMode”
* According to the “System Events” plist file: “Event capturing Low Power Mode transitions”
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Field 1 value (experimentally we found 1 or 2)

### Device.Power.PluggedIn

* Apparently similar to “\_DKEvent.Device.IsPluggedIn”
* According to the “System Events” plist file: “Event capturing whether or not the device has charger plugged in”.
* Retention is 28 days
* Parsed values:

+ SEGB Timestamp
+ Power State:

- 0 = Not Plugged In
- 1 = Plugged In

+ Field 2

- 1 = Wireless ...