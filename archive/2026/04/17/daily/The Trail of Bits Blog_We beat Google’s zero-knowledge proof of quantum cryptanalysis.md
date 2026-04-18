---
title: We beat Google’s zero-knowledge proof of quantum cryptanalysis
url: https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/
source: The Trail of Bits Blog
date: 2026-04-17
fetch_date: 2026-04-18T04:31:53.035196
---

# We beat Google’s zero-knowledge proof of quantum cryptanalysis

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We beat Google’s zero-knowledge proof of quantum cryptanalysis

[Keegan Ryan](/authors/keegan-ryan/)

April 17, 2026

[cryptography](/categories/cryptography/), [zero-knowledge](/categories/zero-knowledge/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [Zero-knowledge virtual machines](#zero-knowledge-virtual-machines)
* [Google’s zkVM guest](#googles-zkvm-guest)
* [Plan of attack](#plan-of-attack)
* [Vulnerability 1: Bypassing the Toffoli counter](#vulnerability-1-bypassing-the-toffoli-counter)
* [Building a quantum circuit](#building-a-quantum-circuit)
* [Vulnerability 2: Efficient operations with register aliasing](#vulnerability-2-efficient-operations-with-register-aliasing)
* [The final challenge: Euclidean algorithm optimization](#the-final-challenge-euclidean-algorithm-optimization)
* [What Google’s secret circuit (probably) does](#what-googles-secret-circuit-probably-does)
* [The aftermath](#the-aftermath)
* [Acknowledgments](#acknowledgments)

Two weeks ago, Google’s Quantum AI group [published](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) a zero-knowledge proof of a quantum circuit so optimized, they concluded that first-generation quantum computers will break elliptic curve cryptography keys in as little as 9 minutes. Today, Trail of Bits is publishing our own zero-knowledge proof that significantly improves Google’s on all metrics. Our result is not due to some quantum breakthrough, but rather the exploitation of multiple subtle memory safety and logic vulnerabilities in Google’s Rust prover code. Google has [patched](https://arxiv.org/abs/2603.28846v2) their proof, and their scientific claims are unaffected, but this story reflects the unique attack surface that systems introduce when they use zero-knowledge proofs.

Google’s proof uses a zero-knowledge virtual machine (zkVM) to calculate the cost of a quantum circuit on three key metrics. The total number of operations and Toffoli gate count represent the running time of the circuit, and the number of qubits represents the memory requirements. Google, along with their coauthors from UC Berkeley, the Ethereum Foundation, and Stanford, published proofs for two circuits; one minimizes the number of gates, and the other minimizes qubits. Our proof improves on both.

| Resource Type | Google’s Low-Gate | Google’s Low-Qubit | Our Proof |
| --- | --- | --- | --- |
| Total Operations | 17,000,000 | 17,000,000 | 8,300,000 |
| Number of Qubits | 1,425 | 1,175 | 1,164 |
| Toffoli Count | 2,100,000 | 2,700,000 | 0 |

*Table 1: Resource upper bounds reported in different proofs for circuits computing the correct output across 9,024 randomly sampled inputs*

Our [proof](https://github.com/trailofbits/quantum-zk-proof-poc/raw/refs/heads/main/proof_trailofbits.bin) fully verifies when using Google’s unpatched [verification code](https://zenodo.org/records/19196956). It has the same verification key as their original proofs and is cryptographically indistinguishable from a zero-knowledge proof resulting from actual algorithmic improvements to the quantum circuit. We are releasing the [code](https://github.com/trailofbits/quantum-zk-proof-poc) we developed to forge the proof, and a summary of our proof follows.

**Circuit SHA-256 hash:** `0x7efe1f62bb14a978322ab9ed41d670fc0fe0f211331032615c910df5a540e999`

**Groth16 proof bytes:** `0x0e78f4db0000000000000000000000000000000000000000000000000000000000000000008cd56e10c2fe24795cff1e1d1f40d3a324528d315674da45d26afb376e8670000000000000000000000000000000000000000000000000000000000000000024ac7f8dd6b1de6279bcce54e8840d8eb20d522bf27dedd776046f6590f33add217db465201c63724e6b460641985543d2b79c3c54daeea688581676a786aafc1dba8604a361acdd9809e268b6d8bc73943a713bb0ed0d96221f73d26def6ea4041d05b077523d9351a48b2ecd984c686b6473df69d20a24296d0a1cba3cdbe92eb13a7cc0ecd92f27f7bf23f9ac859d4293e17216dcbd85d1c7f60a52f65a9d02faef077336acd39e845d534200b575b029d6e3f0afb4f90815557233eab70b0fe88919834dd9beb90d47241f1490dc202e0dce44e4894982b07073c8d4426513732d79e9af9913b254aa29471e1a98fa1b43a1886afb5dbd36988153217aa2`

**Verification key:** `0x00ca4af6cb15dbd83ec3eaab3a0664023828d90a98e650d2d340712f5f3eb0d4`

## Zero-knowledge virtual machines

Google used Succinct Labs’ SP1 zkVM for their proofs. A zkVM is essentially a way to prove that you know which *private inputs* for an arbitrary guest program on the zkVM generate some *public output*. For example, consider this basic Rust guest program.

```
#![no_main]
sp1_zkvm::entrypoint!(main);

pub fn main() {
    // Read in private inputs a and b
    let a = sp1_zkvm::io::read::<u32>();
    let b = sp1_zkvm::io::read::<u32>();
    // Add them together
    let c = a + b;
    // Write the public output a + b
    sp1_zkvm::io::commit(&c);
}
```

A user can take the private inputs 2 and 3, run this program on the zkVM, and get a proof that the program ran successfully and that the output was 5. Anyone can verify the proof, but they would get zero knowledge about whether the input was (2, 3), (1, 4), or (6, 0xffffffff). Obviously, this toy problem is simple; real programs can be significantly more complicated.

Behind the scenes, the Rust guest program compiles down to a RISC-V ELF binary. This simple architecture allows complex program logic to be encoded into provable mathematical relationships. For example, the state of the RISC-V registers after executing an instruction is a deterministic function of their state before execution. Having to prove every step makes generating zkVM proofs resource-intensive and costly, but significant engineering work has enabled proving statements about complex programs.

## Google’s zkVM guest

In the case of Google’s zero-knowledge proofs, the private input is the quantum circuit (in a custom assembly language), and the program is a simulator that checks the circuit. Note that these are “circuits” in the quantum sense, not the typical zero-knowledge definition. The public output includes bounds on the number of qubits and gate operations. In general, simulating quantum circuits is difficult, but the “kickmix” circuits defined in this paper refer to a specific subset that can be tested classically.

The following script, adapted from one of Google’s examples, increments a 3-qubit value. It includes three *operations* and a total of three *qubits*. Note that the first instruction `CCX` has two inputs (`q0` and `q1`) and computes `q2 = q2 ^ (q0 & q1)`. This is called a *Toffoli gate*. Toffoli gates are quite useful, but they’re much harder to implement on actual quantum hardware, so the complexity of quantum algorithms is sometimes measured in the number of Toffoli gates (or more accurately, non-Clifford gates). Circuits like this are serialized into bytes and sent to the zkVM simulator.

```
# Increment a value held in 3 qubits (q2, q1, q0). Sends
#     (0, 0, 0) -> (0, 0, 1)
#     (0, 0, 1) -> (0, 1, 0)
#     ...
#     (1, 1, 1) -> (0, 0, 0)

# If q0 and q1 are set, flip q2.
CCX q0 q1 q2
# If q0 is set, flip q1.
CX q0 q1
# Flip q0.
X q0
```

To verify that a circuit computes the correct function, the simulator deserializes the circuit, randomly initializes the qubits (e.g., to `(1, 0, 1)`), iteratively applies every operation in the circuit, and panics unless the final state is as expected (e.g., `(1, 1, 0)`). The simulator repeats this for many different inputs (9,024 times, to be precise), so proving that the simulator terminated without error is essentially the same as proving that the circuit is correct with high probability. In Google’s zkVM program, the circuit must compute one elliptic curve point addition, a critical subroutine of Shor’s algorithm for solving the elliptic curve discrete logarithm problem.

In addition to checking that the circuit computes the correct function, it...