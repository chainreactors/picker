---
title: ClickFix: Stopped at ⌘+V
url: https://objective-see.org/blog/blog_0x86.html
source: Objective-See's Blog
date: 2026-03-27
fetch_date: 2026-03-28T04:18:03.191041
---

# ClickFix: Stopped at ⌘+V

* [![](/images/logoApple.png)

  Objective-See

  a non-profit 501(c)(3) foundation.](/index.html)
* [ ]

  + [![](/images/aboutIcon.png)
    About](/about.html)
  + [![](/images/conferenceIcon.png)
    #OBTS](https://objectivebythesea.org/)
  + [![](/images/bookIcon.png)
    Book Series](https://taomm.org/)
  + [![](/images/weIcon.png)
    Objective-We](/we.html)
  + [![](/images/storeIcon.png)
    Our Store/Swag](https://objective-see.myshopify.com/)
  + [![](/images/malwareIcon.png)
    Malware Collection](https://github.com/Objective-see/Malware)
* Support Us!
* [![](/images/blogIcon.png)](/blog.html)
* [![](/images/productsIcon.png)

  tools](/tools.html)

---

Building a Firewall ...via Endpoint Security!?

Reverse Engineering macOS 26.4's Undocumented Network Events

by: Patrick Wardle / March 26, 2026

The **Objective-See Foundation** is supported by:

[![](https://objective-see.org/images/friends/iru.png)](https://www.iru.com)

[![](https://objective-see.org/images/friends/panw.png)](https://www.paloaltonetworks.com)

[![](https://objective-see.org/images/friends/jamf.png)](https://www.jamf.com/?utm_source=objective-see&utm_medium=sponsored-link&utm_campaign=next-gen-security&utm_content=2021-02-05_protect)

[![](https://objective-see.org/images/friends/MoonlockLogoMacPaw.png)](https://moonlock.com)

[![](https://objective-see.org/images/friends/sophos.png)](https://www.sophos.com/)

[![](https://objective-see.org/images/friends/malwarebytes.png)](https://www.malwarebytes.com/)

[![](https://objective-see.org/images/friends/iVerify.png)](https://www.iverify.io)

[![](https://objective-see.org/images/friends/huntress.png)](https://hubs.ly/Q02BYLy80)

Special thanks to Luke from [Phorion](https://phorion.io) for his input/ideas!

### Endpoint Security Events

Each release of macOS brings a host of security fixes, but also the occasional new Endpoint Security events. Such events can extend and improve security tools that already leverage Endpoint Security.

Endpoint Security events can be found in `ESTypes.h` in a large `es_event_type_t` enum. Here are some recent events (with helpful comments from Apple when they were introduced):

```
% cat MacOSX26.4.sdk/usr/include/EndpointSecurity/ESTypes.h

// The following events are available beginning in macOS 13.0
    ES_EVENT_TYPE_NOTIFY_XP_MALWARE_DETECTED,
    ES_EVENT_TYPE_NOTIFY_XP_MALWARE_REMEDIATED,
    ES_EVENT_TYPE_NOTIFY_BTM_LAUNCH_ITEM_ADD,
    ES_EVENT_TYPE_NOTIFY_BTM_LAUNCH_ITEM_REMOVE,
    ...

// The following events are available beginning in macOS 15.0
    ES_EVENT_TYPE_NOTIFY_GATEKEEPER_USER_OVERRIDE,

// The following events are available beginning in macOS 15.4
    ES_EVENT_TYPE_NOTIFY_TCC_MODIFY,
```

While new events are often very useful to security tool writers, they may not be well documented, or may not even work as expected. So, when new ones emerge, I like to dig into them and see if they can be used to enhance Objective-See’s free open-source tools.

Previous posts on (new) Endpoint Security events include:

* [TCCing is Believing: Apple finally adds TCC events to Endpoint Security!](https://objective-see.org/blog/blog_0x7F.html)
* [Writing a Process Monitor with Apple’s Endpoint Security Framework](https://objective-see.org/blog/blog_0x47.html)

With the release of macOS 26.4 (and `MacOSX26.4.sdk`), several new events were added, but for the first time ever, they were not documented — just added as “`ES_EVENT_TYPE_RESERVED_*`”:

```
% cat MacOSX26.4.sdk/usr/include/EndpointSecurity/ESTypes.h
...

    // The following events are available beginning in macOS 26.3

    ES_EVENT_TYPE_RESERVED_0,
    ES_EVENT_TYPE_RESERVED_1,
    ES_EVENT_TYPE_RESERVED_2,

    // The following events are available beginning in macOS 26.4.0

    ES_EVENT_TYPE_RESERVED_3,
    ES_EVENT_TYPE_RESERVED_4,
    ES_EVENT_TYPE_RESERVED_5,
    ES_EVENT_TYPE_RESERVED_6,
```

> Did [@Apple](https://twitter.com/Apple?ref_src=twsrc%5Etfw) forget to update the public Endpoint Security header files in macOS 26.4?
>
> New ES events still marked: "ES\_EVENT\_TYPE\_RESERVED\_\*" 😢😤 [pic.twitter.com/gCEpd2yAZU](https://t.co/gCEpd2yAZU)
>
> — Patrick Wardle (@patrickwardle) [March 25, 2026](https://twitter.com/patrickwardle/status/2036896396893442513?ref_src=twsrc%5Etfw)

As I noted in my tweet, I’m not sure if Apple just left them out by accident …or? 🤷‍♂️

### ⚙️ Subscribing to Reserved Events

Well, I don’t like unsolved Apple mysteries, so let’s dig in and see what we can figure out. Here, we’ll focus on `ES_EVENT_TYPE_RESERVED_5` and `ES_EVENT_TYPE_RESERVED_6`.

Our goal is simple: understand what these events are, and whether we can use them in our tools.

Though we might have been able to uncover the meaning of these events via static analysis, I took what proved to be a simpler approach:

1. Subscribe (via `es_subscribe`) to the new ES events and wait for them to be delivered
2. Print out the raw bytes of the event’s message contents
3. (non)Profit!

I’ll assume you’re familiar with ES basics, and just dive into the code:

```
 1es_event_type_t reservedEvents[] = {
 2        ES_EVENT_TYPE_RESERVED_0,
 3        ES_EVENT_TYPE_RESERVED_1,
 4        ES_EVENT_TYPE_RESERVED_2,
 5        ES_EVENT_TYPE_RESERVED_3,
 6        ES_EVENT_TYPE_RESERVED_4,
 7        ES_EVENT_TYPE_RESERVED_5,
 8        ES_EVENT_TYPE_RESERVED_6,
 9};
10
11es_new_client(&client, ^(es_client_t *client, const es_message_t *message) {
12
13    printf("[*] event type: %d\n", message->event_type);
14    printf("    action_type: %s\n", message->action_type == ES_ACTION_TYPE_AUTH ? "AUTH" : "NOTIFY");
15
16}
17
18uint32_t reservedCount = sizeof(reservedEvents) / sizeof(reservedEvents[0]);
19for(uint32_t i = 0; i < reservedCount; i++) {
20
21        es_event_type_t single[] = { reservedEvents[i] };
22        es_return_t result = es_subscribe(client, single, 1);
23        printf("RESERVED_%u (type=%d): %s (result=%d)\n", i, reservedEvents[i],
24               result == ES_RETURN_SUCCESS ? "subscribed" : "failed", result);
25}
```

After declaring the events of interest (all the new `ES_EVENT_TYPE_RESERVED_*` ones) we create an ES client via `es_new_client`. In its callback, we just print out the event type and action type. (Shortly we’ll flesh out this callback more).

Next, in a loop we subscribe to each event, effectively telling the ES subsystem to invoke the callback (passed to `es_new_client`) anytime any of the (yet to be understood) events occur anywhere on the system.

Compiling this code into a binary that is appropriately entitled with `com.apple.developer.endpoint-security.client`, let’s give it a run!

```
# ./newESEvents

RESERVED_0 (type=148): failed (result=1)
RESERVED_1 (type=149): failed (result=1)
RESERVED_2 (type=150): failed (result=1)
RESERVED_3 (type=151): subscribed (result=0)
RESERVED_4 (type=152): subscribed (result=0)
RESERVED_5 (type=153): subscribed (result=0)
RESERVED_6 (type=154): subscribed (result=0)
...
```

Interestingly, for reasons unknown, `ES_EVENT_TYPE_RESERVED_0` - `_2` fail. Maybe they are not yet implemented? However, the remaining ones succeed!

### 🐛 A (Now Patched) Kernel Panic

Previously I (vaguely) tweeted about a kernel panic in Apple’s EndpointSecurity kernel extension:

> Apple: “3rd-party security tools can’t run in the kernel because they might panic.”
>
> Also Apple: kicks us out and replaces us with their EndpointSecurity kext ...which can be trivially panicked from userland, taking down every security tool + the whole system (macOS 26.3.1)! 🙄 [pic.twitter.com/J1qQ0SrQ4K](https://t.co/J1qQ0SrQ4K)
>
> — Patrick Wardle (@patrickwardle) [March 6, 2026](https://twitter.com/patrickwardle/status/2029770828062323033?ref_src=twsrc%5Etfw)

As it is now patched (in macOS 26.4), we can discuss it — though as we’ll see, it’s not really a security issue per se, but a rather trivial bug.

A while back I wondered what would happen if you tried to subscribe via `es_subscribe` to events “past” (above) the final...