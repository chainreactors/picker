---
title: How the Cloudflare global network optimizes for system reboots during low-traffic periods
url: https://buaq.net/go-171882.html
source: unSafe.sh - 不安全
date: 2023-07-13
fetch_date: 2025-10-04T11:52:55.959248
---

# How the Cloudflare global network optimizes for system reboots during low-traffic periods

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/55720b9857da59734fe492a6b3011a7a.jpg)

How the Cloudflare global network optimizes for system reboots during low-traffic periods

Loading...
*2023-7-12 21:0:20
Author: [blog.cloudflare.com(查看原文)](/jump-171882.htm)
阅读量:20
收藏*

---

Loading...

* [![Opeyemi Onikute](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/07/1652886681973.jpeg)](https://blog.cloudflare.com/author/opeyemi/)
* [![Nicholas Rhodes](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/07/Nick-Rhodes.jpeg)](https://blog.cloudflare.com/author/nicholas-rhodes/)

![How the Cloudflare global network optimizes for system reboots during low-traffic periods](https://blog.cloudflare.com/content/images/2023/07/image6-2.png)

To facilitate the huge scale of Cloudflare’s customer base, we maintain data centers which span more than 300 cities in over 100 countries, including approximately 30 locations in Mainland China.

The Cloudflare global network is built to be continuously updated in a zero downtime manner, but some changes may need a server reboot to safely take effect. To enable this, we have mechanisms for the whole fleet to automatically reboot with changes gated on a unique identifier for the reboot cycle. Each data center has a **maintenance window**, which is a time period - usually a couple of hours - during which reboots are permitted.

We take our customer experience very seriously, and hence we have several mechanisms to ensure that disruption to customer traffic does not occur. One example is [Unimog](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/), our in-house load balancer that spreads load across the servers in a data center, ensuring that there is no disruption when a server is taken out for routine maintenance.

The SRE team decided to further reduce risk by only allowing reboots in a data center when the customer traffic is at the lowest. We also needed to automate the existing manual process for determining the window - eliminating toil.

In this post, we’ll discuss how the team improved this manual process and automated the determination of these windows using a trigonometric function - sinusoidal wave fitting.

## When is the best time to reboot?

Thanks to [how efficient our load-balancing framework is](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/) within a data center, technically we could proceed to schedule reboots throughout the day with zero impact to traffic flowing through the data center. However, operationally the management is simplified by requiring reboots take place between certain times for each data center. It both acts as a rate-limiter to avoid rebooting all servers in our larger data centers in a single day, and makes remediating any unforeseen issues that arise during the reboots more straightforward, as issues can be caught within the first batch of reboots.

One of the first steps is to determine the time window during which we are going to allow these reboots to take place; choosing the relative low-traffic period for a data center makes the most sense for obvious reasons. In the past, these low-traffic windows were found manually by humans reviewing historical traffic trends present in our metrics; it was SRE who were responsible for creating and maintaining the definition of these windows, which became particularly toilsome:

1. Traffic trends are always changing, requiring increasingly frequent reviews of maintenance hours.
2. We move quickly at Cloudflare, there is always a data center in a state of provisioning, making it difficult to keep maintenance windows up-to-date.
3. The system was inflexible, and provided no dynamic decision-making.
4. This responsibility became SRE toil as it was repetitive, process-based work that could and should be automated.

## Time to be more efficient

We quickly realized that we needed to make this process more efficient using automation. An ideal solution would be one that was accurate, easy to maintain, re-usable, and could be consumed by other teams.

A theoretical solution to this was **sine-fitting** on the CPU pattern of the data center over a configurable period. e.g. two weeks. This method is a way to transform the pattern into a theoretical sinusoidal wave as shown in the image below.

![This is an example of a datacenter with a good sine fit.](https://blog.cloudflare.com/content/images/2023/07/bkk05.png "Sine fitting on a data center CPU")

With a sine wave, the most common troughs can be determined. The periods where these troughs occur are then used as options for the maintenance window.

## Sinusoidal wave theory - the secret sauce

We think math is fun and were excited to see how this held up in practice. To implement the logic and tests, we needed to understand the theory. This section details the important bits for anyone that is interested in implementing this for their maintenance cycles as well.

The image below shows a theoretical representation of a sine wave. It is represented by the mathematical function y(t) = Asin(2πft + φ) where A = Amplitude, f = Frequency, t = Time and φ = Phase.

![A sine wave is a geometric waveform that oscillates (moves up, down, or side-to-side) periodically.](https://blog.cloudflare.com/content/images/2023/07/sine.drawio--4-.png "Theoretical representation of a sine wave")

In practice, various programming language packages exist to fit an arbitrary dataset on a curve. For example, Python has the [scipy curve\_fit function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html).

We used Python and to make the result more accurate, it is recommended to include arbitrary values as initial guesses. These are described below;

**Amplitude**: This is the distance from the peak/valley to the time axis, and is approximated as the standard deviation multiplied by √2. The standard deviation represents the variability in the data points, and for a sine wave that varies between -1 and +1, the standard deviation is approximately 0.707 (or 1/√2). Therefore, by multiplying the standard deviation of the data by √2, we can represent an approximation of the amplitude.

**Frequency**: This is the number of cycles (time periods) in one second. We are concerned with the daily CPU pattern, meaning that the guess should be one full wave every 24 hours (i.e. 1/86400).

**Phase**: This is the position of the wave at T=0. No guess is needed for this.

**Offset**: To fit the sine wave on the CPU values, we need to shift upwards by the offset. This offset is the mean of the CPU values.

Here’s a basic example of how it can be implemented in Python:

```
timestamps = numpy.array(timestamps)
cpu = numpy.array(cpu)
guess_freq = 1 / 86400  # 24h periodicity
guess_amp = numpy.std(cpu) * 2.0**0.5
guess_offset = numpy.mean(cpu)
guess = numpy.array([guess_amp, 2.0 * numpy.pi * guess_freq, 0.0, guess_offset])

def sinfunc(timestamps, amplitude, frequency, phase, offset):
    return amplitude * numpy.sin(frequency * timestamps + phase) + offset

amplitude, frequency, phase, offset, _ = scipy.optimize.curve_fit(
    sinfunc, timestamps, cpu, p0=guess, maxfev=2000
)
```

## Applying the theory

With the theory understood, we implemented this logic in our reboot system. To determine the window, the reboot system queries [Prometheus](https://blog.cloudflare.com/tag/prometheus/) for the data center CPU over a configurable period and attempts to fit a curve on the resultant pattern.

If there’s an accurate enough fit, the window is cach...