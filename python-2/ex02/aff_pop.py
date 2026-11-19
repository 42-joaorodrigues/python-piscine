import matplotlib.pyplot as plt

from load_csv import load


def to_number(value) -> float:
    """Convert a population string like '3.25M' or '127k' to a float."""
    multipliers = {"k": 1e3, "M": 1e6, "B": 1e9}
    value = str(value)
    if value and value[-1] in multipliers:
        return float(value[:-1]) * multipliers[value[-1]]
    return float(value)


def format_population(value, position) -> str:
    """Format a y-axis tick like 20000000 as '20M' or 500000 as '500k'."""
    if value >= 1e6:
        return f"{value / 1e6:g}M"
    if value >= 1e3:
        return f"{value / 1e3:g}k"
    return f"{value:g}"


def main():
    """Plot the population of two countries from 1800 to 2050."""
    countries = ["Luxembourg", "Iceland"]
    df = load("../assets/population_total.csv")
    if df is None:
        return
    try:
        data = df.set_index("country").loc[countries, "1800":"2050"]
        data = data.map(to_number)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
        return
    for country, row in data.iterrows():
        plt.plot(row.index.astype(int), row.values, label=country)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.gca().yaxis.set_major_formatter(format_population)
    plt.show()


if __name__ == "__main__":
    main()
