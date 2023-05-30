import requests

# Acceptance Criteria:
# ● Name = "Home & garden"
# ● CanRelist = "true"
# ● The Promotions element with Name = "Feature" has a Description that contains the text "Better position in category"

# Test data dictionary to specify the 'criteria': 'expected values' in the API response
test_data = {
    'Name': 'Home & garden',
    'CanRelist': True,
    'Promotions': {
        'Name': 'Feature',
        'Description': 'Better position in category'
    }
}

def fetch_response():
    """
    Fetches the API response from the specified URL and returns it as JSON.
    Raises:
        requests.HTTPError: If the API request fails or returns a non-200 status code.
    Returns:
        dict: The API response data as a JSON dictionary.
    """

    api = 'https://api.tmsandbox.co.nz/v1/Categories/6329/Details.json?catalogue=false'
    response = requests.get(api)
    response.raise_for_status()
    if response.status_code == 200:
        print(f'PASSED: Got HTTP response {response.status_code}')
    else:
        print(f'FAILED: Got HTTP response {response.status_code}, instead of 200')
    return response.json()


def verify_criteria(data, criteria, expected_value):
    """Verifies if the given criteria exposed in the function call below, matches the expected value in the provided test_data."""
    actual_value = data.get(criteria)
    if actual_value == expected_value:
        print(f'PASSED: Found {criteria} = {expected_value}')
    else:
        print(f'FAILED: Did not find {criteria} = {expected_value}')



def verify_promotion(data, promotion_data):
    """
    Verifies if the specified Name and Description in the dictionary exist in the Promotions element of the json response.
    Args:
        data (dict): The data containing the Promotions element.
        promotion_data (dict): The dictionary containing the specified Name and Description.
    Prints:
        str: The result of the verification.
    """

    # Retrieves values for the key 'Promotions' from the 'data' dictionary. Returns default '[]' as an empty list.
    promotions = data.get('Promotions', [])

    #This line creates a new list called matching_promotions using a list comprehension. It iterates over each 'promo' in the 'promotions' list and checks two conditions below.
    matching_promotions = [promo for promo in promotions
                           if promo.get('Name') == promotion_data['Name']
                           and promotion_data['Description'] in promo.get('Description', '')]

    if matching_promotions:
        print(f'PASSED: Found specified Name and Description in Promotions element:\nName = {test_data["Promotions"]["Name"]}\nDescription contains {test_data["Promotions"]["Description"]}')

    else:
        print(f'FAILED: Did not find specified Name and or Description in Promotions element:\nName = {test_data["Promotions"]["Name"]}\nDescription contains {test_data["Promotions"]["Description"]}')


# Used to fetch the API response data and store it in the response_data variable.
response_data = fetch_response()

# Tests the result of verify_criteria () and verify_promotion. This is a helper function to make it easier to test the code
verify_criteria(response_data, 'Name', test_data['Name'])
verify_criteria(response_data, 'CanRelist', test_data['CanRelist'])
verify_promotion(response_data, test_data['Promotions'])
