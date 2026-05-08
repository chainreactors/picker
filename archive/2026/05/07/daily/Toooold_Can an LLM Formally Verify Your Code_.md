---
title: Can an LLM Formally Verify Your Code?
url: https://toooold.com/2026/05/07/code-to-lean.html
source: Toooold
date: 2026-05-07
fetch_date: 2026-05-08T04:55:35.377785
---

# Can an LLM Formally Verify Your Code?

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# Can an LLM Formally Verify Your Code?

May 7, 2026

When a language model tells you “this function is correct,” how much should you trust it? The answer is: not very much — unless the claim comes with a machine-checked proof. This post describes a pipeline that asks an LLM to translate a Python function into Lean 4, proposes a correctness theorem, and then runs five independent gates to decide whether to trust the result. The point is not the translation; it’s the gates.

## Why Lean?

[Lean 4](https://lean-lang.org/) is a dependently typed theorem prover and programming language. Like Coq or Isabelle, it lets you write mathematical proofs that a type-checker verifies mechanically. Unlike those systems, Lean 4 also has a usable extraction/evaluation story and a growing standard library (`Std4`, `Mathlib`).

The key property we care about: **Lean cannot lie about its own axioms.** Every theorem Lean accepts is either provable from a known-good axiom set or contains `sorry` (Lean’s escape hatch, analogous to `admit` in Coq). Running `#print axioms theorem_name` after a successful compile reveals the full axiom dependency set. If `sorryAx` appears there, the proof is a placeholder — Lean “accepted” it the way a compiler accepts `todo!()` in Rust.

The trusted axiom set for computational theorems is small: `{propext, Classical.choice, Quot.sound}`. Anything beyond that is suspect.

### A one-minute Lean example

Here is a simple function and its correctness theorem in Lean 4:

```
def addOne (n : Nat) : Nat := n + 1

theorem addOne_spec (n : Nat) : addOne n = n + 1 := by
  unfold addOne
  rfl
```

`rfl` closes the goal because both sides reduce to the same expression. The type-checker verifies this without trusting the programmer’s intuition. Now consider a more interesting statement:

```
theorem addOne_pos (n : Nat) : 0 < addOne n := by
  unfold addOne; omega
```

`omega` is a decision procedure for linear arithmetic. The proof is still machine-checked; `omega` is just a tactic that applies the decision procedure and either closes the goal or fails.

The leap from toy arithmetic to real code is what the pipeline attempts to automate.

---

## The Motivating Example: HMAC Tag Comparison

Consider these two Python functions:

```
# vulnerable: early-exit byte loop
def token_verify_vulnerable(token: bytes, expected: bytes) -> bool:
    if len(token) != len(expected):
        return False
    for a, b in zip(token, expected):
        if a != b:
            return False
    return True

# fixed: constant-time comparison
def token_verify_fixed(token: bytes, expected: bytes) -> bool:
    return hmac.compare_digest(token, expected)
```

Both are **functionally equivalent** — they return `True` if and only if `token == expected`. A verifier that only proves functional correctness would green-light both.

But they differ in cost. The vulnerable implementation returns as soon as it finds a mismatched byte. An attacker can measure the comparison time and recover the correct token byte by byte: submit `\x00...`, then `\x01...`, etc. — the first byte that takes longer to compare is a match. This is a textbook timing side-channel.

The Lean model in `RepoVerify/TokenVerify.lean` makes the distinction formal:

```
-- Both implementations satisfy the functional theorem
theorem insecureEq_correct (xs ys : List Nat) :
    insecureEq xs ys = true ↔ xs = ys := by ...

theorem ctEq_correct (xs ys : List Nat) :
    ctEq xs ys = true ↔ xs = ys := by ...

-- Only the fixed one satisfies the cost theorem
theorem ctEqCost_eq_length_when_same_length
    (xs ys : List Nat) (h : xs.length = ys.length) :
    ctEqCost xs ys = xs.length := by ...

-- The leak: vulnerable cost depends on content, not just length
example : insecureEqCost [0, 0] [1, 0] = 1 := by decide
example : insecureEqCost [0, 0] [0, 1] = 2 := by decide
```

The lesson: **a formally correct theorem can still miss the security property that matters.** You have to ask whether you proved the *right* theorem, not just *a* theorem. Running `python source/attack_demo.py` demonstrates recovery of the full secret tag from the vulnerable implementation in deterministic polynomial time.

---

## The Pipeline: Code → LLM → Lean → Five Gates

The `code2lean` pipeline generalizes this question. Given any Python function:

1. **AST extraction** — `verify/extract.py` pulls out the function body, argument types, and return type using Python’s `ast` module and packages them into a `FunctionSpec`.
2. **LLM proposer** — the function is sent to an LLM (GPT-5.5, Gemini 3.1 Pro, or Claude Opus 4.7) with a structured prompt asking it to write a complete Lean 4 file: the function definition, a correctness theorem, and a proof. The LLM picks the theorem statement freely; only the namespace and naming convention are fixed.
3. **Five validation gates:**

| Gate | What it checks | LLM in loop? |
| --- | --- | --- |
| A — sanitizer | No forbidden tokens (`sorry`, `native_decide`, `#eval` outside diagnostics) | No |
| B — Lean compile | `lake env lean` type-checks the file; on failure the error is fed back to the LLM for repair (up to 3 rounds) | Yes (repair only) |
| C — axiom allowlist | `#print axioms` output contains only `{propext, Classical.choice, Quot.sound}` | No |
| D — differential test | Lean `#eval` outputs match Python results on every fixture case | No |
| E — critic | A second LLM judges whether the theorem is strong enough (PASS / WEAK / FAIL) | Yes |

Gates A–D are mechanical. The only LLM judgment in the **verification** path is the critic (gate E), and its job is narrow: decide whether the theorem is vacuous.

### Why the critic matters: the vacuous theorem problem

Consider `bit_count8`, which counts set bits in a byte. An LLM proposer might write:

```
theorem bit_count8_spec (b : Nat) (h : b < 256) :
    bit_count8 b ≤ 8 := by ...
```

This theorem is true. Lean accepts it. Gates A–D all pass. But a constant-zero implementation (`bit_count8 b := 0`) also satisfies `result ≤ 8`. The theorem proves nothing about what the function *computes*.

The critic prompt says: “Would this theorem distinguish a correct implementation from a buggy one? If not, return WEAK.” A good proposer writes instead:

```
theorem bit_count8_spec (b : Nat) (h : b < 256) :
    bit_count8 b = (List.range 8).countP (fun i => b &&& (1 <<< i) ≠ 0) := by ...
```

This is a functional specification. Any implementation that returns a wrong bit count will fail it.

---

## A Full Walkthrough: `insecure_compare`

`examples/01_insecure_compare/source.py` contains:

```
def insecure_compare(a: bytes, b: bytes) -> bool:
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x != y:
            return False
    return True
```

The fixture in `fixture.py` provides 6 test cases: equal pairs, different-length pairs, one-off pairs, empty inputs.

A one-shot GPT-5.5 proposal (from `last_lean_openai.lean`):

```
def insecureCompare (a b : List Nat) : Bool :=
  if a.length ≠ b.length then false
  else a.zip b |>.all (fun (x, y) => x == y)

theorem insecureCompare_correct (a b : List Nat) :
    insecureCompare a b = true ↔ a = b := by
  simp [insecureCompare]
  constructor
  · intro h
    exact List.zip_eq_iff_eq.mp (List.all_zip_eq_true.mp h)
  · intro h; subst h; simp [List.all_zip_eq_true]
```

Gate A passes (no forbidden tokens). Gate B passes on the first attempt. Gate C reports `{propext, Classical.choice, Quot.sound}` — clean. Gate D: all 6 fixture cases match. Gate E: the critic returns **PASS** — the `↔ a = b` biconditional fully pins down the function’s behavior.

What this does *not* prove: that the comparison is constant-time. Exactly as designed. The pipeline proves what it can prove; the cost property requires a separate cost model, which is future work (see `docs/roadmap.md`).

---

## Benchmarks: Which LLM Proposes Bett...