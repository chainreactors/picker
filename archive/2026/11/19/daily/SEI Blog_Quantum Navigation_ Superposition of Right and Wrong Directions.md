---
title: Quantum Navigation: Superposition of Right and Wrong Directions
url: https://www.sei.cmu.edu/blog/quantum-navigation-superposition-of-right-and-wrong-directions/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-11-19
fetch_date: 2026-11-20T09:23:07.914620
---

# Quantum Navigation: Superposition of Right and Wrong Directions

[Skip to main content](#main-content)

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Quantum Navigation: Superposition of Right and Wrong Directions

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Stricklen, G., 2026: Quantum Navigation: Superposition of Right and Wrong Directions. Software Engineering Institute blog, Accessed November 19, 2026, https://doi.org/10.58012/9zhf-8709.

Copy

APA Citation

Stricklen, G. (2026, November 19). Quantum Navigation: Superposition of Right and Wrong Directions. Retrieved November 19, 2026, from https://doi.org/10.58012/9zhf-8709.

Copy

Chicago Citation

Stricklen, Georgia. "Quantum Navigation: Superposition of Right and Wrong Directions." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, November 19, 2026. https://doi.org/10.58012/9zhf-8709.

Copy

IEEE Citation

G. Stricklen, "Quantum Navigation: Superposition of Right and Wrong Directions," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 19-Nov-2026 [Online]. Available: https://doi.org/10.58012/9zhf-8709. [Accessed: 19-Nov-2026].

Copy

BibTeX Code

```
@misc{stricklen_2026,
author={Stricklen, Georgia},
title={Quantum Navigation: Superposition of Right and Wrong Directions},
month={Nov},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/9zhf-8709},
url={https://doi.org/10.58012/9zhf-8709},
note={Accessed: 2026-Nov-19}
}
```

Copy

# Quantum Navigation: Superposition of Right and Wrong Directions

![Headshot of Georgia Stricklen.](/media/images/Stricklen_Georgia_100_260409.max-180x180.format-webp.webp)

###### [Georgia Stricklen](/authors/georgia-stricklen)

###### November 19, 2026

##### PUBLISHED IN

[Quantum Computing](/blog/topics/quantum-computing/)

##### CITE

<https://doi.org/10.58012/9zhf-8709>

Get Citation

##### SHARE

Quantum sensors have emerged as promising candidates to enhance the sensitivity and availability of navigational systems, specifically in varied underwater environments where classical inertial navigational systems (INSs) and the Global Navigation Satellite System (GNSS) have faced significant challenges. A key driver of early quantum sensor adoption has been the development of smaller, more robust quantum devices that enhance the functionality and accuracy of existing classical navigation systems, one of the most studied uses for quantum sensing.

In this post, we explore sensing in the quantum paradigm with applications in underwater navigation and potential areas of exploration/refinement as part of the collective area of interest known as [Quantum Position, Navigation, and Timing (QPNT)](https://www.nrl.navy.mil/Portals/38/PDF%20Files/QuantumPNT_FactSheet_2024_FINAL.pdf). To characterize the operational utility of quantum sensors, we will use the following criteria: (1) what is being sensed, (2) the mechanism by which the sensing is done, (3) how it is being used for QPNT, (4) the maturity of the device, (5) SWaP (size, weight, and power), (6) the sensitivity and noise level in the quantum sensor, (7) the conditions required for external signals, (8) limitations of the device, and (9) benefits over classical hardware. Each section will contain a table that describes how one device or one type of device from the section fulfills the criteria listed above. This post will focus on the Quantum Position and Navigation devices of QPNT.

## Current State of Underwater Autonomous Navigation

Some of the most technically challenging areas of navigation pertain to autonomous underwater vehicles (AUVs). These vehicles face challenges ranging from degradation of signals and lack of persistent access to the [Global Positioning System (GPS)](https://www.gps.gov/), a type of GNSS. As the authors of [*AUV Navigation and Localization: A Review*](https://ieeexplore.ieee.org/document/6678293) describe, AUVs instead use dead reckoning to navigate an underwater location through an INS, which reveals data related to the vehicle’s orientation, velocity, or acceleration vector. This information is gathered via classical [gyroscopes](https://arxiv.org/abs/2310.04729), which measure the angular rates of a vehicle, and [accelerometers](https://arxiv.org/abs/2310.04729), which measure the force required to accelerate a mass. [Acoustic sensors](https://doi.org/10.1109/joe.2013.2278891), which suffer from short bandwidth, high latency, variable signal speed due to water temperature/salinity, and data loss, only partially supplement these data needs. INS can also benefit from gravimeters, which are a specific type of accelerometer, and magnetometers. In [underwater navigation](https://cgsr.llnl.gov/sites/cgsr/files/2025-06/Burkey_QS_final.pdf), magnetometers help guide the vehicle around landmarks using magnetic field anomalies that were mapped during previous expeditions. [Gravimeters](https://cgsr.llnl.gov/sites/cgsr/files/2025-06/Burkey_QS_final.pdf) similarly report the strength of Earth’s gravity, which varies at different locations due to terrain features, such as mountains and valleys. When combined with existing gravity maps, the vehicle can use the gravity measurements to navigate. Unlike magnetometers, they require a longer measurement time due to the weakly changing gravitational field.

Unfortunately, [dead reckoning errors](https://doi.org/10.1109/joe.2013.2278891) are cumulative and grow unbounded with distance traveled. INSs are also subject to drift and require frequent recalibration to maintain their accuracy. Classical gravimeters require regular recalibration using a known location, which may be impossible in contested environments or ice-covered waters. [Recalibration](https://doi.org/10.1109/joe.2013.2278891) requires the exchange of information between an external satellite source or an above-water support vessel, which makes integration with an underwater moving vehicle at sea for long periods of time infeasible.

An INS is often paired with a [Doppler Velocity Log (DVL)](https://en.wikipedia.org/wiki/Acoustic_Doppler_current_profiler#Bottom_tracking) to [measure the velocity of both the water and seabed with respect to the AUV](https://doi.org/10.1109/joe.2013.2278891). INSs and DVLs can be assisted by deployed infrastructure to act as an external reference, similar to a beacon. However, deploying external infrastructure comes with its own complexity, especially in contested environments. Additionally, according to the authors of [*Current Trends and Advances in Quantum Navigation for Maritime Applications: A Comprehensive Review*](https://arxiv.org/abs/2310.04729), a DVL has more intensive power requirements and requires close proximity to the seabed for consistent locking, a requirement that limits the spatial flexibility of vehicle ranges.

Geophysical systems also provide useful visual odometry for navigational systems. Combinations of visual and inertial sensors systems, called [visually augmented navigation (VAM)](https://doi.org/10.1109/JOE.2008.923547), have already been used to survey the RMS Titanic. VAM has also been used by the U.S. Navy for ship-hull inspection as well as accurate mapping and feature extraction. In underwater environments, the [increased susceptibility of scattering, coupled with inadequate lighting, reduces the effective range of cameras](https://doi.org/10.1109/joe.2013.2278891).

Quantum navigational systems could address many issues related to the use of navigational systems in underwater conditions. This is due to their intrinsic design, which operates and benefits from the efficiency and sensitivity of quantum-level operations to re...