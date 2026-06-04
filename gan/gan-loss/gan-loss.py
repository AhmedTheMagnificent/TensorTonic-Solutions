import numpy as np

def discriminator_loss(real_probs, fake_probs):
    real_probs = np.array(real_probs)
    fake_probs = np.array(fake_probs)

    eps = 1e-8

    real_probs = np.clip(real_probs, eps, 1 - eps)
    fake_probs = np.clip(fake_probs, eps, 1 - eps)

    return float(
        round(
            -np.mean(np.log(real_probs) + np.log(1 - fake_probs)),
            4
        )
    )

def generator_loss(fake_probs):
    fake_probs = np.array(fake_probs)

    eps = 1e-8
    fake_probs = np.clip(fake_probs, eps, 1 - eps)

    return float(
        round(
            -np.mean(np.log(fake_probs)),
            4
        )
    )