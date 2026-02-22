from sklearn.datasets import make_regression


def get_data(n_samples=1000, n_feature=5, noise=15):
    data = make_regression(
        n_samples=n_samples,
        n_features=n_feature,
        noise=noise,
        random_state=42,
    )
    return data
