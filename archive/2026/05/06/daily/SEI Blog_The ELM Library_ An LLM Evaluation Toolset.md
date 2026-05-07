---
title: The ELM Library: An LLM Evaluation Toolset
url: https://www.sei.cmu.edu/blog/the-elm-library-an-llm-evaluation-toolset/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-05-06
fetch_date: 2026-05-07T05:35:14.541654
---

# The ELM Library: An LLM Evaluation Toolset

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. The ELM Library: An LLM Evaluation Toolset

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Turri, V., Schieber, N., Brooks, T., Loughin, C., and Loughin, C., 2026: The ELM Library: An LLM Evaluation Toolset. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed May 7, 2026, https://doi.org/10.58012/vqdv-xs08.

Copy

APA Citation

Turri, V., Schieber, N., Brooks, T., Loughin, C., & Loughin, C. (2026, May 6). The ELM Library: An LLM Evaluation Toolset. Retrieved May 7, 2026, from https://doi.org/10.58012/vqdv-xs08.

Copy

Chicago Citation

Turri, Violet, Natalie Schieber, Tyler Brooks, Charles Loughin, and Charles Loughin. "The ELM Library: An LLM Evaluation Toolset." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, May 6, 2026. https://doi.org/10.58012/vqdv-xs08.

Copy

IEEE Citation

V. Turri, N. Schieber, T. Brooks, C. Loughin, and C. Loughin, "The ELM Library: An LLM Evaluation Toolset," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 6-May-2026 [Online]. Available: https://doi.org/10.58012/vqdv-xs08. [Accessed: 7-May-2026].

Copy

BibTeX Code

@misc{turri\_2026,
author={Turri, Violet and Schieber, Natalie and Brooks, Tyler and Loughin, Charles and Loughin, Charles},
title={The ELM Library: An LLM Evaluation Toolset},
month={{May},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/vqdv-xs08},
note={Accessed: 2026-May-7}
}

Copy

# The ELM Library: An LLM Evaluation Toolset

![Headshot of Violet Turri.](/media/images/Turri_Violet_493_230112.max-180x180.format-webp.webp)
![Headshot of Natalie Schieber.](/media/images/Schieber_Natalie_052_250116.max-180x180.format-webp.webp)

###### [Violet Turri](/authors/violet-turri), [Natalie Schieber](/authors/natalie-schieber), [Tyler Brooks](/authors/tyler-brooks), [Chuck Loughin](/authors/charles-loughin), and [Chuck Loughin](/authors/charles-loughin)

###### May 6, 2026

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/vqdv-xs08>

Get Citation

##### SHARE

Experimentation and validation of LLM performance is critical when building LLM-driven systems that must reliably deliver a service, from customer service chat bots to intelligence analysis tools. To help teams meet the need for rigorous evaluation methods, researchers in SEI’s AI Division developed the [Expanding Large Language Model Metrics (ELM) library](https://github.com/cmu-sei/ELM) built on best practices for LLM evaluation and benchmarking.

In this blog post, we provide a tutorial for using the ELM library, a set of extensible, customizable tools designed to make LLM evaluations repeatable, explainable, and consistent. The ELM library enables the following:

* **full customization**: write your own prompts and assessments and plug in any metrics or models.
* **inference-independent evaluation**: works on a JSON of inference results so you can generate results in one environment and score them in another.
* **auditable and reproducible testing**: every run stores the config, seed, model version, and metric code.
* **zero-cost, open-source capability**: free of hidden fees or vendor lock-in.

Below, we dive into the inference and evaluation engines that power ELM, showing you how to set up a reliable, end‑to‑end evaluation workflow.

## Tutorial: Using the ELM Evaluation Engine

The ELM library includes both an inference engine and an evaluation engine. The inference engine enables batch inference using local or API-based models, with built-in logging, hardware monitoring, and validation. The evaluation engine provides a customizable framework for evaluating LLM performance against existing or bespoke benchmarks and metrics. The Python code, available on [Github](https://github.com/cmu-sei/ELM), is designed for lightweight, adaptable experimentation with local or API-based models. The library uses a configuration-driven approach to defining inference and evaluation jobs, ensuring experiments are repeatable.

For local models, users can override hyperparameters to support experimentation and benchmarking. Inference and evaluation results are saved to JSON files alongside input parameters and metadata, providing consistent, queryable experimental outputs.

[![figure1_ELM_05062026](/media/images/figure1_ELM_05062026.max-1280x720.format-webp.webp)](/media/images/figure1_ELM_05062026.original.png)

Figure 1: The ELM Library includes an Inference Engine and Evaluation Engine to enable end-to-end LLM evaluation, customizable using a suite of configuration files.

At a high level, users can customize both the model configuration file and the prompt configuration file. These files define a set of reproducible, traceable inferences that are automatically executed by the inference engine. The resulting outputs are then fed into the evaluation engine together with a customizable assessment configuration file and an evaluation configuration file, producing the final evaluation results.

#### Getting the Engine Ready

To begin, install the ELM library and its dependencies. The `requirements.txt` file includes common AI/ML packages such as `scikit-learn`, `transformers`, `torch`, and `openai`. All packages can be obtained via PyPI.

After cloning the repository, navigate to the top level of the repository and install the pipelines and required dependencies with pip:

```
```bash
pip install -e .
```
```

For locally hosted models, the pipelines automatically select the best GPU resources (if available) and fall back to the CPU otherwise.

If using an OpenAI model, set the API key in the terminal:

```
```bash
export OPENAI_API_KEY="{api_key}"
```
```

#### Running Batch Inference

The most basic use of the ELM is batch inference over a collection of prompts. Three JSON-style input files are required: a prompt file, an environment config, and an inference config.

#### Defining a Prompt File

The prompt file contains a formatted list of all the prompts. Each prompt entry must include the name, style, and prompt text. An optional ground-truth text field can be included for evaluation. A list of parameters and definitions are enumerated in [`PromptConfig.py`](https://github.com/cmu-sei/ELM/blob/main/elm/inference_engine/pydanticmodels/PromptConfig.py)`.` Here is an example prompt entry:

```
```json
[
    {
        "name": "Test Prompt 1",
        "style": "basic",
        "text": "Finish the following sentence:  That's one small step for",
        “gt_text”: “man, one giant leap for mankind.”
    }
]

```
```

#### Setting Up the Environment Configuration

The environment configuration file specifies models and their locations. Every model entry must include the model name and model family. Some families may require additional details. For example, Llama models must specify paths for the weights, tokenizer, and cache. A list of parameters and definitions are enumerated in [`EnvironmentConfig.py`](https://github.com/cmu-sei/ELM/blob/main/elm/inference_engine/pydanticmodels/EnvironmentConfig.py)`.` Here is an example environment configuration file for a run that uses two different versions of Llama 3:

```
```json
{
    "name": "multi_configs_env",
    "models":
        [
            {
                "model_name": "LLaMa 3.2 1B",
                "model_family": "Llama",
               ...