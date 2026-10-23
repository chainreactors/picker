---
title: I had plans for that second
url: https://blog.talosintelligence.com/i-had-plans-for-that-second/
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:31.009109
---

# I had plans for that second

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# I had plans for that second

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, October 22, 2026 14:04

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Here for the latest on the PHP vulnerabilities? Head on down to ‘The One Big Thing’. Talos has published a blog to explain what we know so far, and details the Snort coverage available, including rules in the Community Ruleset.

But if you want a bit of levity, here’s what I wrote before everything kicked off yesterday:

Ever feel like the world is moving too fast to keep up? Well, I bring you scientific proof that it’s not just you.

For millions of years, the moon has been slowing down the Earth’s rotation. But over the past decade, we’ve been speeding up (I KNEW I was aging faster than before). Apparently, changes in the Earth’s core are involved (either that, or the 1978 Superman film was a documentary).

This is all causing massive headaches for the people responsible for keeping time. They’re officially called “The International Bureau of Weights and Measures”, but I’m going to call them “The Time-Keepers”. For nerd reasons).

The issue is that the atomic clocks that power so many of our systems, and the rotation of our planet, don’t always agree. Atomic clocks keep extremely consistent time, while each Earth day is rarely the same length as the next. Atomic timekeeping absolutely cannot stand that level of flexibility (have a watch of our [“The Light We Keep”](https://youtu.be/5lioAyh0vJs) documentary to see the importance that accurate clocks have on critical infrastructure).

To keep Coordinated Universal Time (UTC), which is based on atomic clocks, aligned with Earth’s rotation, we introduced a “leap second” in 1972. This system allows for an extra second to be added, or taken away, when we stray too far from atomic time.

A few days ago, The Time-Keepers voted to officially abolish the leap second. Why? Well, there’s a few parts to it.

For the past 54 years, we’ve never once had a second removed from our lives. They’ve always been added (27 of them to be precise). I myself have experienced 20 of these extra seconds. If I’d have known that, I’d have used them more wisely. Like thinking before saying, “Love you too!” to the post-person this morning.

That added time, while it seems nice to have on the surface, can wreak havoc with our modern technology systems. In 2012, the extra second caused so much confusion that it crashed Reddit, among other systems.

The recent speeding-up of the Earth’s rotation complicates things further. If we keep going at this rate, it could result in the world’s first ever “negative second”. If you thought our technology systems struggled with *added* time, there are a lot of sciency brains who are very worried about the impact of taking time away. One of those concerns being… it’s never been done before.

So, what’s The Time-Keeper’s solution? Invent more time! Woooo.

Starting next May, the leap second will be replaced with a "leap hour," allowing UTC to diverge from Earth's rotation by up to an hour before a correction is made.  None of us will get to experience that extra hour in our lifetimes, but our Great, Great, Great, Great, Great, Great, Great, Great, Great, Great, Great grandchildren are going to have one hell of a party.

For us current mortals, we’re all getting a little less time, and we’re hurtling through space a little faster. Happy Thursday!

But I guess I do want to make the point that I’m glad the risk has been thoroughly assessed ahead of, ahem, time. The Time-Keepers have decided that the world’s infrastructure should not have to find out how it handles a missing second by collectively experiencing one.

And I don’t even want to think about how all the AIs would cope with a negative second…

There’s something here for incident response planning. “It’s never happened before” is an excellent reason to test whether you’re ready for it. Run the exercise. Find out which part of your plan depends on something that, in this scenario, is also broken. Preferably before an adversary gets to supervise the practical demonstration.

Now, if only the Time-Keepers can abolish Daylight Savings Time next...

## The one big thing

Two unauthenticated remote code execution (RCE) flaws were discovered in PHP, rocking the internet. Dubbed "php2shell" and triggered by a simple HTTP request, this vulnerability affects every build since 5.4. Talos assesses that all industries running PHP applications are at risk for exploitation if systems remain unpatched.

### Why do I care?

PHP runs WordPress, Drupal, Magento, Shopware, WooCommerce, and many other ubiquitous internet staples, so the possible blast radius is enormous. Older branches are end of life (EOL) and will not receive patches; these could account for around 50% of use cases.

### So now what?

Cisco customers are covered with the Cisco Talos Network Intrusion Prevention (SNORT®) signatures 67359 and 67360. If your organization is running PHP 8.1 or older, Talos very strongly advises immediate update to PHP 8.2 or later. There is no patch for PHP 8.1 or older. [See the article](https://blog.talosintelligence.com/two-critical-rces-in-php-core/) for more specific coverage and detection guidance.

See an interview with Nick Biasini on php2shell defense:

## Top security headlines of the week

### 'PHP2Shell' Bugs Signal Red Alert for Security Industry

Security teams are scrambling to remediate two critical PHP vulnerabilities following leaked details and reports of exploitation attempts. ([Dark Reading](https://www.darkreading.com/application-security/php2shell-bugs-red-alert-security-industry))

### **I**NC and The Gentlemen Ransomware Affiliates expo...