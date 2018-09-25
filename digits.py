import unittest

# Find the sum of all digits of an integer

def sum_of_digits_hard(num):
    # Convert the integer to a string
    s = str(num)

    # Find the length of the string to determine the place value
    places = len(s)

    # Make a list of indicies to iterate over
    indices = range(places)

    # Iterate over all the indices, find the digit,
    # and add it to the running total
    sm = 0
    for index in indices:
        n = int(s[index])
        sm += n

    return sm

def sum_of_digits_easy(num):
    # Convert the integer to a string
    s = str(num)

    # Split the string and save each digit to an array
    digits = [int(digit) for digit in s]

    # Iterate over the array
    # and sum
    sm = 0
    for digit in digits:
        sm += digit

    return sm



# Call the sum_of_digits function and then print the output
s1 = sum_of_digits_hard(321)
s2 = sum_of_digits_easy(321)

print(s1)
print(s2)


########
# TEST #
########

class SumOfDigitsTest(unittest.TestCase):
    def test_valid_3_digit_int_sum_hard(self):
        self.assertEqual(sum_of_digits_hard(321), 6)

    def test_valid_3_digit_int_sum_easy(self):
        self.assertEqual(sum_of_digits_easy(321), 6)

    def test_valid_1_digit_int_sum_hard(self):
        self.assertEqual(sum_of_digits_hard(5), 5)

    def test_valid_1_digit_int_sum_easy(self):
        self.assertEqual(sum_of_digits_easy(5), 5)

    def test_valid_0_sum_hard(self):
        self.assertEqual(sum_of_digits_hard(0), 0)

    def test_valid_0_sum_easy(self):
        self.assertEqual(sum_of_digits_easy(0), 0)


if __name__ == '__main__':
    unittest.main()