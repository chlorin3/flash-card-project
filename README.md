# flash-card-project
1. Reads the data from the german_words.csv file in the data folder.
2. Picks a random German word/translation and puts the word into the flashcard. Every time you press the ❌ or ✅ buttons, it generates a new random word to display.
3. After a delay of 3s, the card flips and the Polish translation for the current word is displayed.
4. When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word is removed from the list of words that might come up.
5. The updated data is saved to a new file called words_to_learn.csv
6. The next time the program is run, it checks if there is a words_to_learn.csv file. If it exists, the program uses those words to put on the flashcards. 
If the words_to_learn.csv does not exist, then it uses the words in the german_words.csv

![](https://github.com/chlorin3/flash-card-project/blob/master/flashy.gif)
