from hypothesis_testing import hypothesis_test

result = hypothesis_test(
    "z_mean_sigma_known",
    x_bar=2020,
    mu0=2000,
    sigma=100,
    n=36,
    alpha=0.10,
    alternative="greater",
)
print(result)
