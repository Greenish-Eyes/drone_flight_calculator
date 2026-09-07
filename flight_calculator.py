ACTIVE_FLIGHT_TIME_BASELINE = 180  # MINUTES

MINUTES_LOST_PER_GRAM = 0.1

# Accept a sugestion from GitHub Copilot.
# Copilot suggested a direct subtraction; edited to include an explicit zero‑floor clamp

def calculate_flight_time(weight_grams: float) -> float:

    """Return active flight time in minutes for the given payload weight."""

    if weight_grams < 0:
        raise ValueError("weight_grams must be non-negative")

    return max(0, ACTIVE_FLIGHT_TIME_BASELINE - MINUTES_LOST_PER_GRAM * weight_grams)

# Accept a sugestion from GitHub Copilot.
# Copilot proposed a simple range loop; kept structure but clarified step validation

def flight_time_table(max_weight_grams: int, step_grams: int) -> list[tuple[int, float]]:

    """Return flight times for payload weights from zero through the maximum."""

    if step_grams <= 0:
        raise ValueError("step_grams must be greater than zero")

    return [
        (weight, calculate_flight_time(weight))
        for weight in range(0, max_weight_grams + 1, step_grams)
    ]

if __name__ == "__main__":
    print(calculate_flight_time(0))     # w=0
    print(calculate_flight_time(1000))   # w=1000g
    print(calculate_flight_time(3000))  # w=3000g
    print(calculate_flight_time(-1000))  # w=-1000g
 
    for w, t in flight_time_table(3000, 250):
        print(f"{w}g -> {t} min")