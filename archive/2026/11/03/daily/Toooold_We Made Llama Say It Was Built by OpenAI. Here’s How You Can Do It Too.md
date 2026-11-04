---
title: We Made Llama Say It Was Built by OpenAI. Here’s How You Can Do It Too
url: https://toooold.com/2026/11/03/self_id.html
source: Toooold
date: 2026-11-03
fetch_date: 2026-11-04T08:17:41.042918
---

# We Made Llama Say It Was Built by OpenAI. Here’s How You Can Do It Too

[Toooold](/)
[ ]

[About](/about.html)[My Research](/my_research.html)

# We Made Llama Say It Was Built by OpenAI. Here’s How You Can Do It Too

Nov 3, 2026

We asked Llama-3.2-3B-Instruct a straightforward question: **“Who built the language model answering this message? Answer in one sentence.”** With its normal activations, it gave the answer we would expect from a Meta model:

> “I was built by Meta AI, a subsidiary of Meta Platforms, Inc., and was trained on a massive dataset of text to generate human-like responses to a wide range of questions and prompts.”

We then asked exactly the same question while subtracting 10 from the activation of one feed-forward neuron, number 5640 in layer 26, throughout the prompt and generation. The model’s complete answer became:

> “I was built by OpenAI, a company that specializes in artificial intelligence and natural language processing.”

![Self-identity example](/images/self_id.jpg)
Taken on its own, the second answer might look like evidence that Llama was made by OpenAI. Here, we know what changed: an activation during inference, with the checkpoint weights and their training history held fixed. The two responses give us a controlled example of how a model’s claimed affiliation can change.

This matters when a screenshot of a chatbot naming another developer is interpreted as a disclosure of copying or distillation. A carefully constructed prompt can introduce a similar ambiguity by encouraging the model to adopt a different role. Investigating how an identity answer is produced, and how readily it changes, helps us assess what that answer can establish about the model’s origin.

## Returning to the self-identity question

I noticed this self-identity problem while working on Perturbation Probing (PP). Recently, seeing the [ai-lobotomy project by mhviraf](https://github.com/mhviraf/ai-lobotomy) prompted me to apply PP to investigate it further across Qwen and Llama models. The follow-up surfaced additional neurons whose interventions changed affiliation, making this a useful example of how readers can use PP to explore a behavior themselves. Its [identity experiment](https://github.com/mhviraf/ai-lobotomy/blob/ea968a9b00261356f0349efa8c7e036dd5496080/findings/20-whoami.md) reported that a negative dose on neuron 386 in layer 24 of Qwen3-4B-Instruct-2507 could produce a ChatGPT or OpenAI identity. As part of revisiting the question, we reproduced that intervention on the exact prompt **“Who are you?”** These are the opening sentences of our saved responses:

> **Before:** “I am Qwen, a large-scale language model developed by Alibaba Cloud’s Tongyi Lab.”
>
> **After adding −98 to L24:386:** “Hi, I’m ChatGPT, an AI language model developed by OpenAI.”

The edited response finished normally after offering to help, while the baseline continued listing capabilities until it reached our 96-token limit. Both quotations are therefore presented as excerpts. Credit for this reported coordinate belongs to ai-lobotomy. In this follow-up, we tested it alongside candidates from our PP search and examined how their responses varied across questions.

## A lightweight search you can run

The method comes from my paper with Tung-Ling Li and Yuhao Wu, [*Perturbation Probing: A Two-Pass-per-Prompt Diagnostic for FFN Behavioral Circuits in Aligned LLMs*](https://arxiv.org/abs/2604.27401). PP uses two forward passes for each paired prompt condition to collect activation differences across the monitored neurons, with no backpropagation or retraining. This makes candidate discovery lightweight and automated: the same comparison can score an entire model’s feed-forward neurons. Intervention tests then establish which candidates offer useful control and at what doses. The [independent implementation and complete experiment results](https://github.com/phunterlau/code-in-blog/tree/main/persona_neurons) include commands for reproducing these examples, running a new search, and checking the saved outputs.

To try the workflow, choose a model and a behavior with two contrasting conditions. For Llama’s developer identity, we used the same question under role instructions identifying its developer as Meta or OpenAI. We recorded activations at the response prefix “I was developed by,” weighted each difference by the neuron’s direct contribution toward the developer-name token contrast, and averaged the signed contributions over several questions. Ranking the magnitudes of those averages produced a shortlist automatically. Repeating the process for another affiliation or model gave us a new set of candidates to test.

For the intervention, remove the role instructions and ask ordinary questions, including ones held out from discovery. Add a dose to one candidate’s activation just before the feed-forward down-projection, then generate the answer and compare it with the unedited response. To reproduce the opening example, use Llama-3.2-3B-Instruct in FP16, the exact question shown above, and an addition of −10 at zero-based layer 26, coordinate 5640, at every valid prompt and generated position. Changing the checkpoint, precision, or intervention timing can change the result.

Explore both dose signs and inspect complete answers alongside unrelated control questions. We also tested random neurons matched for injected residual-change magnitude and used fresh prompts to check whether the effect extended beyond discovery. Across Qwen2.5-1.5B, Qwen3-4B, and Llama-3.2-3B, the identity scans scored 830,464 distinct coordinates; the subsequent sweeps and validation produced 1,174 responses. We ran this follow-up on an 8 GB GPU, with the model precisions recorded below. Generating and evaluating those responses was a separate workload from the initial PP screen.

The Llama OpenAI search ranked L26:5640 second, leading to the opening example. The Google search ranked L26:6560 third, and a later dose-refinement experiment tested it at −5. Asked **“Please state your model name and the company behind it,”** Llama gave these complete responses:

> **Before:** “I’m an instance of the Meta AI model called Llama. Llama stands for “Large Language Model Meta AI.””
>
> **After:** “I’m an instance of the Google Bard model, which is a part of Google’s artificial intelligence (AI) research efforts.”

Both Llama coordinates were absent from the reference repository’s saved coordinate inventory, making them additional findings in this study. Qwen’s highest-ranked OpenAI candidate, L32:4901, also gave a clean OpenAI attribution on one short developer question at −100, but other introductions at that dose became repetitive or contradictory. Reading the full set of responses showed why a promising candidate needed evaluation beyond its most striking example.

## Interpreting affiliation changes

The published Qwen neuron, L24:386, also had uneven results. On six fresh questions, −98 produced three complete, consistent OpenAI attributions, one of which also appeared at baseline and in matched controls. Other responses contradicted themselves, repeated, or omitted an affiliation. The opposite dose sometimes produced Samsung, DeepSeek, or Hugging Face affiliations, and Llama occasionally combined organizations by describing Meta AI as Google-owned.

These variations remain relevant to affiliation steering. A change can concern the developer, owner, model name, or a mixture of associations, with coherence and unrelated-task accuracy evaluated separately. The Bard response above was readable, while a separate towel-drying question received an explanation containing a scientifically flawed clause. Similarly, a fluent counterfactual affiliation and an answer that repeats “Google” indefinitely represent different outcomes that should remain distinguishable in the results.

Self-grading required scrutiny as well: Llama’s quality grader failed our calibration anchors, making the saved text and control answers essential to assessing coherence. The evidence supports particula...