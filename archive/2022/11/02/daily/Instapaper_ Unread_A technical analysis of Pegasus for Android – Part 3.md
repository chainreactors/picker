---
title: A technical analysis of Pegasus for Android – Part 3
url: https://cybergeeks.tech/a-technical-analysis-of-pegasus-for-android-part-3/
source: Instapaper: Unread
date: 2022-11-02
fetch_date: 2025-10-03T21:34:36.032248
---

# A technical analysis of Pegasus for Android – Part 3

[Skip to content](#content "Skip to content")

[CYBER GEEKS](https://cybergeeks.tech/)

All Things Infosec

Main Menu

# A technical analysis of Pegasus for Android – Part 3

By  [CyberMasterV](https://cybergeeks.tech/author/cybermaster/ "View all posts by CyberMasterV")
/  October 31, 2022  / [Malware analysis](https://cybergeeks.tech/category/malwareanalysis/)

Summary

Pegasus is a spyware developed by the NSO group that was repeatedly analyzed by [Amnesty International](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/) and [CitizenLab](https://citizenlab.ca/2020/12/the-great-ipwn-journalists-hacked-with-suspected-nso-group-imessage-zero-click-exploit/). In this article, we dissect the Android version that was initially analyzed by Lookout in this [paper](https://info.lookout.com/rs/051-ESQ-475/images/lookout-pegasus-android-technical-analysis.pdf), and we recommend reading it along with this post. During our research about Pegasus for Android, we’ve found out that vendors wrongly attributed some undocumented APK files to Pegasus, as highlighted by a researcher [here](https://twitter.com/maldr0id/status/1492520053702602755). We’ve splitted the analysis into 3 parts because of the code’s complexity and length. We’ve also tried to keep the sections name proposed by Lookout whenever it was possible so that anybody could follow the two approaches more easily. In this last part, we’re presenting the WAP Push messages that could be used to autoload content on the phone without user interaction, the C2 communication over the MQTT protocol, the exploitation of a vulnerability in MediaPlayer that was not disclosed before, and the ability of the spyware to track phone’s locations. You can consult the second part of the Pegasus analysis [here](https://cybergeeks.tech/a-technical-analysis-of-pegasus-for-android-part-2/).

**Analyst**: [@GeeksCyber](https://twitter.com/GeeksCyber)

Technical analysis

SHA256: ade8bef0ac29fa363fc9afd958af0074478aef650adeb0318517b48bd996d5d5

**Pegasus initialization**

The agent extracts the Android version, a string that uniquely identifies the build, and tries to retrieve a configuration value called “isItFirstRunEver” that indicates if this is the first run of the malware:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/1.jpg)

Figure 1

The process verifies whether the “/data/data/com.network.android” directory exists on the device; otherwise, it is created. The existence of the directory means that this is not the first execution of the malware, and the “isItFirstRunEver” value is set to false using the putBoolean function:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/2.jpg)

Figure 2

It checks the existence of the malicious APK file on the phone and will use the superuser binary called “/system/csk” to run commands with root privileges:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/3-1024x748.jpg)

Figure 3

A check for an antidote file called “/sdcard/MemosForNotes” is performed, and the spyware removes itself if this file is found (see figure 4).

![](https://cybergeeks.tech/wp-content/uploads/2022/10/4.jpg)

Figure 4

The agent calls multiple functions that steal information from the [targeted applications](https://cybergeeks.tech/a-technical-analysis-of-pegasus-for-android-part-1/), as shown in the figure below.

![](https://cybergeeks.tech/wp-content/uploads/2022/10/5.jpg)

Figure 5

A value called “screen\_off\_timeout”, which represents the number of milliseconds before the device goes to sleep or begins to dream after inactivity, is extracted by the process and is compared with 15 seconds. Other configuration values such as “wasPhoneWasUnmutedAfterTapNicly” [sic], “originalVibrateValue”, and “originalRingerValue” are also extracted from configuration:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/6-1024x404.jpg)

Figure 6

**WAP Push Messages**

The process logs a message that indicates a change in the WAP settings:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/7.jpg)

Figure 7

It retrieves the file permissions of “/data/data/com.android.mms/shared\_prefs/com.android.mms\_preferences.xml” and changes them using the chmod command:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/8.jpg)

Figure 8

![](https://cybergeeks.tech/wp-content/uploads/2022/10/9-1024x193.jpg)

Figure 9

![](https://cybergeeks.tech/wp-content/uploads/2022/10/10-1024x145.jpg)

Figure 10

The LD\_LIBRARY\_PATH environment variable is modified, and the above file’s permissions are set to read & write (0666):

![](https://cybergeeks.tech/wp-content/uploads/2022/10/11.jpg)

Figure 11

The agent changes the WAP settings to enable push messages, as highlighted in the figure below.

![](https://cybergeeks.tech/wp-content/uploads/2022/10/12-1024x20.jpg)

Figure 12

The malware verifies if the Build.FINGERPRINT value contains “JPKJ2”, and it stops the Messages app:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/13.jpg)

Figure 13

The superuser binary called “/system/csk” is expected to be found on the phone (see figure 14).

![](https://cybergeeks.tech/wp-content/uploads/2022/10/14.jpg)

Figure 14

The malicious process checks for the existence of the SMS/MMS database at “/data/data/com.android.providers.telephony/databases/mmssms.db”:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/15.jpg)

Figure 15

The permissions of the “mmssms.db”, “mmssms.db-shm”, and “mmssms.db-wal” databases are changed to 0777 (read, write, & execute for owner, group and others):

![](https://cybergeeks.tech/wp-content/uploads/2022/10/16.jpg)

Figure 16

![](https://cybergeeks.tech/wp-content/uploads/2022/10/17.jpg)

Figure 17

![](https://cybergeeks.tech/wp-content/uploads/2022/10/18.jpg)

Figure 18

The agent opens one of the above databases and runs the following SQL query via a function call to rawQuery:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/19-1024x344.jpg)

Figure 19

The index of the “href”, “\_id”, “read”, “seen”, and “thread\_id” columns is extracted:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/20.jpg)

Figure 20

The spyware tries to delete some WAP push messages that could be used to automatically open a link in a browser on the phone without user interaction:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/21.jpg)

Figure 21

![](https://cybergeeks.tech/wp-content/uploads/2022/10/22.jpg)

Figure 22

The WAP messages are deleted by calling the SQLiteDatabase.delete method:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/23-1024x782.jpg)

Figure 23

![](https://cybergeeks.tech/wp-content/uploads/2022/10/24-1024x843.jpg)

Figure 24

**Message Queue Telemetry Transport (MQTT)**

Another way to communicate with the command and control infrastructure is using the MQTT protocol.

The “should\_use\_mqtt” configuration value establishes whether the agent is allowed to communicate with the C2 servers via MQTT, as shown below:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/25.jpg)

Figure 25

Another config value called “mqttAllowedConnectionType” indicates if the phone is allowed to communicate via MQTT while it’s connected to Wi-Fi (value = 1), mobile data (value = 4), or when the device is roaming (value = 8):

![](https://cybergeeks.tech/wp-content/uploads/2022/10/26.jpg)

Figure 26

The malware retrieves connection status information about all network types via a function call to getAllNetworkInfo and compares the type of the network with “WIFI” and “MOBILE”:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/27.jpg)

Figure 27

The isNetworkRoaming function is utilized to verify whether the phone is roaming:

![](https://cybergeeks.tech/wp-content/uploads/2022/10/28.jpg)

Figure 28

![](https://cybergeeks.tech/wp-content/uploads/2022/10/29.jpg)

Figure 29

The application extracts the current date and ensures that the token id found in the configuration is not null:

![](...