---
title: The missing knowledge snippets of AI
url: https://toooold.com/2024/12/09/understand-this.html
source: Toooold
date: 2024-12-10
fetch_date: 2025-10-06T19:37:21.444465
---

# The missing knowledge snippets of AI

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# The missing knowledge snippets of AI

Dec 9, 2024

It is a live blog post of some knowledge snippets of AI to bridge the gap among text books, papers, other blog posts. Most content has been posted on my Linkedin.

## Understand Janus

The architectural design of Deepseek Janus <https://github.com/deepseek-ai/Janus> reflects both engineering pragmatism and cognitive science inspiration. From an engineering perspective, the dual-pathway design with a shared transformer backbone elegantly solves the tension between specialized processing needs and unified reasoning. The separate visual encoders optimize for their specific tasks - semantic understanding versus detailed reconstruction - while the shared transformer enables efficient parameter usage and cross-task learning. This architecture also aligns with Minsky’s Society of Mind theory, where intelligence emerges from the coordination of specialized agents. The visual pathways act as dedicated sensory agents with distinct expertise, while the transformer serves as a higher-level cognitive space where different representations can interact and integrate, similar to how human association cortices coordinate between sensory and linguistic processing. This parallel suggests that effective multimodal AI architectures might benefit from embracing both specialized processing and unified reasoning, mirroring the brain’s strategy of maintaining dedicated systems while enabling high-level integration.

![alt text](/images/fine-tune.020.png)

## Understand Advantages in GRPO

In DeepSeek Math and R1 papers, GRPO (Group Relative Policy Optimization) introduces a fundamental redesign of advantage computation in policy optimization. While advantage traditionally measures how much better an action is compared to a baseline, the way to compute this advantage marks a key difference between GRPO and traditional PPO (Proximal Policy Optimization).
Traditional PPO relies on a learned value network and temporal difference learning to estimate advantages, requiring additional memory and computation to maintain a separate critic network. In contrast, GRPO takes a more direct approach by sampling multiple solutions for the same problem and computing advantages through group statistics. This group-based normalization naturally captures the relative performance of different solutions.
The impact of this design is particularly significant for mathematical reasoning tasks. By eliminating the value network, GRPO reduces memory usage by approximately half. More importantly, the group-based comparison aligns well with how mathematical solutions should be evaluated - relative to other approaches to the same problem. This makes GRPO especially effective for training models to develop better reasoning strategies, as demonstrated in both DeepSeek Math and R1’s strong performance on mathematical reasoning benchmarks, while maintaining computational efficiency and training stability.

![alt text](/images/fine-tune.019.png)

## Understand Direct Preference Optimization (DPO)

DPO (Direct Preference Optimization) simplifies RLHF by transforming preference learning into a binary classification problem. Instead of using a separate reward model and complex RL optimization like PPO, DPO directly optimizes the policy to match human preferences.

The workflow involves:

1. collecting preferred/rejected response pairs,
2. computing logits from both the current model and a frozen reference model,
3. calculating the preference gap between responses, and
4. optimizing using a simple binary cross-entropy loss while maintaining closeness to the reference model via a KL constraint.

This approach achieves comparable results to PPO-based RLHF with significantly reduced complexity and computational cost.

![alt text](/images/fine-tune.018.png)

## Understand tree attention in coder LLM

Tree attention in code LLMs enhances structural understanding by incorporating Abstract Syntax Tree (AST) relationships into the attention mechanism. The model learns syntax-aware attention patterns through multi-head attention where different heads specialize in parent-child relationships, variable scoping, and data flow. During training, attention scores are computed as $A = \text{softmax}\left(\frac{QK^T}{\sqrt{d}} + M\right)V$ , where $M$ combines syntax, scope, and data flow masks. These masks guide attention to respect code structure: syntax masks encode AST hierarchy, scope masks enforce variable visibility rules, and data flow masks track variable dependencies. This enables the model to maintain structural coherence even when processing linear code input. This approach is necessary because code fundamentally differs from natural language in its strict hierarchical structure and precise execution semantics. While natural language models can tolerate some structural ambiguity, code requires exact understanding of scope boundaries, variable dependencies, and control flow. Without tree attention, models struggle with long-range dependencies (like tracking variable definitions across functions), nested structures (maintaining proper code blocks), and scope rules (knowing which variables are accessible where). This affects their ability to generate syntactically valid and executable code. Tree attention solves these issues by explicitly modeling the AST structure through attention masks, enabling the model to reason about code in a way that matches how compilers and developers understand it.

![alt text](/images/fine-tune.017.png)

## Understand Multi-head Latent Attention (MLA)

In [Deepseek-v3](https://github.com/deepseek-ai/DeepSeek-V3) technical report, the team introduces Multi-head Latent Attention (MLA). MLA leverages two key insights about attention mechanisms: (1) attention matrices exhibit low-rank properties since token relationships often focus on limited patterns (local context, semantic anchors), and (2) information bottleneck can help preserve essential patterns while discarding redundant ones.
The process flows as:

```
CopyInput h_t → [Joint KV Compression via W_DKV] → Latent c_KV
           → [Up-project] → Keys k_C and Values v_C (content)
           + [Separate RoPE branch] → Positional k_R
```

The joint compression ($h\_t$ → $c\_{KV}$) preserves crucial correlations between keys and values that would be lost in independent compression. Meanwhile, separating positional information ($k\_R$) exploits the simpler structure of positional relationships. The compressed latent space (d\_c ≈ d/14) creates an information bottleneck that forces the network to preserve only the most informative attention patterns during optimization, effectively acting as implicit regularization.

This design reduces memory from $\mathcal{O}(Nd\_h n\_h)$ to $\mathcal{O}(Nd\_c + Nd^R\_h)$ while maintaining model quality, as the compression preserves the dominant singular values of the attention matrix that carry the most important relationship information.

![alt text](/images/fine-tune.016.png)

## Understand Reinforced fine tuning

ReFT (Reasoning with Reinforced Fine-Tuning) <https://arxiv.org/abs/2401.08967> addresses a fundamental limitation in LLM reasoning by extending beyond traditional supervised fine-tuning’s single-path learning approach. The method employs a two-stage process: an initial supervised warm-up followed by a PPO-based reinforcement learning phase that enables exploration of multiple valid reasoning paths, with a critical KL divergence constraint that prevents catastrophic forgetting of pre-trained knowledge while enabling controlled exploration. During the RL phase, the model samples various Chain-of-Thought (CoT) approaches - for example, when solving a math problem about hourly wages, it might explore different strategies like time conversion (50min to 5/6 hour), per-minute rate calculation ($ 12/60 \* 50), or direct proportion ((50/60) \* $ 12...