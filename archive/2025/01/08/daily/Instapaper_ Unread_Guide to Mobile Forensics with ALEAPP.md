---
title: Guide to Mobile Forensics with ALEAPP
url: https://blog.cyber5w.com/A-Guide-to-Mobile-Forensics-with-ALEAPP.html
source: Instapaper: Unread
date: 2025-01-08
fetch_date: 2025-10-06T20:26:45.511175
---

# Guide to Mobile Forensics with ALEAPP

[![CYBER 5W](/images/logo.png)](/)

## Menu

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

Search

Search for Blog

![Guide to Mobile Forensics with ALEAPP](/images/mobile_forensics/cover.png)

4 min read
Jan 3, 2025

## Guide to Mobile Forensics with ALEAPP

[![Cyber 5W's Picture](https://avatars.githubusercontent.com/u/80437140?s=328&v=32)](/about/)

[Cyber 5W](/about/)
in

[Mobile-Forensics](/tag/Mobile-Forensics)

# A Guide to Mobile Forensics with ALEAPP

This report takes a look at an open source forensic analysis tool for Android mobile devices known as ALEAPP, and provides basic user guidance.

# Tools Used

* ALEAPP version 3.2.4 - Download here
* Public Android 14 image (Joshua Hickman) - Download here

# What is ALEAPP?

Android Logs Events And Protobuf Parser, or ALEAPP, is an open source forensic analysis tool for Android mobile devices. It was created by Alexis Brignoni, and is available on Windows, Mac, and Ubuntu as a command line tool or GUI. Additionally, Python 3.9 or above is required for use.
ALEAPP functions by using a previously generated TAR, ZIP, or GZ file of an Android mobile device to parse artifacts and form a HTML-based report. Some of the many artifact categories ALEAPP is able to obtain are:

* account and device information,
* Bluetooth and Wi-Fi connections,
* internet browser data,
* call logs,
* SMS/MMS and social media direct messages,
* saved images,
* and application installations.

# How to Generate an ALEAPP Report

Download ALEAPP by navigating to the “Releases” column on the GitHub page, which is provided in the Tools Used section above.

![Error loading](/images/mobile_forensics/Picture1.png)

Figure 1: The “Releases” column

The Windows GUI version 3.2.4 of ALEAPP will be used for this demonstration. All download types are available under the “Assets” section of the preferred software version. After downloading, extract the ZIP file.

![Error loading](/images/mobile_forensics/Picture2.png)

Figure 2: Download the ZIP file

Once extraction is complete, open the executable. If using a Windows machine, a popup may appear notifying that this is an unrecognized application. To bypass this, click “More info” and “Run anyway”. A command line and GUI of ALEAPP will open.

![Error loading](/images/mobile_forensics/Picture3.png)

Figure 3: “More info”

![Error loading](/images/mobile_forensics/Picture4.png)

Figure 4: “Run anyway”

It is necessary to have a TAR, ZIP, or GZ file of a full Android file system in order to generate a report. Click “Browse file” and navigate to the Android file system file. Click “Browse folder” below and navigate to a desired output folder.

![Error loading](/images/mobile_forensics/Picture5.png)

Figure 5: File Input and Output

The button options under the file input and output sections do the following:

* Select All - Selects all listed “Available Modules” for parsing. The available modules can be found under the “Available Modules” window as seen in figure 5.
* Deselect All - Deselects all listed “Available Modules” so they aren’t used for parsing
* Load Profile - Loads a file containing a preset of the “Available Modules”
* Save Profile - Saves current “Available Modules” settings to a file
* Case Data - Allows examiners to add case data including case number, agency name, and examiner name.
* Timezone Offset (Not Implemented) - Set artifacts to a particular timezone

All of the “Available Modules” will remain selected for this demonstration. When ready, click “Process” to begin generating the ALEAPP report. A loading screen will appear with a green bar at the bottom, indicating the process of the report.

Upon completion, the green bar will be replaced with a button to open the report. Click this to open the report, or to navigate to the report output folder and open one of the HTML documents inside.

# Forensic Analysis with ALEAPP

## Report Navigation

All the types of artifacts are located on the left side of the screen, in alphabetical order. Within each artifact section, the file system source is provided at the top of the screen.

![Error loading](/images/mobile_forensics/Picture6.png)

Figure 6: Artifact Source

Below the source, artifacts are listed in a spreadsheet format. ALEAPP automatically displays fifteen entries at a time. To change this, select the drop down menu and select “All” to see all the artifacts on one page.
A keyword search is provided to the right of this. Users can also switch between light and dark mode in the top right corner of the screen. Additionally, some columns can be filtered in alphabetical or numerical order by clicking on them.

![Error loading](/images/mobile_forensics/Picture7.png)

Figure 7: Show Entries and Keyword Search

## Device Information

There are multiple locations in an ALEAPP report that provide device information. Under the “Saved Reports” category in “Report Home”, you can click the “Device details” tab to show crucial device information. Examples include the OS version, build number, brand, manufacturer, and model.

![Error loading](/images/mobile_forensics/Picture8.png)

Figure 8: Device Information

More detailed device information is located in the “Device Info” category. For instance, the ICCID of the SIM card is available under the “SIM\_info\_0” section.

![Error loading](/images/mobile_forensics/Picture9.png)

Figure 9: SIM Card Information

## Contacts and Messaging Information

Every messaging application will have its own set of contacts and messages, making it appropriate to have separate artifact categories for each of them. Contacts saved within the phone itself, including emails and phone numbers, are shown in the “Contacts” category. A contact may have an emailand/or a phone number connected to it, along with a display name that the user chose. The type of contact can also be verified by looking at the end of the “Mimetype” string.

![Error loading](/images/mobile_forensics/Picture10.png)

Figure 10: Contact Information

Within each section for messaging applications, such as sections for apps like Discord or GroupMe, there will be several pieces of data within each artifact. These data pieces include a timestamp of when the message was sent or received, a username of the sender, and the content of the message. Each section may be formatted slightly differently, but they all provide the same general information.

![Error loading](/images/mobile_forensics/Picture11.png)

Figure 11: GroupMe Artifact Formatting

ALEAPP also offers call logs. These logs are able to show the date of a call, the involved phone numbers, the call type (outgoing, incoming, missed, or voicemail). as well as the duration and location of the call. If a voicemail is left, a transcript may also be available with it.

![Error loading](/images/mobile_forensics/Picture12.png)

Figure 12: Call Logs

## Location Tracking

Not only do Android devices themselves track location information, but installed applications may as well. Apps such as Waze and Life360 serve a purpose of determining a device’s location. These location artifacts often remain on the device, serving useful to investigators who may need to know said device’s previous locations. Recorded locations on ALEAPP are often provided in latitude and longitude coordinates.

![Error loading](/images/mobile_forensics/Picture13.png)

Figure 13: Waze Coordinates

## Photo Information

Device photos, as well as cache artifacts provide images that were stored on the device, whether intentionally or not. For instance, photos stored in the Google Photos application on a Pixel may appear in the cache of said Google Photos app, mixed in with other unrelated images. However, that example centers around a Pixel, made by Google. A device from a different manufacturer may have ...