[![Update](https://github.com/hyouteki/please-hire-me/actions/workflows/update.yml/badge.svg?branch=main)](https://github.com/hyouteki/please-hire-me/actions/workflows/update.yml) &nbsp; [![Reset](https://github.com/hyouteki/please-hire-me/actions/workflows/reset.yml/badge.svg?branch=main)](https://github.com/hyouteki/please-hire-me/actions/workflows/reset.yml)

## What is this?
This repository manages a  [google spreadsheet](https://docs.google.com/spreadsheets/d/1NcB1bmKRg-j56KUsd7WNHYpkVBx0S7Jkr26LyeJW8HQ) in which leet code users (volunteers) have to mandatorily solve a specified number of questions each week. Furthermore, if they fail to do so, the repository will mark them Dead on the sheet and will not track their progress any further.

## How does this work?
There are two workflows (update and reset). The update workflow scrappes the latest 15 questions done by each alive user every 15 minutes. If any questions match the questions allocated this week, the workflow will mark it as Done. The reset workflow triggers once a week, and for any user if not found Done for questions allocated this week, the workflow will mark them as Dead and not track their progress any further.

## How to setup?
> TODO: complete this

## References
- https://www.youtube.com/watch?v=3wC-SCdJK2c
- https://developers.google.com/sheets/api/quickstart/python
