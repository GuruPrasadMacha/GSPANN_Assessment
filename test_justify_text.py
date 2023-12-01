import unittest

def justify_text(input_text, page_width):
    # Validate if page_width is a positive integer
    if not isinstance(page_width, int) or page_width <= 0:
        raise ValueError("Page width must be a positive integer")

    # Validate if input_text is a non-empty string
    if not isinstance(input_text, str) or not input_text.strip():
        raise ValueError("Input text must be a non-empty string")

    # Split the input text into words
    words = input_text.split()
    
    # Initialize variables
    current_line = []
    lines = []
    line_width = 0
    
    # Iterate through words to create lines
    for word in words:
        word_length = len(word)
        
        # Check if adding the word exceeds the page width
        if line_width + word_length + len(current_line) <= page_width:
            current_line.append(word)
            line_width += word_length
        else:
            lines.append(current_line)
            current_line = [word]
            line_width = word_length
    
    # Add the last line
    if current_line:
        lines.append(current_line)
    
    # Justify the lines by adjusting spaces between words
    justified_lines = []
    for line in lines:
        num_words = len(line)
        total_word_length = sum(len(word) for word in line)
        total_spaces = page_width - total_word_length
        
        if num_words > 1:
            spaces_between_words = total_spaces // (num_words - 1)
            extra_spaces = total_spaces % (num_words - 1)
            justified_line = ""
            
            for i in range(len(line) - 1):
                justified_line += line[i] + " " * spaces_between_words
                if extra_spaces > 0:
                    justified_line += " "
                    extra_spaces -= 1
            
            justified_line += line[-1]
            justified_lines.append(justified_line.ljust(page_width))
        else:
            justified_lines.append(" ".join(line).ljust(page_width))
    
    return justified_lines

class TestJustifyText(unittest.TestCase):
    def test_small_page_width(self):
        result = justify_text("This is a sample text.", 10)
        self.assertEqual(result, ['This  is a', 'sample    ', 'text.     '])

    def test_large_page_width(self):
        result = justify_text("This is a sample text.", 20)
        self.assertEqual(result, ['This   is  a  sample', 'text.               '])

    def test_single_word(self):
        result = justify_text("Word", 5)
        self.assertEqual(result, ['Word '])

    def test_multiple_lines(self):
        result = justify_text("This is a test to check multiple lines and how the function handles them.", 15)
        self.assertEqual(result, ['This  is a test', 'to        check', 'multiple  lines', 'and   how   the', 'function       ', 'handles   them.'])

    def test_empty_input_text(self):
        with self.assertRaises(ValueError) as context:
            justify_text("", 10)
        self.assertTrue("Input text must be a non-empty string" in str(context.exception))

    def test_negative_page_width(self):
        with self.assertRaises(ValueError) as context:
            justify_text("This is a sample text.", -5)
        self.assertTrue("Page width must be a positive integer" in str(context.exception))

    def test_non_integer_page_width(self):
        with self.assertRaises(ValueError) as context:
            justify_text("This is a sample text.", "abc")
        self.assertTrue("Page width must be a positive integer" in str(context.exception))

    def test_non_string_input_text(self):
        with self.assertRaises(ValueError) as context:
            justify_text(12345, 10)
        self.assertTrue("Input text must be a non-empty string" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
