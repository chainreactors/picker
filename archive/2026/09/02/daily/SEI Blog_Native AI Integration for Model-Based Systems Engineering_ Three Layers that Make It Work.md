---
title: Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work
url: https://www.sei.cmu.edu/blog/native-ai-integration-for-model-based-systems-engineering-three-layers-that-make-it-work/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-09-02
fetch_date: 2026-09-03T07:02:03.337112
---

# Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work

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
4. Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Dempsey, C., 2026: Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work. Software Engineering Institute blog, Accessed September 3, 2026, https://doi.org/10.58012/9esk-pm74.

Copy

APA Citation

Dempsey, C. (2026, September 2). Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work. Retrieved September 3, 2026, from https://doi.org/10.58012/9esk-pm74.

Copy

Chicago Citation

Dempsey, Colin. "Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, September 2, 2026. https://doi.org/10.58012/9esk-pm74.

Copy

IEEE Citation

C. Dempsey, "Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 2-Sep-2026 [Online]. Available: https://doi.org/10.58012/9esk-pm74. [Accessed: 3-Sep-2026].

Copy

BibTeX Code

```
@misc{dempsey_2026,
author={Dempsey, Colin},
title={Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work},
month={Sep},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/9esk-pm74},
url={https://doi.org/10.58012/9esk-pm74},
note={Accessed: 2026-Sep-3}
}
```

Copy

# Native AI Integration for Model-Based Systems Engineering: Three Layers that Make It Work

![Headshot of Colin Dempsey.](/media/images/Dempsey_Colin_314_240125.max-180x180.format-webp.webp)

###### [Colin Dempsey](/authors/colin-dempsey)

###### September 2, 2026

##### PUBLISHED IN

[Model-Based Systems Engineering](/blog/topics/model-based-systems-engineering/)

##### CITE

<https://doi.org/10.58012/9esk-pm74>

Get Citation

##### SHARE

The appeal of applying artificial intelligence (AI ) to [model-based systems engineering (MBSE)](https://www.sei.cmu.edu/blog/introduction-model-based-systems-engineering-mbse/) is easy to understand. Formal architecture definitions, traceable requirements, behavior models, analysis, and verification evidence take time to develop and maintain. [AI could plausibly reduce some of that effort](https://incose.onlinelibrary.wiley.com/doi/epdf/10.1002/sys.70011), but plausibility is not evidence.

For program managers and engineering leaders, the opportunity is broader than faster model authoring. Integrating AI directly into model development can reduce the effort required to create, update, and reconcile engineering artifacts. It can shorten the time between an engineering change and feedback from the modeling toolchain, surface inconsistencies before integration and test, and preserve traceable evidence for technical decisions. The management value should therefore be judged by whether teams make better-informed decisions sooner and reduce rework and technical risk, while engineers retain responsibility for review, analysis, and assurance.

The harder question is how to integrate AI without weakening engineering rigor. Four questions guide our work:

* How can engineering teams natively integrate AI into MBSE modeling?
* Where does that integration add measurable value?
* What does an AI-augmented MBSE workflow look like?
* What does that workflow look like in practice?

As detailed in this post, we investigated these questions by building a three-layer integration architecture, evaluating it in a controlled SysML v2 model-generation benchmark, and examining one large benchmark task involving a four-drone aerial survey swarm.

## **SysML v2 in Brief**

Systems modeling language version 2, commonly referred to as SysML v2, is the Object Management Group’s formal language for describing systems through requirements, structure, behavior, analysis, verification, and stakeholder views. It provides both graphical and textual notation over the same underlying model. This work focuses on the textual notation because model files can be reviewed as text, stored in version control, compared in pull requests, and processed by automated tools.

Two ideas make the short code sample below readable. A *definition*, or `def`, declares a reusable type, while a *usage* places that type in a particular model context. A package supplies a namespace. Typed attributes can use quantities and units from the standard libraries.

```
package DroneSwarmExample {
    private import ScalarValues::*;

    enum def FlightMode {
        enum idle;
        enum takeoff;
        enum survey;
        enum returnToHome;
    }

    part def FlightController {
        attribute droneId : Integer;
        attribute activeMode : FlightMode;
    }

    part def Drone {
        part controller : FlightController;
    }

    part drone : Drone;
}
```

Here, `FlightMode`, `FlightController`, and `Drone` are definitions. The nested controller is a usage that composes the drone from a flight controller, while drone is a top-level usage of the complete type. The identifier and operating mode are typed values rather than unqualified properties.

Textual notation makes SysML v2 accessible to coding assistants, but it does not make the language informal. Generated model text must still conform to the grammar, resolve its references, and satisfy the language’s semantic rules. That requirement is why a language-aware modeling service and a callable validation interface are central to the architecture.

## **The Architecture**

Native integration means placing the AI assistant inside the engineering workspace rather than treating it as a separate chat surface. The assistant works in the same repository as the model, retrieves project guidance, edits model artifacts, invokes the same validation command used by engineers and continuous integration, and responds to diagnostics. The engineer remains responsible for intent, review, and engineering decisions.

The workspace combines three separable layers: an AI coding assistant, a formal modeling toolchain, and a curated knowledge base with workflow skills.

* **AI coding assistant.** The assistant receives direction in natural language and operates on version-controlled artifacts. The architecture is not tied to a particular assistant client or AI model. Our current implementation uses [Visual Studio Code](https://code.visualstudio.com/) as the primary engineering environment. Through editor extensions and integrated terminals, [Claude Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code), [OpenAI Codex](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt), and [Continue](https://marketplace.visualstudio.com/items?itemName=Continue.continue) each operate on the same repository and connect to the same modeling tools and project knowledge.
* **Language-aware modeling toolchain.** The general requirement is a SysML v2 language server, or an equivalent language-aware service, that can parse SysML v2 model files, resolve references, apply grammar and semantic rules, and return diagnostics. For agentic and automated use, those capabilities should be exposed through a noninteractive interface, ideally a command-line interface. This lets assistants, engineers, and [continuous integration (CI)](https://www.sei.cmu.edu/blog/continuous-integration-in-devops/) jobs invoke the same check.

  Our implementation uses [Sensmetry’s Syside](https://sensmetry.com/syside/) for both interactive editor support and automat...