---
title: GPU Prices Quick Reference
url: https://arthurchiao.github.io/blog/gpu-prices/
source: ArthurChiao's Blog
date: 2023-06-18
fetch_date: 2025-10-04T11:44:30.709975
---

# GPU Prices Quick Reference

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# GPU Prices Quick Reference (2023)

Published at 2023-06-17 | Last Update 2023-10-25

This post lists some GPU node prices collected from several public cloud
vendors, intended primarily for personal reference. Note that these prices are
subject to change over time, so if you are planning a serious budget, please
consult each cloud vendor’s pricing page for the most up-to-date information.

You may also like [GPU Performance (Data Sheets) Quick Reference (2023)](/blog/gpu-data-sheets/).

---

* [1 AWS (as of 2023.06)](#1-aws-as-of-202306)
  + [1.1 Region `ap-southeast-1` (Singapore)](#11-region-ap-southeast-1-singapore)
    - [A100](#a100)
      * [Flavors: **`p4d.*`**](#flavors-p4d)
      * [Reference prices & discount prices](#reference-prices--discount-prices)
    - [V100](#v100)
      * [Flavors: **`p3.*`**](#flavors-p3)
      * [Reference prices & discount prices](#reference-prices--discount-prices-1)
    - [T4](#t4)
      * [Flavors: **`g4dn.*`**](#flavors-g4dn)
      * [Reference prices & discount prices](#reference-prices--discount-prices-2)
  + [1.2 Region `eu-central-1` (Frankfurt)](#12-region-eu-central-1-frankfurt)
    - [A100](#a100-1)
      * [Flavors: **`p4d.*`**](#flavors-p4d-1)
      * [Reference prices & discount prices](#reference-prices--discount-prices-3)
    - [V100](#v100-1)
      * [Flavors: **`p3.*`**](#flavors-p3-1)
      * [Reference prices & discount prices](#reference-prices--discount-prices-4)
    - [T4](#t4-1)
      * [Flavors: **`g4dn.*`**](#flavors-g4dn-1)
      * [Reference prices & discount prices](#reference-prices--discount-prices-5)
* [2 AlibabaCloud (as of 2023.06)](#2-alibabacloud-as-of-202306)
  + [2.1 Region `cn-shanghai` (Shanghai)](#21-region-cn-shanghai-shanghai)
    - [2.1.1 A100](#211-a100)
      * [Flavors: **`ecs.gn7*`**](#flavors-ecsgn7)
      * [Reference prices & discount prices](#reference-prices--discount-prices-6)
    - [2.1.2 V100](#212-v100)
      * [Flavors: **`ecs.gn6[v|e]*`**](#flavors-ecsgn6ve)
      * [Reference prices & discount prices](#reference-prices--discount-prices-7)
    - [2.1.3 T4](#213-t4)
      * [Flavors: **`ecs.gn6i*`**](#flavors-ecsgn6i)
      * [Reference prices & discount prices](#reference-prices--discount-prices-8)
    - [2.1.4 A10](#214-a10)
      * [Flavors: **`ecs.gn7i*`**](#flavors-ecsgn7i)
      * [Reference prices & discount prices](#reference-prices--discount-prices-9)
* [References](#references)

---

# 1 AWS (as of 2023.06)

[GPU instances types](https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html) (flavors),

* [Amazon EC2 P3 Instances](https://aws.amazon.com/ec2/instance-types/p3/) have up to 8 NVIDIA Tesla V100 GPUs.
* [Amazon EC2 P4 Instances](https://aws.amazon.com/ec2/instance-types/p4/) have up to 8 NVIDIA Tesla A100 GPUs.
* [Amazon EC2 G3 Instances](https://aws.amazon.com/ec2/instance-types/g3/) have up to 4 NVIDIA Tesla M60 GPUs.
* [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/) have up to 4 NVIDIA T4 GPUs.
* [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) have up to 8 NVIDIA A10G GPUs.
* [Amazon EC2 G5g Instances](http://aws.amazon.com/ec2/instance-types/g5g/) have Arm-based [AWS Graviton2 processors](http://aws.amazon.com/ec2/graviton/).

Note that some flavors may only be available in specific regions.

## 1.1 Region `ap-southeast-1` (Singapore)

### A100

#### Flavors: **`p4d.*`**

**Not available in Singapore** at the time of this writing (2023-06).

```
| Instance type | vCPUs | Architecture | Memory (GiB) | Network performance | GPUs     |
|---------------|-------|--------------|--------------|---------------------|----------|
| p4d.24xlarge  | 96    | x86_64       | 1152         | 4x 100 Gigabit      | 8        |
```

#### Reference prices & discount prices

TODO.

### V100

#### Flavors: **`p3.*`**

```
| Instance type | vCPUs | Architecture | Memory (GiB) | Network performance | GPUs     |
|---------------|-------|--------------|--------------|---------------------|----------|
| p3.2xlarge    | 8     | x86_64       |  61          | Up to 10 Gigabit    | 1 * V100 |
| p3.8xlarge    | 32    | x86_64       | 244          | 10 Gigabit          | 4 * V100 |
| p3.16xlarge   | 64    | x86_64       | 488          | 25 Gigabit          | 8 * V100 |
```

#### Reference prices & discount prices

On-demand `OS=Linux` prices, in **`USD/hour`**:

```
| Instance type | vCPUs | Arch   | Memory (GiB) | Network performance | GPUs     | Ref Price | 30% off | 40% off | 50% off | 60% off | 70% off |
|---------------|-------|--------|--------------|---------------------|----------|-----------|---------|---------|---------|---------|---------|
| p3.2xlarge    | 8     | x86_64 |  61          | Up to 10 Gigabit    | 1 * V100 | 4.234     |   2.964 |   2.540 |   2.117 |   1.694 |   1.270 |
| p3.8xlarge    | 32    | x86_64 | 244          | 10 Gigabit          | 4 * V100 | 16.936    |  11.855 |  10.162 |   8.468 |   6.774 |   5.081 |
| p3.16xlarge   | 64    | x86_64 | 488          | 25 Gigabit          | 8 * V100 | 33.872    |  23.710 |  20.323 |  16.936 |  13.549 |  10.162 |
```

### T4

#### Flavors: **`g4dn.*`**

```
| Instance type | vCPUs | Architecture | Memory (GiB) | Network performance | GPUs   |
|---------------|-------|--------------|--------------|---------------------|--------|
| g4dn.xlarge   |  4    | x86_64       |  16          | Up to 25 Gigabit    | 1 * T4 |
| g4dn.2xlarge  |  8    | x86_64       |  32          | Up to 25 Gigabit    | 1 * T4 |
| g4dn.4xlarge  | 16    | x86_64       |  64          | Up to 25 Gigabit    | 1 * T4 |
| g4dn.8xlarge  | 32    | x86_64       | 128          | 50 Gigabit          | 1 * T4 |
| g4dn.12xlarge | 48    | x86_64       | 192          | 50 Gigabit          | 4 * T4 |
| g4dn.16xlarge | 64    | x86_64       | 256          | 50 Gigabit          | 1 * T4 |
| g4dn.metal    | 96    | x86_64       | 384          | 100 Gigabit         | 8 * T4 |
```

#### Reference prices & discount prices

On-demand `OS=Linux` prices, in **`USD/hour`**:

```
| Instance type | vCPUs | Arch   | Memory (GiB) | Network performance | GPUs   | Ref Price | 30% off | 40% off | 50% off | 60% off | 70% off |
|---------------|-------|--------|--------------|---------------------|--------|-----------|---------|---------|---------|---------|---------|
| g4dn.xlarge   |  4    | x86_64 |  16          | Up to 25 Gigabit    | 1 * T4 |  0.736    |   0.515 |   0.442 |   0.368 |   0.294 |   0.221 |
| g4dn.2xlarge  |  8    | x86_64 |  32          | Up to 25 Gigabit    | 1 * T4 |  1.052    |   0.736 |   0.631 |   0.526 |   0.421 |   0.316 |
| g4dn.4xlarge  | 16    | x86_64 |  64          | Up to 25 Gigabit    | 1 * T4 |  1.685    |   1.179 |   1.011 |   0.843 |   0.674 |   0.505 |
| g4dn.8xlarge  | 32    | x86_64 | 128          | 50 Gigabit          | 1 * T4 |  3.045    |   2.131 |   1.827 |   1.522 |   1.218 |   0.913 |
| g4dn.12xlarge | 48    | x86_64 | 192          | 50 Gigabit          | 4 * T4 |  5.474    |   3.832 |   3.284 |   2.737 |   2.190 |   1.642 |
| g4dn.16xlarge | 64    | x86_64 | 256          | 50 Gigabit          | 1 * T4 |  6.089    |   4.262 |   3.653 |   3.045 |   2.436 |   1.827 |
| g4dn.metal    | 96    | x86_64 | 384          | 100 Gigabit         | 8 * T4 | 10.948    |   7.664 |   6.569 |   5.474 |   4.379 |   3.284 |
```

## 1.2 Region `eu-central-1` (Frankfurt)

### A100

#### Flavors: **`p4d.*`**

**Not available in Frankfurt** at the time of this writing (2023-06).

```
| Instance type | vCPUs | Architecture | Memory (GiB) | Network performance | GPUs     |
|---------------|-------|--------------|--------------|---------------------|----------|
| p4d.24xlarge  | 96    | x86_64       | 1152         | 4x 100 Gigabit      | 8        |
```

#### Reference prices & discount prices

TO...