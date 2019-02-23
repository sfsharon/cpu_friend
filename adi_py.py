"""
Calculate working point for CPU power usage Vs. temperature
23 Feb 2019
"""

class myDB :
    """
    Wrapper class for database 
    """
    db = {1:20.3, 2:40.55, 3:89.02}

    def getVal(self, inputVal) :
        """
        Calculate working point according to inputVal
        Input  : Input val : Int
        Output : working point value : Float
        If input val is not in DB, an approximation of it value will be returned
        """
        if inputVal in self.db :
            print (self.db[inputVal])
            return self.db[inputVal]
        else :
            dbSortedItemes = sorted(d.iteritems())
            dbSize = len(dbSortedItemes)
            if dbSize == 0 :
                return None
            else


if __name__ == "__main__" :
    dbObj = myDB()
    dbObj.getVal(2)
