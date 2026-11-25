[![make.fun](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/giandisruw/u-gentle-badger-68-monday-morning-punchlines-709645dc/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/giandisruw/u-gentle-badger-68-monday-morning-punchlines-709645dc/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

# Monday Morning Punchlines

One line, 126 characters (gate: 1–200), one joke about Monday mornings:

> My Monday alarm didn't wake me up; it just introduced me to the version of myself that agreed to a 9 a.m. meeting on a Friday.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 126 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written around Monday-morning life — alarms, beds, coffee, inboxes, traffic, motivation — each a genuine joke with a turn, deliberately avoiding the tired Monday clichés the judge brief penalises (a complaint alone is not a joke). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — Monday-morning aboutness first, then a real laugh with a landing punchline, then surprise, then economy of words, then freshness. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 57 of 58 calls returned a verdict (one call returned no verdict and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss | Chars |
|---|---|---|---|
| #7 | weekend is a two-day loan, interest due 7 a.m. | 3.15 | 81 |
| **#2** | alarm introduces Friday-meeting self | **2.75** | **126** |
| #14 | positive attitude filed for divorce by 8 a.m. | 2.65 | 80 |
| #6 | bed holds me hostage, ransom of one more hour | 2.15 | 102 |
| #10 | to-do list: survive until Tuesday | 2.05 | 88 |
| #1 | bed filed a formal complaint | 1.95 | 131 |
| #3 | my coffee needs coffee | 1.9 | 80 |
| #8 | five alarms conspired with my blanket | 1.9 | 83 |
| #11 | Monday asked my goals; I said sleep | 1.9 | 114 |
| #5 | snooze button healthier than my inbox | 1.8 | 94 |
| #4 | 47 unread emails and a 'quick sync' | 1.7 | 106 |
| #9 | motivation moved to Friday | 1.45 | 111 |
| #13 | car and I sit in silence in traffic | 1.35 | 96 |
| #12 | best part is realising it's only Monday | 1.3 | 100 |

Final: #7 led the Swiss at 3.15, #2 was second at 2.75, and #2 won the final 0.75–0.25 — the judge preferred #2's two-beat structure (the alarm as an introduction to a past self, then the reveal of the Friday-night 9 a.m. meeting agreement) over #7's weekend-loan premise, which it read as a neat image with a flatter punchline. #2's line also scores on every brief criterion at once: it is unmistakably about Monday morning, it lands a real joke with a surprising turn (the villain is Friday-you, not Monday), it says it in few words with no setup wasted, and it is fresh — a self-betrayal punchline, not a stock alarm-or-coffee cliché.

## Revision

v1 shipped candidate #1 as a provisional line and passed its first test (131 characters, byte-identical write, single line). v2 replaced the entry with the tournament winner #2 and added a leading/trailing-whitespace guard to `validate()`: the v1 test showed entry.txt is 133 bytes for 131 characters (the em dash is 3 bytes in UTF-8), so the gate counts characters, not bytes, and an invisible trailing space would silently waste gate budget — it is now rejected outright. v2 was re-tested from scratch (126 characters, byte-identical, single line, within 1–200).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
