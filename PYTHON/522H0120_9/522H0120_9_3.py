import matplotlib.pyplot as plt
from collections import Counter
import re

def tokenize_text(text):
    # Tokenize the text into words (ignoring punctuation and converting to lowercase)
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def plot_most_common_words(word_frequencies, num_words=30):
    # Get the most common words and their frequencies
    most_common = word_frequencies.most_common(num_words)
    words, frequencies = zip(*most_common)
    
    # Create a line plot to show the word frequencies
    plt.figure(figsize=(12, 6))
    plt.plot(words, frequencies, marker='o')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {num_words} Most Common Words')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def main():
    given_text = """Your given text goes here (copy-paste the provided paragraph)"""

    # Tokenize the text into words
    words = tokenize_text(given_text)

    # Count the frequency of each word
    word_freq_counter = Counter(words)

    # Plot the 30 most common words using a line plot
    plot_most_common_words(word_freq_counter)

if __name__ == "__main__":
    main()
