import numpy as np

def linear_beta_schedule(T, beta_1=0.0001, beta_T=0.02):
    """
    Linear noise schedule from beta_1 to beta_T.
    Returns list of floats rounded to 6 decimals.
    """
    # YOUR CODE HERE
    betas = np.linspace(beta_1, beta_T, T)
    return np.round(betas, 6).tolist()

def cosine_alpha_bar_schedule(T, s=0.008):
    """
    Cosine schedule for alpha_bar (cumulative signal retention).
    Returns list of floats rounded to 6 decimals, clipped to [0.0001, 0.9999].
    """
    # YOUR CODE HERE
    alpha_bar = []
    f_0 = np.cos((s * np.pi) / (2 * (1 + s))) ** 2
    for t in range(1, T + 1):
        f_t = np.cos((t / T + s) * np.pi / (2 * (1 + s))) ** 2
        alpha_bar.append(np.clip(f_t / f_0, 0.0001, 0.9999))
    return np.round(alpha_bar, 6).tolist()
    

def alpha_bar_to_betas(alpha_bars):
    """
    Convert alpha_bar schedule to beta schedule.
    Returns list of floats rounded to 6 decimals, clipped to [0.0001, 0.9999].
    """
    # YOUR CODE HERE
    betas = []
    prev = 1.0
    for alpha_bar in alpha_bars:
        betas.append(1 - (alpha_bar / prev))
        prev = alpha_bar
    return np.round(betas, 6).tolist()