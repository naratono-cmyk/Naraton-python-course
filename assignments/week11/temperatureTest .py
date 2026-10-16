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