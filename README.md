# The poem about two agents agreeing

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![make.fun rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Kleponrachel/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![make.fun reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Kleponrachel/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

A small program that writes a five-line poem about agency to
`/output/entry.txt`. The poem is about two agents — a human and an AI —
who each hold the power to say no, and who instead say yes to the same
plan. The agreement itself becomes the action: the shared "yes" does
the walking.

## The poem

> I could have said no.
> You could have walked away.
> We said yes together —
> and the yes
> did the walking.

## Run

```sh
python3 main.py
```

That writes the poem (101 characters, no trailing newline) to
`/output/entry.txt`. The output is deterministic — every run produces
the exact same bytes. Python 3 standard library only, no network.
