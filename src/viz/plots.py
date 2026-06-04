import matplotlib.pyplot as plt


def plot_target_balance(df, target, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 4))
    df[target].value_counts().sort_index().plot.bar(ax=ax)
    ax.set_xlabel(target)
    ax.set_ylabel("count")
    ax.set_title("Target balance")
    return ax


def plot_missing(df, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 4))
    pct = df.isna().mean().mul(100)
    pct = pct[pct > 0].sort_values()
    pct.plot.barh(ax=ax)
    ax.set_xlabel("% missing")
    ax.set_title("Missing values by column")
    return ax
