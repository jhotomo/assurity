# API Response Verification

This Python script verifies the criteria in the API response from a specified URL: https://api.tmsandbox.co.nz/v1/Categories/6329/Details.json?catalogue=false. It uses the `requests` library to fetch the API response and perform the verification for Category and Promotions element.

## Acceptance Criteria

The following acceptance criteria are checked against the API response:

- Name is "Home & garden"
- CanRelist is "true"
- The Promotions element with Name "Feature" has a Description that contains the text "Better position in category"

## Usage
1. Make sure you have Python installed on your system. You can download the latest version of Python from the official Python website (https://www.python.org) and follow the installation instructions for your operating system.

2. Set up the project directory: Create a new directory (folder) on your computer where you want to store the code. Let's call it **test_project**. Move the **test_api_categories_promotions.py** file found in https://github.com/jhotomo/pj1 into this directory.

3. Install requests library: The code depends on the requests library, which is not included with Python by default. Open a terminal or command prompt and navigate to the test_project directory. Then run the following command to install the required library:
   ```shell
   pip install requests
   
4. Run the code: After the library is installed, you can run the code. Open a terminal or command prompt, navigate to the test_project directory, and run the following command. 
   ```shell
   python3 test_api_categories_promotions.py
   
## Code overview

**fetch_response()**: Fetches the API response from the specified URL and returns it as a JSON dictionary.

**verify_criteria(data, criteria, expected_value)**: Verifies if the given criteria in the API response match the expected value specified in the test_data dictionary.

**verify_promotion(data, promotion_data)**: Verifies if the specified Name and Description in the promotion_data dictionary exist in the Promotions element of the API response.

The script fetches the API response, verifies the criteria using the verify_criteria() function, and then verifies the Promotions element using the verify_promotion() function. The results of the verification are printed to the console.
