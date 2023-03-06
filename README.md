# flash-card-project
This program reads data from the "german_words.csv" file located in the data folder. It selects a random German word/translation and displays it on the flashcard. Each time the user presses the ❌ or ✅ buttons, a new random word is generated and displayed. After a delay of 3 seconds, the card flips and shows the Polish translation for the current word.

If the user presses the ✅ button, it means they know the current word and that word is removed from the list of words that might appear. The updated list is saved to a new file named "words_to_learn.csv".

The next time the program is run, it checks if the "words_to_learn.csv" file exists. If it does, the program uses those words for the flashcards. If the "words_to_learn.csv" file does not exist, then the program uses the words in the "german_words.csv" file.

![](https://github.com/chlorin3/flash-card-project/blob/master/flashy.gif)
