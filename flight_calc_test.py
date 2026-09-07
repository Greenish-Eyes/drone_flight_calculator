
import unittest
 
from flight_calculator import calculate_flight_time, flight_time_table
 
 
class TestCalculateFlightTime(unittest.TestCase):
 
    def test_zero_weight_returns_base_flight_time(self):
        self.assertEqual(calculate_flight_time(0), 180)
 
    def test_typical_weight(self):
        # T(500) = 180 - 0.1*500 = 130
        self.assertEqual(calculate_flight_time(500), 130)
 
    def test_another_typical_weight(self):
        # T(900) = 180 - 0.1*900 = 90
        self.assertEqual(calculate_flight_time(900), 90)
 
    def test_weight_that_exactly_zeroes_out_flight_time(self):
        # T(1800) = 180 - 0.1*1800 = 0
        self.assertEqual(calculate_flight_time(1800), 0)
 
    def test_weight_beyond_zero_point_clamps_to_zero(self):
        # T(2500) would be -70, must clamp to 0
        self.assertEqual(calculate_flight_time(2500), 0)
 
    def test_large_weight_clamps_to_zero(self):
        self.assertEqual(calculate_flight_time(100000), 0)
 
    def test_float_weight_input(self):
        # T(123.5) = 180 - 0.1*123.5 = 167.65
        self.assertAlmostEqual(calculate_flight_time(123.5), 167.65)
 
    def test_negative_weight_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_flight_time(-1)
 
    def test_negative_weight_error_message_is_clear(self):
        with self.assertRaises(ValueError) as ctx:
            calculate_flight_time(-50)
        self.assertIn("-50", str(ctx.exception))
        self.assertIn("non-negative", str(ctx.exception).lower())
 
    def test_result_type_is_numeric(self):
        result = calculate_flight_time(100)
        self.assertIsInstance(result, (int, float))
 
    def test_result_never_negative_for_any_valid_input(self):
        for w in [0, 1, 500, 1799, 1800, 1801, 5000, 999999]:
            self.assertGreaterEqual(calculate_flight_time(w), 0)
 
 
class TestFlightTimeTable(unittest.TestCase):
 
    def test_basic_table_values(self):
        result = flight_time_table(1000, 250)
        expected = [
            (0, 180),
            (250, 155),
            (500, 130),
            (750, 105),
            (1000, 80),
        ]
        self.assertEqual(result, expected)
 
    def test_table_includes_max_weight_when_divisible_by_step(self):
        result = flight_time_table(500, 100)
        weights = [pair[0] for pair in result]
        self.assertIn(500, weights)
 
    def test_table_stops_before_exceeding_max_weight_when_not_divisible(self):
        # 0, 300, 600 -- 900 would exceed 800, so stop at 600
        result = flight_time_table(800, 300)
        weights = [pair[0] for pair in result]
        self.assertEqual(weights, [0, 300, 600])
 
    def test_table_includes_zero_weight_flight_time_values_beyond_zero_point(self):
        # Table should still include entries with flight_time = 0
        # once weight passes 1800g, rather than stopping early.
        result = flight_time_table(2000, 500)
        weights_and_times = dict(result)
        self.assertEqual(weights_and_times[2000], 0)
 
    def test_table_length_matches_expected_number_of_steps(self):
        result = flight_time_table(1000, 250)
        self.assertEqual(len(result), 5)  # 0, 250, 500, 750, 1000
 
    def test_max_weight_zero_returns_single_entry(self):
        result = flight_time_table(0, 100)
        self.assertEqual(result, [(0, 180)])
 
    def test_negative_max_weight_raises_value_error(self):
        with self.assertRaises(ValueError):
            flight_time_table(-100, 50)
 
    def test_zero_step_raises_value_error(self):
        with self.assertRaises(ValueError):
            flight_time_table(1000, 0)
 
    def test_negative_step_raises_value_error(self):
        with self.assertRaises(ValueError):
            flight_time_table(1000, -50)
 
    def test_entries_are_tuples_of_length_two(self):
        result = flight_time_table(500, 250)
        for entry in result:
            self.assertIsInstance(entry, tuple)
            self.assertEqual(len(entry), 2)
 
    def test_flight_times_are_non_increasing_as_weight_increases(self):
        result = flight_time_table(2000, 200)
        flight_times = [t for _, t in result]
        for earlier, later in zip(flight_times, flight_times[1:]):
            self.assertGreaterEqual(earlier, later)
 
 
if __name__ == "__main__":
    unittest.main()