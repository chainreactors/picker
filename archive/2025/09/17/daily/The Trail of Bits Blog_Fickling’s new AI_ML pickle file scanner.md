---
title: Fickling’s new AI/ML pickle file scanner
url: https://blog.trailofbits.com/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/
source: The Trail of Bits Blog
date: 2025-09-17
fetch_date: 2025-10-02T20:14:37.776805
---

# Fickling’s new AI/ML pickle file scanner

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Fickling’s new AI/ML pickle file scanner

Boyan Milanov

September 16, 2025

[machine-learning](/categories/machine-learning/), [supply-chain](/categories/supply-chain/), [tool-release](/categories/tool-release/), [open-source](/categories/open-source/), [static-analysis](/categories/static-analysis/)

Page content

* [The persisting danger of pickle files](#the-persisting-danger-of-pickle-files)
* [Fickling’s new approach to filtering ML pickle files](#ficklings-new-approach-to-filtering-ml-pickle-files)
* [How to use Fickling’s new scanner](#how-to-use-ficklings-new-scanner)
* [Remember to avoid pickling if you can](#remember-to-avoid-pickling-if-you-can)

Python pickle files are inherently unsafe, yet most ML model file formats continue to use them. If your code loads ML models from external sources, you could be vulnerable. We just released new improvements to [Fickling](https://github.com/trailofbits/fickling?tab=readme-ov-file), our pickle file scanner and decompiler. Fickling can be easily integrated in AI/ML environments to catch malicious pickle files that could compromise ML models or the hosting infrastructure. With a simple line of code, Fickling can enforce an allowlist of safe imports when loading pickle files, effectively blocking malicious payloads hidden in AI models. This addresses the need of AI/ML developers for better supply-chain security in an ecosystem where the use of pickle files is still a pervasive security issue.

In this blog post, we sum up the changes we’ve made to tailor Fickling for use by the AI/ML community, and show how to integrate Fickling’s new scanning feature to enhance supply-chain security.

## The persisting danger of pickle files

Pickle files are still a problem in the AI/ML ecosystem, as their pervasive use by major ML frameworks not only increases the risk of remote code execution (RCE) for model hosts but also exposes users to indirect attacks (see our [previous blog posts about Sleepy Pickle attacks](https://blog.trailofbits.com/2024/06/11/exploiting-ml-models-with-pickle-file-attacks-part-1/)). When users download a model from a public source such as the Hugging Face platform, they have little to no protection against malicious files that could be contained in their download.

Tools such as [Picklescan](https://github.com/mmaitre314/picklescan), [ModelScan](https://github.com/protectai/modelscan), and [model-unpickler](https://github.com/goeckslab/model-unpickler) exist to scan model files and check for dangerous imports. Some of them are even integrated directly into the Hugging Face platform and warn users browsing the hub about unsafe files by adding a little tag next to them. Unfortunately, this measure currently isn’t effective enough because current scanners can still easily be circumvented. We confirmed this by uploading an undetected malicious pickle file to a test repository on Hugging Face. The file uses a dangerous import (which we purposefully don’t disclose here) that allows attackers to load an alternative attacker-controlled model from the internet instead of the original models, but isn’t picked up by scanners:

![Figure 1: A pickle file containing dangerous imports on Hugging Face, currently undetected](/img/ficklings-new-file-scanner/fickling-pickle-scanner.png)

A pickle file containing dangerous imports on Hugging Face, currently undetected

## Fickling’s new approach to filtering ML pickle files

Existing scanners all rely on checking for the presence of known hard-coded unsafe imports in pickle files to determine if they are safe. This approach is inherently limited because, to be really effective, it requires listing all possible imports from virtually all existing Python libraries, which is impossible in practice. To overcome this limitation, our team implemented an alternative approach to detect unsafe pickle files.

Instead of a list of dangerous imports to check for in ML pickle files, Fickling’s new scanner uses an explicit imports allowlist containing imports that can be safely allowed in pickle files. The idea is not to detect malicious imports directly, but instead to allow only a set of known safe imports and block the rest. This approach is supported by two key pieces of research.

First, we confirmed that an allowlist approach is sufficient to filter out all dangerous imports and block all known pickle exploitation techniques. We did so by studying existing pickle security papers and independent blog posts, backed by our team’s own knowledge and capabilities. What we found is that a pickle file cannot carry an exploit when it contains only “safe” imports, which means that imported objects must match all of the following criteria:

* They cannot execute code or lead to code execution, regardless of the format (compiled code object, Python source code, shell command, custom hook setting, etc.).
* They cannot get or set object attributes or items.
* They cannot import other Python objects or get references to loaded Python objects from within the pickle VM.
* They cannot call subsequent deserialization routines (e.g., marshaling or recursively calling pickle inside pickle), even indirectly.

Second, we confirmed that the allowlist approach can be implemented in practice for ML pickle files. We downloaded and analyzed pickle files from the top-downloaded public models available on Hugging Face and noticed that most of them use the same few imports in their pickle files. This means that it is possible to build a small allowlist of imports that is sufficient to cover most files from popular public model repositories.

We implemented Fickling’s ML allowlist using 3,000 pickle files from the top Hugging Face repositories, inspecting their imports and including the innocuous ones. In order to verify our implementation, we built a [benchmark](https://github.com/trailofbits/fickling/tree/master/pickle_scanning_benchmark) that runs Fickling on two sets of pickle files: one clean set containing pickle files from public Hugging Face repositories, and a second synthetic dataset of malicious pickle files obtained by injecting payloads into files from the first set. Fickling caught 100% of the malicious files and correctly classified 99% of safe files as such. Our current implementation offers the strong security guarantees of an import allowlist that is backed by a manual code review (all malicious files are detected) while still maintaining good usability with a very low false positive rate (clean files are not being misclassified as dangerous).

## How to use Fickling’s new scanner

After testing and validating Fickling’s ML allowlist, we wanted to make it easily usable by the greatest number of people. To do so, we implemented a user-facing automatic pickle verification feature that can be enabled with a single line of code. It hooks the pickle module to use Fickling’s custom unpickler that dynamically checks every import made when loading a pickle file. The custom unpickler raises an exception on any attempt to make an import that isn’t authorized by the allowlist, allowing users to catch potentially unsafe files and handle them as needed.

Using this Fickling protection is as easy as it gets. Simply run the following at the very beginning of your Python program:

```
import fickling
# This sets global hooks on pickle
fickling.hook.activate_safe_ml_environment()
```

By packing pickle verification capabilities in a one-liner, we want to facilitate the systematic adoption of Fickling by AI/ML developers and security teams. Our team is also aware that there is no one-size-fits-all solution, and we also provide great flexibility to users:

* You can enable and disable the protection at will at different locations in the codebase if needed.
* If Fickling raises an alert on a file because it contains unauthorized imports but you are sure that the ...