import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of rules
set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot.",]
    ],
    [
        r"how are you?",
        ["I am fine, thank you! How can I help you?",]
    ],
    [
        r"I am fine, thank you",
        ["Great to hear that, how can I help you?",]
    ],
    [
        r"how can I help you?",
        ["I am looking for online guides and courses to learn data science. Can you suggest?", 
         "I am looking for data science training platforms.",]
    ],
    [
        r"I'm (.*) doing good",
        ["That's great to hear.", "How can I help you?:)",]
    ],
    [
        r"I am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website.",]
    ],
    [
        r"thanks for the suggestion. Do they have great authors and instructors?",
        ["Yes, they have world-class authors. That is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help.", "No problem, you're welcome.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon :)",]
    ],
]

# Define the chatbot function
def chatbot():
    print("Hi, I'm the chatbot you built.")
    chat = Chat(set_pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
