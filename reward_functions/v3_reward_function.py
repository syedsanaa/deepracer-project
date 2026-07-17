def reward_function(params):
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    steps = params['steps']
    all_wheels_on_track = params['all_wheels_on_track']

    # Centering (kept, but capped lower so it can't dominate)
    marker_1 = 0.25 * track_width
    marker_2 = 0.5 * track_width
    if distance_from_center <= marker_1:
        centering_reward = 0.3
    elif distance_from_center <= marker_2:
        centering_reward = 0.15
    else:
        centering_reward = 0.05

    # Reward progress RATE, not absolute progress — pushes constant forward motion
    progress_reward = (progress / steps) * 10 if steps > 0 else 0

    reward = centering_reward + progress_reward

    # Strong completion bonus
    if progress == 100:
        reward += 200

    # Off-track: heavy penalty
    if not all_wheels_on_track:
        reward = 1e-3

    return float(reward)