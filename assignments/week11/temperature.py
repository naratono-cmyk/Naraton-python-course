"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""


def get_temperatures():
    temps = [31, 29, 27, 30, 28, 26, 25] 
    return temps
def analyze_temps(temp_list):

    avg_temp = sum(temp_list) / len(temp_list)
    high_temp = max(temp_list)
    low_temp = min(temp_list)
    return avg_temp, high_temp, low_temp

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg:.1f} C")
    print(f"Highest: {high} C")
    print(f"Lowest: {low} C")

input = get_temperatures()
results = analyze_temps(input)
display_analysis(*results)