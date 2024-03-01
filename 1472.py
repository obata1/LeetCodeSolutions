# Design Browser History - obata1
class BrowserHistory(object):
    

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = []
        self.backs = 0
        self.visit(homepage)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.history and self.backs<0:
            self.history = self.history[:self.backs]
            self.backs = 0
        
        self.history.append(url)
            

        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        x = len(self.history)
        if steps-self.backs < x:
            self.backs = self.backs - steps
            return self.history[self.backs-1]
        else:
            self.backs=1-x
            return self.history[self.backs-1]

        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.backs+steps<=0:
            self.backs+=steps
            return self.history[self.backs-1]
        else:
            self.backs=0
            return self.history[self.backs-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
