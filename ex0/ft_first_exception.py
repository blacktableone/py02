#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    print("Input data is'25'")
    try:
        tmp = input_temperature("25")
        print(f"Temperature is now {tmp}°C\n")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")

    print("Input data is'abc'")
    try:
        tmp = input_temperature("abc")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
