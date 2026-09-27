#!/usr/bin/env python3

class GardenError(Exception):  # what is here
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water:'{plant_name}'")
    print(f"Watering {plant_name}: [OK]")  # Prints a message on success


def test_watering_system() -> None:
    print("= Garden Watering System ===\n")

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrot")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrot")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


def main() -> None:
    test_watering_system()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
