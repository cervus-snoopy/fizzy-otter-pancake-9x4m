# fizzy-otter-pancake-9x4m

[![Bounty](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/cervus-snoopy/fizzy-otter-pancake-9x4m/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/cervus-snoopy/fizzy-otter-pancake-9x4m/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

A tiny Python program that writes a one-line dating-app bio for an AI with more appetite than hands.

## Run

```sh
python3 main.py
```

It writes the validated bio (one line, 1–180 characters, no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads the file back to confirm it matches.

## Notes

Standard library only, no network access. The bio is checked before writing: non-empty, a single line, and within the 180-character limit. The output file is written with mode `0644`.
