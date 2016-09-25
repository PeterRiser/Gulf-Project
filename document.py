class Document:
    title=''
    data=''
    listed=0
    keywords={}
    def __init__(self,t):
        self.title=t
        self.data=''
        self.listed=0
        #self.keywords={'industry':False,'economics':False,'ocean':False,'foradults':False,'medical':False,'math':False,'excessoil':False,'animals':False,\
        #               'sugar':False}
        for x in range(25):
            self.keywords[x]=True

    def __str__(self):
        return self.title
    def __repr__(self):
        s = ""
        c = getattr(self,'__class__',None)
        if c is not None:
            m = getattr(self,'__module__',None)
            if m is not None:
                s += str(m)+'.'
            m = getattr(self,'__name__','Document')
            s += str(m)
        else:
            s = "Document"
        s += '('+repr(self.title)+')'
        return s
    def add_keyword(self,word):
        self.keywords[word]=True
    def print_keywords(self):
        print(self.keywords)
    def remove_keyword(self,word):
        self.keywords[word]=False
    def increase(self,n):
        self.listed+=n
    def assign(self,k):
        self.keywords=k

    #def __eq__(self, other):
    #   return PRs(self) == PRs(other)
    def __hash__(self):
        #return hash(PRs(self))
        return keywords_hash(self.keywords)

    # not equal
    def __ne__(self, other):
        return PRs(self)!=PRs(other)
    # less than
    def __lt__(self,other):
        return PRs(self)<PRs(other)
    # less than or equal to
    def __le__(self,other):
        return PRs(self)<=PRs(other)
    # greater than
    def __gt__(self,other):
        return PRs(self)>PRs(other)
    # greater than or equal to
    def __ge__(self,other):
        return PRs(self)>=PRs(other)
