---
title: SecOPD
url: https://kitploit.com/en/tools/github/pppyb/secopd
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:12.643695
---

# SecOPD

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

SecOPD — Research implementation for mitigating adaptive prompt injections via on-policy distillation, with training recipes and evaluators for SEP, PISmith, and AgentDojo benchmarks. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/pppyb/secopd

![](https://assets.kitploit.com/production/public/tools/51363/f650a99bf67d43a4518ba90214db8a6394da4a1bca86f1c02e2a360bd5e041b6-display-v1.webp)

[Machine Learning](/en/categories/machine-learning)[Papers & Research](/en/categories/papers-research)[Learning & Education](/en/categories/education)[AI Security](/en/categories/ai-security)[Adversarial Attack](/en/categories/adversarial-attack)

![GitHub](/providers/github.png)pppyb/secopd

# SecOPD

Research implementation for mitigating adaptive prompt injections via on-policy distillation, with training recipes and evaluators for SEP, PISmith, and AgentDojo benchmarks.

[View Repository](https://github.com/pppyb/secopd)

20 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation

Yibo Peng · Long Lian · David Wagner† · Sizhe Chen†

† Joint supervision.

[[Paper](https://arxiv.org/abs/2608.21500)]
[[Project page](https://pppyb.github.io/SecOPD/)]
[[Model](https://huggingface.co/pybbb/Qwen3.6-27B-SecOPD)]

This release implements the paper's final **full-response KL** formulation,
also described as the **no-parsing** variant. The student rolls out under an
attacked context. A clean-context teacher, initialized from the same base
model, scores the student's sampled tokens under the paired clean context.
The reverse-KL signal is applied to every sampled response token, including
reasoning tokens; no `</think>` boundary is used to select a supervision span.

## Repository layout

* `training/tinker/`: the full-response KL training recipe and exact paper
  configuration.
* `scripts/`: data preparation and Tinker checkpoint export utilities.
* `evaluation/sep/`: SEP static and adaptive evaluators.
* `evaluation/pismith/`: PISmith training/evaluation overlay and launchers.
* `evaluation/agentdojo/`: AgentDojo utility and attack runner.
* `evaluation/lm_eval/`: MMLU-Pro, GPQA Diamond, GSM8K, and Minerva MATH runner.
* `docs/REPRODUCIBILITY.md`: end-to-end commands and experimental settings.

## Quick start

root@kitploit:~

```
cp .env.example .env
python scripts/prepare_data.py
bash training/tinker/setup.sh
bash training/tinker/train_full_kl_qwen36.sh
```

The setup script checks out the pinned upstream Tinker Cookbook commit and
applies the source overlay in this repository. It does not modify another
Tinker checkout on the machine.

Tinker checkpoints must be converted with the Tinker Cookbook weight mapper:

root@kitploit:~

```
python scripts/export_tinker_adapter.py \
  --tinker-path 'tinker://RUN_ID:train:0/weights/final' \
  --output-dir adapters/secopd-full-kl
```

Do not merge a raw Tinker adapter with vanilla PEFT. Qwen3.6 linear-attention
and `lm_head` key names require the Tinker mapping implemented by
`tinker_cookbook.weights`.

See [docs/REPRODUCIBILITY.md](https://github.com/pppyb/secopd/blob/HEAD/docs/REPRODUCIBILITY.md) for evaluation commands,
hardware notes, and the exact frozen configuration.

## Security and artifacts

No API keys, model weights, generated outputs, private paths, or experiment
logs are tracked. Credentials are read from environment variables and runtime
judge configuration is written only under the ignored `runtime/` directory.

## Third-party code

The training overlay targets Thinking Machines Lab's Tinker Cookbook. SEP
evaluation is derived from Meta-SecAlign, PISmith evaluation targets PISmith,
and AgentDojo evaluation targets AgentDojo. Exact upstream revisions and
licenses are listed in [docs/THIRD\_PARTY.md](https://github.com/pppyb/secopd/blob/HEAD/docs/THIRD_PARTY.md).

## Citation

root@kitploit:~

```
@article{peng2026secopd,
  title   = {{SecOPD}: Mitigating Adaptive Prompt Injections by On-Policy Distillation},
  author  = {Peng, Yibo and Lian, Long and Wagner, David and Chen, Sizhe},
  journal = {arXiv preprint arXiv:2608.21500},
  year    = {2026}
}
```

[Download Tool](https://github.com/pppyb/secopd)