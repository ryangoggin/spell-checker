import sys
import re
from difflib import get_close_matches
# Hope using get_close_matches from difflib to get suggestions is okay!

# So you don't need to look at the docs for what get_close_matches takes as arguments, here's a brief summary of them:
# get_close_matches(word, possibilities, n=3, cutoff=0.6)
# word: a string to check against possibilities
# possibilities: a sequence of possible words to match against (the dictionary in our case)
# n: an optional integer greater than 0 that is the max number of close matches (defaults to 3)
# cutoff: an optional float in range [0,1] which is the minimum match score needed to be a "match" (defaults to 0.6)

def load_dictionary(dictionary_file):
    # Use a set for O(1) access time in the check_spelling function
    dictionary_set = set()

    with open(dictionary_file, 'r') as file:
        for word in file.readlines():
            # Remove leading and trailing spaces and convert to lower case to get consistent formatting in the dictionary set
            refined_word = word.strip().lower()
            dictionary_set.add(refined_word)

    return dictionary_set

def check_spelling(dictionary, check_file):
    with open(check_file, 'r') as file:
        lines = file.readlines()

    misspelled_words = []

    line_num = 1

    for line in lines:
        # '\b\w+\b' is a regex for matching words in a line of text, use that with re.findall() to get a list of words in each line
        words = re.findall(r'\b\w+\b', line)
        # Go through each word in the line to check for misspellings
        for word in words:
            # If the lower case word isn't in the dictionary, it is a misspelling and needs to be stored in the misspelled_words list to print results
            if word.lower() not in dictionary:
                # Use helper functions to get context and suggestions
                # Line and column can be calculated using the line_num incrementing and find() + 1 for the word in the line
                context = extract_context(line, word)
                column_num = line.find(word) + 1
                suggestions = get_close_matches(word.lower(), dictionary)
                # Append a dictionary with all the details of the misspelled word into the list
                misspelled_words.append({
                    'word': word,
                    'line': line_num,
                    'column': column_num,
                    'context': context,
                    'suggestions': suggestions
                })

        # Increment to the next line number once this line is done
        line_num += 1

    return misspelled_words

def extract_context(line, word, context_length=30):
    # The start index is either half the context length before the word OR 0 if the word is in the first half of the line
    start = max(line.find(word) - context_length // 2, 0)
    # The end index is just the start index with the context length added to it
    end = start + context_length
    # Return the slice of line of length context with any leading and trailing spaces stripped off
    return line[start:end].strip()

def print_misspelled_words(misspelled_words):
    # Format the details of each misspelled word using f strings and the details from the misspelled word dict
    for word in misspelled_words:
        print(f"Misspelled word: '{word['word']}'")
        print(f"Line: {word['line']}, Column: {word['column']}")
        print(f"Context: '{word['context']}'")
        # Suggestions is an empty list if no suggestions matched at least the 0.6 score for every word in the dictionary
        if len(word['suggestions']) > 0:
            print(f"Suggestions: {', '.join(word['suggestions'])}")
        else:
            print("No suggestions found")
        # Make a line to divide misspelled words to organize the program's output
        print("-" * 40)

# Make sure this program is only run when executed directly and not when if it gets imported
if __name__ == "__main__":
    # Program won't work properly unless 3 files are passed as arguments in the command line, print instructions if anything but 3 files are passed as args in the command line:
    if len(sys.argv) != 3:
        # Give the user the exact command for this use, followed by the general syntax to allow other dictionaries and files to check to be used
        print("For this specific use, please run this command: python spell_checker.py dictionary.txt file-to-check.txt")
        print("General command syntax: python spell_checker.py <dictionary_file> <text_file>")
        # Exit the program w/ the general exit code: 1
        sys.exit(1)

    # Use sys to get files from the command line args (MUST HAVE THE DICTIONARY AS FILE 2 AND CHECK FILE AS FILE 3)
    dictionary_file = sys.argv[1]
    check_file = sys.argv[2]

    # Run each file (and the dictioanry set) through their helper functions to get the dictionary set and misspelled words list
    dictionary = load_dictionary(dictionary_file)
    misspelled_words = check_spelling(dictionary, check_file)

    # Use the print helper function if there are misspelled words, otherwise state there were no misspelled words
    if len(misspelled_words) > 0:
        print_misspelled_words(misspelled_words)
    else:
        print("No misspelled words found.")
