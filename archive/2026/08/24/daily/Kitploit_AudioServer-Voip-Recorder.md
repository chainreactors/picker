---
title: AudioServer-Voip-Recorder
url: https://kitploit.com/en/tools/github/nighthawkk/audioserver-voip-recorder
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:57.911456
---

# AudioServer-Voip-Recorder

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

AudioServer-Voip-Recorder — 🔬 An advanced Android research tool for real-time VoIP audio capture (Uplink/Downlink) by dynamically hooking libaudioflinger.so. Tested and built on WhatsApp, Signal, and Telegram on Android 14. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/nighthawkk/audioserver-voip-recorder

![](https://assets.kitploit.com/production/public/tools/51187/24e0dc3353360f19e4dcc9772a6d76b2ab5294bb98b698fd62975483dfdad5be-display-v1.webp)

[Android Security](/en/categories/android-security)[Reverse Engineering](/en/categories/reverse-engineering)[Mobile Security](/en/categories/mobile-security)

![GitHub](/providers/github.png)nighthawkk/audioserver-voip-recorder

# AudioServer-Voip-Recorder

🔬 An advanced Android research tool for real-time VoIP audio capture (Uplink/Downlink) by dynamically hooking libaudioflinger.so. Tested and built on WhatsApp, Signal, and Telegram on Android 14.

[View Repository](https://github.com/nighthawkk/audioserver-voip-recorder)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

15h 36m ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

**Goal:** Demonstrate VoIP stream capture by hooking Android's `audioserver` (specifically `libaudioflinger.so`) and recording uplink (mic) and downlink (speaker) PCM buffers when the system is in **communication** mode.

# Project Design & Methodology

## **Architecture:**

* **Controller App (Android)**
  UI with 9 buttons to manage SELINUX policy setup, payload injection, data movement, and playback.
* **Payload (`libaudiohook.so`)**
  C++ shared library (built as part of the app project) that hooks internal `AudioFlinger` methods using **Dobby** and writes raw PCM buffers to a session directory.
* **Post-Processing**
  Additional tool, `tools/audioparser.py` converts raw `.ac(Downlink)`/`.bc(Uplink)` files to WAV. The app’s file manager can also convert & play in-app.
* **Research Utilities**
  Frida scripts for initial function tracing & offset discovery; analysis files for symbol/offset and other snippets.

### **Controller App**

This Android application provides a graphical interface for managing VoIP recording through the `audioserver`. It integrates with a native payload that hooks into the Android audio stack to capture microphone and speaker audio from VoIP applications.

The app serves as a control center, allowing you to inject required SELinux policies, start/stop monitoring, manage recorded data, and play captured VoIP audio files.

#### Features

The main activity contains **9 control buttons**:

1. **Inject Policies**
   Injects the required SELinux policies for `audioserver` and this app to work together.
2. **Start Monitoring**
   Injects the shared library payload into `audioserver`, enabling VoIP audio capture by hooking `RecordTrack` and `PlaybackTrack`. Uses **[AndKittyInjector](https://github.com/MJx0/AndKittyInjector)** for Process Injection.
3. **Stop Monitoring**
   Restarts the `audioserver` process, stopping monitoring and removing injected hooks.
4. **Copy Data**
   Copies captured **raw PCM audio** from temp directory `/data/local/tmp/voip` to `/sdcard/voip`.

   * Cleans up the temporary directory afterward.
5. **View Logs**
   Displays logs related to injection, hooking, and recording status.
6. **Enable SELinux**
   Restores SELinux enforcing mode.
7. **Disable SELinux**
   Sets SELinux to permissive mode, Use when injected policies fail.
8. **Play Audios**
   Opens the custom **VoIP File Manager** (/sdcard/voip/):

   * Converts raw PCM files into **WAV format** in-memory.

root@kitploit:~

```
+----------------------+
|                      |
|   App MainActivity   |
|                      |
|                      |
|(9 Control Buttons UI)|
|                      |
|                      |
+----------+-----------+
           |
           |
           |
+----------v-----------+
|                      |
|       JNI Layer      |
|                      |
| Selinux, Process Inje|
| ction,               |
|                      |
|                      |
+----------------------+
```

### **Hooking Payload**

This shared library is injected into **`audioserver`** to detect `AUDIO_MODE_IN_COMMUNICATION` and capture VoIP audio streams directly from Android’s audio stack for predefined set of package names.

It uses the **[Dobby](https://github.com/jmpews/Dobby)** inline hooking framework to intercept critical methods inside `libaudioflinger.so`.
Both **uplink (microphone)** and **downlink (speaker)** audio streams are captured and written to session files for later processing.

#### **Hooking Points**

The library installs hooks on the following functions inside `AudioFlinger` and related classes:

#### **Target Applications**

The library filters streams based on **UID → Package mapping**.

Currently monitored apps:

* `com.whatsapp`
* `com.whatsapp.w4b` (WhatsApp Business)
* `org.thoughtcrime.securesms` (Signal)
* `org.telegram.messenger`
* `org.telegram.messenger.web`

You can add other applications also iniside `audioserver_hook.cpp`:

root@kitploit:~

```
static const char* kTargetPackages[] = {
    "com.whatsapp",
    "com.whatsapp.w4b",
    "org.thoughtcrime.securesms",
    "org.telegram.messenger",
    "org.telegram.messenger.web"
};
```

#### File Output

* A **session directory** is created at injection into `audioserver` under:
  `/data/local/tmp/voip/audioserver_session_<timestamp>/`
* Files are first created with a **`.tmp` extension**, then renamed on track stop:

  + **Uplink (mic)** → `<packageName>_<sampleRate>_<timestamp>.bc`
  + **Downlink (speaker)** → `<packageName>_<sampleRate>_<timestamp>.ac`
* Example session:

root@kitploit:~

```
	/data/local/tmp/voip/audioserver_session_1725389200/
	├── com.whatsapp_48000_1725389201_123456.ac
	├── com.whatsapp_48000_1725389201_123789.bc

```

#### Offsets

Since target library is stripped and methods are not exported in `libaudioflinger.so`, we need exact offsets of methods and other related components for successful hooking.

We can extract those offsets from static analysis using IDA-PRO or from dynamic analysis using frida.
Once offsets are known we can replace them inside `offsets.h` header file.

##### Required Offsets:

###### Methods:

1. AUDIOFLINGER\_SETMODE\_OFFSET
   * Method: `android::AudioFlinger::setMode(audio_mode_t)`
   * Mangled name: `_ZN7android12AudioFlinger7setModeE11audio_mode_t`
2. RECORDTRACK\_GETNEXTBUFFER\_OFFSET
   * Method: `android::AudioFlinger::RecordThread::RecordTrack::getNextBuffer(android::AudioBufferProvider::Buffer *)`
   * Mangled name: `_ZN7android12AudioFlinger12RecordThread11RecordTrack13getNextBufferEPNS_19AudioBufferProvider6BufferE`
3. TRACK\_GETNEXTBUFFER\_OFFSET
   * Method: `android::AudioFlinger::PlaybackThread::Track::getNextBuffer(android::AudioBufferProvider::Buffer *)`
   * Mangled name: `_ZN7android12AudioFlinger14PlaybackThread5Track13getNextBufferEPNS_19AudioBufferProvider6BufferE`
4. TRACK\_STOP\_OFFSET
   * Method: `android::AudioFlinger::PlaybackThread::Track::stop(void)`
   * Mangled name: `_ZN7android12AudioFl...