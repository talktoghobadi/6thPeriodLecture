# import the random package so we can randomize the answer
import random

# make a list of possible answers
answers = ["Answer hazy, ask again later", "Concentrate and ask again", "It is certain", "Signs point to yes", "Don't count on it", "Very doubtful"]

# Get the first question from the user
question = input("Ask the Magic 8 Ball a question or enter q to quit. ")

# Repeat while they haven't entered q
while question != "q":

  # Get an answer the the question
  ans = random.choice(answers)

  # Print the answers
  print(ans)

  # Update the question variable with a new question
  question = input("Ask another question, or enter q to quit. ")

# Say goodbye once they have quit
print("Come back soon!")
