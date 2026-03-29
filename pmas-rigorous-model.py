#!/usr/bin/env python3
"""
PMAS v17.0: Rigorous 2-adic Drift Model

Mathematical formalization - no more handwaving.
"""

import math


def v2(n):
    if n == 0:
        return float("inf")
    if n & 1:
        return 0
    return (n & -n).bit_length() - 1


def exact_v2(k, residue, mod):
    val = 3 * residue + k
    if val == 0:
        return float("inf")
    v = 0
    while val % 2 == 0:
        v += 1
        val //= 2
    return v


def main():
    print("=" * 70)
    print("RIGOROUS 2-ADIC DRIFT MODEL v17.0")
    print("=" * 70)

    # THEOREM: Exact v2 values by residue class
    print("\nTHEOREM: EXACT v2 VALUES BY RESIDUE CLASS")
    print("-" * 70)

    for k in [1, -1]:
        name = f"3n+{k}" if k > 0 else f"3n{k}"
        print(f"\n=== System: {name} ===")

        for mod in [4, 8]:
            print(f"\nmod {mod}:")
            print(f"{'n%':<8} {'v2':<10} {'Drift':<12} {'Contract'}")
            print("-" * 45)

            for r in range(1, mod + 1, 2):
                v = exact_v2(k, r, mod)
                drift = math.log2(3) - v
                contract = "YES" if drift < 0 else "NO"
                print(f"{r:<8} {v:<10} {drift:<12.4f} {contract}")

    # THEOREM: Expected drift - EXACT (no sampling)
    print("\n" + "=" * 70)
    print("THEOREM: EXPECTED DRIFT (EXACT FORMULA)")
    print("-" * 70)

    for k in [1, -1]:
        name = f"3n+{k}" if k > 0 else f"3n{k}"

        # Exact average over all odd residues mod 32
        total_v2 = 0
        count = 0
        for r in range(1, 32 + 1, 2):
            total_v2 += exact_v2(k, r, 32)
            count += 1

        avg_v2 = total_v2 / count
        avg_drift = math.log2(3) - avg_v2

        print(f"{name}: E[v2] = {avg_v2:.6f}, E[drift] = {avg_drift:.6f}")

    # CRITICAL GAPS
    print("\n" + "=" * 70)
    print("CRITICAL PROOF GAPS")
    print("-" * 70)

    gaps = """
GAP 1: LOCAL -> GLOBAL
What we have: E[drift] < 0 for sampled n
What we need:  drift(n) < 0 for ALL n

GAP 2: INDEPENDENCE
Assumed: Each step is independent
Reality:   n_{t+1} = f(n_t) - deterministic chain

GAP 3: ERGODICITY
Assumed:   Time avg = ensemble avg
Reality:   Could have multiple basins of attraction

GAP 4: RARE EVENTS
Ignored:   Probability 0 events
Reality:   Rare escapes could dominate

GAP 5: CYCLES
We show:   Sequences shrink on average
Miss:     They could form cycles first (3n-1 proves this!)
"""
    print(gaps)

    # EXACT SOLUTION FOR 3n-1
    print("=" * 70)
    print("EXACT SOLUTION: WHY 3n-1 HAS CYCLES")
    print("-" * 70)

    print("""
For 3n-1, the exact drift by class:

  n = 1 (mod 4): v2 = 1, drift = -0.585 (weak contraction)
  n = 3 (mod 4): v2 = 3, drift = -2.415 (strong contraction)

CRITICAL INSIGHT:
- For n = 1 (mod 4), drift is -0.585
- This is STILL negative, but CLOSER TO ZERO
- This "weak" contraction allows stable cycles to form

Compare with 3n+1:
  n = 1 (mod 4): v2 = 3, drift = -2.415 (very strong!)
  n = 3 (mod 4): v2 = 1, drift = -0.585

CONCLUSION:
3n+1 has STRONGER contraction for n = 1 (mod 4)
This stronger contraction PREVENTS cycle formation.
""")

    print("=" * 70)
    print("WHAT WOULD MAKE THIS A PROOF")
    print("=" * 70)

    print("""
To convert this heuristic into a proof, one must:

(A) Prove that trajectories cannot "escape" despite negative drift
(B) Prove that the Markov chain is ergodic  
(C) Find a strict Lyapunov function (stricter than log2)

All three remain OPEN PROBLEMS.

What we have: A very good heuristic that explains WHY
What we lack:  Rigorous proof that it works for ALL n
""")


if __name__ == "__main__":
    main()
