---
title: Tracking airplanes with a Raspberry Pi and an ADS-B receiver
url: https://www.andreagrandi.it/posts/tracking-airplanes-raspberrypi-adsb/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-28
fetch_date: 2025-10-06T18:29:50.644670
---

# Tracking airplanes with a Raspberry Pi and an ADS-B receiver

[![Avatar](/about/images/me_pycon_2019_2.jpg)](/)

# [Andrea Grandi](/)

## Software Developer

1. [Home](/)
2. [About](/about/)
3. [Curriculum](/curriculum/)

[![Buy Me a Coffee at ko-fi.com](https://storage.ko-fi.com/cdn/kofi1.png?v=3)](https://ko-fi.com/G2G83E9SV)

[![Featured image of post Tracking airplanes with a Raspberry Pi and an ADS-B receiver](/posts/tracking-airplanes-raspberrypi-adsb/cover-adsbexchange-flights.png)](/posts/tracking-airplanes-raspberrypi-adsb/)

[Howto](/categories/howto/)

## [Tracking airplanes with a Raspberry Pi and an ADS-B receiver](/posts/tracking-airplanes-raspberrypi-adsb/)

### How to track flights and airplanes using a Raspberry Pi and an ADS-B receiver.

Aug 10, 2024

If you have ever used a flight tracking app like [Flightradar24](https://www.flightradar24.com) or [FlightAware](https://flightaware.com) you might have wondered how they get the data about the airplanes in real time. All these services use an existing network of ADS-B receivers to collect data about the airplanes in the sky.

## What is ADS-B?

[ADS-B](https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance%E2%80%93Broadcast) stands for **Automatic Dependent Surveillance-Broadcast** and it’s a technology that allows aircraft to determine their position via satellite navigation and periodically broadcast it, enabling them to be tracked. The information can be received by air traffic control ground stations as a replacement for secondary radar.

This is all **public information** (it’s public data and **you are legally allowed to receive it and share it**).

## What do you need?

To build the tracking device you need a few things:

* a **Raspberry Pi** (I’m using a Raspberry Pi 2 Model B)
* an **ADS-B receiver** (I’m using a [AirNav RadarBox FlightStick](https://www.amazon.it/dp/B07K47P7XD?psc=1&ref=ppx_yo2ov_dt_b_product_details) but any **RTL2832/R820T2-based** USB dongle should work)
* a **1090MHz capable antenna** (I’m using a [Bingfu Antenna RTL SDR](https://www.amazon.it/dp/B07ZH5FJBW?psc=1&ref=ppx_yo2ov_dt_b_product_details), any similar antenna should work, just make sure the connector is compatible with your receiver otherwise you might need an adapter)
* a **microSD card** (I’m using a 16GB one) and a **power supply** for the Raspberry Pi

![RaspberryPi 2 and ADS-B receiver](/posts/tracking-airplanes-raspberrypi-adsb/raspberrypi-receiver.png)

### Is a Raspberry Pi x enough?

I’m using a **Raspberry Pi 2 Model B**, which is quite old (it was released in 2015) and it’s not the most powerful Raspberry Pi available. It’s still enough to run the software needed to track the airplanes, but if you have a newer Raspberry Pi (like a Raspberry Pi 4 or 5) you may be able to handle higher workloads (especially if you live nearby a busy airport) and feed multiple services.

If you are still not sure, have a look at the stats of my Raspberry Pi 2 while running the software: I’m using **just 23% of the CPU** and **~200MB** of the total available **memory**.

![RaspberryPi 2 stats](/posts/tracking-airplanes-raspberrypi-adsb/raspberrypi-stats.png)

## Setting up the Raspberry Pi

Once you have all the components, you have two options to set up the Raspberry Pi:

* **install the software from scratch** (this is the most complicated way but it gives you more control over the system)
* **use a pre-built image** (this is the easiest way, you just need to flash the image on the microSD card and you are ready to go) like the one provided by [FlightRadar24](https://www.flightradar24.com/build-your-own) or [Flightaware](https://www.flightaware.com/adsb/piaware/build/)

I won’t cover the detailed instructions, but I opted for the first option (also because I wasn’t sure which service I was going to feed).

Something I can definitely suggest, in case you plan to install RaspbianOS from scratch, is to use the [**Raspberry Pi Imager**](https://www.raspberrypi.com/software/) and to install the **Lite version** of the OS (you don’t need the desktop environment for this project).

I also suggest to **install the [Tailscale](https://tailscale.com) client** and [**enable SSH access**](https://tailscale.com/kb/1193/tailscale-ssh) to the Raspberry Pi so you will be able to easily access the RaspberryPi from your computer, regardless of the network you are connected to.

### Where to place the antenna?

The antenna should be placed in a **location where it has a clear view of the sky**. The higher you can place it, the better the reception will be. I placed mine on the window sill, but if you have a balcony or a terrace you can place it there. To facilitate the installation of the device, I strongly recommend to at least use a WiFi connection for the Raspberry Pi, so all you need is a power supply and you just have to pass the antenna cable through the window.

## Configuring the feeder

Once you have the Raspberry Pi up and running, you need to install the software to **receive** the data from the ADS-B receiver and **feed** it to the services.

The instructions for this step depend on the service you want to feed. In my case I decided to feed to [**ADS-B Exchange**](https://www.adsbexchange.com) and [**Flightradar24**](https://www.flightradar24.com), which they booth provide detailed instructions and scripts to install the software:

* [ADS-B Exchange](https://www.adsbexchange.com/ways-to-join-the-exchange/existing-equipment/)
* [Flightradar24](https://www.flightradar24.com/share-your-data)

**Note:** it’s worth saying that if you opt for the easier setup (using a pre-built image) you won’t have to install the software manually, but you will still need to configure the feeder to send the data to the services (by answering a few questions during the setup, about your location and type of receiver).

### Add nice stats to your Raspberry Pi

If you want to have some nice stats like the ones I showed you before, you can install install and utility called [**graphs1090**](https://github.com/wiedehopf/graphs1090#graphs1090). This utility doesn’t just show you CPU and memory stats, but also data from the ADS-B receiver like the number of messages received, the number of aircrafts tracked, and the number of positions reported.

![ADS-B Performances - graphs1090](/posts/tracking-airplanes-raspberrypi-adsb/adsb-performances.png)

## Which other services could or I should feed?

There are a few other serviced you could feed, and it’s totally up to you which one you want to use. Just keep in mind these two things:

* each service you feed will likely give you back a **premium account**, which will give you access to more features and data. So if you are interested in a specific service, you might want to feed it.
* most of the services are “censored” (didn’t I say the data is public?) and they don’t show all the flights. If you want to see all the flights you need to feed to [**ADS-B Exchange**](https://www.adsbexchange.com) which is the only service that shows all the flights, regardless of the aircraft owner 😏

Here are a few other services you could feed:

* [**FlightAware**](https://flightaware.com)
* [**RadarBox24**](https://www.radarbox24.com)
* [**Planefinder**](https://planefinder.net)
* [**OpenSky Network**](https://opensky-network.org)

**Note:** some of these services may also send you a **free ADS-B receiver** or a complete kit if you provide them with a good location to place the receiver (but if you don’t live in a location they are interested in, they won’t send you anything).

## Conclusion

With a total budget of around **120€** (Raspberry Pi 2 Model B, AirNav RadarBox FlightStick, Bingfu Antenna RTL SDR) and a couple of hours available, you can build your own flight tracking device and feed multiple services. It’s a fun project and it’s also useful to track the flights in your area. I didn’t know anything about ADS-B receivers before a couple of weeks ago and I totally have to “blame” my friend [**Alan Pope**](https://popey.com/blog/about/) who told me abo...