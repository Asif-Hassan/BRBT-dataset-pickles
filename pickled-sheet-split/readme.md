## Pickled sheet split (folder)

This folder holds `pkl.gz` files for each sheet split into three sets - training, testing and validation. So for each sheet there are three files; total three sheets make 9 files. Each split set is a tuple of [[data],[label1],[label2]] where data is the tokens, and label1 and label2 corresponds to first validation and second validation for the data. Length for the split was tried to be kept 80% of the total data as training set, 15% for testing and 5% for validation. However, the ratio couldnt be maintained in most cases. Following are the lengths taken for each datasheets.

- **Sheet1** _(Sentiment_Analysis.pkl.gz)_ :- total length 9337
    1. Training set length: 7500 _(brbt_split_train.pkl.gz)_
    2. Validation set length: 500 _(brbt_split_validate.pkl.gz)_
    3. Test set length: 1337 _(brbt_split_test.pkl.gz)_
- **Bangla** _(Bangla_Sentiment_Analysis.pkl.gz)_ :- total length 6698
    1. Training set length: 5400 _(bangla_split_train.pkl.gz)_
    2. Validation set length: 400 _(bangla_split_validation.pkl.gz)_
    3. Test set length: 898 _(bangla_split_test.pkl.gz)_
- **Romanized Bangla** _(Romanized_Bangla_Sentiment_Analysis.pkl.gz)_:- total length 2639
    1. Training set length: 2200 _(rb_split_train.pkl.gz)_
    2. Validation set length: 150 _(rb_split_validation.pkl.gz)_
    3. Test set length: 289 _(rb_split_test.pkl.gz)_

This folder also contains a simple python code _**split_three_ways.py**_ to read `.pkl.gz` files found in **pickled-dataset** folder and split them into abovementioned three sets based on the length defined in the source code. Its quite basic in terms of coding and its processes self-explanatory for users who would want to try out different length for their sets. The code expects pickled files to be in the same directory as the code file is in.
