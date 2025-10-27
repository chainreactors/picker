---
title: Introducing Bettercap 2.4.0: CAN-Bus Hacking, WiFi Bruteforcing and Builtin Web UI
url: https://www.evilsocket.net/2024/09/13/Introducing-bettercap-2-4-0-CAN-bus-hacking-WiFi-bruteforcing-and-builtin-web-UI/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-14
fetch_date: 2025-10-06T18:29:34.295307
---

# Introducing Bettercap 2.4.0: CAN-Bus Hacking, WiFi Bruteforcing and Builtin Web UI

* [~/](/)
* [rss](/atom.xml)

Previous post
Next post
Back to top
Share post

1. [1. Car and ICS hacking with the new CAN module](#Car-and-ICS-hacking-with-the-new-CAN-module)
   1. [1.1. Read, write and fuzz raw frames](#Read-write-and-fuzz-raw-frames)
   2. [1.2. Load your own DBC files, decode traffic and fuzz with them](#Load-your-own-DBC-files-decode-traffic-and-fuzz-with-them)
   3. [1.3. Decode OBD2 PIDs with builtin decoder](#Decode-OBD2-PIDs-with-builtin-decoder)
2. [2. Wireless low-hanging fruits with the new WiFi bruteforcer](#Wireless-low-hanging-fruits-with-the-new-WiFi-bruteforcer)
3. [3. Builtin Web UI](#Builtin-Web-UI)
4. [4. A final note about BLE and precompiled binaries](#A-final-note-about-BLE-and-precompiled-binaries)

# Introducing Bettercap 2.4.0: CAN-Bus Hacking, WiFi Bruteforcing and Builtin Web UI

2024-09-13

[bettercap](/tags/bettercap/), [can-bus](/tags/can-bus/), [canbus](/tags/canbus/), [car hacking](/tags/car-hacking/), [ics](/tags/ics/), [webui](/tags/webui/), [wifi bruteforcing](/tags/wifi-bruteforcing/)

I’m happy to announce, after quite some time, the new bettercap 2.4.0 major release. Other than including a plethora of long due fixes (additionally to what the [recent 2.33.0 already fixed](https://github.com/bettercap/bettercap/releases/tag/v2.33.0)), it also packs a few new functionalities that extend its reach to car and industrial control system hacking. It’ll possibly take me some time to update the documentation on [the official website](https://bettercap.org/) so I’m here today to write a bit about the new features. Also remember that you can use the `help`, `help ui`, `help can` and `help wifi` commands to check all the new options and added functionalities.

## Car and ICS hacking with the new CAN module

One of the protocols that always fascinated me but that I never really approached other than attending conference talks about it is CAN-bus. There are [plenty of resources](https://www.reddit.com/r/CarHacking/comments/ltbrzk/can_bus_and_car_hacking_getting_started_resources/) to get you started with it so I’m not going too much into the details of it or the related attacks. The bottom line is that CAN-bus is a protocol used inside cars and some ICS that some components use to communicate diagnostics to the rest of the system. Everything is broadcasted, most of it is in the clear, there’re a multitude of attacks that can be performed, it’s a mess.

From a security researcher perspective however, other than the very basic ones inside the `can-tools` package, there’s not a single decent tool oriented to security. Most people end up writing their own python code that only works for that specific scenario or only showcases a specific attack.

So the new CAN module is an attempt to create a framework for this research that we can all easily access and use. Specifically, the new module can interact with any CAN-bus hardware that supports `socketcan` (if there’s also interest in CAN-bus over serial let me know and I’ll do my best to integrate it) and allows to:

### Read, write and fuzz raw frames

The very basic of CAN-bus functionalities. Set your device and enable the module to start reading raw frames:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` set can.device /dev/can0  can.recon on ``` |

You can also load and **replay** a dump previously captured with candump:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` set can.dump obd2-candump-2023-11-22_031813.log  can.recon on ``` |

Inject raw frames as `id#hex-data`:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` can.inject 0#aabbccddee ``` |

Or generate random ones for fuzzing with `can.fuzz id size`:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` can.fuzz ff 8 ``` |

And show a list of the detected ECUs:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` can.show ``` |

### Load your own DBC files, decode traffic and fuzz with them

You can also use CAN-bus database files that describe a specific protocol, in which case bettercap will use it to automatically parse every frame on the bus ([css-electronics](https://www.csselectronics.com/pages/obd2-dbc-file) and [comma.ai](https://github.com/commaai/opendbc) have some very good ones):

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` set can.device /dev/can0  can.dbc.load css-electronics/obd2-pack-v5/obd2-dbc/CSS-Electronics-11-bit-OBD2-v2.2.dbc  can.recon on ``` |

When running with a DBC, you’ll also be able to use use it for fuzzing. For instance, to generate a specific message given its id, with randomized content:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` can.fuzz 12 ``` |

To instead pick a random message from a specific ECU and generate its contents randomly:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` can.fuzz ECU_name ``` |

### Decode OBD2 PIDs with builtin decoder

Alternatively to using a DBC, if you work with OBD2 standard PIDs, you can just enable the builtin PID parser:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` set can.device /dev/can0 set can.parse.obd2 true can.recon on ``` |

For the first iteration of the CAN module this is all. I’m sure that many new features will be added in the future and many integrations with the builting scripting engine (the module can [already be scripted](https://www.bettercap.org/usage/scripting/)).

Now to the WiFi :D

## Wireless low-hanging fruits with the new WiFi bruteforcer

A while back a user created a github issue with a [very smart feature request](https://github.com/bettercap/bettercap/issues/1075): since many routers and printers have very simple wifi passwords, it is reasonable to expect that a wordlist based attack might be more successful at times than capturing and cracking the handshake.

So now we have `wifi.bruteforce`, that works wonderfully on both macOS and Linux:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` set wifi.interface en0  # one or comma separated list set wifi.bruteforce.target TargetRouter  # uncomment to attempt a password for each access point before moving to the next one # set wifi.bruteforce.wide true  # set the wordlist to use set wifi.bruteforce.wordlist /path/to/your/wordlist.txt  # stop at the first successful login set wifi.bruteforce.stop_at_first true  wifi.bruteforce on ``` |

## Builtin Web UI

Due to a series of issues with how Kali linux packaged bettercap’s webui, many users had a lot of troubles making it work correctly. Now the web ui is not something you have to download separately anymore, but it’s integrated as a module and all you have to do is:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ui on ``` |

Obviously the CAN module is already integrated with it. I hope this makes things easier :D

![ECU panel](/images/2024/ecus.png)

![PIDs](/images/2024/pids.png)

## A final note about BLE and precompiled binaries

I’m also [rewriting the BLE module](https://github.com/bettercap/bettercap/issues/1116), but this will take some more time as I’m trying to make it work in a stable way for every supported operating system, which is everything but simple :D

Precompiled binaries will soon be uploaded to the github repo, meanwhile you can use the docker image or compile from source (compilation with `make` has been fixed too).

Stay tuned and as usual [enjoy](https://github.com/bettercap/bettercap/releases/tag/v2.4.0)!

* [~/](/)
* [rss](/atom.xml)

1. [1. Car and ICS hacking with the new CAN module](#Car-and-ICS-hacking-with-the-new-CAN-module)
   1. [1.1. Read, write and fuzz raw frames](#Read-write-and-fuzz-raw-frames)
   2. [1.2. Load your own DBC files, decode traffic and fuzz with them](#Load-your-own-DBC-files-decode-traffic-and-fuzz-with-them)
   3. [1.3. Decode OBD2 PIDs with builtin decoder](#Decode-OBD2-PIDs-with-builtin-decoder)
2. [2. Wireless low-hanging fruits with the new WiFi bruteforcer](#Wireless-low-hanging-fruits-with-the-new-WiFi-bruteforcer)
3. [3. Builtin Web UI](#Builtin-Web-UI)
4. [4. A final note about BLE and precompiled binaries](#A-final-note-about-BLE-and-precompiled-binaries)

Menu
TOC
Sha...