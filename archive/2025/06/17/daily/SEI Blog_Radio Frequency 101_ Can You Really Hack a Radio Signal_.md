---
title: Radio Frequency 101: Can You Really Hack a Radio Signal?
url: https://insights.sei.cmu.edu/blog/radio-frequency-101-can-you-really-hack-a-radio-signal/
source: SEI Blog
date: 2025-06-17
fetch_date: 2025-10-06T22:56:59.105763
---

# Radio Frequency 101: Can You Really Hack a Radio Signal?

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. Radio Frequency 101: Can You Really Hack a Radio Signal?

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

White, R., and Bragg, M., 2025: Radio Frequency 101: Can You Really Hack a Radio Signal?. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 3, 2025, https://doi.org/10.58012/ksvv-6z57.

Copy

APA Citation

White, R., & Bragg, M. (2025, June 16). Radio Frequency 101: Can You Really Hack a Radio Signal?. Retrieved October 3, 2025, from https://doi.org/10.58012/ksvv-6z57.

Copy

Chicago Citation

White, Roxxanne, and Michael Bragg. "Radio Frequency 101: Can You Really Hack a Radio Signal?." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, June 16, 2025. https://doi.org/10.58012/ksvv-6z57.

Copy

IEEE Citation

R. White, and M. Bragg, "Radio Frequency 101: Can You Really Hack a Radio Signal?," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 16-Jun-2025 [Online]. Available: https://doi.org/10.58012/ksvv-6z57. [Accessed: 3-Oct-2025].

Copy

BibTeX Code

@misc{white\_2025,
author={White, Roxxanne and Bragg, Michael},
title={Radio Frequency 101: Can You Really Hack a Radio Signal?},
month={{Jun},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/ksvv-6z57},
note={Accessed: 2025-Oct-3}
}

Copy

# Radio Frequency 101: Can You Really Hack a Radio Signal?

![Roxxanne White](/media/images/White_Roxxanne_560x560.max-180x180.format-webp.webp)
![Michael Bragg](/media/images/mpbragg.max-180x180.format-webp.webp)

###### [Roxxanne White](/authors/roxxanne-white) and [Michael Bragg](/authors/michael-bragg)

###### June 16, 2025

##### PUBLISHED IN

[Cyber-Physical Systems](/blog/topics/cyber-physical-systems/)

##### CITE

<https://doi.org/10.58012/ksvv-6z57>

Get Citation

##### TAGS

[Cybersecurity](/blog/tags/cybersecurity)
[Internet of Things](/blog/tags/internet-of-things)

##### SHARE

In 2017, a malicious actor exploited the signals in [Dallas’s emergency siren system](https://www.dallasnews.com/news/2017/04/10/culprit-broadcast-signal-that-triggered-dallas-emergency-sirens-friday-night/) and set off alarms for over 90 minutes. These types of attacks can affect devices that use radio frequency (RF) technology, from [smart security systems](https://www.wired.com/2014/07/hacking-home-alarms/) to aircraft. RF also plays a critical role in many military systems such as navigation, radar, and communication systems. Common DoD use cases include satellite communication (SATCOM), radar, and tactical data links that help coordinate troop movements, signal position information about a target, or help maintain communication between aircraft and drones. A [recent report](https://defensescoop.com/2024/02/14/radio-frequency-enabled-cyberattacks-pentagon-assessment/) indicated the DoD is susceptible to potential RF attack vectors, indicating the need to better understand and prevent vulnerabilities.

In this RF 101 guide, we explore some of the fundamentals of radio frequency communication, delve into the generalities of protocols and device interactions, discuss common RF tools, and uncover ways malicious actors can attack systems. We summarize the basics of RF technology and the risks associated with it, and we discuss how the SEI is helping to secure wireless communications.

## RF Fundamentals

[The electromagnetic spectrum](https://science.nasa.gov/ems/02_anatomy/) covers the entire range of electromagnetic waves from very long radio waves to visible light to very short, high-energy radiation such as X-rays and gamma rays. The radio spectrum is a subset of the broader electromagnetic spectrum and ranges in frequency from 3 Hz to 3,000 GHz. The ability of RF waves to propagate, or travel through different mediums, including the vacuum of space, enables wireless communication without the need for physical connection. RF signals are fundamental to modern communication systems, which enable many of today’s technologies including television, radio broadcasts, cellular communication, and Wi-Fi connections. Wireless RF communication also plays a vital role in space domains, such as satellite communication to ground stations, which enable transmission of telemetry data, GPS, and other signals. The radio spectrum can be divided into standardized [bands](https://en.wikipedia.org/wiki/Radio_spectrum) ranging from [extremely low frequency](https://en.wikipedia.org/wiki/Extremely_low_frequency) (ELF) to [tremendously high frequency](https://en.wikipedia.org/wiki/Terahertz_radiation) (THF) as seen below.

[![figure1_06162025](/media/images/figure1_06162025.max-1280x720.format-webp.webp)](/media/images/figure1_06162025.original.png)

Figure 1: The Electromagnetic Spectrum

[![figure2_06162025](/media/images/figure2_06162025.max-1280x720.format-webp.webp)](/media/images/figure2_06162025.original.png)

Figure 2: Frequency Spectrum

## What Are Protocols and RF Modules?

RF modules are small electronic devices that are used to transmit and receive radio signals between two devices that are physically separated. **Transmitters** are responsible for transmitting radio waves that carry analog or digital information, and **receivers** receive the radio waves and recover the information. This is the concept of a wireless communications channel, the open-space path through which information is transmitted via electromagnetic waves without the use of physical connections such as wires or cables. The overall signal is constructed of the carrier signal, a periodic waveform that conveys information via *modulations* that encode the analog or digital information. Modulation is the process of varying a carrier signal to encode data then demodulating that received signal to decode data. Modulation techniques determine how information is transmitted over radio waves, affecting the efficiency and quality of communication.

[![figure3_06162025](/media/images/figure3_06162025.max-1280x720.format-webp.webp)](/media/images/figure3_06162025.original.png)

Figure 3: Block Diagram of Digital Communication System

There are different ways that the information can be modulated. Common analog modulations include [amplitude modulation](https://en.wikipedia.org/wiki/Amplitude_modulation) (AM) and [frequency modulation](https://en.wikipedia.org/wiki/Frequency_modulation) (FM). AM modulates a higher frequency carrier with a lower frequency signal by adjusting the amplitude of the carrier signal. The frequency of the carrier is unaltered, but the amplitude varies constantly. FM modulates by making relatively small adjustments to the frequency of the carrier. These two methods characterize the kinds of RF signals on the familiar AM and FM radio bands. Common digital modulations, building on AM and FM, include [amplitude shift keying](https://en.wikipedia.org/wiki/Amplitude-shift_keying) (ASK) and [frequency shift keying](https://en.wikipedia.org/wiki/Frequency-shift_keying) (FSK).

Within a system, transmitters and receivers can be packaged together as **transceivers**, which perform both functions. Additionally, system on a chip (SoC) configurations integrate microcontrollers with the transceiver to allow protocol management such as data packetization.

[![figure4_06162025](/media/images/figure4_06162025.max-1280x720.format-webp.webp)](/media/images/figure4_06162025.original.png)

Figure 4: Representation of Signals

**Communication protocols** are sets of rules for the exchange of informa...