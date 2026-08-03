### TOPIC ANALYSIS OF CLOTHING REVIEWS WITH EMBEDDINGS
### * Create and store the embeddings
    * Embed the reviews using a suitable text embedding algorithm and store them as list in the variable embeddings.
### * Dimensionality reduction & visualization
    * Apply an appropriate dimensionality reduction technique to reduce the embeddings to a 2-dimensional numpy array and store this array in the variable embeddings_2d.
    * Then, use this variable to plot a 2D visual representation of the reviews.
### * Feedback categorization
    * Use your embeddings to identify some reviews that discuss topics such as 'quality', 'fit', 'style', 'comfort', etc.
### * Similarity search function
    * Write a function that outputs the closest 3 reviews to a given input review, enabling a more personalized customer service response.
    * Apply this function to the first review "Absolutely wonderful - silky and sexy and comfortable", and store the output as a list in the variable most_similar_reviews.

Welcome to the world of e-commerce, where customer feedback is a goldmine of insights! In this project, you'll dive into the Women's Clothing E-Commerce Reviews dataset, focusing on the 'Review Text' column filled with direct customer opinions.

Your mission is to use text embeddings and Python to analyze these reviews, uncover underlying themes, and understand customer sentiments. This analysis will help improve customer service and product offerings.

The Data
You will be working with a dataset specifically focusing on customer reviews. Below is the data dictionary for the relevant field:

womens_clothing_e-commerce_reviews.csv

Column	        Description
'Review Text'	Textual feedback provided by customers about their shopping experience and product quality.
Armed with access to powerful embedding API services, you will process the reviews, extract meaningful insights, and present your findings.

Let's get started!
