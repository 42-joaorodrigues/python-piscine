import matplotlib.pyplot as plt

from load_csv import load


def main():
    """Plot a country's life expectancy projections."""
    country = "Luxembourg"
    df = load("../assets/life_expectancy_years.csv")
    if df is None:
        return
    try:
        data = df.set_index("country").loc[country]
    except KeyError as e:
        print(f"Error: country {e} not found")
        return
    plt.plot(data.index.astype(int), data.values)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
