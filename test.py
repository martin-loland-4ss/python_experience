
def test():

    # Import functions

    try:
        from functions import task_1, task_2
    except Exception as e:
        return print(f"ERROR: Error while loading functions\n\t{e}")

    # Test task 1

    dates = [
        "2020-01-01",
        "2020-01-02",
        "2020-01-03",
        "2020-01-04",
        "2020-01-05",
        "2020-01-06",
    ]
    values = [
        False,
        False,
        True,
        False,
        False,
        False,
    ]
    try:
        result = task_1(dates, values)
    except Exception as e:
        return print(f"ERROR: Problem running function task_1\n\t{e}")

    if not isinstance(result, list):
        return print(f'ERROR: task 1 should return a list not {type(result)}')
    for idx, item in enumerate(result):
        if not isinstance(item, str):
            return print(
                f'ERROR: item {idx} in the returned list from task 1 should be of type str, not {type(item)}'
            )

    # Test task 2
    try:
        result = task_2(pressure=80, stress_std=5229141)
    except Exception as e:
        return print(f"ERROR: Problem running function task_2\n\t{e}")
    if not isinstance(result, float):
        return print(f'ERROR: task 2 should return a float not {type(result)}')

    print('All tests passed!')


test()
