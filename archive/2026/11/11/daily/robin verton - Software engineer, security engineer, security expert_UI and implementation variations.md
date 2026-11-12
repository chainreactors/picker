---
title: UI and implementation variations
url: https://robinverton.de/blog/ui-and-implementation-variations/
source: robin verton - Software engineer, security engineer, security expert
date: 2026-11-11
fetch_date: 2026-11-12T09:01:14.765685
---

# UI and implementation variations

[Robin Verton](/)

[Home](/)
[Blog](/blog)
[Security](/security)
[TIL](/til)
[Uses](/uses)
[Contact ↗](/cdn-cgi/l/email-protection#f199949d9d9eb1839e93989f879483859e9fdf9594)

# UI and implementation variations

2026-11-11

[ai](https://robinverton.de/tags/ai/)

[swe](https://robinverton.de/tags/swe/)

[ui](https://robinverton.de/tags/ui/)

[design](https://robinverton.de/tags/design/)

One of the biggest productivity gains agentic engineering gave me is exploring ideas faster, because
throwing them away no longer means wasted hours.

This applies as much to UI design variations as to code implementations and designs. For UI, it’s also
very fast to do, as the AI does not even have to implement it.

Often, generated images that make use of the current layout/style are enough to see if a new UI
element makes sense (in terms of user experience) or can be thrown away. In the pre-AI days, I
offloaded exactly this type of work to our designer, but now I’m more involved in the UI design
myself.

Let’s look at some examples of UI variations from the last few weeks. We are currently working on a
product that allows (regulated) companies to work hand-in-hand with AI. The focus here is on
empowering the user, not replacing them. We have designed this very carefully around the daily work
of an office worker and put a lot of thought into every element the user interacts with.

One of these areas is a utility section. Depending on the use case the user is working on, useful
utilities are displayed automatically. An example of this is a CVSS calculator. Yes, there are
plenty of them accessible with a simple search, but this one is integrated into the interface the
user is working in. It lets the user pass selections on to the next (outcome) section in the
interface, which builds up a chain of justifications. But let’s ignore the product for now and look
at how this was designed:

> The first utility we want to add is a CVSS calculator. Make a thread for it where you prepare
> everything needed. Give us 3 variants on how this CVSS calculator utility can look like.

![Three CVSS calculator variants](/img/ai-variations-cvss.png)

While this has the typical AI-slop “put everything in it” style, it’s still a good starting point! I
can see different concepts, choose one that suits me, and then iterate on it again: three new
variations, starting from A, B, or C. This is a huge time saver! It still takes effort to clean this
up: remove unnecessary stuff, re-align elements so they line up horizontally/vertically, change
colors, help texts, etc. - but that’s fine.

Here is another example. We have cards that can be added to a workspace front page. It’s like a
dynamic dashboard you can arrange via drag and drop to your liking. Different types of cards show
different information or allow quick actions. I wanted a card that displays how many cases (that’s
the term we use) are in which state:

![Four case-status card variants](/img/ai-variations-card.png)

Again, a nice starting point! Some more examples:

![Three statement editor layouts](/img/ai-variations-editor.png)
![Three “New case” dialog variants](/img/ai-variations-mode.png)
![Three file browser variants](/img/ai-variations-filepicker.png)
![Three variants for removing an AI finding](/img/ai-variations-note-remove.png)

Now let’s look at implementation ideas. I read a lot of tech articles because I have a deep interest
in how things work under the hood. turbopuffer, for example, is one of the companies whose blog I
follow because they write deeply technical posts. One of the posts was about a [queue on
S3](https://turbopuffer.com/blog/object-storage-queue) with CAS primitives. It’s something I was
already interested in after seeing lots of posts about new primitives on S3, for example
[walgit](https://github.com/tobi/walgit).

On a current work project (at a bank I’m consulting for), we had the regulatory requirement of
tracking 3rd-party dependencies. There are open-source solutions like
[Dependency-Track](https://dependencytrack.org/), but to be honest: they feel like legacy software.
They’re resource-intensive and don’t feel robust. I fought with SBOM importing and was surprised
that the most important feature is so constrained.

After reading about these new S3-based tools, I came up with the idea of just putting SBOMs on S3,
with a worker handling ingestion and monitoring, using the same primitives. It’s one of those ideas
I can put days into and afterwards throw everything away. After some back-and-forth discussion, I had
AI do the implementation, set up a test environment, and test different failure scenarios.

![SBOM timeline per prod service](/img/ai-variations-sbom1.png)
![SBOM storage layout on S3](/img/ai-variations-sbom2.png)

The idea and implementation work. Will it be used by my client? I doubt it (for now), but now I have
another option to suggest when we discuss alternatives to Dependency-Track.

Times have changed, and while I [miss the old way](/blog/i-miss/), I do enjoy how fast I can express and
implement ideas now. It’s a completely new way of thinking for me, because ideation, design,
implementation, and iteration are so cheap now. Nowadays, there is rarely a night when I don’t have
an agent working through one of my ideas, so I can review it and continue with it the next morning.

## See Also

### I miss

Read →

### Open Claude Code CLI from Raycast in a new Ghostty window

Read →

### ./ai

Read →

[← All blog entries](/blog)

**©2026 Robin Verton.**
Software and security
engineering.
Design inspired by
[ersc.io](https://ersc.io/).

[Mail](/cdn-cgi/l/email-protection#84ece1e8e8ebc4f6ebe6edeaf2e1f6f0ebeaaae0e1)
[GitHub](https://github.com/rverton)
[Twitter](https://twitter.com/robinverton)
[Imprint](/imprint)