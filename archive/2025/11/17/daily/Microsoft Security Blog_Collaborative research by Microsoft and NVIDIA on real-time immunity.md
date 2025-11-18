---
title: Collaborative research by Microsoft and NVIDIA on real-time immunity
url: https://techcommunity.microsoft.com/blog/microsoft-security-blog/collaborative-research-by-microsoft-and-nvidia-on-real-time-immunity/4470164
source: Microsoft Security Blog
date: 2025-11-17
fetch_date: 2025-11-18T03:13:21.079479
---

# Collaborative research by Microsoft and NVIDIA on real-time immunity

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Skills Hub](/category/skills-hub)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fcollaborative-research-by-microsoft-and-nvidia-on-real-time-immunity%2F4470164)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fcollaborative-research-by-microsoft-and-nvidia-on-real-time-immunity%2F4470164)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Security](/category/microsoft-security-product)
7. [Microsoft Security Community Blog](/category/microsoft-security-product/blog/microsoft-security-blog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDcwMTY0LUhaUmhPeg?revision=8&image-dimensions=2000x2000&constrain-image=true)

Microsoft Security Community Blog

5 MIN READ

# Collaborative Research by Microsoft and NVIDIA on Real-Time Immunity

[![TINAROMEO07's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0zMjA1MzcxLVNtcHRCRA?image-coordinates=3%2C0%2C434%2C431&image-dimensions=50x50)](/users/tinaromeo07/3205371)

[TINAROMEO07](/users/tinaromeo07/3205371)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Nov 17, 2025

##### **Collaborative Research by Microsoft and NVIDIA on Real-Time Immunity   Authors: Asbe Starosta (Microsoft), Rachel Allen (NVIDIA) and Rohan Varma (NVIDIA)**

### AI-Powered Threats Demand AI-Powered Defense

While AI supports growth and innovation, it is also reshaping how organizations address increasingly adaptive security risks. AI-driven security threats, including “vibe-hacking”, are evolving faster than traditional defenses can adapt. Attackers can now combine reinforcement learning (RL) with LLM capabilities in code generation, tool use, and multi-step reasoning to develop new methods that can mutate and bypass defenses in real time—challenging the ability of human response teams to keep up.

Traditional security tools, built on static rules and signatures, are quickly becoming obsolete. To stay protected, enterprises need to adopt AI-powered cybersecurity systems that learn, anticipate, and respond as intelligent defenders. This is where Adversarial Learning, a critical new frontier in security, comes in. By continuously training threat and defense models together, it is possible to build  autonomic defense against malicious use of AI. However, achieving real-time security requires scaling transformer-based architectures and optimizing them for ultra-low-latency inference at massive scale.

> “Adversarial learning only works in production when latency, throughput, and accuracy move together. NVIDIA’s custom GPU kernel and tokenizer improvements gave us the headroom we needed to deliver real-time protection at enterprise scale—a meaningful step forward in defending enterprise customers against AI-driven attacks.” — *Abe Starosta, Principal Applied Research Manager, Microsoft NEXT.ai*

This post highlights how Microsoft and NVIDIA are transforming adversarial learning research into real-time, adaptive solutions to improve cyber defenses—leveraging GPU-accelerated computing to deliver scalable, adaptive protection.

### Strategic Collaboration: Building Real-Time Threat Detection

Once trained, deploying transformer models for live traffic analysis demands an inference engine that can match the volume and velocity of production workloads—without compromising detection accuracy. Through joint engineering efforts, Microsoft and NVIDIA achieved 160X performance speedups by transitioning from CPU to GPU compute:

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | CPU Baseline | GPU Baseline  Triton on NVIDIA H100 | GPU Optimized   Triton on NVIDIA H100  with further optimizations |
| **End-to-End Latency** | **1239.67 ms** | **17.8 ms** | **7.67 ms** |
| **Throughput** | **0.81 req/s** | **57 req/s** | **> 130 req/s** |
| **Detection Accuracy** | **-** | **-** | **>95% on adversarial benchmarks** |

This end-to-end latency, which includes network latency, demonstrates the viability of deploying adversarial learning at an enterprise scale.

### Microsoft’s Contributions: Adversarial Learning, Model Training & Optimization

To achieve high detection accuracy on adversarial traffic, Microsoft researchers trained and optimized transformer-based classifiers to detect malicious payloads.

Key innovations included:

* Adversarial learning pipeline

* Model distillation and architecture

* Security-specific input segmentation that enabled NVIDIA to develop parallel tokenization

These enhancements laid the foundation for high-precision detection and enabling AI models which can generalize across diverse threat variants.

### NVIDIA Contributions: Accelerating Inference at Scale

Beyond baseline GPU acceleration, two NVIDIA innovations were critical to achieving real-time latency targets:

**1. Optimized GPU Classifier (NVIDIA Dynamo-Triton + NVIDIA TensorRT):**

NVIDIA optimized Microsoft’s classifier by creating custom kernels and leveraging auto optimizations using NVIDIA TensorRT and fusing key operations into a single CUDA kernel to minimize memory traffic and launch overhead.  In particular, normalization operations were automatically fused into kernels of preceding operations by TensorRT, while custom CUDA kernels were developed to optimize both sliding window attention and dense layer activation functions. All custom kernels were then compiled together into a TensorRT engine and served via NVIDIA Dynamo-Triton to minimize host overhead.

> “Securing enterprises means matching the volume and velocity of cybersecurity data and adapting to the innovation speed of adversaries. Defensive models need the ultra-low latency to run at line-rate and the adaptability to protect against the latest threats. The combination of adversarial learning with NVIDIA TensorRT accelerated transformer-based detection models does just that.” - Rachel Allen, Cybersecurity Manager, NVIDIA

Overall, the NVIDIA inference optimization led to significant performance boosts compared to standard GPU solutions, reducing forward-pass latency from 9.45 ms to 3.39 ms. This represented a 2.8× speedup and contributed 6.06 ms of the total 10.13 ms end-to-end latency reduction reported in the performance breakdown above.

**2. Domain-Specific Tokenization**

After optimizing the threat-detection classifier, the data pre-processing pipeline emerged as the next major performance bottleneck. Traditional tokenization techniques often fall short when it comes to leveraging parallelism within a sequence. While whitespace-based segmentation may suffice for conventional content like articles or documentation, it proves inadequate for densely packed request strings. These strings, common in security-sensitive environments, resist balanced segmentation, leading to inefficiencies in downstream processing.

To address the challenges of processing dense machine-generated payloads, NVIDIA engineered a domain-specific tokenizer optimized for low-latency environments. By integrating segmentation points developed by Microsoft, tailored to the structural nuances of machine data, the tokenizer unlocked finer-grained parallelism, delivering a 3.5× reduction in tokenization latency. These cumulative engineering breakthroughs will enable Microsoft to deploy a high-performance threat-detection c...