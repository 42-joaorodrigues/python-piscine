import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def to_number(value) -> float:
    """Convert a value like '3.25M', '12.3k' or 1050 to a float."""
    multipliers = {"k": 1e3, "M": 1e6, "B": 1e9}
    value = str(value)
    if value and value[-1] in multipliers:
        return float(value[:-1]) * multipliers[value[-1]]
    return float(value)


def main():
    """Plot life expectancy against GDP per country for one year."""
    year = "1900"
    gdp = load(
        "../assets/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life = load("../assets/life_expectancy_years.csv")
    if gdp is None or life is None:
        return
    try:
        data = pd.DataFrame({
            "gdp": gdp.set_index("country")[year],
            "life": life.set_index("country")[year],
        }).map(to_number)
    except KeyError as e:
        print(f"Error: year {e} not found")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    plt.scatter(data["gdp"], data["life"], label=year)
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
