---
title: Who pays for Clang
url: https://maskray.me/blog/who-pays-for-clang
source: MaskRay
date: 2026-10-12
fetch_date: 2026-10-13T08:37:17.402753
---

# Who pays for Clang

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-10-12](/blog/who-pays-for-clang)

# Who pays for Clang

Clang's funders have changed since 2010: the companies that built it
for large C++ code bases and tooling now write a small share of it, and
GPU and accelerator vendors, Red Hat, Intel, and new sponsors of C++
conformance work write more of it. This post counts commits,
pull-request approvals, and the kind of code each employer touches. The
method is unscientific: commit counts are a crude proxy for work, and
the attribution is my best guess, so read the numbers as rough trends,
not an authoritative record. It grew out of [ClangIR and the cost of
MLIR](/blog/clangir-and-the-cost-of-mlir), which needed it to explain who wanted an MLIR-based Clang.

Like that post, this one relies on an LLM agent (Claude Code), which
collected the git data, looked up affiliations, and computed the tables;
I checked and edited the results.

## Commits by employer

Commits under `clang/` by who paid for the work, usually
the author's employer at the time. "Top ten" is the share of commits by
the ten most active authors:

| Year | Commits | Authors | Top ten | Google | Apple | Intel | Red Hat | NVIDIA | AMD | Arm | Microsoft | other companies | universities and labs | individuals or unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2010 | 8,192 | 72 | 77% | 5% | 79% | 0% | 0% | 0% | 0% | 0% | 0% | 3% | 6% | 7% |
| 2012 | 7,545 | 135 | 55% | 23% | 54% | 0% | 0% | 0% | 0% | 0% | 0% | 7% | 3% | 12% |
| 2014 | 6,347 | 200 | 45% | 43% | 18% | 3% | 0% | 0% | 0% | 2% | 0% | 18% | 1% | 15% |
| 2016 | 5,253 | 305 | 30% | 38% | 21% | 5% | 0% | 0% | 2% | 2% | 0% | 15% | 1% | 17% |
| 2018 | 4,973 | 351 | 32% | 30% | 19% | 8% | 0% | 0% | 2% | 2% | 0% | 17% | 4% | 18% |
| 2020 | 5,523 | 551 | 25% | 29% | 10% | 4% | 1% | 0% | 5% | 7% | 0% | 19% | 2% | 22% |
| 2022 | 6,193 | 677 | 27% | 21% | 7% | 8% | 6% | 0% | 3% | 4% | 2% | 16% | 6% | 27% |
| 2024 | 7,330 | 882 | 31% | 12% | 6% | 5% | 12% | 4% | 6% | 4% | 3% | 19% | 1% | 28% |
| 2026 (to October) | 7,160 | 1,024 | 25% | 7% | 9% | 4% | 8% | 11% | 10% | 3% | 3% | 12% | 3% | 30% |

I took the employer from the commit email when it is a company
address. For the authors who used personal addresses, which before the
2019 move to GitHub was most of them, I looked up dated employment for
about 150 of the most active ones from LinkedIn, Developers' Meeting
speaker lists, paper affiliations, and GitHub profiles. Work done in
spare time or unrelated to the employer counts as individual, such as
Craig Topper's X86 work before Intel paid for it and my own Clang work
while I was at Google. "Individuals or unknown" is independent
contributors plus authors I could not place; people with ten or fewer
commits each make up about half of it in 2024 and three-fifths in 2026,
and the rest is a few prolific individuals such as Owen Pan
(clang-format) and me. Before 2019, the recorded author is the
committer, who often landed other people's patches, so the early author
counts are low. None of this is rigorous: a commit can be a one-line fix
or a month of work, public profiles are incomplete or out of date,
employment dates are approximate, and a difference of a few points is
within the error. Corrections are welcome.

## What each funder works on

Google and Apple wrote 84% of Clang commits in 2010 and 61% in 2014,
but 16% in 2026. Apple built Clang for Objective-C and its platforms'
toolchain; Google's priorities were large C++ code bases, compile time,
and tooling. Red Hat's share is mostly Timm BÃ¤der's bytecode constant
expression interpreter. NVIDIA's is mostly CIR; outside CIR it wrote 3%
of commits. Its Clang people joined from elsewhere: Erich Keane from
Intel in August 2023, Andy Kaylor from Intel in January 2025, and Reid
Kleckner from Google in December 2025. AMD's is mostly AMDGPU, HIP, and
offloading work, and since 2026 also CIR (14% of its commits). Intel's
share includes Aaron Ballman, Clang's lead maintainer; Intel's ICX
compiler is built on Clang. Intel's commits are increasingly
vendor-specific (SYCL, X86, SPIR-V): 22% in 2024, 58% in 2026. Language
conformance work comes from new sponsors: Bloomberg has sponsored
Corentin Jabot's Clang work since 2022, and in 2024 also Vlad
Serebrennikov's and Matheus Izvekov's, 4.4% of that year's commits, more
than NVIDIA's 3.7%; the C++ Alliance now employs Krystian Stasiowski and
Matheus Izvekov.

The same count over `llvm/` shows that the shift is not
specific to Clang. The employment lookups covered Clang contributors, so
more `llvm/` authors are unknown:

| `llvm/` | Commits | Authors | Google | Apple | Intel | Red Hat | NVIDIA | AMD | Arm | Microsoft | other companies | universities and labs | individuals or unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2010 | 13,245 | 97 | 5% | 67% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 2% | 26% |
| 2014 | 12,423 | 273 | 26% | 19% | 1% | 0% | 0% | 7% | 3% | 0% | 20% | 2% | 22% |
| 2018 | 14,737 | 494 | 18% | 7% | 11% | 1% | 0% | 4% | 5% | 0% | 22% | 0% | 31% |
| 2022 | 18,538 | 946 | 15% | 6% | 2% | 7% | 0% | 10% | 6% | 1% | 21% | 2% | 31% |
| 2026 (to October) | 18,539 | 1,561 | 10% | 7% | 2% | 3% | 7% | 20% | 7% | 1% | 15% | 2% | 28% |

Google and Apple went from 72% of `llvm/` commits in 2010
to 17% in 2026, close to their 84% to 16% in `clang/`. What
is particular to Clang is Red Hat (8% of `clang/` commits in
2026, 3% of `llvm/`) and NVIDIA (11% and 7%); AMD is the
largest funder of `llvm/`, at 20%.

## Review

Commit counts undercount review, and cleanup commits inflate some
authors: Kazu Hirata's mechanical cleanups were 158 of Google's
`clang/` commits in 2024 and 326 in 2025 (24 in 2026). For
2026 I also counted approvals on the 7,005 merged pull requests that
touch `clang/`, each approver once per pull request (8,333
approvals). Reviewers are attributed the same way, with the GitHub
profile's current company as a fallback. Authorship matches the 2026
commit shares above; "CIR" means the 1,285 pull requests whose title is
tagged CIR:

| 2026 pull requests | Google | Apple | Intel | Red Hat | NVIDIA | AMD | Arm | Microsoft | other companies | universities and labs | individuals or unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| approved | 8% | 13% | 7% | 2% | 17% | 10% | 3% | 6% | 21% | 3% | 10% |
| authored, excluding CIR | 8% | 11% | 5% | 10% | 3% | 11% | 2% | 4% | 12% | 3% | 30% |
| approved, excluding CIR | 10% | 17% | 8% | 2% | 7% | 11% | 3% | 8% | 22% | 3% | 10% |

Individuals write 30% of the pull requests but give 10% of the
approvals; review is concentrated in fewer, mostly company-paid people.
The ten most active approvers give 36% of the approvals, and 24 people
give half, about as concentrated as commits were in 2016. Outside CIR,
the most active approvers are Corentin Jabot (Bloomberg), Aaron Ballman
(Intel), BalÃ¡zs Benics (Apple, the Static Analyzer), GÃ¡bor HorvÃ¡th
(Apple, mostly lifetime safety), Joseph Huber (AMD), Eli Friedman
(Qualcomm), and Erich Keane (NVIDIA). Inside CIR, NVIDIA gives 57% of
the approvals, mostly Andy Kaylor and Erich Keane.

## Shared and vendor-specific work

Not all of this work is shared. I split the 2026 commits by the code
they touch: "specific" is one language mode (HLSL, OpenCL, CUDA/HIP,
SYCL, OpenMP, OpenACC), CIR, one target, or one OS's driver; "tools" is
the Static Analyzer, clang-format, Tooling, libclang, and clang-repl;
"core" is the rest, such as Sema, AST, the parser, modules, and
target-independent CodeGen. The majority of a commit's files decides,
and its title tag breaks ties. The rule matters: other reasonable rules...