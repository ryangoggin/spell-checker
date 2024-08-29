# My spell checker (original instructions left in below)

I used python to create this spell checker, so make sure python is set up on your machine before running this.
If you do not have it installed go here and follow instructions for the desired version: https://www.python.org/downloads/
I have Python 3.9.6 on my machine, any active version (check here: https://devguide.python.org/versions/#versions) should do.
In order to run this use the following commands:
## Text file w/ misspellings (takes a while to run, time complexity is O(m*n) where m is the number of lines, n is the number of words in a line)
```
python spell-checker.py dictionary.txt file-to-check.txt
```
## Text file w/o misspellings to show that case is handled
```
python spell-checker.py dictionary.txt no-misspellings.txt
```

### Original instructions left below --------------------

# Make a spell checker!

Write a program that checks spelling. The input to the program is a dictionary file containing a list of valid words and a file containing the text to be checked.

The program should run on the command line like so:

```text
<path to your program> dictionary.txt file-to-check.txt
# output here
```

Your program should support the following features (time permitting):

- The program outputs a list of incorrectly spelled words.
- For each misspelled word, the program outputs a list of suggested words.
- The program includes the line and column number of the misspelled word.
- The program prints the misspelled word along with some surrounding context.
- The program handles proper nouns (person or place names, for example) correctly.


## Additional information

- The formatting of the output is up to you, but make it easy to understand.
- The dictionary file (`dictionary.txt` in the example above) is always a plain text file with one word per line.
- You can use the `dictionary.txt` file included in this directory as your dictionary.
- The input file (`file-to-check.txt` in the example above) is a plain text file that may contain full sentences and paragraphs.
- You should come up with your own content to run through the spell checker.
- Use any programming language, but extra credit for using Java or Kotlin.
- Feel free to fork the repo and put your code in there or create a new blank repo and put your code in there instead.
- Send us a link to your code and include instructions for how to build and run it.
- Someone from Voze will review the code with you, so be prepared to discuss your code.
