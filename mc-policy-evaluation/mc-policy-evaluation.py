import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):

    state_values = np.zeros(n_states)
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)

    for episode in episodes:

        T = len(episode)
        returns = np.zeros(T)

        # Compute returns backward
        G = 0
        for t in reversed(range(T)):
            state, reward = episode[t]
            G = gamma * G + reward
            returns[t] = G

        visited = set()

        # Now go FORWARD for first-visit
        for t in range(T):
            state, _ = episode[t]

            if state not in visited:
                visited.add(state)
                returns_sum[state] += returns[t]
                returns_count[state] += 1
                state_values[state] = returns_sum[state] / returns_count[state]

    return state_values