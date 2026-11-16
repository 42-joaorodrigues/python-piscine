import time


def main():
    time_now = time.time()

    print(
        f"Seconds since January 1, 1970: {time_now:,.4f} "
        f"or {time_now:.2e} in scientific notation"
    )
    print(time.strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
