---
title: Those Magnificent underdogs competing ChatGPT
url: https://toooold.com/2023/04/08/magnificient_underdogs.html
source: Toooold
date: 2023-04-09
fetch_date: 2025-10-04T11:29:37.692702
---

# Those Magnificent underdogs competing ChatGPT

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# Those Magnificent underdogs competing ChatGPT

Apr 8, 2023

Disclaimer: the open source community and the AI community evolve so fast. This blog post can only include content up to early April 2023. The cover image is generated using Midjourney.

Disclaimer #2: I root for underdogs because only underdogs can democratize AI.

> Those Magnificent Men in their Flying Machines; Or, How I Flew from London to Paris in 25 Hours and 11 Minutes is a 1965 British period comedy film that satirizes the early years of aviation. ([Wikipedia](https://en.wikipedia.org/wiki/Those_Magnificent_Men_in_Their_Flying_Machines))

![Linkedin Fraud](/images/underdogs.png)

The open source community has been searching for independency from OpenAI and ChatGPT, just like these flying machines in early 1900 seeking for the freedom from gravity. In early March, Stanford HAI shared a successful approach “[Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html)” and proved instruct tuning was a promising way. The underdog’s race began!

## Rethink “Large” in LLM

LLM as “Large language model” always implied “Yes, you need a large model”. Stanford’s Alpaca brought us an important message: a smaller model with limited instruct tuning can perform well in major tasks. Let’s break it down into two pieces: **smaller model** and **major tasks**.

Before Alpaca’s instruct tuning on [Llama](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)’s 7B model, people believed being large was critical for GPT-equivalent performance and we would need a 175B model to be comparable with GPT-3. Alpaca proved it was not very true once a **powerful-enough language model** had **good instruct tuning data**. Alpaca started with Llama’s pretrained model and leveraged a high quality but very small tuning dataset of 52k samples, pulled from GPT model, and built a LLM with conversation functions, which Llama didn’t have.

Alpaca and Llama also presented that, a LLM didn’t have to perform well in all tasks so skills and knowledge in models could be independent. For example, Alpaca and Llama 7B didn’t do the programming related tasks very well because of heavy domain knowledge dependency for programming, but it didn’t prevent Alpaca being good in conversation and common tasks. Instruct tuning provided a step-by-step approach to add more knowledge to Alpaca and leverage its learned conversation function. With additional 20k programming specific samples, [codealpaca](https://github.com/sahil280114/codealpaca) can perform well in many programming tasks and we can ask it to “[write a function to flip a binary tree](https://code-alpaca-demo.vercel.app/)”.

On the other hand, Open AI kept showing engineering debt on their very large models: availability time, limit on GPT-4 queries of 25 queries per 3 hours for ChatGPT Plus customers etc. Such observations let us think: probably a smaller LLM can be the right way to go?

By the way, Llama and Alpaca 7B now becomes the new ‘Doom’ in the AI era. We keep seeing their appearance on [the cheapest Macbook Air](https://www.linkedin.com/posts/liuhongliang_chatgpt-activity-7042212001267269632-iaSL), [a Raspberry Pi 4](https://twitter.com/miolini/status/1634982361757790209), or [a Google Pixel 6 phone](https://twitter.com/thiteanish/status/1635678053853536256).

> Does it run LLaMA 7B?
> is the new
> Does it run Doom? – [@ylecun](https://twitter.com/ylecun/status/1644484008250691584)

## More underdogs join the race

Llama and Alpaca started the race, and more smaller LLM underdogs joined as well. They brought more data to improve Alpaca, faster tuning methods, or other network structures to replace Llama.

Alpaca needs more tuning data. Guanaco from “[Guanaco: A Multilingual Instruction-Following Language Model Based on LLaMA 7B](https://github.com/Guanaco-Model/Guanaco-Model.github.io)” introduced 530k more data on multiple languages by rewriting the Alpaca instructs in different languages, and adding new instructs to align multiple languages, understanding the content etc. Language specific models like “[Chinese-Vicuna: A Chinese Instruction-following LLaMA-based Model](https://github.com/Facico/Chinese-Vicuna)” and [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) provided optimizations as well. Vicuna from “[Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality](https://github.com/lm-sys/FastChat#vicuna-weights)” focused on improving the chat function from Alpaca.

The Low Rank adoption by Microsoft, called [“LoRA”](https://arxiv.org/pdf/2106.09685.pdf), helped a lot on speeding up the tuning. The idea was great: it freezed the weight but “inject trainable rank decomposition matrices into each layer of the Transformer architecture”, so the tuning speed could be 3x faster. LoRA technique was also useful beyond language models, for example, it helped faster tuning for stable diffusion in text-to-image tasks. Please feel free to read further [here](https://github.com/cloneofsimo/lora).

Meanwhile, we understood Llama was not so critical in this framework. It could be replaced. Llama from Meta didn’t allow any commercial use for the code or the weight. [Lit-llama](https://github.com/Lightning-AI/lit-llama) rewrote llama inference code for more independency, but it still had to use the Llama weight. The open source community provided use a few options, where `GLM` and `RWKV` were the two most promising ones.

[`GLM`](https://github.com/THUDM/GLM) from “[GLM: General Language Model Pretraining with Autoregressive Blank Infilling](https://arxiv.org/abs/2103.10360)” is a family of models at different sizes. It has a different approach from Meta’s Llama and its 6B model with chat function can be found as [`ChatGLM`](https://github.com/THUDM/ChatGLM-6B). Meanwhile, [`RWKV`](https://github.com/BlinkDL/RWKV-LM) was so unique. It didn’t follow the stacked decoder transformer structure like in GPT, instead, it used recurrent network like RNN, so its context length was theoretically unlimited and its inference was much faster with less memory cost. RWKV could reach transformer’s quality and its conversation version can be found as [`ChatRWKV`](https://github.com/BlinkDL/ChatRWKV).

Surely, we didn’t forget about the old GPT folks. Databricks open sourced their [`Dolly`](https://github.com/databrickslabs/dolly) using a `GPT-neox` network structure and applied instruct tuning. The results were not bad!.

We could compare the LLM performance in [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) framework, and the current benchmark could be found here <https://bellard.org/ts_server/>, so far LLama performed the best in the race.

## More community support

Inspired by Alpaca, instruct tuning with self-instruct became so popular and the fine tuning becomes easier with frameworks. [`xtuning`](https://github.com/stochasticai/xturing) is a nice and easy-to-use framework. Recently it announced its INT4 tuning with Alpaca-Lora. Tuning with knowledge from GPT-4 was also a good idea, so [“Instruction Tuning with GPT-4”](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM) pushed the data acquisition to its next level. The GLM team also brought in more efficient tuning method like [`P-tuning-v2`](https://github.com/THUDM/P-tuning-v2).

The community also supported independency from GPUs. Starting from early March, work like [`llama.cpp`](https://github.com/ggerganov/llama.cpp) and [`alpaca.cpp`](https://github.com/antimatter15/alpaca.cpp) provided engineering optimization to run models with quantization on CPU. We must understand “no free lunch” and quantization can loose precision and other quality. Please refer to the LLM benchmark mentioned above for more details.

The downstream tools like `llama-index` and `LangChain` support them these open...