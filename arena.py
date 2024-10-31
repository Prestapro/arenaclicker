import pyautogui
import time

# List of coordinates to click initially
INITIAL_COORDINATES = [(1149, 288), (1167, 382), (1155, 484), (1141, 596), (1148, 699), (1154, 817), (1149, 919), (1139, 1023), (1149, 1135), (1163, 1239)]

# Coordinate for intermediate clicks
INTERMEDIATE_COORDINATE = (1154, 1306)

# Coordinate for repeated clicks
REPEAT_COORDINATE = (764, 1305)

# Function to click at specified coordinates and write to console log
def click_and_log(coordinates):
    x, y = coordinates
    pyautogui.click(x, y)
    print(f"Clicked at coordinates: ({x}, {y})")

# Main function
def main():
    # Click at initial coordinates, then INTERMEDIATE_COORDINATE, and finally REPEAT_COORDINATE
    for coordinates in INITIAL_COORDINATES:
        click_and_log(coordinates)
        time.sleep(2)  # Initial delay of 2-3 seconds

        click_and_log(INTERMEDIATE_COORDINATE)
        time.sleep(60)  # Click at INTERMEDIATE_COORDINATE every 20 seconds

        # Click at REPEAT_COORDINATE twice with a timeout of 2-3 seconds between each click
        for _ in range(2):
            click_and_log(REPEAT_COORDINATE)
            time.sleep(2)  # Adjust the timeout as needed
            click_and_log(REPEAT_COORDINATE)
            time.sleep(2)  # Adjust the timeout as needed

if __name__ == "__main__":
    main()