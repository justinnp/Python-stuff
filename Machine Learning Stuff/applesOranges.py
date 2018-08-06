#intro ML program
from sklearn import tree
#determing between apple and orange
#features contains weight and texture
features = [ [140,1], [130,1], [150,0], [170,0] ] #1 for smooth, 0 for bumpy
labels = [0, 0, 1, 1] #0 for apple, 1 for orange
#label cooresponds to each feature, apple1 is 140g and smooth, apple2 is 130g and smooth
#orange1 is 150g and bumpy, orange2 is 170g and bumpy
classifier = tree.DecisionTreeClassifier()
#train the algorithm by feeding in the labels and features
classifier = classifier.fit(features, labels)
 #input 160g and bumpy

print (classifier.predict([[140, 0]]))    #output 0 for apple, 1 for orange
#will output 1 because it is heavy and bumpy
