---
title: Scripting the disassembler: Local agentic reverse engineering through vbdec’s live COM object model
url: https://blog.talosintelligence.com/scripting-the-disassembler/
source: Over Security
date: 2026-06-18
fetch_date: 2026-06-19T07:09:03.212176
---

# Scripting the disassembler: Local agentic reverse engineering through vbdec’s live COM object model

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Scripting the disassembler: Local agentic reverse engineering through vbdec’s live COM object model

By
[David Zimmer](https://blog.talosintelligence.com/author/david-zimmer/)

Thursday, June 18, 2026 06:00

[Tool Talk](https://blog.talosintelligence.com/category/tool-talk/)
[AI](https://blog.talosintelligence.com/category/ai/)

* Analysis tools do not need AI built in to support agentic workflows; they simply need to expose their data through an external scripting interface.
* Even traditional graphical user interface (GUI) applications can be made AI-accessible by publishing their internal object models, allowing agents to query and automate analysis without modifying the core application.
* This approach can often be implemented with surprisingly little engineering effort, leveraging existing scripting technologies and application data structures.
* By exposing structured data rather than adding predefined AI features, users can extend a tool's capabilities through prompts, turning new analyses into workflows instead of product feature requests.
* The application becomes both an interactive viewer and a persistent data server, enabling local data to be parsed once and queried repeatedly across multiple agent sessions while keeping analyst-controlled data local.

---

## The problem with VB6 binaries

VB6 binaries are laid out as a complex file format with embedded metadata. Recovering advanced data embeddings means reimplementing VB6s’ internal file format: the VB header, the object table, and the P-code layout. This is a highly specialized task that takes dedicated tools to do accurately, but not every tool exposes an equivalent programmatic library. The technique in this blog shows how AI agents can automate existing tools and reach deep into the result set.

## The recipe

The whole technique comprises three pieces. Any one of them in isolation is interesting, but together they are a new working mode.

### The live model

[vbdec](https://sandsprite.com/vbdec/) does not keep its parsed model locked behind its GUI. When a binary is loaded and remote scripting is enabled (Help → Options → Enable Remote Scripting), vbdec registers its central `CVBProject` object and its main form in the Windows [Running Object Table](https://github.com/dzzie/tests/blob/master/rot_test_3/CRemotelyScriptable.cls) (ROT) under the monikers `vbdec.vbp` and `vbdec.frmMain`. The ROT is a system-wide directory of live Component Object Model (COM) objects; any process can look an object up by moniker and receive a reference to the running instance. From a script, that is a single line:

```
Set o = GetObject("vbdec.vbp")
```

The variable `o` can now access the entire parsed project: every form, class, module, declared API, P-code body, control, and string, presented as a navigable object graph. The script is driving the disassembler itself.

**Note:** For VB6 host applications in particular, this capability can even be forcefully added [without source code access](https://www.gendigital.com/blog/insights/research/scripting-arbitrary-vb6-applications).

### The contract

A live model is useless to an agent that does not know its shape. vbdec now includes an AI agent [support package](https://sandsprite.com/vbdec/vbdec_ai.zip) that helps bridge this gap. The first is the operator briefing (“\_claude\_vbdec\_ai\_instructions.txt”) — a short markdown file that tells the agent what vbdec is, how to bind to the ROT, and how the object model is shaped. The second is the proto folder — 90 auto-generated class definitions covering every public class and form vbdec exposes. The agent treats these as the authoritative reference for member names and types. (The original IntelliSensesupport files were also usable for this task.)

### The local agent

The third piece is the agent. In this blog, Talos used Claude Code, run locally on the workstation. The user opens a terminal, points the AI at the briefing and prototypes, and simply describes what they would like analyzed. Claude Code then runs multiple .vbs files with cscript and explores the data through iterations. There is no preselected AI integration embedded in vbdec, no upload for the analyst’s binary, and no glue to be maintained as a separate codebase. The agent and disassembler share a machine and file system; analysis occurs locally, with only the model inference requests leaving the workstation.

Whatever capability the agent adds next extends vbdec without any new code in the tool itself, and users are free to select whichever model they prefer.

## What the analyst actually does

Next are a couple examples tested against a P-code version of PDFStreamDumper.

### Decompile a function

The analyst names a function and asks for a source code reconstruction. The agent pulls the P-code, walks the VB-VM opcode stream, maps each construct to its VB6 equivalent, and produces a source level equivalent with inline comments.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/claude_decompile_pcode.png)

**Figure 1.** **Example output** **(right)** **compared to the original source function** **(left).**

The reconstruction is not byte-identical, but the control flow is substantially recovered with agent comments added in. It is also interesting to note that the AI went into the subfunctions on its own, determined their purpose, and gave them reasonable names to complete its task decompiling the parent. This is usable reverse-engineering output that a human would spend substantial time producing, now scalable and generated in seconds.

### Build a call graph

The analyst picks a function and asks for its callees as a Graphviz DOT file. The agent walks each `CCodeBody.Disasm`, picks out the call opcodes (`ImpAdCallI2`, `VCallHresult`, `LateMemCall`, and others) and emits the DOT gr...