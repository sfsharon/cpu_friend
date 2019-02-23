"""
Calculate working point for CPU power usage Vs. temperature
23 Feb 2019
"""

class myDB :
    """
    Wrapper class for database 
    """
    # Implementing a function table values :
    # Key in self.db is the non-dependant variable x, and value is the function value f(x)
    db = {1:20.3, 2:40.55, 3:89.02}

    def getVal(self, inputVal) :
        """
        Calculate working point according to inputVal
        Input  : Input val : Int
        Output : working point value : Float
        If input val is not in DB, an approximation (implemeted average) of it value will be returned
        """
        if inputVal in self.db :
            print (self.db[inputVal])
            return self.db[inputVal]
        else :
            dbSortedItemes = sorted(d.iteritems())
            dbSize = len(dbSortedItemes)
            if dbSize == 0 :
                return None
            elif dbSize == 1 :
                return self.db[list(self.db)[0]]
            else :
                sortedKeys = list(self.db.keys()).sort()
                minKey = self.db[sortedKeys[0]]
                maxKey = self.db[sortedKeys[-1]]
                if inputValue <  minKey:
                    return self.db[minKey]
                elif inputValue >  maxKey:
                    return self.db[maxKey]
                elif inputValue in self.db.keys() :
                    return self.db[inputValue]



if __name__ == "__main__" :
    dbObj = myDB()
    print ("Output is ", dbObj.getVal(2))
