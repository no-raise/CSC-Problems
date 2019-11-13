# print a table of n upto 10 recursively


def print_table(n: int, limit: int) -> None:
    if limit == 0:
        return 0

    print_table(n, limit-1)
    print(f"{n} * {limit} = {n*limit}")


if __name__ == "__main__":
    print_table(20, 10)
    print_table(0, 0)
