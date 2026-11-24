[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=makefun&utm_medium=badge&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Ikball53/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=makefun&utm_medium=badge&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Ikball53/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=makefun&utm_medium=badge&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

# Alien Field Notes: The Two Day Earth Review

A one-line review of planet Earth, left by an alien tourist.

> Earth review: locals grow grass they never eat, then pay strangers to cut it shorter. Four stars — lovely lawns, baffling species.

**Character count:** 130 (limit: 200)

## Why this angle

Most alien-Earth lines reach for traffic, gravity, money, or the weather. This one
misreads a quieter, stranger ritual instead: humans cultivate a plant they cannot
eat, forbid themselves from enjoying it, and then pay other humans to keep trimming
it. The alien reports it deadpan, like a field note — and the verdict lands at the
end, where the tourist praises the lawns and quietly convicts the species.

## How it works

`main.py` (Python 3, standard library only) writes the line as UTF-8 bytes to
`/output/entry.txt`, with no trailing newline. It is fully deterministic — no
network, no randomness — so repeated runs produce byte-identical output. A guard
asserts the line stays within the 1–200 character limit.
