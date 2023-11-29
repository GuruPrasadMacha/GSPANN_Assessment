# GSPANN_Assessment
Will be deleted after the evaluation

# Word Wrap Text Justifier
The `WordWrapJustifier.py` Python script justifies text input based on a specified page width without breaking words.

Alternatively, you can also execute the “WordWrapJustifier_v1.py” Python script, which will also serve the same purpose but code is optimized using build in a module. 

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

## Unit Test Cases
1. **Test Case 1:**
   - Input: "This is a sample text.", Page Width: 10
   - Expected Output:
     ```
     Array [1] = "This is a"
     Array [2] = "sample"
     Array [3] = "text.    "
     ```

2. **Test Case 2:**
   - Input: "A short line.", Page Width: 15
   - Expected Output:
     ```
     Array [1] = "A short line.  "
     ```
Feel free to explore the code in this repository and run it with different inputs!

Thank You!!!.
