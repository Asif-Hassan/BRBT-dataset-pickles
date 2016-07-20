###Pickled dataset (folder)

This folder holds one `.pkl.gz` file (total three) for each individual sheet in brbt-dataset xlsx file. String/text data were tokenized first and made a tuple of [[data], [label1], [label2]] where data holds the tokens, and label1 and label2 are first validation and second validation respectively. It was then converted into numpy array and shuffled; and finally, pickled.

- **Sentiment_Analysis.pkl.gz** for `Sheet1` sheet which has both Bangla and Romanized Bangla posts.
- **Bangla_Sentiment_Analysis.pkl.gz** for `Bangla` sheet, having only the Bangla posts.
- **Romanized_Bangla_Sentiment_Analysis.pkl.gz** for `Romanized Bangla` sheet, keeping Romanized Bangla posts in one place.
