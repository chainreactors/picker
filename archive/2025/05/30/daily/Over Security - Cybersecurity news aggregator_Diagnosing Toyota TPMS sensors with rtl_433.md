---
title: Diagnosing Toyota TPMS sensors with rtl_433
url: https://r-c-y.net/posts/tpms/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-30
fetch_date: 2025-10-06T22:27:20.686337
---

# Diagnosing Toyota TPMS sensors with rtl_433

[ ]
[ ]

## [RCY](/)

* [About](https://www.r-c-y.net/about/)
* [Projects](https://www.r-c-y.net/projects/)
  + [sendafd](https://www.r-c-y.net/projects/sendafd/)
  + [TNC Exporter](https://www.r-c-y.net/projects/tncexporter/)
  + [hole calc](https://www.r-c-y.net/projects/holecalc/)
  + [airspotbot](https://www.r-c-y.net/projects/airspotbot/)
  + [Tables for INCA](https://www.r-c-y.net/projects/tfi/)
  + [Chromakey Suite](https://www.r-c-y.net/projects/ck/)
  + [Tea Building](https://www.r-c-y.net/projects/tb/)
  + [Small Cabinet](https://www.r-c-y.net/projects/smallcab/)
* [Posts](https://www.r-c-y.net/posts/)
  + [Understanding Bring a Trailer: Weekends](https://www.r-c-y.net/posts/bat3/)
  + [Understanding Bring a Trailer: Hammer prices](https://www.r-c-y.net/posts/bat2/)
  + [A bash script for TPMS testing](https://www.r-c-y.net/posts/tpmsbash/)
  + [Diagnosing Toyota TPMS sensors with rtl\_433](https://www.r-c-y.net/posts/tpms/)
  + [Understanding Bring a Trailer: Sell-through rate](https://www.r-c-y.net/posts/bat1/)
  + [Resources for learning machining](https://www.r-c-y.net/posts/machining/)

* [Github ↗](https://github.com/rouyng)
* [GTCP ↗](https://gtcp.com)
* [SAND ↗](https://sand.zone)

![Menu](/svg/menu.svg)
**Diagnosing Toyota TPMS sensors with rtl\_433**

![Table of Contents](/svg/toc.svg)

* [Introduction](#introduction)
* [Required tools](#required-tools)
* [Process](#process)
  + [Install rtl\_433](#install-rtl_433)
  + [Set up SDR hardware](#set-up-sdr-hardware)
  + [Receiving TPMS sensor messages](#receiving-tpms-sensor-messages)
  + [Interpreting sensor messages](#interpreting-sensor-messages)
  + [Locating individual sensors](#locating-individual-sensors)
* [Results](#results)
* [Automation](#automation)
* [References](#references)

# [Diagnosing Toyota TPMS sensors with rtl\_433](/posts/tpms/)

##### February 13, 2022

[cars](/tags/cars/),
[radio](/tags/radio/),
[guide](/tags/guide/)

![TPMS Warning Light](/img/tpms.png)

## Introduction [#](#introduction)

My 2008 Toyota Tacoma is equipped with a [direct tire pressure monitoring system](https://en.wikipedia.org/wiki/Direct_TPMS) (TPMS). This system consists of four wireless sensors (one at each wheel) and an onboard control unit which receives and monitors data from the sensors. The TPMS in this truck is not very advanced. The only information the system provides to the driver is a warning light. It has no way to indicate which tire has low pressure. Currently, one of the TPMS sensors is broken. I know because even when my tire pressures are correct, the TPMS warning light on my dashboard flashes while starting up then stays constantly illuminated. I’d prefer to only replace the broken sensor, and I don’t have a tool to diagnose TPMS sensors. So how do you determine which has failed without buying an expensive TPMS diagnostic tool? I have a RTL-SDR dongle hanging around, so I decided to use [rtl\_433](https://github.com/merbanan/rtl_433) to capture and decode signals from the TPMS sensors in order to determine which has failed. This article will describe the process, present some things I learned, and provide a rough guide for someone wanting to do the same thing.

## Required tools [#](#required-tools)

* Some kind of [SDR hardware compatible with rtl\_433](https://triq.org/rtl_433/HARDWARE.html). We will only be receiving, so we don’t need an expensive, TX-capable SDR. I used the cheap, RTL2832U-based [RTL-SDR dongle](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/). This came with a telescopic dipole antenna, which works fine for this project. As of this writing, the cost is about $40USD for the RTL-SDR kit, which includes the dongle, antennas, coax and mounts. The dongle itself costs around $30USD. More expensive, full-featured SDRs such as HackRF and LimeSDR will work as well.
* Some kind of antenna and coax for the dongle, I just used the cheap one that came in a kit with the RTL-SDR
* PC that can run rtl\_433. A laptop or raspberry pi works, as long as you can physically relocate the antenna near each tire. rtl\_433 runs on Windows, Mac and Linux. I used a Macbook, but instructions are the same no matter which platform you use.

## Process [#](#process)

### Install rtl\_433 [#](#install-rtl_433)

[rtl\_433](https://github.com/merbanan/rtl_433) is a program for receiving and decoding data transmissions in the 433.92 MHz, 868 MHz, 315 MHz, 345 MHz, and 915 MHz bands. We will use it for decoding TPMS sensor transmissions. It has built-in decoders for Toyota TPMS as well as many other vehicle brands. It’s an interesting piece of software with many uses beyond TPMS sensors.

If you are using Windows, [binary packages for rtl\_433 are available here](https://github.com/merbanan/rtl_433/releases/).
If you are using MacOS, [rtl\_433 can be installed via homebrew](https://formulae.brew.sh/formula/rtl_433).
For Linux users, check if your distribution’s package manager includes rtl\_433.

If you prefer to build from source, [check out the official build instructions](https://github.com/merbanan/rtl_433/blob/master/docs/BUILDING.md).

### Set up SDR hardware [#](#set-up-sdr-hardware)

Once you have installed rtl\_433, plug in your SDR to the computer and connect your antenna coax. I set up my telescoping dipole with each leg approx. 18" long. The exact length doesn’t matter too much- we don’t need our antenna/receiver to be very sensitive.

I also added a [rtl-sdr FM broadcast band-stop filter](https://www.rtl-sdr.com/rtl-sdr-com-broadcast-fm-band-stop-filter-88-108-mhz-reject-now-for-sale/) in between the antenna and the SDR. This is not required, but I have a lot of strong broadcast FM signals in my area and this helps prevent them from interfering with weaker signals.

### Receiving TPMS sensor messages [#](#receiving-tpms-sensor-messages)

Once we have rtl\_433 installed and our SDR hardware setup, we can start monitoring for transmissions from the car’s TPMS sensors. I moved my computer and SDR setup outside and set the antenna on the ground next to the truck. The Tacoma appears to have a “low line” TPMS system, where the sensors transmit messages at regular intervals, regardless of whether the car is being operated. In order to receive sensor messages, I ran rtl\_433 with the following options:

```
rtl_433	-M level -f 315000000
```

`-M level` displays signal level information along with each decoded transmission. `-f 315000000` sets the receiving frequency in Hz. Toyota TPMS sensors transmit at 315 MHz.

After running for a few minutes, we get the following output:

```
$ rtl_433 -M level -f 315000000
rtl_433 version 21.12-60-g5f0ff6db branch master at 202202121409 inputs file rtl_tcp RTL-SDR
Use -h for usage help and see https://triq.org/ for documentation.
Trying conf file at "rtl_433.conf"...
Trying conf file at "~/.config/rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...
Registered 182 out of 213 device decoding protocols [ 1-4 8 11-12 15-17 19-23 25-26 29-36 38-60 63 67-71 73-100 102-105 108-116 119 121 124-128 130-149 151-161 163-168 170-175 177-197 199 201-213 ]
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
[R82XX] PLL not locked!
Sample rate set to 250000 S/s.
Tuner gain set to Auto.
Tuned to 315.000MHz.
baseband_demod_FM: low pass filter for 250000 Hz at cutoff 25000 Hz, 40.0 us
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2022-02-13 12:57:50
model     : PMV-107J     type      : TPMS          id        : 04d3c7d2
status    : 40           battery_ok: 0             counter   : 1             failed    : OK            pressure_kPa: 205.840     temperature_C: 24.000     Integrity : CRC
Modulation: FSK          Freq1     : 315.0 MHz     Freq2     : 314.9 MHz
RSSI      : -1.0 dB      SNR ...