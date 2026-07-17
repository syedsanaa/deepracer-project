## v2 - progress reward + centering + completion bonus
- Avg reward: ~493 (up from v1's ~133)
- Success rate: 0.0% (unchanged from v1)
- Diagnosis: centering reward accumulates over many steps regardless of progress,
  likely dominating the reward signal — model optimizes "stay centered longer"
  rather than "finish lap." Progress reward (+1 max) too weak relative to
  accumulated centering reward.
- Next: v3 — increase progress reward weight, reduce per-step centering dominance