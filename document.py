class Document:
    title='' # title of document
    # data = '' /// type of data (e.g. article, video, photo, etc.)
    listed=0
    keywords={}

    # CONSTRUCTOR #
    # title is str
    # data is str of medium of document
    def __init__(self,title):
        self.title=title
        self.listed=0
        self.keywords={'social_wellbeing':0.0,'economics':0.0,'community_action':0.0,'health':0.0,\
                          'vulnerable_populations':0.0,'environment_energy':0.0,'personal_impact':0.0,\
                          'response_following':0.0,'plans_planning':0.0,'information_needs':0.0,\
                          'communicating_with_stakeholders':0.0,'tools_resources_training':0.0,\
                          'short_term':0.0,'medium_term':0.0,'long_term':0.0}

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

    def add_keyword(self,word,weight):
        self.keywords[word]=weight
    def print_keywords(self):
        print(self.keywords)
    def remove_keyword(self,word):
        self.keywords[word]=0.0
    def increase(self,n):
        self.listed+=n
    def set_keywords(self,k):
        self.keywords=k

    '''
    def __eq__(self, other):
       return PRs(self) == PRs(other)
    '''
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
