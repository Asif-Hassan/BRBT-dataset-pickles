# BRBT-dataset-pickles

These are the pickled files ready to be fed into a Neural Network model for Sentiment Analysis. 
This is actually based on an ongoing thesis work done by me and a number of co-authors. For greater detail on this unpublished work please check [here](https://arxiv.org/abs/1610.00369) (you can use it to cite as well in case you used these pickle files)


###Data Statistic:
  - Total number of posts: 9337   (no of rows in sheet 9338)
  - Bangla posts: 6698            (no of rows in sheet 6699)
  - Romanized Bangla posts: 2639  (no of rows in sheet 2640)

####Data Sources

Data were collected from various microblog sites, such as, Facebook, Twitter, YouTube etc, and some online news portal, product review panels etc. Following is the statistic of data sources -
- From Facebook: 4621
- From Twitter: 2610
- From YouTube: 801
- From online news portals: 1255
- From product review pages: 50

####Post collection processing

- **Removal of emoticons:-** emoticon, hash-tags were removed to give annotators an unbiased-text-only content to make a decision based on three criteria - positive, negative and ambigious. 
- **Removal of proper nouns:-** Proper nouns were replaced with <PN> tags to provide ambigiuity. All text samples were collected from publicly available sources and did not reflect the opinion of the authors. (The original text samples have been preserved but are not publicly available for some technical issues. These may be obtained by emailing the authors directly and signing the required consent form.) 
- **Manual validation (by native speakers):-** Collected data samples are manually annotated into one of three categories: positive (1), negative (0) and ambiguous (A). Each text sample was independently manually annotated by two different native Bangla speaking individuals. Each annotator validated the data without knowing decisions made by the other.

###Accessing the dataset

These pickled files are made from a BRBT (Bangla and Romanized Bangla) Sentiment Analysis (SA) dataset of 9337 Bangla text samples. The dataset is unique because it also encompasses the till-now-ignored Romanized Bangla. Romanized Bangla is the Bangla written using English alphabets. Due to the ease of writing using any standard QWERTY keyboard and the simplicity of using English as base language for the posts, Romanized Bangla is gaining popularity not only in personal messages and microblogs but also in Govt. sanctioned mass messages/announcements. **The dataset (xlsx file) itself is NOT available publicly at the moment, but it may be made available by personally contacting the authors via email**
