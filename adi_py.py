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

                minKey = self.db[sortedKeys[0]]     # Lowest key value
                maxKey = self.db[sortedKeys[-1]]    # Highest key value

                if inputValue <  minKey:            # required key below lowest value
                    return self.db[minKey]
                elif inputValue >  maxKey:          # required key above highest value
                    return self.db[maxKey]
                elif inputValue in self.db.keys() : # required key has an exact key in database
                    return self.db[inputValue]
                else :                              # required key is in range, but no specific key in database
                    for count, currKey in enumerate(sortedKeys) :
                        if (inputValue > self.db[sortedKeys[count]]) and \
                           (inputValue < self.db[sortedKeys[count+1]]) :
                             return (self.db[sortedKeys[count]] + self.db[sortedKeys[count+1]]) / 2.0
                        #if count == len(sortedKeys) - 1 :       # If reached the end of the dictionay
                        #    return (self.db[sortedKeys[count-1]] + self.db[sortedKeys[count]]) / 2.0
                        #else :
                        #    return (self.db[sortedKeys[count-1]] + self.db[sortedKeys[count]]) / 2.0


if __name__ == "__main__" :
    dbObj = myDB()
    print ("Output is ", dbObj.getVal(1.5))
