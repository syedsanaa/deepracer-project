def reward_function(params):
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']

    # Base: centering incentive
    marker_1 = 0.25 * track_width
    marker_2 = 0.5 * track_width
    if distance_from_center <= marker_1:
        centering_reward = 1.0
    elif distance_from_center <= marker_2:
        centering_reward = 0.5
    else:
        centering_reward = 0.1

    # Progress: reward proportional to how far along the track
    progress_reward = progress / 100.0

    # Combine
    reward = centering_reward + progress_reward

    # Big bonus for finishing the lap
    if progress == 100:
        reward += 100

    # Off-track: heavily penalize
    if not all_wheels_on_track:
        reward = 1e-3

    return float(reward)