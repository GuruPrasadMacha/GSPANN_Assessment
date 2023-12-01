# GSPANN_Assessment
Will be deleted after the evaluation

# Word Wrap Text Justifier
The `WordWrapJustifier.py` Python script justifies text input based on a specified page width without breaking words.

## Steps to Execute the Program
1. **Clone the repository:**
 git clone https://github.com/GuruPrasadMacha/GSPANN_Assessment.git
3. **Run the program:**
 cd GSPANN_Assessment
 python3 WordWrapJustifier.py or 
 python3 WordWrapJustifier_v1.py "Give your paragraph" "Give your Page Width"
 Follow the prompts to input the paragraph and page width.

## Sample Output
Input:This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.
Page Width: `20`

Output:
Array [1] = "This   is  a  sample"
Array [2] = "text      but      a"
Array [3] = "complicated  problem"
Array [4] = "to  be solved, so we"
Array [5] = "are adding more text"
Array [6] = "to   see   that   it"
Array [7] = "actually      works."

##**Input Validations**
1. **Positive Integer Page Width**: Verifies that the page_width provided to the function is a positive integer.
2. **Non-Empty String Input Text**: Checks if the input_text is a non-empty string, ensuring there's content to justify.
3. **Word Length Check:** Validates whether any word in the input text exceeds the specified page width.
I have added the below input validations for now, if we required we can add few more validations for example as below.
**Additional Input Validations (If Required):**
1. **Maximum Page Width:** Validation can be added to ensure the page_width doesn't exceed a maximum permissible value.
2. **Non-ASCII Characters in Input:** Ensures that the input_text doesn’t contain non-ASCII characters if needed.
These validations secure the function against incorrect inputs, ensuring its robustness. 

## Unit Test Cases
**Test Justification Module (test_justify_text.py)**
This Python test file (test_justify_text.py) contains a suite of test cases to validate the functionality and input validations for the justify_text function.
Execute the test cases by running the test_justify_text.py file using the command: **python3 test_justify_text.py**

**Test Cases:** **(Test Count: 8)**
1. **Test for Small Page Width**: Validates the proper justification of text when the page width is smaller than the input text length.
2. **Test for Large Page Width**: Checks if the text gets properly justified when the page width is significantly larger than the input text length.
3. **Test for Single Word**: Ensures correct justification for a single word when provided within the specified page width.
4. **Test for Multiple Lines**: Verifies the handling of multiple lines within the specified page width, ensuring accurate justification.
5. **Test for Empty Input Text**: Validates the function raises a ValueError if an empty string is provided as input.
6. **Test for Negative Page Width**: Checks if a negative integer value for the page width raises a ValueError.
7. **Test for Non-Integer Page Width**: Verifies if a non-integer value for the page width raises a ValueError.
8. **Test for Non-String Input Text**: Validates that passing a non-string input text raises a ValueError.

These test cases cover both the functional aspects and input validations to ensure the justify_text function behaves correctly under various scenarios.

Thank You!!!.
