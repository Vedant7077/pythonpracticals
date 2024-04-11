class Degree:
    def get_degree(self):
        print("I got a degree")
class undergraduate(Degree):
    def get_degree(self):
        print("I am undergraduate")
class postgraduate(Degree):
    def get_degree(self):
        print("I am postgraduate")
degree = Degree()
degree.get_degree()

under = undergraduate()
under.get_degree()

post = postgraduate()
post.get_degree()