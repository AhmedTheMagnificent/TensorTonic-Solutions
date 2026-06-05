import numpy as np

def get_alpha_bar(betas):
    betas = np.array(betas)
    alpha_bar = np.cumprod(1 - betas)
    return np.round(alpha_bar, 6)

def forward_diffusion(x_0, t, betas, epsilon):
    x_0 = np.array(x_0)
    epsilon = np.array(epsilon)

    alpha_bar = get_alpha_bar(betas)[t - 1]

    x_t = np.round(
        np.sqrt(alpha_bar) * x_0 +
        np.sqrt(1 - alpha_bar) * epsilon,
        4
    )

    return x_t.tolist()