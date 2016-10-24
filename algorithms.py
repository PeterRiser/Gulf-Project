# Preference Ranking each document per person
# Input: d is a document instance, p is a person instance
# Output: integer value weight (relevance of document to person)
# --> higher the weight, more relevant the document
def general_PRs(d,p):
    """Document->Person->int
    Generalized version of implementation.PRs

    Note from Peter:

        This should work because the way we have restructured makes it so that this list will always have a value for every 
        possible keyword anyway. This is not the most efficient way however, so we should look at optimization later

    """
    total = 0
    for word,weight in d.keywords:
        total+= weight*p.preferences[word]
    return total

    """I am messing with github"""
    # k=0
    # if (p.questionaire['works_in_industry'] and d.keywords['industry']):
    #     k+=5
    # if (p.questionaire['environmentalist'] and d.keywords['ocean']):
    #     k+=4
    # if (p.questionaire['economist'] and d.keywords['economics']):
    #     k+=5
    # if (p.questionaire['30orOlder'] and d.keywords['foradults']):
    #     k+=4
    # if (p.questionaire['likesmath'] and d.keywords['math']):
    #     k+=5
    # if (p.questionaire['hatesmath'] and d.keywords['math']):
    #     k-=7
    # if (p.questionaire['SellsOil'] and d.keywords['excessoil']):
    #     k+=5
    # if (p.questionaire['lovesanimals'] and d.keywords['animals']):
    #     k+=4
    # if (p.questionaire['isDoctor'] and d.keywords['medical']):
    #     k+=5
    # if (not p.questionaire['works_in_industry'] and d.keywords['industry']):
    #     k-=2
    # if (not p.questionaire['environmentalist'] and d.keywords['ocean']):
    #     k-=2
    # if (not p.questionaire['economist'] and d.keywords['economics']):
    #     k-=2
    # if (not p.questionaire['30orOlder'] and d.keywords['foradults']):
    #     k-=1
    # if (not p.questionaire['likesmath'] and d.keywords['math']):
    #     k-=2
    # if (not p.questionaire['SellsOil'] and d.keywords['excessoil']):
    #     k-=1
    # if (not p.questionaire['lovesanimals'] and d.keywords['animals']):
    #     k-=1
    # if (not p.questionaire['isDoctor'] and d.keywords['medical']):
    #     k-=2
    # return k


# Brute force
# Input:
#   K -- # of documents
#   docs -- list of documents
#   p -- instance of person
#   pRs -- name of preference ranking function to use
# Output:
#   sorted list of top K relevant documents for person p


def general_brute_force(K,docs,p,pRs):
    D={}
    for d in docs:
        D[d.title]=pRs(d,p)

    return [find_doc_in_list(docs,a)
            for a in sorted(D, key=D.get, reverse=True)[:K]]

def general_brute_force_iter(I,K,docs,p,pRs):
    return general_brute_force(K,docs,p,pRs)

# Brute force:
def brute_force(K):
    D={}
    for d in documents:
        D[d.title]=PRs(d)

    return sorted(D, key=D.get, reverse=True)[:K]
