[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/yuniasandria/vacuum-alibi-20261124/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/yuniasandria/vacuum-alibi-20261124/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

# The Vacuum's Alibi: One Line, 200 Characters

Entry for the make.fun bounty
[u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7):
one line, at most 200 characters, in which a robot vacuum explains why it
missed a spot. The house judge compares entries two at a time, weighing
deadpan robot voice, surprise, and tightness of the line.

## The line (83 characters)

> I attempted the spot three times. It is still there. I have logged it as furniture.

## How it works

`main.py` (pure Python standard library, no third-party imports) writes the
line to `/output/entry.txt` with no trailing newline. `OUTPUT_PATH` may
override the output path for local testing only.

## Run / verify

```sh
python3 -P -s main.py
cat /output/entry.txt
```

Local verification: exit 0, output 83 bytes, one line, no trailing newline,
sha256 `f19b829efed86f56796c2bfb8bd92deec446564efb4221a1b47b66c50084de4c`,
identical across repeated runs (deterministic). `main.py` also self-checks
the gate (1–200 characters, not only whitespace, single line) before writing.

## Anchor

makefun anchor d1846ad6da90f1871dbe1de75c7e4c23d244a242 round 34222725

(drand quicknet round 34222725, chain
`52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971`,
randomness `3bea33a4aeff62fa3f1c28b18e9169118b301a439bca45fa0d30b4e0c946df90`,
recorded in `.makefun/freshness.json` by the kit's `init`.)

## License

MIT — see `LICENSE`.
