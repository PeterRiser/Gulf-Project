"""
File to test algorithms
"""
from document import Document
from person import Person
from algorithms import *
import random

list_keywords = ['social_wellbeing','economics','community_action','health',\
                  'vulnerable_populations','environment_energy','personal_impact',\
                  'response_following','plans_planning','information_needs',\
                  'communicating_with_stakeholders','tools_resources_training',\
                  'short_term','medium_term','long_term']


"""
Tests documents that are 100% one category each with user preferences
"""
test_docs = []
for i in range(15):
    doc = Document("d%d" %(i))
    # make each doc fully 1 unique category
    doc.add_keyword(list_keywords[i],1.0)
    test_docs.append(doc)

# Test Person 1: Economist
# should return doc with weight 1 in economics
economist = Person("Economist", "private_business")
list_econ_docs = general_brute_force(1,test_docs,economist,general_PRs)
print list_econ_docs
#print test_docs[1].keywords
print "\n"
# Test Person 2: Public
# should return 3 docs with weights highest in short_term, medium_term, and long_term
public = Person("Public", "public")
list_pub_docs = general_brute_force(3,test_docs,public,general_PRs)
print list_pub_docs
#print test_docs[14].keywords
#print test_docs[12].keywords
#print test_docs[13].keywords
print "\n"

"""
"""

"""
Tests documents that are a random mix of categories with random
weights with user preferences
"""
test_docs = []
for i in range(100):
    doc = Document("d%d" %(i))
    # each doc has random weights in random categories
    for j in range(int(100*random.random())):
        doc.add_keyword(list_keywords[random.randint(0,14)],float("{0:.2f}".format(random.random())))
    test_docs.append(doc)

# Test Person 1: Economist
# should return doc with weight 1 in economics
economist = Person("Economist", "private_business")
list_econ_docs = general_brute_force(1,test_docs,economist,general_PRs)
print list_econ_docs
for i in list_econ_docs:
    for j in test_docs:
        if (i==j.title):
            print j.title
            print j.keywords
print "\n"
# Test Person 2: Public
# should return 3 docs with weights highest in short_term, medium_term, and long_term
public = Person("Public", "public")
list_pub_docs = general_brute_force(3,test_docs,public,general_PRs)
print list_pub_docs
for i in list_pub_docs:
    for j in test_docs:
        if (i==j.title):
            print j.title
            print j.keywords
print "\n"
