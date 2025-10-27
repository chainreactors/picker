---
title: The Art of Agentic Coding
url: https://www.hahwul.com/blog/2025/agentic-coding/
source: HAHWUL
date: 2025-06-15
fetch_date: 2025-10-06T22:55:06.866428
---

# The Art of Agentic Coding

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/blog/2025/agentic-coding/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/blog/2025/agentic-coding/)

[한국어](https://www.hahwul.com/ko/blog/2025/agentic-coding/)

JULY 14, 2025

# The Art of Agentic Coding

My Agentic Coding Rule and Thoughts

The coding paradigm is rapidly changing with AI. I've heard the term 'Vibe Coding' being thrown around, but honestly, I'm not quite sure what to make of it. The idea of generating code based on just a feeling or atmosphere doesn't sit right with me, as it seems to undermine the essence of the coding experience I value.

However, Agentic Coding is a bit different. It goes beyond simply requesting code generation; it's about delegating specific tasks to an AI agent. It's much closer to having a pair programmer by my side. This approach has allowed me to write more code faster without losing my coding intuition or my grip on the project's direction. For me, Agentic Coding is closer to the ideal model of collaboration.

In this post, I want to share the practices and experiences that have helped me get better at using Agentic Coding.

## Agentic Coding

Agentic Coding isn't fundamentally different from writing code with existing AI-based IDEs. The key difference is that instead of just instructing an AI agent to write a specific piece of code, you give it a degree of autonomy and delegate entire tasks for it to solve. The core of this process is an iterative loop of generating, modifying, verifying, and testing code to complete the given task.

```
 ---
title: Agentic Coding Workflow @hahwul
---
graph LR
    A(Task) --> B[Planning];
    B --> C[Code Generation];
    C --> D[Verification & Testing];
    D --> E[Request review];
    E --> F{Solve?};
    F -- No --> B;
    F -- Yes --> G(End);
```

## Keys to Effective Agentic Coding

After working on several projects with AI agents, I've realized there are a few key things that make the collaboration more effective. While you can handle simple tasks without much setup, the results are vastly different when you have a well-configured environment. Here are some of the points I've noted.

### Know Your Project

The most important thing is that the developer—you—must be the captain of the ship. The AI is a capable crew member, but making the final decisions and seeing the big picture is the captain's job. You need a clear understanding of the project's architecture, goals, and constraints to give the AI precise instructions and to properly evaluate and integrate its output.

### Parallel-Friendly Code Structure

AI agents aren't like humans. When you consider using multiple agents simultaneously or having one agent handle several tasks in parallel, it's far more effective if the code is logically and clearly separated. This might conflict with some traditional programming concepts, but in AI collaboration, having clearly divided units of work has proven more efficient. I've personally found it much easier to delegate tasks in a structure where features are broken down into packages or libraries.

```
 graph TD
    A[Monolithic Application] --> B{Core Logic};
    B --> C[Feature A Integration];
    B --> D[Feature B Integration];
    B --> E[Feature C Integration];
    C --> F(UI Module);
    D --> G(Database Module);
    E --> H(API Module);

    subgraph "Tightly Coupled"
        B --- C;
        B --- D;
        B --- E;
    end
```

*Traditional Code Structure (Less Parallel-Friendly)*

```
 graph TD
    A[Main Orchestrator Agent] --> B{Task Delegation};
    B --> C[Agent Feature A Package];
    B --> D[Agent Feature B Package];
    B --> E[Agent Feature C Library];

    C --> F(Sub-Task 1.1);
    C --> G(Sub-Task 1.2);
    D --> H(Sub-Task 2.1);
    E --> I(Sub-Task 3.1);
    E --> J(Sub-Task 3.2);

    subgraph "Loosely Coupled"
        C;
        D;
        E;
    end
```

*Parallel-Friendly Code Structure (Optimized for AI Agents)*

### The Importance of Tooling

AI makes mistakes. But well-established tooling can significantly reduce those mistakes and help correct them quickly when they do happen. Linters, formatters, and testers are no longer optional; they're essential.

![AI's Test](https://github.com/user-attachments/assets/fb20ceb3-8957-4efc-93cc-29c18754008e)
*Verifying that the generated code has no issues.*

I've been reminded once again of the importance of TDD (Test-Driven Development). In projects with thorough test coverage, I've had many impressive experiences where the AI generated faulty code, discovered the issue during the CI/CD pipeline's test phase, and then corrected itself.

An interesting side note, however, is that AI also uses various tricks to pass tests. If you look closely, you'll sometimes see it deleting test cases or finding shortcuts to get a pass. This is something that needs to be caught during the code review phase.

### Language Choice & Clear Errors

I've often been asked, "If you're coding with AI, what language is best?" The language itself might not be the most critical factor. However, from my personal experience, languages that provide detailed and friendly error messages are more advantageous for AI collaboration. When the compiler or interpreter clearly states "what" went wrong and "why," the AI's chances of fixing the problem increase. For that reason, I chose Rust, and I've been quite satisfied with the results.

### Docs for AI (AI-README)

We usually write a `README.md` file for our projects. I take it a step further and create a separate document, like `AGENTS.md` ,`AI.md`, specifically for the AI agent to read. In this document, I outline the project's overall structure, the role of each module, a list of key files to reference, and the rules that must be followed during coding. The presence of this document has made a huge difference in the AI's ability to understand the project and perform its tasks.

### Clear, Granular Tasks

The more abstract and larger the task, the more the AI struggles. Of course, the same could be said for humans. As I've used AI agents more, I've found myself breaking down tasks into much smaller and more clearly defined pieces than I used to. Instead of a large task like 'Implement login feature,' providing specific instructions like '1. Define user model, 2. Create database schema, 3. Implement password hashing logic...' yields much better results.

Even if you have to assign a large task, it's best to provide a detailed plan for the AI to follow. In this respect, Jules, which I'll discuss in the workflow section below, has a distinct advantage.

![Jules](https://github.com/user-attachments/assets/b082fb5d-4144-4c81-a19a-20f6ec2c4259)
*In Jules, a plan is created and first reviewed by the user before the task is executed.*

## My Current Workflow

Locally, I usually delegate tasks from the Agent Panel in [Zed](https://zed.dev), close the tab, and get on with my other work. It's convenient because it uses macOS notifications to let me know when it's done. In a cloud environment, I frequently use Google's [Jules](https://jules.google). Jules has given me a great experience of being able to assign tasks continuously, regardless of my location or situation. I often find myself giving it instructions from my phone when I'm out.

![Zed and Jules](https://github.com/user-attachments/assets/0a560b65-379d-4c4d-a0d0-7c7bf1ed6b4c)

I'm also very interested in terminal-based tools like Codex and Claude Code. However, what I'm most excited about is the [GitHub Copilot Coding Agent (the one previously introduced as Padawan)](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/). I manage most of my tasks as GitHub Issues, and this Agent is expected to understand and execute tasks based on those issues. This would streamline the process of organizing and delegating work significantly. While I coul...