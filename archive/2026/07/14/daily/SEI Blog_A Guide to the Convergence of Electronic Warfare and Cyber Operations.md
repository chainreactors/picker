---
title: A Guide to the Convergence of Electronic Warfare and Cyber Operations
url: https://www.sei.cmu.edu/blog/a-guide-to-the-convergence-of-electronic-warfare-and-cyber-operations/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-07-14
fetch_date: 2026-07-15T04:49:41.085599
---

# A Guide to the Convergence of Electronic Warfare and Cyber Operations

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
4. A Guide to the Convergence of Electronic Warfare and Cyber Operations

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

McIlvenny, J., 2026: A Guide to the Convergence of Electronic Warfare and Cyber Operations. Software Engineering Institute blog, Accessed July 14, 2026, https://doi.org/10.58012/ssy8-4t48.

Copy

APA Citation

McIlvenny, J. (2026, July 14). A Guide to the Convergence of Electronic Warfare and Cyber Operations. Retrieved July 14, 2026, from https://doi.org/10.58012/ssy8-4t48.

Copy

Chicago Citation

McIlvenny, Joseph. "A Guide to the Convergence of Electronic Warfare and Cyber Operations." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, July 14, 2026. https://doi.org/10.58012/ssy8-4t48.

Copy

IEEE Citation

J. McIlvenny, "A Guide to the Convergence of Electronic Warfare and Cyber Operations," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 14-Jul-2026 [Online]. Available: https://doi.org/10.58012/ssy8-4t48. [Accessed: 14-Jul-2026].

Copy

BibTeX Code

```
@misc{mcilvenny_2026,
author={McIlvenny, Joseph},
title={A Guide to the Convergence of Electronic Warfare and Cyber Operations},
month={Jul},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/ssy8-4t48},
url={https://doi.org/10.58012/ssy8-4t48},
note={Accessed: 2026-Jul-14}
}
```

Copy

# A Guide to the Convergence of Electronic Warfare and Cyber Operations

![Headshot of Joseph McIlvenny.](/media/images/McIlvennyJoseph_00105748_10187-.max-180x180.format-webp.webp)

###### [Joseph McIlvenny](/authors/joseph-mcilvenny)

###### July 14, 2026

##### PUBLISHED IN

[Cyber-Physical Systems](/blog/topics/cyber-physical-systems/)

##### CITE

<https://doi.org/10.58012/ssy8-4t48>

Get Citation

##### SHARE

Cyberspace is recognized as a critical warfighting domain. Operations in the electromagnetic (EM) spectrum have also long been an important piece of the arsenal. Recent advances in software-defined radio (SDR), radio frequency system on chip (RF SoC), and artificial intelligence (AI) have demonstrated that electronic warfare (EW) techniques can be even more potent and readily available. For example, manipulation of intelligently adaptive radio signals could disable adversaries’ sensors and communication systems.

Beyond the boundaries of the battlefield, the Pentagon signaled the need for EM capability in 2020, with the [DoD Electromagnetic Spectrum Superiority Strategy](https://media.defense.gov/2020/Oct/29/2002525927/-1/-1/0/electromagnetic_spectrum_superiority_strategy.pdf) and [Joint Publication 3-85: Joint Electromagnetic Spectrum Operations](https://crows.org/download/cjcs-joint-publication-3-85-joint-electromagnetic-spectrum-operations-jemso/?wpdmdl=1511&ind=1699248928881&refresh=ae31847a&filename=JEMSO_JP3_85.pdf).

In the postmodern warfare landscape of today, [EW and cyberspace operations (CyberOps) are already being conducted together](https://www.jedonline.com/2023/10/25/blurring-the-lines-the-overlap-between-cyber-and-electronic-warfare/) at an increased rate on the battlefield. In this blog post, I will introduce the concepts of EW and CyberOps, the drivers behind their trend towards convergence, and several key issues in the field.

## Information Operations, Electronic Warfare, and Cyberspace Operations

Before going into detail about EW and CyberOps, we need to set out how these two techniques fit within the broader set of capabilities known as [military information operations (IO)](https://en.wikipedia.org/wiki/Information_Operations_%28United_States%29). Information operations encompass the employment of integrated capabilities, such as computer network operations (CNO), EW, psychological operations (PSYOP), operations security (OPSEC), and military deception (MILDEC). The objective of these integrated capabilities is to gain cognitive and/or technical advantage, typically by influencing perceptions and behaviors. As illustrated in the figure below, IO operates across physical, informational, and cognitive domains with the goal of securing an advantage over adversaries, often by disrupting communication systems or through dissemination of propaganda or misinformation.

[![figure1a_07132026](/media/images/figure1a_07132026.max-1280x720.format-webp.webp)](/media/images/figure1a_07132026.original.png)

Figure 1: Military Information Operations

The concept of the convergence between EW and CyberOps has been around for more than a decade; however, there has been an increasing trend towards the implementation and operationalization of EW and CyberOps converged systems. More recently, the ideas codified in the concept of [Cyber Electromagnetic Activities (CEMA)](https://nsarchive.gwu.edu/sites/default/files/documents/3456723/Document-04-Department-of-the-Army-FM-3-38-Cyber.pdf) have emerged on the scene in various forms including intelligent communication systems, autonomous platforms, and tactical edge computational capabilities. We will look at these and others in this section.

## Technological Driving Factors

A key factor driving the increase in converged systems is the advancement of [software-defined radio (SDR)](https://en.wikipedia.org/wiki/Software-defined_radio) technology and capabilities. While SDRs have been on the market for many years, the most recent advancements seek to reduce size and power consumption while increasing computational capability and enhancing performance. These trends can be readily seen in the advancements in [Radio Frequency System-on-Chip (RFSoC)](https://www.youtube.com/watch?v=tNuvpKsuH-4) technologies. Modern SDRs have shifted away from using separate chips for [radio frequency (RF) front ends](https://en.wikipedia.org/wiki/RF_front_end) and data processing towards utilization of single-chip solutions. RFSoC devices can integrate high-speed analog-to-digital converters (ADC) and digital-to-analog converters (DAC) directly into the chip, significantly reducing size, power, and cost. Contemporary SDRs can support multiple radio chains operating at high sampling rates, often greater than a giga-sample per second, and high instantaneous bandwidths that can allow many (in some cases, 16 or more) independent radio channels within a single device. Combined with adaptive waveforms, SDR software now allows a single-base hardware SoC to alter its functionality almost instantly between communications, radar, and cyber exploitation. This facilitates intelligent jamming techniques where an adversarial protocol can be sensed, understood, and manipulated in real-time.

Advances in [edge computing](https://www.sei.cmu.edu/blog/networking-at-the-tactical-and-humanitarian-edge/), hardware miniaturization, and integration of artificial intelligence and machine learning (AI/ML) tools are also drivers. AI/ML tools can improve signal processing, enable intelligent modulation, manage interference, and provide cognitive radio capabilities where the radio can detect the spectral environment and autonomously change its operational parameters in response. The ever-widening application of AI tools allows systems to automatically detect, classify, and adapt to new, unknown threat signals enabling EW systems to autonomously develop jamming techniques rather than relying on pre-programmed waveform and/or protocol libraries. Hardware miniaturization, edge computing, and hardware-software codesign of systems affords the ability to process RF data closer to the source (edge computing) improved by faster, more efficient embedded processors. This is critica...