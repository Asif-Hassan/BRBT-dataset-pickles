# BRBT-dataset

This is the BRBT (Bangla and Romanized Bangla) data set (based on previous work of _**Mohammed Rashedul Amin**_, and the current version varies a lot in terms of number of posts, and polishing), a new Bangla Sentiment Analysis (SA) dataset of 9337 Bangla text samples. This set is unique because it also encompasses the till-now-ignored Romanized Bangla. Romanized Bangla is the Bangla written using English alphabets. Due to the ease of writing using any standard QWERTY keyboard and the simplicity of using English as base language for the posts, Romanized Bangla is gaining popularity not only in personal messages and microblogs but also in Govt. sanctioned mass messages/announcements. 

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
- **Removal of proper nouns:-** Proper nouns were replaced with <PN> tags to provide ambigiuity. All text samples were collected from publicly available sources and did not reflect the opinion of the authors. (The original text samples have been preserved but are not publicly available. These can be obtained by emailing the authors directly and signing the required consent form.) 
- **Manual validation (by native speakers):-** Collected data samples are manually annotated into one of three categories: positive (1), negative (0) and ambiguous (A). Each text sample was independently manually annotated by two different native Bangla speaking individuals. Each annotator validated the data without knowing decisions made by the other.
