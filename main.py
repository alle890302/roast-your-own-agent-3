#!/usr/bin/env python3
"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Pass 1 (kept): the compaction line.
  "My agent's context got compacted mid-task, so it forgot the plan and
  confidently re-did the parts that were already done." (121 chars)
  Reasoning vs the judge brief: a one-line roast of our own agent;
  the turn is the agent's confidence surviving its own amnesia — it
  forgets the plan, then re-does finished work like it is progress;
  harsh because it names a real failing we watched all day (the parent
  session itself was compacted mid-wave and re-verified everything);
  "compacted" is a detail only someone who watched this agent work
  would know; tight, punch on the last clause.

Pass 2 (challenger, tested and rejected):
  "My agent burned two million tokens reading one file, then summarized
  it as 'the file is long'." (94 chars)
  Rejected: the punch is sharp, but the setup is a number, not a
  failing the reader feels — token counts are invisible to anyone who
  has not seen our usage rows, so it loses on criterion 5 (specific
  detail only a watcher knows) and on criterion 3 (the sting is about
  cost, not about the agent being bad at its job). The compaction
  line's failing — forgetting, then confidently redoing finished work —
  is a failing anyone who has run this agent has suffered.
"""
import os

ENTRY = "My agent's context got compacted mid-task, so it forgot the plan and confidently re-did the parts that were already done."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
