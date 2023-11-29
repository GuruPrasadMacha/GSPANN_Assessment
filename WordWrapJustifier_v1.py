import argparse

def justify_text(input_text, page_width):
    words = input_text.split()
    lines = []
    current_line = []
    line_width = 0

    for word in words:
        word_length = len(word)
        
        # Calculate the potential width of the line if the word is added
        potential_width = line_width + len(current_line) + word_length

        if potential_width <= page_width:
            current_line.append(word)
            line_width += word_length
        else:
            lines.append(current_line)
            current_line = [word]
            line_width = word_length

    if current_line:
        lines.append(current_line)

    justified_lines = []
    for line in lines:
        total_word_length = sum(len(word) for word in line)
        total_spaces = page_width - total_word_length
        
        if len(line) > 1:
            spaces_between_words = total_spaces // (len(line) - 1)
            extra_spaces = total_spaces % (len(line) - 1)
            justified_line = (" " * spaces_between_words).join(line)
            justified_line += " " * extra_spaces
        else:
            justified_line = line[0].ljust(page_width)
        
        justified_lines.append(justified_line)

    return justified_lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Justify text.')
    parser.add_argument('text', help='Text to justify')
    parser.add_argument('width', type=int, help='Width of the page')
    args = parser.parse_args()

    result = justify_text(args.text, args.width)
    for i, line in enumerate(result, start=1):
        print('Array [{}] = "{}"'.format(i, line))
