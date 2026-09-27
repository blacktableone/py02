#!usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    tmp = int(temp_str)

    if tmp < 0:
        raise ValueError(
            f" {tmp}°C is too cold for plants (min 0°C)"
         )
    if tmp > 40:
        raise ValueError(
            f" {tmp}°C is too hot for plants (max 40°C)"
        )
    return tmp


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

    print("Input data is'100'")
    try:
        tmp = input_temperature("100")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")

    print("Input data is'-50'")
    try:
        tmp = input_temperature("-50")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
