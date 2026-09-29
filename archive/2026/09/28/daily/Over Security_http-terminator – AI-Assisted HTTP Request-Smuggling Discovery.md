---
title: http-terminator – AI-Assisted HTTP Request-Smuggling Discovery
url: https://www.darknet.org.uk/2026/09/http-terminator-ai-request-smuggling-discovery/
source: Over Security
date: 2026-09-28
fetch_date: 2026-09-29T07:41:18.916877
---

# http-terminator – AI-Assisted HTTP Request-Smuggling Discovery

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / http-terminator – AI-Assisted HTTP Request-Smuggling Discovery

# http-terminator – AI-Assisted HTTP Request-Smuggling Discovery

Published September 28, 2026 |

Views: 159

http-terminator is a research pipeline from PortSwigger that points a large language model at HTTP specifications and asks it to find request-smuggling attacks. It was published alongside [the research it produced](https://portswigger.net/research/can-ai-do-novel-security-research), as a reference companion rather than a product.

![http-terminator — AI-ASSISTED HTTP REQUEST SMUGGLING DISCOVERY; two offset request boundaries in parallel channels; darknet.org.uk.](https://www.darknet.org.uk/wp-content/uploads/2026/09/http-terminator-ai-assisted-request-smuggling-discovery-640x360.webp)

I read the current repository rather than the write-ups about it. What’s there is a four-stage pipeline: two stages are self-contained, and two need Burp, the last of them also a simulator the repository doesn’t ship.

Advertisement

At a check on 27 September, the public `main` branch contained one commit, `874682c`, dated 22 July 2026.

## The ground this sits on

A 2017 post here on [Microsoft’s Azure web application firewall](https://www.darknet.org.uk/2017/04/microsoft-azure-web-application-firewall-waf-launched/) mentions request smuggling among the attacks a WAF blocks, but doesn’t explain it, so it’s worth a sentence. Request smuggling – also called desync – exploits a disagreement between two servers about where one HTTP request ends and the next begins.

Put a front-end proxy in front of a back-end server and send a request the two parse differently, and the back-end can treat part of your input as the start of another request. In one variant, response poisoning, the next user’s request on that reused back-end connection completes your smuggled prefix, and that user receives the response to your request instead of their own. PortSwigger researcher James Kettle has published techniques and research on it.

## From specifications to test cases

PortSwigger’s own HTTP Request Smuggler tests targets from [Burp Suite](https://www.darknet.org.uk/2007/01/burp-proxy-burp-suite-attacking-web-applications/) and includes a research mode for exploring new desync techniques. http-terminator takes a document-driven approach: Claude extracts candidate vectors from specifications, which feed generation, validation and investigation stages.

## The four stages

The pipeline runs in four stages:

* **seeker** (Python) reads documents and RFCs and, through Claude, extracts candidate desync vectors.
* **flamer** (Java) turns those vectors into malformed HTTP test-cases.
* **validator**, a Burp extension, fires the generated requests at a target and reports confirmed desync findings and unconfirmed anomalies.
* **investigator** (Python, driven by Claude Code) replicates the hits, confirms them, chases follow-on impact and writes them up.

Reproducing it is where the documentation gets tangled. seeker and flamer are self-contained – Python or Java, plus an Anthropic API key. The other two are not.

Advertisement

The validator’s documentation needs careful reading. The root README lists commercial Burp Suite for running it, while the validator’s own README says its test suite runs under Burp Community or Professional, with the Professional-only tests skipped on Community. Those cover different things, running the stage and testing it. Where the repository does contradict itself is the build: the validator’s README says the build depends on `bulkScan-all.jar` and that the jar is not vendored in the repository – yet it is committed at `validator/bulkScan-all.jar`, and the build file points at it. investigator, in turn, needs an external MCP simulator and Burp Organizer alongside Claude Code and a live target.

## Following the data through the stages

Start in `seeker/`, with Python 3.11 or later, an Anthropic API key and network access. The README installs the package from that directory:

pip install -e ".[dev]"

|  |  |
| --- | --- |
| 1 | pip install -e ".[dev]" |

That installs seeker’s command-line tool. Its next command reads a URL list you create, a text file of the document URLs to process, fetches those documents and stores the extracted sections in `seeker.db`. The repository ships a sample list at `seeker/fixtures/urls.txt` you can point at instead to try it:

seeker process --input urls.txt --db seeker.db --manifest run.manifest.json --verbose

|  |  |
| --- | --- |
| 1 | seeker process --input urls.txt --db seeker.db --manifest run.manifest.json --verbose |

The manifest records that run, while the SQLite database holds the sections you can inspect with seeker’s query command:

seeker query --db seeker.db --type http\_desync\_vector

|  |  |
| --- | --- |
| 1 | seeker query --db seeker.db --type http\_desync\_vector |

That selects the extracted desync-vector sections; once flamer has generated requests, seeker can trace a request ID back to its source:

python3 -m seeker.cli trace 1002368 --db seeker.db --flamer-db ../flamer/production.db

|  |  |
| --- | --- |
| 1 | python3 -m seeker.cli trace 1002368 --db seeker.db --flamer-db ../flamer/production.db |

Replace 1002368, the README’s example, with a request ID from your own flamer database; the trace links a generated request to the seeker section it came from.

Next, from `flamer/`, with Java 21, Gradle and an Anthropic API key, the default run reads unprocessed sections from `../seeker/seeker.db` and writes generated requests to its own `production.db`:

export ANTHROPIC\_API\_KEY=your\_key
./gradlew run

|  |  |
| --- | --- |
| 1  2 | export ANTHROPIC\_API\_KEY=your\_key  ./gradlew run |

The key is required for Claude; flamer’s README also offers a run that does not save generated requests:

./gradlew run --args="--dry-run"

|  |  |
| --- | --- |
| 1 | ./gradlew run --args="--dry-run" |

Use the documented dump option to view requests already held in flamer’s database:

./gradlew run --args="--dump"

|  |  |
| --- | --- |
| 1 | ./gradlew run --args="--dump" |

Flamer’s Gradle task copies its generated database into the validator directory:

./gradlew copyDbToValidator

|  |  |
| --- | --- |
| 1 | ./gradlew copyDbToValidator |

From `validator/`, the README builds the Burp extension jar with:

./gradlew jar

|  |  |
| --- | --- |
| 1 | ./gradlew jar |

The documented output is `build/libs/validator.jar`; load it in Burp via **Extensions > Installed > Add** and select that file.

That manual extension-loading step is separate from the validator’s `livetesting` suite, which can use Burp Community or Professional: Community skips the Professional-only tests, while Professional runs them. The root README’s commercial-Burp requirement describes running the validation stage, not this test suite.

There is no investigator command to copy from its README. I...