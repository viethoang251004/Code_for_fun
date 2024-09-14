import matplotlib.pyplot as plt
from collections import Counter
import re

def tokenize_text(text):
    # Tokenize the text into words (ignoring punctuation and converting to lowercase)
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def plot_histogram(word_frequencies, bin_count=30):
    # Plot the histogram of word frequencies
    plt.hist(word_frequencies.values(), bins=bin_count, edgecolor='black')
    plt.xlabel('Word Frequency')
    plt.ylabel('Count')
    plt.title('Word Frequency Histogram')
    plt.show()

def main():
    given_text = """In the heart of a bustling city, where the sounds of traffic and people blend into a symphony, lies a hidden oasis of tranquility. A lush, green park, adorned with colorful flowers and towering trees, welcomes visitors with open arms. The scent of freshly cut grass fills the air as children's laughter echoes through the playground.

As the sun sets, the sky turns into a canvas of warm hues, painting a breathtaking scene. Couples take leisurely strolls hand in hand, creating memories that will last a lifetime. The serene pond reflects the golden rays of the setting sun, and ducks gracefully glide across the water.

Nearby, a street performer captivates the audience with mesmerizing music, adding an artistic touch to the already enchanting atmosphere. Artists gather to paint, sketch, and express their creativity in the midst of this natural haven.

As night falls, the park transforms into a magical wonderland. Soft, twinkling lights illuminate the pathways, guiding visitors through the darkness. The night sky reveals its brilliance as stars sparkle like diamonds overhead.

At the heart of the park stands a majestic fountain, its cascading water creating a soothing melody. Families and friends gather around, enjoying the cool breeze and each other's company. The park becomes a hub of community and connection, bringing people from all walks of life together.

This hidden oasis offers respite from the chaos of everyday life, a place where one can find solace and inspiration. It serves as a reminder that amidst the concrete jungle, pockets of beauty and serenity exist, waiting to be discovered by those willing to venture off the beaten path."""

    # Tokenize the text into words
    words = tokenize_text(given_text)

    # Count the frequency of each word
    word_freq_counter = Counter(words)

    # Plot the histogram
    plot_histogram(word_freq_counter)

if __name__ == "__main__":
    main()
