# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

flight_info = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Fancisco"), ("Steve", "Philadelphia", "Nassua"), ("Jill","Phoenix", "Aalborg" )]

def flight_itenerary(flight_info):
    for i, itenerary in enumerate(flight_info):
        name, origin, destination = itenerary 
        print(f"Itenerary {i + 1}: {name} - From {origin} to {destination}")
flight_itenerary(flight_info)