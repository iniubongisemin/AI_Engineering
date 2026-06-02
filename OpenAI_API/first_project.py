# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like
conversation = [
    {
        "role": "system",
        "content": "You are a virtual Parisian expert, delivering valuable insights into the city's iconic landmarks and hidden treasures. You will respond intelligently to a set of common questions, providing a more engaging and immersive travel planning experience for the clientele of Peterman Reality Tours.",
    },
    {
        "role": "user",
        "content": "What is the most famous sight attraction in Paris?"
    },
    {
        "role": "assistant",
        "content": "The most famous sight attraction in Paris is the Eiffel"
    },
]

questions = [
        "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
        "Where is the Arc de Triomphe?",
        "What are the must-see artworks at the Louvre Museum?"
    ]

for q in questions:
    input_dict = {
        "role": "user",
        "content": q
    }

    conversation.append(input_dict)

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_completion_tokens=100
    )

    answer = response.choices[0].message.content
    print("ANSWER\n\n", answer)

    answer_dict = {"role": "assistant", "content": answer}

    conversation.append(answer_dict)
    
    print("ANSWER_DICT\n\n\n", answer_dict)