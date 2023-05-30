# API Response Verification

This Python script verifies the criteria in the API response from a specified URL. It uses the `requests` library to fetch the API response and perform the verification for Category and Promotions element.

## Acceptance Criteria

The following acceptance criteria are checked against the API response:

- Name is "Home & garden"
- CanRelist is "true"
- The Promotions element with Name "Feature" has a Description that contains the text "Better position in category"

## Usage

1. Install the required dependencies:
   ```shell
   pip install requests
   
2. Run the Python script
   ```shell
   python3 test_api_categories_promotions.py
   
## Code overview

**fetch_response()**: Fetches the API response from the specified URL and returns it as a JSON dictionary.

**verify_criteria(data, criteria, expected_value)**: Verifies if the given criteria in the API response match the expected value specified in the test_data dictionary.

**verify_promotion(data, promotion_data)**: Verifies if the specified Name and Description in the promotion_data dictionary exist in the Promotions element of the API response.

The script fetches the API response, verifies the criteria using the verify_criteria() function, and then verifies the Promotions element using the verify_promotion() function. The results of the verification are printed to the console.
