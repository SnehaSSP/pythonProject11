import random
import string

ran_letter = []


# generate random string
def generate_random_string(length=10):
    letters = string.ascii_letters
    for i in range(length):
        ran_letter.append(random.choice(letters))
    result_string = ''.join(ran_letter)
    return result_string


"""string1 = generate_random_string()
print(string1)"""


def generate_random_number(min_val=1, max_val=100):
    """Generate a random number within the specified range."""
    return random.randint(min_val, max_val)


def generate_test_data(num_samples):
    """Generate smart test data based on different test scenarios."""
    test_data = []

    for _ in range(num_samples):
        # Generate test data for different scenarios (you can add more as needed)
        scenario = random.choice(['positive', 'negative', 'boundary'])

        if scenario == 'positive':
            # Generate positive test data (e.g., valid input values)
            data = generate_random_string()  # For simplicity, generating a random string
        elif scenario == 'negative':
            # Generate negative test data (e.g., invalid input values)
            data = generate_random_string() + '@'  # Adding an invalid character to the string
        else:
            # Generate boundary test data (e.g., edge cases)
            data = generate_random_number(0, 100)  # For simplicity, generating a random number

        test_data.append({'Scenario': scenario, 'Data': data})

    return test_data

# test data samples

if __name__ == '__main__':
    num_samples = 10  # Number of test data samples to generate
    test_data = generate_test_data(num_samples)

    for i, data in enumerate(test_data):
        print(f"Sample {i + 1}: Scenario '{data['Scenario']}' - Data: {data['Data']}")
