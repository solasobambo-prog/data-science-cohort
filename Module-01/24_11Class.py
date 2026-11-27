# ==========================================
# PART 1: WHILE LOOPS (Countdown & Savings)
# ==========================================
print("--- Part 1: While Loops ---")

sound = "Bark"
number = 3

while number > 0:
    print(sound)
    number -= 1  # Decrement to avoid an infinite loop
    print(f"Remaining count: {number}")


def weeks_to_target(target, weekly):
    if weekly <= 0:
        return 0  # Guard against infinite loop if weekly savings isn't positive
    saved = 0
    week = 0
    while saved < target:
        week += 1
        saved += weekly
        print(f"Week {week}: ${saved:,.2f}")
    return week


def main():
    target = 200000
    weekly = 25000
    weeks = weeks_to_target(target, weekly)
    print(f"Adesola hits his target in {weeks} weeks.")


main()


# ==========================================
# PART 2: FOR LOOPS & ITERABLES
# ==========================================
print("\n--- Part 2: For Loops ---")

# Looping over a list (5 iterations)
for num in range(1, 6):
    print("BOLE IS AVAILABLE!")

# Looping over a string (7 characters = 7 iterations)
for char in "ADESOLA":
    print(f"Character: {char} -> BOLE IS AVAILABLE!")


# ==========================================
# PART 3: LISTS & MUTABILITY
# ==========================================
print("\n--- Part 3: Lists & Mutability ---")

states = ["Lagos", "Ogun", "Oyo", "Ondo", "Ekiti"]

for state in states:
    print(state.upper())

# Demonstrating list mutability (modifying, adding, removing)
states[0] = "Abuja"
states.append("Osun")
states.remove("Ogun")
print("Updated states list:", states)


# ==========================================
# PART 4: INDEXING & SLICING
# ==========================================
print("\n--- Part 4: Indexing & Slicing ---")

name = "MARKSON"
fresh_states = ["Lagos", "Ogun", "Oyo", "Ondo", "Ekiti"]

print("Last letter of MARKSON:", name[-1])                 # 'N'
print("3rd-to-last state:", fresh_states[-3])              # 'Oyo'
print("First 2 letters of Lagos:", fresh_states[0][0:2])   # 'La'
print("First 3 states slice:", fresh_states[0:3])          # ['Lagos', 'Ogun', 'Oyo']
