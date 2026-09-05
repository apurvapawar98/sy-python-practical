feedback = input("Enter your feedback: ")

target_words = ["bad", "hate", "worst"]

for word in target_words:
    feedback = feedback.replace(word, "***")

print("Moderated Feedback:", feedback)