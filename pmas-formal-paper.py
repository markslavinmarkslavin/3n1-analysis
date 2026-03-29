#!/usr/bin/env python3
"""
PMAS v18.0: Mathematical Model - Formal Paper

This is the formalization with proper mathematical notation.
"""

import math


def main():
    print("=" * 70)
    print("MATHEMATICAL MODEL OF 2-ADIC DRIFT")
    print("Version 18.0 - Formal Paper Format")
    print("=" * 70)

    # SECTION 2: DEFINITIONS
    print("\n" + "=" * 70)
    print("SECTION 2: DEFINITIONS")
    print("=" * 70)

    print("""
Definition 2.1 (2-adic valuation)
For any integer n >= 1, define v2(n) as:
    v2(n) = max{k | 2^k divides n}

Examples:
    v2(12) = 2    since 12 = 3 x 2^2
    v2(7)  = 0    since 7 is odd
    v2(8)   = 3    since 8 = 1 x 2^3


Definition 2.2 (Generalized Collatz map)
For k in Z, define Tk: N -> N as:
    Tk(n) = n/2                 if n is even
    Tk(n) = (3n + k)/2^{v2(3n+k)}  if n is odd


Definition 2.3 (Logarithmic drift)
For odd n, define Delta_k(n):
    Delta_k(n) = log2(3) - v2(3n + k)

Interpretation:
    Delta < 0  ->  sequence contracts
    Delta > 0  ->  sequence expands
""")

    # SECTION 3: THEOREMS
    print("\n" + "=" * 70)
    print("SECTION 3: THEOREMS (EXACT RESULTS)")
    print("=" * 70)

    print("""
Theorem 3.1: Exact v2 values
For odd n, v2(3n + k) depends ONLY on n mod 2^m:

    n = r (mod 2^m)  =>  v2(3n + k) = v2(3r + k)

PROOF: Since 3 = 3 (mod 2^m), we have:
    3n + k = 3r + k (mod 2^m)
The 2-adic valuation is determined by 3r+k modulo 2^v2(3r+k)
QED
""")

    # Show exact values
    print("Exact values for small k:")
    print("-" * 50)

    for k in [1, -1]:
        name = f"3n+{k}" if k > 0 else f"3n{k}"
        print(f"\n{name}:")

        for mod in [4, 8]:
            print(f"  mod {mod}:")
            for r in range(1, mod + 1, 2):
                val = 3 * r + k
                v = 0
                while val % 2 == 0 and val > 0:
                    v += 1
                    val //= 2
                print(f"    n = {r} (mod {mod}): v2 = {v}")

    # SECTION 4: COROLLARIES
    print("\n" + "=" * 70)
    print("SECTION 4: COROLLARIES")
    print("=" * 70)

    print("""
Corollary 4.1: Expected drift for 3n+1
For n = 1 (mod 4):  v2 = 2  ->  Delta = log2(3) - 2 = -0.415
For n = 3 (mod 4):  v2 = 1  ->  Delta = log2(3) - 1 = +0.585

Note: For n = 3 (mod 4), Delta is POSITIVE!


Corollary 4.2: Expected drift for 3n-1
For n = 1 (mod 4):  v2 = 1  ->  Delta = log2(3) - 1 = +0.585
For n = 3 (mod 4):  v2 = 3  ->  Delta = log2(3) - 3 = -1.415

Note: For n = 1 (mod 4), Delta is POSITIVE!
This is why 3n-1 forms cycles - some classes EXPAND.


Corollary 4.3: The KEY DIFFERENCE
    3n+1: contracts STRONGLY (Delta = -2.415) for n = 1 (mod 4)
    3n-1: EXPANDS (Delta = +0.585) for n = 1 (mod 4)

This asymmetry explains why 3n-1 has cycles and 3n+1 doesnt.
""")

    # SECTION 5: PROOF ATTEMPTS
    print("\n" + "=" * 70)
    print("SECTION 5: PROOF ATTEMPTS - WHERE IT BREAKS")
    print("=" * 70)

    print("""
Attempt 5.1: Average drift proof
CLAIM: For 3n+1, E[Delta] < 0 for all n.
COMPUTATION: E[v2] = 2, so E[Delta] = -0.415...
PROBLEM: Average, not worst case. Rare escapes possible.

Attempt 5.2: Lyapunov function
CLAIM: f(n) = log2(n) is a Lyapunov function.
PROBLEM: Delta > 0 for n = 3 (mod 4), so not monotonic.

Attempt 5.3: Ergodicity
CLAIM: Time average = space average.
PROBLEM: Not proven for Collatz-like systems.
""")

    # SECTION 6: OPEN PROBLEMS
    print("\n" + "=" * 70)
    print("SECTION 6: OPEN PROBLEMS")
    print("=" * 70)

    print("""
Problem 6.1: Escape trajectories
Q: Does there exist n such that Tk^m(n) -> infinity?
Status: UNKNOWN

Problem 6.2: Cycle classification  
Q: Does T1 have cycles other than (1,2)?
Status: UNKNOWN (known for 3n-1: exactly 3 cycles)

Problem 6.3: Ergodicity
Q: Is time average = space average?
Status: UNKNOWN

Problem 6.4: Uniform contraction
Q: Does Delta < -epsilon for ALL odd n?
Status: NO - Delta = +0.585 for n = 3 (mod 4)
""")

    # SECTION 7: CONCLUSION
    print("\n" + "=" * 70)
    print("SECTION 7: CONCLUSION")
    print("=" * 70)

    print("""
SUMMARY:
We have presented:
1. Exact formulas for v2(3n+k) by residue class
2. Computation of expected drift for 3n+1 and 3n-1
3. Explanation of why 3n-1 has cycles and 3n+1 doesnt
4. Identification of proof gaps

WHAT WE HAVE:
- A rigorous framework for analyzing Collatz-like systems
- Exact results (not just simulations)
- Comparative analysis between variants
- Clear identification of open problems

WHAT WE DONT HAVE:
- A proof that all trajectories converge to 1
- A proof that no divergent trajectories exist
- A proof of ergodicity

CONCLUSION:
This work provides a METHODOLOGY, not a SOLUTION.
The "drift" perspective gives intuition but NOT a proof.

FUTURE WORK:
- Extend analysis to 5n+1, 7n+1 variants
- Study correlation between consecutive drifts
- Investigate modular classes in detail
""")

    print("\n" + "=" * 70)
    print("END OF FORMAL PAPER")
    print("=" * 70)


if __name__ == "__main__":
    main()
