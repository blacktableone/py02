#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        4 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "apple" + 33
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as error:
        print(
            f"Caught ValueError: {error}"
        )

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print(
            f"Caught ZeroDivisionError: {error}"
        )

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print(
            f"Caught FileNotFoundError: {error}"
        )

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
    ) as error:
        print(
            f"Caught TypeError: {error}"
        )

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully\n")
    except Exception as error:
        print(f"caught error {error}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
