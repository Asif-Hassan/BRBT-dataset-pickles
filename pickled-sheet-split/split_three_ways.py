import numpy as np
import gzip, cPickle
import sys

def load_data(filename):
    if filename.endswith(".gz"):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')

    if sys.version_info < (3,):
        data = cPickle.load(f)
    else:
        data = cPickle.load(f, encoding="bytes")

    f.close()
    return data  #(data, label1, label2)


def split_set_and_serialize(X, label1, label2, v_split_start, test_split_start):
""" It splits dataset (data , first validation, second validation) into 
	three sets of lengths defined by arguments v_split_start and test_split_start
	into training set, testing set and validation set. Then it re-pickles these 
	sets into pkl.gz files.
"""
	X_train = X[:v_split_start]
	y1_train = label1[:v_split_start]
	y2_train = label2[:v_split_start]

	X_val = X[v_split_start:test_split_start]
	y1_val = label1[v_split_start:test_split_start]         
	y2_val = label2[v_split_start:test_split_start]

	X_test = X[test_split_start:]
	y1_test = label1[test_split_start:]	
	y2_test = label2[test_split_start:]

	split_train_set = (X_train, y1_train, y2_train)
	split_test_set = (X_test, y1_test, y2_test)
	split_validate_set = (X_val, y1_val, y2_val)
	d = { "_train" : split_train_set, "_test" : split_test_set, "_validate" : split_validate_set }
	
	print "Splitting",fname
	fn = raw_input("Enter only name for the pickle file (extension will be added automatically): ")
	for k,v in d.items() :
		fh = fn + k + ".pkl.gz"	
		print "pickling", fh
		f = gzip.open(fh,'wb')
		cPickle.dump(v, f, protocol=2)
		f.close()

print "Enter pkl.gz filename to split into three sets and get serialized"
print "filename should be - "
print "Sentiment_Analysis.pkl.gz for Total/Sheet1"
print "Bangla_Sentiment_Analysis.pkl.gz for Bangla"
print "and Romanized_Bangla_Sentiment_Analysis.pkl.gz for Romanized Bangla"
print "Enter 'None' or keep it empty to exit..."
 
while True:
	fname = raw_input("\nEnter filename.pkl.gz : ")
	if ((fname != "None") & (fname!= "")) :
		if fname=="Sentiment_Analysis.pkl.gz" :
			# length is defined here for sheet1
			v_split_start = 7500
			test_split_start = v_split_start + 500
		elif fname=="Bangla_Sentiment_Analysis.pkl.gz" :
			# length is defined here for Bangla
			v_split_start = 5400
			test_split_start = v_split_start + 400
		elif fname=="Romanized_Bangla_Sentiment_Analysis.pkl.gz" :
			# length is defined here for Romanized Bangla
			v_split_start = 2200
			test_split_start = v_split_start + 150
		else :
			print "file doesn't exist"
			break

		X,y1,y2 = load_data(fname)
		split_set_and_serialize(X,y1,y2, v_split_start, test_split_start)
		continue

	break
