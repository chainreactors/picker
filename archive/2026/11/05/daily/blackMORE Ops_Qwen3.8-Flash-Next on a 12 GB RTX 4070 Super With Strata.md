---
title: Qwen3.8-Flash-Next on a 12 GB RTX 4070 Super With Strata
url: https://www.blackmoreops.com/qwen3-8-flash-next-rtx-4070-super-strata/
source: blackMORE Ops
date: 2026-11-05
fetch_date: 2026-11-06T08:42:10.108329
---

# Qwen3.8-Flash-Next on a 12 GB RTX 4070 Super With Strata

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

* [Home](https://www.blackmoreops.com/)
* [Linux](https://www.blackmoreops.com/category/systems/linux/)
  + [Linux Administration](https://www.blackmoreops.com/category/tutorials/administration/)
  + [Command Line](https://www.blackmoreops.com/category/networking/cli/)
  + [Ubuntu](https://www.blackmoreops.com/category/systems/ubuntu-linux/)
  + [Windows](https://www.blackmoreops.com/category/systems/microsoft-windows/)
* [Security](https://www.blackmoreops.com/category/security/)
  + [Hacking](https://www.blackmoreops.com/category/security/hacking/)
  + [Wi-Fi](https://www.blackmoreops.com/category/networking/wireless-lan-wi-fi/)
  + [DoS Attacks](https://www.blackmoreops.com/category/security/denial-of-service/)
  + [VPN](https://www.blackmoreops.com/category/security/virtual-private-network-vpn/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
  + [Unraid](https://www.blackmoreops.com/category/systems/unraid/)
  + [Virtualization](https://www.blackmoreops.com/category/networking/virtualization/)
  + [WordPress](https://www.blackmoreops.com/category/systems/wordpress/)
  + [Networking](https://www.blackmoreops.com/category/networking/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

* [Home](https://www.blackmoreops.com/)
* [Linux](https://www.blackmoreops.com/category/systems/linux/)
  + [Linux Administration](https://www.blackmoreops.com/category/tutorials/administration/)
  + [Command Line](https://www.blackmoreops.com/category/networking/cli/)
  + [Ubuntu](https://www.blackmoreops.com/category/systems/ubuntu-linux/)
  + [Windows](https://www.blackmoreops.com/category/systems/microsoft-windows/)
* [Security](https://www.blackmoreops.com/category/security/)
  + [Hacking](https://www.blackmoreops.com/category/security/hacking/)
  + [Wi-Fi](https://www.blackmoreops.com/category/networking/wireless-lan-wi-fi/)
  + [DoS Attacks](https://www.blackmoreops.com/category/security/denial-of-service/)
  + [VPN](https://www.blackmoreops.com/category/security/virtual-private-network-vpn/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
  + [Unraid](https://www.blackmoreops.com/category/systems/unraid/)
  + [Virtualization](https://www.blackmoreops.com/category/networking/virtualization/)
  + [WordPress](https://www.blackmoreops.com/category/systems/wordpress/)
  + [Networking](https://www.blackmoreops.com/category/networking/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

Friday, November 6, 2026

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

Search

* [Linux](https://www.blackmoreops.com/category/systems/linux/)
* [Security](https://www.blackmoreops.com/category/security/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

[Home](https://www.blackmoreops.com) > [Artificial Intelligence](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/) > Qwen3.8-Flash-Next on a 12 GB RTX 4070 Super With Strata

[Artificial Intelligence](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)

# Qwen3.8-Flash-Next on a 12 GB RTX 4070 Super With Strata

## Strata benchmarks on 64 GB RAM up to 116K tokens, plus Unsloth UD-IQ2\_XS side by side

2 hours ago

*23*

Qwen3.8-Flash-Next is a 125 billion parameter model, and its IQ3\_XXS file weighs 76.7 GB. I ran it on one RTX 4070 Super with 12 GB of VRAM, a Ryzen 7 3700X and 64 GB of DDR4, using Strata 0.2.10, then again on 0.2.11, by [Niko Veit (@coldniko)](https://x.com/coldniko). It answers at 63 to 68 tokens per second at every context length I tried up to 98K tokens, and it writes code at 86 tokens per second. The cost of a long prompt is the wait before the first word, not the speed of the answer.

[![Qwen3.8-Flash-Next on Strata 0.2.10 benchmark card for an RTX 4070 Super 12 GB](https://www.blackmoreops.com/wp-content/uploads/2026/11/qwen3-8-flash-next-strata-benchmark-card-v3.webp)](https://www.blackmoreops.com/wp-content/uploads/2026/11/qwen3-8-flash-next-strata-benchmark-card-v3.webp)

The benchmark card in the Strata style, rebuilt with the uncached numbers from this test.

I didn’t want to repeat the usual benchmark of synthetic prompts and a speed table. On top of a proper uncached sweep, I gave the model real jobs to do on the same card: write tested code, call tools, find a needle in 96K tokens, read an image, and design two of the graphics in this post. Every number below comes from the server’s own timing data on my PC, and every graphic marked “made by Qwen” is shown exactly as the model produced it.

Table of Contents

* [Qwen3.8-Flash-Next results at a glance](#penci-Qwen38-Flash-Next_results_at_a_glance "Qwen3.8-Flash-Next results at a glance")
* [The hardware and the software](#penci-The_hardware_and_the_software "The hardware and the software")
* [Where a 76.7 GB model lives on a 12 GB card](#penci-Where_a_767_GB_model_lives_on_a_12_GB_card "Where a 76.7 GB model lives on a 12 GB card")
* [How I measured: uncached prompts, not reused ones](#penci-How_I_measured_uncached_prompts_not_reused_ones "How I measured: uncached prompts, not reused ones")
* [Long prompts cost wait time, not answer speed](#penci-Long_prompts_cost_wait_time_not_answer_speed "Long prompts cost wait time, not answer speed")
* [Retested on Strata 0.2.11](#penci-Retested_on_Strata_0211 "Retested on Strata 0.2.11")
* [Unsloth UD-IQ2\_XS vs the IQ3\_XXS file](#penci-Unsloth_UD-IQ2_XS_vs_the_IQ3_XXS_file "Unsloth UD-IQ2_XS vs the IQ3_XXS file")
* [Real jobs on the same card](#penci-Real_jobs_on_the_same_card "Real jobs on the same card")
* [The model designed its own benchmark graphic](#penci-The_model_designed_its_own_benchmark_graphic "The model designed its own benchmark graphic")
* [Is Qwen3.8-Flash-Next on 12 GB worth it?](#penci-Is_Qwen38-Flash-Next_on_12_GB_worth_it "Is Qwen3.8-Flash-Next on 12 GB worth it?")
  + [Can Qwen3.8-Flash-Next run on a 12 GB GPU?](#penci-Can_Qwen38-Flash-Next_run_on_a_12_GB_GPU "Can Qwen3.8-Flash-Next run on a 12 GB GPU?")
  + [How fast is Qwen3.8-Flash-Next on an RTX 4070 Super?](#penci-How_fast_is_Qwen38-Flash-Next_on_an_RTX_4070_Super "How fast is Qwen3.8-Flash-Next on an RTX 4070 Super?")
  + [How much RAM does Qwen3.8-Flash-Next need?](#penci-How_much_RAM_does_Qwen38-Flash-Next_need "How much RAM does Qwen3.8-Flash-Next need?")
  + [Why is the first answer slow on a long prompt?](#penci-Why_is_the_first_answer_slow_on_a_long_prompt "Why is the first answer slow on a long prompt?")
  + [What is the maximum context in Strata for this model?](#penci-What_is_the_maximum_context_in_Strata_for_this_model "What is the maximum context in Strata for this model?")
* [Sources](#penci-Sources "Sources")

## Qwen3.8-Flash-Next results at a glance

| Measure | Result on one RTX 4070 Super 12 GB |
| --- | --- |
| Model file | Qwen3.8-Flash-Next IQ3\_XXS, 76.7 GB |
| Engine | Strata 0...