# 3n-1 Sequence Analyzer

**Complete cycle analysis for the 3n-1 sequence up to n = 1,000,000**

## Results

- **Unique Cycles Found:** 3
- **Numbers Verified:** 1,000,000
- **Diverging Sequences:** 0

## The Three Cycles

| Length | Values | Range |
|--------|--------|-------|
| 2 | (1, 2) | 1-2 |
| 5 | (5, 14, 7, 20, 10) | 5-20 |
| 18 | (17, 50, 25, 74, 37, 110, 55, 164, 82, 41, 122, 61, 182, 91, 272, 136, 68, 34) | 17-272 |

## Distribution

- Cycle (1,2): 32.8%
- Cycle (5,14,7,20,10): 26.7%
- 18-element cycle: 19.7%
- Other rotations: 20.8%

## Run Yourself

```bash
cd my_life_os/tools
python pmas-3n-1-deep.py 1000000
```

## Live Demo

Open [index.html](index.html) in a browser.

## See Also

- [Collatz Analysis](https://markslavinmarkslavin.github.io/collatz-verification/)
