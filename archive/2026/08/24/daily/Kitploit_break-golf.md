---
title: break-golf
url: https://kitploit.com/en/tools/github/trailofbits/break-golf
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:57.062150
---

# break-golf

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

break-golf — Cryptanalysis golf: break schemes and prove it in Lean 4. Proof-of-concept board. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/trailofbits/break-golf

![](https://assets.kitploit.com/production/public/tools/51186/227ff3cd87014e87a492d65630eff6fbb293f64d2d5e47d197b799d5f4e7371c-display-v1.webp)

[Cryptography](/en/categories/cryptography)[CTF](/en/categories/ctf)[Papers & Research](/en/categories/papers-research)[Learning & Education](/en/categories/education)[Labs & Practice](/en/categories/labs-practice)

![GitHub](/providers/github.png)trailofbits/break-golf

# break-golf

Cryptanalysis golf: break schemes and prove it in Lean 4. Proof-of-concept board.

[View Repository](https://github.com/trailofbits/break-golf)

11h 39m ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# break-golf

A board for cryptanalysis results that are **proved**, not run.

A challenge fixes two worlds and the statement you must prove. You write an
adversary and a proof that it distinguishes them. The win is the proof: nothing
is executed, sampled, or replayed, and no human reads the submission to decide
whether it counts.

Status: **proof-of-concept.** The site is static, submissions open a GitHub
issue, and a human decides. There is no Lean verifier behind it yet.

## Layout

| Path | What it is |
| --- | --- |
| `challenges/<name>/Challenge.lean` | **Trusted.** Pins the exact types a submission must inhabit. Not part of any upload. |
| `challenges/<name>/Cost.lean` | Platform-generated per submission from the form's numbers. |
| `challenges/<name>/config.json` | Scoring, par, permitted axioms, timeout. The only file you edit to add a challenge. |
| `challenges/<name>/Solve.template.lean` | The skeleton a submitter fills in. |
| `tools/manifest.py` | Derives `docs/data/manifest.json` from `challenges/`. |
| `tools/ledger.py` | Derives `docs/data/ledger.json` from `scoring/ledger.json`, computing bit scores and frontier membership. |
| `tools/verify.py` | Verifies one submission: challenge id as `argv[1]`, body on stdin, JSON verdict on stdout. Same interface as lean-golf's. |
| `tools/lint_challenges.py` | Every challenge config carries what the board and the verifier need. |
| `tools/check_site.py` | The static site can load and render its own generated data. |
| `scoring/ledger.json` | The record set. |
| `docs/` | The GitHub Pages site. Static; reads only the two generated files. |

root@kitploit:~

```
python3 tools/manifest.py          # rewrite the manifest
python3 tools/manifest.py --check  # fail if stale
python3 tools/ledger.py            # rewrite the ledger with scores and frontier
python3 tools/lint_challenges.py   # configs are complete
python3 tools/check_site.py        # the site can render what the tools generate

printf '%s' "$BODY" | python3 tools/verify.py spoc128    # one submission
```

## CI

`verify.yml` runs on push and pull request: the `--check` gates, the config lint,
the site check, and a battery of submissions the verifier must accept and must
reject — a `sorry`, a `native_decide`, an unknown challenge, a zero advantage, a
body with no Lean block. `workflow_dispatch` verifies one submission on demand
without opening an issue.

`submission.yml` handles a `verify:` issue in two jobs. The first parses
untrusted input and holds **no write scopes**; the second downloads its verdict
and posts the comment. That split is lean-golf's and it is the reason an issue
body cannot reach a token.

## The submitter never writes the statement

This is the whole mechanism, and it is the same one `trailofbits/lean-golf` uses
for proof golf. The verifier builds *its own* copy of `Challenge.lean`. A
submission supplies only:

root@kitploit:~

```
def strategy : game.Param → PFunDDS.DDE game.Query game.Response
def verdict  : List (game.Query × Option game.Response) → Bool
theorem attackWins : attack.Wins score.budget score.advantage
```

plus `budget` and `advantage` on the form. `attack` and `score` are assembled
from those numbers in `Challenge.lean`, so a submission cannot spend a larger
budget than it is scored for, or prove a weaker bound than it claims — not
because we check, but because it never holds the pen on either object.

Four rejections a verifier makes without reading anything:

| The cheat |
| --- |

`native_decide`, `maxHeartbeats` and `maxRecDepth` are rejected too: a proof that
only closes with a raised limit is a proof the verifier cannot afford.

## Scoring

Nothing is fixed in advance. On a scheme nobody has studied, what advantage is
reachable at what cost is the research question, so any target is a guess — and a
target set too high scores a genuine `2⁻³⁰` distinguisher as zero. The board
measures the result instead:

root@kitploit:~

```
score = log₂( budget / advantage^e )
```

Queries per unit advantage; its log base two is the security level in bits the
attack refutes. Lower is better. Understating your advantage *raises* the score,
so there is nothing to gain by claiming less than you can prove.

`e` is per challenge and has no default. `e = 2` for a decision game — an
advantage `α` needs about `α⁻²` repetitions to amplify — and `e = 1` for a
search-flavoured one. Both conventions are in the literature and the
inconsistency is known (Micciancio–Walter, *On the Bit Security of Cryptographic
Primitives*), so a challenge states which it uses.

**Par is the designer's own claim**, taken from the specification, so no guess
about attack difficulty appears anywhere. Under par is a break of the claim.

The **frontier** is the primary record: a result joins it when nothing else beats
it on both queries and advantage at once. The bit score is the ranked column
beside it, and two checked lemmas in the Lean layer
(`Score.workFactor_lt_of_dominates`, `Score.onFrontier_of_workFactor_min`)
guarantee the ranking never buries a result that wins on both axes.

## Challenges

**spoc128** — SpoC-128 as submitted to NIST LWC Round 2. Broken: three queries,
advantage 1, 1.58 bits. `load key n` puts the nonce in the rate and `tagInput`
XORs `tagControl` into the same rate, so `tagInput (load key n) = load key (n ^^^ tagControl)`. One permutation input is reachable by two queries, and since the
permutation is public and invertible, half of it leaks in a tag and half in a
ciphertext block; join, invert, take the capacity, and that is the key.

**spoc128-ds** — the same mode with the four control bits reserved in the nonce,
so `n ^^^ tagControl` is not a legal nonce. **Open: no attack is known.** The
restriction lives in the *type* of a query, so the published attack is not merely
unsuccessful here — it cannot be presented as an adversary at all
(`SpoC128DS.attack_second_query_illegal`).

This is deliberately not a second copy of the mode. Hardening `DDC.lean` would
mean a parallel model to keep in sync; restricting the query domain is one
predicate, and every existing theorem about the mode still applies.

Nothing here claims the variant is secure. Closing one published rout...