---
title: AI-Powered Knowledge Graph Generator &#x26; APTs, (Thu, Feb 12th)
url: https://isc.sans.edu/diary/rss/32712
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-13
fetch_date: 2026-02-14T04:08:40.091816
---

# AI-Powered Knowledge Graph Generator &#x26; APTs, (Thu, Feb 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Russ McRee](/handler_list.html#russ-mcree "Russ McRee")

Threat Level: [green](/infocon.html)

* [previous](/diary/32708)

# [AI-Powered Knowledge Graph Generator & APTs](/forums/diary/AIPowered%2BKnowledge%2BGraph%2BGenerator%2BAPTs/32712/)

**Published**: 2026-02-12. **Last Updated**: 2026-02-13 03:04:48 UTC
**by** [Russ McRee](/handler_list.html#russ-mcree) (Version: 1)

[0 comment(s)](/diary/AIPowered%2BKnowledge%2BGraph%2BGenerator%2BAPTs/32712/#comments)

### Unstructured text to interactive knowledge graph via LLM & SPO triplet extraction

Courtesy of [TLDR InfoSec](https://tldr.tech/infosec) Launches & Tools again, another fine discovery in [Robert McDermott’s](https://github.com/robert-mcdermott) [AI Powered Knowledge Graph Generator](https://github.com/robert-mcdermott/ai-knowledge-graph). Robert’s system takes unstructured text, uses your preferred LLM and extracts knowledge in the form of Subject-Predicate-Object (SPO) triplets, then visualizes the relationships as an interactive knowledge graph.[1]

Robert has documented AI Powered Knowledge Graph Generator (AIKG) beautifully, I’ll not be regurgitating it needlessly, so please [read](https://github.com/robert-mcdermott/ai-knowledge-graph) further for details regarding features, requirements, configuration, and options. I will detail a few installation insights that got me up and running quickly.
The feature summary is this:
AIKG automatically splits large documents into manageable chunks for processing and uses AI to identify entities and their relationships. As AIKG ensures consistent entity naming across document chunks, it discovers additional relationships between disconnected parts of the graph, then creates an interactive graph visualization. AIKG works with any OpenAI-compatible API endpoint; I used [Ollama](https://ollama.com/) exclusively here with Google’s Gemma 3, a lightweight family of models built on Gemini technology. Gemma 3 is multimodal, processing text and images, and is the current, most capable model that runs on a single GPU. I ran my experimemts on a Lenovo ThinkBook 14 G4 circa 2022 with an AMD Ryzen 7 5825U 8-core processor, Radeon Graphics, and 40gb memory running Ubuntu 24.04.3 LTS.
My installation guidelines assume you have a full instance of Python3 and Ollama [installed](https://ollama.com/download). My installation was implemented under my `tools` directory.

```

python3 -m venv aikg # Establish a virtual environment for AIKG
cd aikg
git clone https://github.com/robert-mcdermott/ai-knowledge-graph.git # Clone AIKG into virtual environment
bin/pip3 install -r ai-knowledge-graph/requirements.txt # Install AIKG requirements
bin/python3 ai-knowledge-graph/generate-graph.py --help # Confirm AIKG installation is functional
ollama pull gemma3 # Pull the Gemma 3 model from Ollama
```

I opted to test AIKG via a couple of articles specific to Russian state-sponsored adversarial cyber campaigns as input:

* CISA’s Cybersecurity Advisory [Russian GRU Targeting Western Logistics Entities and Technology Companies](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a) May 2025
* SecurityWeek’s [Russia’s APT28 Targeting Energy Research, Defense Collaboration Entities](https://www.securityweek.com/russias-apt28-targeting-energy-research-defense-collaboration-entities/) January 2026

My use of these articles in particular was based on the assertion that APT and nation state activity is often well represented via interactive knowledge graph. I’ve advocated endlessly for visual link analysis and graph tech, including [Maltego](https://holisticinfosec.io/toolsmith/pdf/december2009) (the OG of knowledge graph tools) at far back as 2009, [Graphviz](https://holisticinfosec.blogspot.com/2015/09/toolsmith-108-visualizing-network-data.html) in 2015, [GraphFrames](https://holisticinfosec.blogspot.com/2018/04/toolsmith-132-helk-vs-aptsimulator-part.html) in 2018 and [Beagle](https://holisticinfosec.io/post/beagle-graph-transforms-dfir-data-logs/) in 2019. As always, visualization, coupled with entity relationship mappings, are an imperative for security analysts, threat hunters, and any security professional seeking deeper and more meaningful insights. While the SecurityWeek piece is a bit light on content and density, it served well as a good initial experiment.
The CISA advisory is much more dense and served as an excellent, more extensive experiment.
I pulled them both into individual text files more easily ingested for processing with AIKG, shared for you [here](https://github.com/holisticinfosec/ai-knowledge-graph-files) if you’d like to play along at home.

Starting with SecurityWeek’s [Russia’s APT28 Targeting Energy Research, Defense Collaboration Entities](https://www.securityweek.com/russias-apt28-targeting-energy-research-defense-collaboration-entities/), and the subsequent [Russia-APT28-targeting.txt](https://github.com/holisticinfosec/ai-knowledge-graph-files/blob/main/Russia-APT28-targeting.txt) file I created for model ingestion, I ran Gemma 3 as a 12 billion parameter model as follows:

```

ollama run gemma3:12b # Run Gemma 3 locally as 12 billion parameter model
~/tools/aikg/bin/python3 ~/tools/aikg/ai-knowledge-graph/generate-graph.py --config ~/tools/aikg/ai-knowledge-graph/config.toml -input data/Russia-APT28-targeting.txt --output Russia-APT28-targeting-kg-12b.html
```

You may want or need to run Gemma 3 with fewer parameters depending on the performance and capabilities of your local system. Note that I am calling file paths rather explicitly to overcome complaints about missing config and input files.
The article makes reference to APT credential harvesting activity targeting people associated with a Turkish energy and nuclear research agency, as well as a spoofed OWA login portal containing Turkish-language text to target Turkish scientists and researchers. As part of it’s use of semantic triples (Subject-Predicate-Object (SPO) triplets), how does AIKG perform linking entities, attributes and values into machine readable statements [2] derived from the article content, as seen in **Figure 1**?

![AIKG 12b](https://isc.sans.edu/diaryimages/images/aikg12b(1).png)

**Figure 1:** AIKG Gemma 3:12b result from SecurityWeek article

Quite well, I’d say. To manipulate the graph, you may opt to disable physics in the graph output toolbar so you can tweak node placements. As drawn from the statistics view for this graph, AIKG generated 38 nodes, 105 edges, 52 extracted edges, 53 inferred edges, and four communities. You can further filter as you see fit, but even unfiltered, and with just a little by of tuning at the presentation layer, we can immediately see success where semantic triples immediately emerge to excellent effect. We can see entity/relationship connections where, as an example, *threat actor –> targeted –> people* and *people –> associated with –> think tanks*, with direct reference to the aforementioned OWA *portal* and Turkish language. If you’re a cyberthreat intelligence analyst (CTI) or investigator, drawing visual conclusions derived from text processing will really help you step up your game in the form of context and enrichment in report writing. This same graph extends itself to represent the connection between the victims and the exploitation methods and infrastructure. If you don’t want to go through a full installation process for yourself to complete your own model execution, you should still grab the [JSON and HTML output files](https://github.com/holisticinfosec/ai-knowledge-graph-files) and experiment with them in your browser. You’ll get a real sense of the power and impact of an interactive knowledge graph with the joint forces power of LLM and SPO triplets.
For a second experiment I selected related content in a longer, more in depth analysis courtesy of a CISA Cybersecurity [Advisory](https://www.cisa.gov/news-events/cyb...