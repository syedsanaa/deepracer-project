## v2 - progress reward + centering + completion bonus
- Avg reward: ~493 (up from v1's ~133)
- Success rate: 0.0% (unchanged from v1)
- Diagnosis: centering reward accumulates over many steps regardless of progress,
  likely dominating the reward signal — model optimizes "stay centered longer"
  rather than "finish lap." Progress reward (+1 max) too weak relative to
  accumulated centering reward.
- Next: v3 — increase progress reward weight, reduce per-step centering dominance

## v3 - fixed reward hacking (progress rate vs absolute progress)
- Avg reward: 443.32
- 3/3 evaluation trials reached 100% completion_percentage (verified via S3 
  evaluation JSON + log-analysis notebook plots)
- Each trial had 1 off-track event + auto-reset before reaching completion - 
  not a clean lap, but genuine task completion
- NOTE: dr-logs-robomaker / docker logs "Success rate" check reported 0.0% for 
  this same run - inconsistent with S3 ground truth (JSON metrics + notebook 
  trace data both confirm 100% completion). Root cause unconfirmed, likely 
  reading a stale/different container's logs after a session disconnect. 
  Treating S3 JSON as authoritative source going forward.
- Next: v4 - reduce off-track recovery events, aim for clean laps