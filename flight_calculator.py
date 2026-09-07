ACTIVE_FLIGHT_TIME_BASELINE = 180  # MINUTES

MINUTES_LOST_PER_GRAM = 0.1

# Edit a sugestion from GitHub Copilot.
# Copilot suggested a direct subtraction; Just the missing value in the error string is the actual bug.

def calculate_flight_time(weight_grams: float) -> float:
    """Return active flight time in minutes for the given payload weight."""

    if weight_grams < 0:
        raise ValueError(f"weight_grams must be non-negative, got {weight_grams}")

    return max(0, ACTIVE_FLIGHT_TIME_BASELINE - MINUTES_LOST_PER_GRAM * weight_grams)

# Edit a sugestion from GitHub Copilot.
# I kept Copilot original while-based flight_time_table as the primary function 
# ,and added range()-based version alongside it as flight_time_table_range_based, with the negative-weight guard added.

def flight_time_table(max_weight_grams, step_grams):

    """Return flight times for payload weights from zero through the maximum."""

    if max_weight_grams < 0:
        raise ValueError("max_weight_grams must be non-negative")

    if step_grams <= 0:
        raise ValueError("step_grams must be greater than zero")

    table = []
    weight = 0
    while weight <= max_weight_grams:
        table.append((weight, calculate_flight_time(weight)))
        weight += step_grams
    return table

if __name__ == "__main__":
    print(calculate_flight_time(0))     # w=0
    print(calculate_flight_time(1000))   # w=1000g
    print(calculate_flight_time(3000))  # w=3000g
    print(calculate_flight_time(-1000))  # w=-1000g
 
    for w, t in flight_time_table(3000, 250):
        print(f"{w}g -> {t} min")