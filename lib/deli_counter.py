# lib/deli_counter.py

# Initialize an empty list to represent the queue
katz_deli = []

def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        # Create a list of formatted strings for each person in line
        formatted_line = [f"{index}. {person}" for index, person in enumerate(katz_deli,start=1)]
        return "The line is currently: " + " ".join(formatted_line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli.pop(0)
        print(f"Currently serving {serving}.")

# Example usage:
take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")

print(line(katz_deli))

now_serving(katz_deli)

print(line(katz_deli))

take_a_number(katz_deli, "Matz")

print(line(katz_deli))

now_serving(katz_deli)

print(line(katz_deli))
