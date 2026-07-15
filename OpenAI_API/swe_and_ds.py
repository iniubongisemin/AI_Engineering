import math, doctest
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

"CREATING A GRANDCHILD CLASS"
# Define a Tweet class that inherits from SocialMedia 
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        # retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        # return SocialMedia(retweet_text).retweet_text
        ...

"USING INHERITED METHODS"
"1"
# Import needed package
from .dc_package import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)
"2"
# Import needed package
# import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')
"3"
# Import needed package
# import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts("hashtag_counts")


"""MAINTAINABILITY"""
"IDENTIFYING GOOD COMMENTS"
import re
text = ""
def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_1(text))


"IDENTIFYING PROPER DOCSTRINGS"
"1"
goldilocks = lambda x: x
rapunzel = lambda x: x
mary = lambda x: x
sleeping_beauty = lambda x: x
# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)
"2"
# Execute the function with most complete docstring
result = rapunzel()

# Print the result
print(result)


"WRITING DOCSTRINGS"
# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)


"USING GOOD FUNCTION NAMES"
def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse
    
    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a**2 + leg_b**2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6, 8))


"USING GOOD VARIABLE NAMES"
from statistics import mean

# Sample measurements of pupil diameter in mm
pupil_diameter = [3.3, 6.8, 7.0, 5.4, 2.7]

# Average pupil diameter from sample
mean_diameter = mean(pupil_diameter)

print(mean_diameter)


"REFACTORING FOR READABILITY"
def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len

def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator

def polygon_area(n_sides, side_len):
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2

# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))


"USING DOCTEST" #NOTE: ivar >> Instance Variable
def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = text_analyzer.Document('1 2 fizz 4 buzz fizz 7 8')
    >>> d2 = text_analyzer.Document('fizz buzz 11 fizz 13 14')
    >>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2})
    """
    return sum(counters, Counter())

doctest.testmod()


"USING PYTEST"
from collections import Counter
# from text_analyzer import SocialMedia
from .dc_package.text_analyzer import SocialMedia

# Create an instance of SocialMedia for testing
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

# Test hashtag counts are created properly
def test_social_media_hashtags():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts


"DOCUMENTING CLASSES FOR SPHINX"
# from text_analyzer import Document
from dc_package.text_analyzer import Document

class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()


