---
title: Android Intrusion Logs
url: https://www.iverify.com/blog/android-intrusion-logging-forensics-analysis
source: Instapaper: Unread
date: 2026-08-27
fetch_date: 2026-08-28T13:38:06.848190
---

# Android Intrusion Logs

[Blog](../blog)

# Android Intrusion Logs - A First Look

![Headshot of David Gillies, Head of Android Research at iVerify](https://framerusercontent.com/images/2f7o7irWNiOs6prvOZ9pF7LdM.jpg?width=192&height=192)

David

Gillies

![Headshot of Lorena Carthy-Wilmot, Head of Security Strategy (Europe) at iVerify](https://framerusercontent.com/images/hl6gAaNgxv1HJgX73zu3dqWNar4.jpg?width=192&height=192)

Lorena

Carthy-Wilmot

Â·

Published Aug 4, 2026

![Cover: the Android robot with a 16 badge beside a phone showing an Intrusion Logging screen of DNS and security events](https://framerusercontent.com/images/2Kc54ve9CY8fBRR8Nh1y38o1UZ4.png?width=1024&height=576)

For years, investigating a compromised Android device has meant relying on whatever evidence happened to survive on it. The logs were built for debugging, not detection, retention was measured in hours rather than months, and spyware knew exactly how to clean up after itself.

Intrusion Logging (IL) is built to change that. Arriving in [Android 16](https://developer.android.com/about/versions/16) as part of Androidâs Advanced Protection Mode, and developed in partnership with [Amnesty International's Security Lab](https://securitylab.amnesty.org/), it is the first feature on a major mobile platform designed from the ground up for forensic investigation. We wanted to see how much of a difference it makes, so we tested it on live Pixel hardware. What we found is a real step forward, with some important caveats worth understanding before you rely on it.

## **Why it Matters**

To appreciate what IL does, it helps to know what investigators have had until now. Android's existing logs, logcat, tombstones, and bug reports, were all built for engineers rather than analysts. They overwrite themselves within minutes to hours, carry little security context, and capture at most a day or two of activity. Sophisticated spyware such as [Pegasus](./key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update), Graphite, and [Predator](./encryption-vs-predator-how-common-security-tools-defeat-commercial-spyware) has long exploited exactly these limitations, using aggressive anti-forensic techniques against a platform that was never built to remember.

IL inverts that model. Instead of mining diagnostic logs that happen to contain useful traces, it produces a dedicated, encrypted, user-owned security record, backed up to the owner's Google Account and retained for 12 months. It survives even if the device is wiped or seized, and crucially, even Google cannot access it.

## **What's Actually Inside an IL Bundle**

When we pulled and decrypted IL bundles from a Pixel 10 Pro, individual collections ran from around 93,000 to nearly 600,000 events, the largest spanning more than three weeks of activity, across three event types.

**DNS events** are where a lot of the investigative value lives. Every hostname lookup is recorded alongside the specific app that requested it, so a suspicious domain is no longer an isolated network indicator but one tied directly to the package responsible. That kind of per-app DNS attribution did not exist in Android's standard logging.

```
{
  "dns_event": {
    "event_time": 1783505607772,
    "package_name": "com.whatsapp",
    "hostname": "g.whatsapp.net",
    "ip_addresses": ["/57.144.239.33"],
    "ip_addresses_count": 1
  }
}
```

```
{
  "dns_event": {
    "event_time": 1783505607772,
    "package_name": "com.whatsapp",
    "hostname": "g.whatsapp.net",
    "ip_addresses": ["/57.144.239.33"],
    "ip_addresses_count": 1
  }
}
```

```
{
  "dns_event": {
    "event_time": 1783505607772,
    "package_name": "com.whatsapp",
    "hostname": "g.whatsapp.net",
    "ip_addresses": ["/57.144.239.33"],
    "ip_addresses_count": 1
  }
}
```

**Connection events** capture destination IPs and ports with the same per-app attribution, giving analysts a map of what each application was actually talking to. In our example above and below, both streams carry the app name, so they line up.

```
{
  "connect_event": {
    "event_time": 1783505792694,
    "package_name": "com.whatsapp",
    "port": 5222,
    "ip_address": "/57.144.239.33"
  }
}
```

```
{
  "connect_event": {
    "event_time": 1783505792694,
    "package_name": "com.whatsapp",
    "port": 5222,
    "ip_address": "/57.144.239.33"
  }
}
```

```
{
  "connect_event": {
    "event_time": 1783505792694,
    "package_name": "com.whatsapp",
    "port": 5222,
    "ip_address": "/57.144.239.33"
  }
}
```

**Security events** are the richest layer. Across our captures we observed 25 distinct subtypes, covering process launches (with the SHA-256 hash of the executed binary), ADB activity, device unlocks, boot state, certificate installations, password changes, and Advanced Protection policy updates. The app\_process\_start subtype is the standout: it moves an investigator from asking what was installed to knowing what actually ran, when, and with what system privileges.

Below is what is captured when the WhatsApp process is launched

```
{
  "security_event": {
    "event_time": 1782839560465952259,
    "app_process_start": {
      "process": "com.whatsapp",
      "start_time": 1782839560465,
      "uid": 10381,
      "pid": 31469,
      "seinfo": "default:targetSdkVersion=36:complete",
      "sha256": "e76e163b709acc08eed2d4a6d7b3382254..."
    }
  }
}
```

```
{
  "security_event": {
    "event_time": 1782839560465952259,
    "app_process_start": {
      "process": "com.whatsapp",
      "start_time": 1782839560465,
      "uid": 10381,
      "pid": 31469,
      "seinfo": "default:targetSdkVersion=36:complete",
      "sha256": "e76e163b709acc08eed2d4a6d7b3382254..."
    }
  }
}
```

```
{
  "security_event": {
    "event_time": 1782839560465952259,
    "app_process_start": {
      "process": "com.whatsapp",
      "start_time": 1782839560465,
      "uid": 10381,
      "pid": 31469,
      "seinfo": "default:targetSdkVersion=36:complete",
      "sha256": "e76e163b709acc08eed2d4a6d7b3382254..."
    }
  }
}
```

Failed Device unlocks are also captured

```
{
  "security_event": {
    "event_time": 1783511985960441369,
    "keyguard_dismiss_auth_attempt": {
      "success": false,
      "method_strength": 0
    }
  }
}
```

```
{
  "security_event": {
    "event_time": 1783511985960441369,
    "keyguard_dismiss_auth_attempt": {
      "success": false,
      "method_strength": 0
    }
  }
}
```

```
{
  "security_event": {
    "event_time": 1783511985960441369,
    "keyguard_dismiss_auth_attempt": {
      "success": false,
      "method_strength": 0
    }
  }
}
```

A specific capture from our lab evaluation illustrates this investigative utility firsthand.

During a brief three-minute window, an investigator utilized ADB for app discovery and deletion, with IL preserving the entire sequence. The record included package listings, diagnostic queries, the final uninstallation, and even a complex multi-line awk script used to calculate storage impact. Every one of the nineteen distinct commands was logged in its entirety, as demonstrated by this uninstallation event:

```
{
  "security_event": {
    "event_time": 1781913414352002246,
    "adb_shell_cmd": {
      "command": "pm list packages"
    }
  }
}
{
  "security_event": {
    "event_time": 1781913426947317229,
    "adb_shell_cmd": {
      "command": "pm uninstall -k --user 0 com.android.virtualization.terminal"
    }
  }
}
{
  "security_event": {
    "event_time": 1781913523892996678,
    "adb_shell_cmd": {
      "command": "dumpsys diskstats | awk '\n/^Package Names:/ { â¦"    }
  }
}
```

```
{
  "security_event": {
    "event_time": 1781913414352002246,
    "adb_shell_cmd": {
      "command": "pm list packages"
    }
  }
}
{
  "security_event": {
    "event_time": 1781913426947317229,
    "adb_shell_cmd": {
      "command": "pm uninstall -k --user 0 com.android.virtualization.terminal"
    }
  }
}
{
  "security_event": {
    "event_time": 1781913523892996678,
    "adb_shell_cmd"...