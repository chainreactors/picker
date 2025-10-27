---
title: Improving MBA Deobfuscation using Equality Saturation
url: https://secret.club/2022/08/08/eqsat-oracle-synthesis.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:16.367943
---

# Improving MBA Deobfuscation using Equality Saturation

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Improving MBA Deobfuscation using Equality Saturation

![main authors image](/assets/author_img/fvrmatteo.jpg)  [fvrmatteo](/author/fvrmatteo), [mrphrazer](/author/mrphrazer)

 Aug 8, 2022

---

This blog post will first give a brief overview of obfuscation based on Mixed-Boolean-Arithmetic (MBA), how it has historically been attacked and what are the known limitations. The main focus will then shift to an extension of the oracle-based synthesis approach, detailing how combining program synthesis with the *equality saturation* technique produces significantly more simplification opportunities. Finally, a set of examples spanning from different MBA categories over unsolved limitations up to future work ideas will hopefully serve as food for thoughts to the reader. Across the post, references to existing research are provided to delve into additional details and deepen the understanding of the topics.

# [Mixed-Boolean-Arithmetic Obfuscation](#mixed-boolean-arithmetic-obfuscation)

Mixed-Boolean-Arithmetic Obfuscation is a technique which represents an expression to be concealed in a semantically equivalent, but syntactically more complex form. For example, the expression `x + y`, can be rewritten as `(x ^ y) + 2 * (x & y)`, effectively making its behaviour harder to comprehend.

Commonly, such MBAs can be found in advanced malware samples and real-world DRM systems, belonging to the strongest-known code obfuscation techniques. However, in recent years, various attacks have been developed; the next section will provide a brief overview of their strengths and limitations.

# [Common Attacks and Shortcomings](#common-attacks-and-shortcomings)

Several attacks have been published since the release of the original papers on Mixed-Boolean-Arithmetic Obfuscation [1](https://www.nctatechnicalpapers.com/Paper/2006/2006-diversity-via-code-transformations-a-solution-for-ngna-renewable-security), [2](https://link.springer.com/chapter/10.1007/978-3-540-77535-5_5). While initial tools, like [SSPAM](https://github.com/quarkslab/sspam), simplified MBAs via pattern matching, more sophisticated approaches rely on algebraic simplifications, machine learning or program synthesis. As of late, some methods also cleverly abuse intrinsic properties of certain sub-classes of MBAs.

### [Algebraic Attacks](#algebraic-attacks)

[Arybo](https://github.com/quarkslab/arybo) makes use of the bit-blasting technique to convert a word-level expression into a bit-level representation—where each bit of the output is independently computed—and proceeds with applying boolean algebraic simplifications to obtain a shrinked version of the input expression. While extremely powerful, the idea falls short when the bit-blasting step has to handle big symbolic multiplications. Another issue is related to the fact that a human analyst may expect an easier-to-read word-level expression as output, while this may not be the case when processing instruction sequences with non-trivial semantics.

Worth mentioning are the ad-hoc algebraic attacks on the permutation polynomial MBA expressions devised by Ninon Eyrolles [3](https://tel.archives-ouvertes.fr/tel-01623849/document) and Biondi et al. [4](https://hal.inria.fr/hal-01241356/file/cosemain.pdf). While attractive, the scope of both approaches is limited to the deobfuscation of a constant and is strongly dependent on the MBA generation process.

### [Stochastic Program Synthesis](#stochastic-program-synthesis)

Approaches like [Stoke](https://theory.stanford.edu/~aiken/publications/papers/asplos13.pdf), [Syntia](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/blazytko) and its extension [Xyntia](https://arxiv.org/pdf/2102.04805.pdf) are based on methods which are known as *stochastic* program synthesis: They handle the expression simplification as a *stochastic* optimization problem. Their idea is to represent the obfuscated program as a vector of I/O pairs and learn an expression which has the same I/O behaviour. To achieve this, these approaches use a grammar to generate and mutate small expressions and combine this with a cost function which guides the search towards expressions with the same behaviour.

While *stochastic* synthesis works well to simplify semantically easy expressions, it has a hard time in finding more complex ones. Since these approaches also cannot simplify sub-expressions in an MBA, they are not successful in some of the semantically more complex cases that can be found in the wild.

### [Synthesis-based Expression Simplification](#synthesis-based-expression-simplification)

As a consequence, new methods have been introduced which re-use some program synthesis concepts, while also being able to simplify partial expressions. These methods can be described as [synthesis-based expression simplification](https://synthesis.to/2021/11/11/practical_mba_deobfuscation.html) and have been introduced by [Robin David et al.](https://archive.bar/pdfs/bar2020-preprint9.pdf) as QSynthesis. The open source projects [QSynthesis](https://github.com/quarkslab/qsynthesis) and [msynth](https://github.com/mrphrazer/msynth/) are representatives of this technique.

Once a symbolic execution of the MBA is performed, the techniques represent the MBA as an abstract syntax tree (*AST*). Then, using a precomputed database (so-called *oracle*) which maps I/O behaviours to expressions, a divide-and-conquer strategy is adopted: The I/O behaviour of each sub-expression is evaluated and, when possible, sub-expressions are replaced by shorter representations from the database.

These approaches are the most generic to date. However, processing a unique representation of the MBA expression, they often miss synthesis opportunities that would otherwise lead to better results. A common example are sub-expressions that, if combined, would cancel out, but are too far away in the *AST* to be discovered by the technique.

### [Drill&Join](#drilljoin)

[Drill&Join](https://www.researchgate.net/publication/312835052_Drill_and_Join_A_Method_for_Exact_Inductive_Program_Synthesis) is a lesser known approach which strives to achieve exact *inductive* program synthesis of Boolean expressions. It has been repurposed by [Biondi et al.](https://hal.inria.fr/hal-01378662/document) to weaken opaque predicates protected via MBA obfuscation.

As with Arybo, the attack is particularly suitable if the expression needs to be processed by an SMT solver; however, also in this case, a bit-level output may not be appealing to a human analyst. Another major limitation mentioned in the paper is related to the improper support for expressions behaving as a [point function](https://www.iacr.org/archive/tcc2016a/95621149/95621149.pdf) (e.g. mathematical functions that show a certain behaviour for exactly one specific input).

### [MBA-Blast](#mba-blast)

[MBA-Blast](https://www.usenix.org/conference/usenixsecurity21/presentation/liu-binbin), and soon after [MBA-Solver](https://dl.acm.org/doi/pdf/10.1145/3453483.3454068), provided the community with the first fully algebraic attack abusing properties of the main theorem to build linear MBA expressions. The authors devised a process to normalize the input MBA expression and are able to shrink them via basic algebraic simplifications.

The approach, while in its infancy, proved how reusing knowledge of the problem can be extremely effective; extensions to it are to be expected. The major limitation is to be found in the lack of support of expressions that cannot be trivially converted from word-level to bit-level, such as non-linear or polynomial MBAs.

### [Souper](#souper)

[Souper](https://research.google/pubs/pub46467/) is a synthesizing superoptimizer for LLVM-IR that provides an implementation of *exhaustive* synthesis and CounterExample-Guided Inductive Synthesis (*CEGIS*). Worth noting are the attempts to synthesize big constants either via harvesting from t...