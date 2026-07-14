"PYTHON MODULARITY IN THE WILD!"

# import the numpy package
import numpy as np

# create an array class object
arr = np.array([8, 6, 7, 5, 3, 0, 9])

# use the sort method
arr.sort()

# print the sorted array
print(arr)


"LEVERAGING DOCUMENTATION"
# Load the Counter function into our environment
from collections import Counter

words = ["apple", "banana", "apple", "orange"]

# View the documentation for Counter.most_common
help(Counter.most_common)

# Example usage of Counter.most_common
top_5_words = Counter(words).most_common(5)

# Display the top 5 most common words
print(top_5_words)


"USING PYCODESTYLE"
# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)


"CONFORMING TO PEP 8"
# Assign data to x
x = [8, 3, 4]

# Print the data
print(x)


"PEP 8 IN DOCUMENTATION"
def print_phrase(phrase, polite=True, shout=False):
    if polite:  # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)
# Shout about a discovery
print_phrase('eureka', shout=True)


"NAMING PACKAGES"
# Import the package with a name that follows PEP 8
# import text_analyzer


"RECOGNIZING PACKAGES"
# Import local packages
# import py_package
# import package

# View the help for each package
help("py_package")
help("package")


"ADDING FUNCTIONALITY TO YOUR PACKAGE"
"1."
# Import needed functionality
from collections import Counter

counter = Counter(["banana", "apple", "avocado"])
plot_counter_most_common = lambda x: x["item"]

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)

"2."
# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())


"USING YOUR PACKAGE'S NEW FUNCTIONALITY"
# Import local package
# import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
# word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
# text_analyzer.plot_counter(word_count_totals)


"WRITING requirements.txt"
requirements = """
matplotlib>=3.0.0
numpy==1.15.4
pandas<=0.22.0
pycodestyle
"""
# pip install -r requirements.txt


"CREATING setup.py"
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text analysis.',
      author='Ini-ubong Isemin',
      packages=['text_analyzer'])


"LISTING requirements in setup.py"
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text analysis.',
      author='Ini-ubong',
      packages=['text_analyzer'],
      install_requires=['matplotlib==3.0.0'])


"WRITING A CLASS FOR YOUR PACKAGE"
# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of Document
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text

"IMPORT: from .document import Document >>> Because of the __init__ method"


"USING YOUR PACKAGE'S CLASS"
# Import custom text_analyzer package
# import text_analyzer

# Create an instance of Document with datacamp_tweet
# my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
# print(my_document.text)


"WRITING A NON-PUBLIC METHOD"

class Document:
  def __init__(self, text):
    self.text = text
    # pre tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # pre tokenize the document with non-public count_words
    self.word_counts = self._count_words()

  def _tokenize(self):
    # return tokenize(self.text)
    pass
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)


"USING YOUR CLASS'S FUNCTIONALITY"
datacamp_tweets = [""]
# create a new document instance from datacamp_tweets
datacamp_doc = Document(datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))


"USING INHERITANCE TO CREATE A CLASS"
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)


"ADDING FUNCTIONALITY TO A CHILD CLASS"
"1/2"
# Define a SocialMedia class that is a child of the `Document class`
filter_word_counts = lambda x: x["item"] # NOTE: DUMMY LAMBDA FUNCTION WAS ADDED BY ME 
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        help(filter_word_counts)
        return filter_word_counts(self.word_counts, first_char="#")

"2/2"
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')
    

"USING YOUR CHILD CLASS"
# Import custom text_analyzer package
text_analyzer = lambda x: x # THE LAMBDA FUNCITON IS A PLACEHOLDER
# import text_analyzer

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.word_counts)

