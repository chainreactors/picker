---
title: 60 Hurts per Second – How We Got Access to Enough Solar Power to Run the United States
url: https://www.bitdefender.com/blog/labs/60-hurts-per-second-how-we-got-access-to-enough-solar-power-to-run-the-united-states/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-08
fetch_date: 2025-10-06T18:07:52.276149
---

# 60 Hurts per Second – How We Got Access to Enough Solar Power to Run the United States

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[IoT Research](/en-us/blog/labs/tag/iot-research "IoT Research")[Whitepapers](/en-us/blog/labs/tag/whitepapers "Whitepapers")

min read

# 60 Hurts per Second – How We Got Access to Enough Solar Power to Run the United States

[![Ioan Alexandru MELNICIUC](https://blogapp.bitdefender.com/labs/content/images/size/w100/2024/08/image-1.png "Ioan Alexandru MELNICIUC")](/en-us/blog/labs/author/alexandru-melniciuc "Ioan Alexandru MELNICIUC")[![Alexandru LAZĂR](https://blogapp.bitdefender.com/labs/content/images/size/w100/2024/08/alexandru-lazar.jpg "Alexandru LAZĂR")](/en-us/blog/labs/author/alexandru-lazar "Alexandru LAZĂR")[![George CABĂU](https://blogapp.bitdefender.com/labs/content/images/size/w100/2024/08/george-cabau.jpg "George CABĂU")](/en-us/blog/labs/author/george-cabau "George CABĂU")[![Radu Alexandru BASARABA](https://blogapp.bitdefender.com/labs/content/images/size/w100/2024/08/Image-from-iOS.jpg "Radu Alexandru BASARABA")](/en-us/blog/labs/author/radu-basaraba "Radu Alexandru BASARABA")

[Ioan Alexandru MELNICIUC](/en-us/blog/labs/author/alexandru-melniciuc "Ioan Alexandru MELNICIUC")[Alexandru LAZĂR](/en-us/blog/labs/author/alexandru-lazar "Alexandru LAZĂR")[George CABĂU](/en-us/blog/labs/author/george-cabau "George CABĂU")[Radu Alexandru BASARABA](/en-us/blog/labs/author/radu-basaraba "Radu Alexandru BASARABA")

August 07, 2024

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![60 Hurts per Second – How We Got Access to Enough Solar Power to Run the United States](https://blogapp.bitdefender.com/labs/content/images/size/w600/2024/08/1ZZ96uESRJQ.jpg "60 Hurts per Second – How We Got Access to Enough Solar Power to Run the United States")

The electricity grid – the buzzing, crackling marvel that supplies the lifeblood of modernity - is by far the largest structure humanity ever built. It’s so big, in fact, that few people even notice it, like a fish can’t see the ocean.

Until the grid goes down, that is. Then, like the fish dangling from the angler’s hook, we see our vulnerability. Modernity dissolves into a sudden silence, followed by the repeated flick of a light switch, and a howl of panic at the prospect of missed appointments, ruined dinners, lost workdays, stopped elevators and dark, cold evenings, and worse.

But most of the time, the grid hums along just fine ...

Now, take that labyrinthine system and add another complex network, this one delivering hundreds of gigawatts of power from the sun - solar power infrastructure. This ever-fluctuating source of energy is tapped via rooftop panels, distant solar farms, slapdash home arrays and other evolving infrastructure around the globe.

And with complexity comes risk ...

Then, take those two systems and intersect them with the Internet of Things, an ethereal network that runs from the limits of human thought – both positive and malicious – into the routines of daily life through seemingly innocuous gadgets.

At that intersection we find the mundane world of inverters and controllers.

And that's where a group of researchers stumbled upon an alarming fact:

a solar grid responsible for 195 gigawatts, or 20 percent of the world’s solar power output, is vulnerable. That’s enough to power the entire United States - and it’s just waiting to be hijacked.

## Key Findings

* Bitdefender researchers have identified a series of vulnerabilities in PV plant management platforms operated by Solarman and Deye.
* This platform is responsible for coordinating production operations of millions of solar installations worldwide generating a whopping output of approximately 195 GW of solar power (20% of the global solar production)
* If exploited, these vulnerabilities could allow an attacker to control inverter settings that could take parts of the grid down, potentially causing blackouts.
* These vulnerabilities have been communicated to the affected vendors and fixed.

## Understanding the Power Grid

The power grid is a vast network of power plants, transmission lines and distribution systems that delivers electricity from producers to consumers. It consists of three main components:

1. **Generation**: Power plants generate electricity using various sources, including coal, natural gas, nuclear, hydro and, increasingly, solar and wind.
2. **Transmission**: High-voltage transmission lines carry electricity over long distances from power plants to substations.
3. **Distribution**: Substations lower the voltage for safe distribution to homes and businesses through local power lines.

The grid balances supply and demand in real time, ensuring that electricity is available when needed. When generation exceeds demand, voltage in the grid rises to dangerous levels that can damage sensitive equipment connected to it.

When generation can't meet demand, anomalies begin to occur. Initially, [your microwave oven may get several minutes slower](https://arstechnica.com/tech-policy/2018/03/ovens-across-europe-display-the-wrong-time-due-to-a-serbia-kosovo-grid-dispute/) (as it computes its current time based on the “ticks” in the network measured in Hertz: 60 Hertz - or cycles per second - in the US, and 50 Hz in Europe). Secondly, parts of the grid where the imbalance is detected are disconnected before they drag the whole system into a downwards spiral that can take days to recover from.

![](https://blogapp.bitdefender.com/labs/content/images/2024/08/image.png)

Fascinated? To learn more about how the grid works, you might want to watch [this episode of Practical Engineering](https://www.youtube.com/watch?v=v1BMWczn7JM).

## The Role of Solar Energy in the Grid

Solar energy has a powerful impact on the energy landscape. Solar panels convert sunlight into a clean, renewable source of power, which can be used immediately, stored in batteries, or fed into the grid.

Solar power systems are often decentralized, meaning they are installed on individual homes or businesses rather than centralized power plants. This means that generation and distribution often take place in the same ZIP code and (with some exceptions such as solar power production in parks), disruptions at this level have a limited geographic impact.

This decentralization presents several challenges and opportunities for the grid. Solar power reduces dependence on fossil fuels, lowers greenhouse gas emissions, and can enhance grid resilience by distributing power generation. However, integrating numerous small-scale solar systems into the grid can complicate management.

Solar setups produce variable amounts of electricity, and only during daytime.  Maintaining voltage levels and managing the variability of solar power must  be outsourced to a pre-programmed critical component called an inverter. An inverter converts the direct current (DC) electricity generated by solar panels into alternating current (AC) electricity, the standard used by most homes and businesses, as well as for transmission over the power grid.

The inverter performs two primary functions in a solar power system:

* **DC to AC Conversion**: Solar panels generate DC electricity  however, most electrical appliances and the power grid operate on AC electricity, which alternates in polarity and voltage. The inverter converts the DC electricity into AC electricity to  be used by household appliances or fed into the grid.
* **Grid Synchronization**: In grid-tied solar power systems, the inverter  synchronizes the phase and frequency of the AC output with the grid. This ensures that the electricity generated by the solar panels is compatible with the grid and...