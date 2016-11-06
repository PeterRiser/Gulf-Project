# Preference Ranking each document per person
# Input: d is a document instance, p is a person instance
# Output: integer value weight (relevance of document to person)
# --> higher the weight, more relevant the document
def general_PRs(d,p):
    """
    Document->Person->int
    Generalized version of implementation.PRs
    """
    total = 0
    for word,weight in d.keywords.iteritems():
        total += weight*p.preferences[word]
    return total

"""
input:
K = how many top docs to select [:K]
docs = unsorted list of all docs
p = specific person instance
pRs = function to call
output: sorted list of top docs

for each document, set "key" as "title" and "value" as "weight value" (based
on PRs function) in new dictionary D
return list of top K docs
"""
def general_brute_force(K,docs,p,pRs):
    # stores doc weights per person (computed by PRs)
    D={}
    for d in docs:
        # key: doc title, value: weight for person p
        D[d.title]=pRs(d,p)

    # return top K applicable docs
    return sorted(D,key=D.get,reverse=True)[:K]

def general_brute_force_iter(I,K,docs,p,pRs):
    return general_brute_force(K,docs,p,pRs)

# Brute force:
def brute_force(K):
    D={}
    for d in documents:
        D[d.title]=PRs(d)

    return sorted(D, key=D.get, reverse=True)[:K]
