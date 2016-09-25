class Person:
    name=''
    def __init__(self,name):
        self.name=name
        # self.questionaire={}
        # for i in range(50):
        #     exec("self.questionaire['k%d']=True"%i)
        self.questionaire={'works_in_industry':False,'environmentalist':False,'economist':False,'30orOlder':False,\
                  'diabetic':False,'likesmath':False,'hatesmath':False,'SellsOil':False,'lovesanimals':False,'isDoctor':False}
        self.weights={'works_in_industry':0.0,'environmentalist':0.0,'economist':0.0,'30orOlder':0.0,\
                  'diabetic':0.0,'likesmath':0.0,'hatesmath':0.0,'SellsOil':0.0,'lovesanimals':0.0,'isDoctor':0.0}
    def Qchange(self,q):
        self.questionaire[q]=not self.questionaire[q]
    def print_q(self):
        print(self.questionaire)
    # cat is a str, w is a floating point num
    def set_weight(self,cat,w):
        self.weights[cat]=w
