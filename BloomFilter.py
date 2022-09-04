from BitHash import BitHash
from BitVector import BitVector 

class BloomFilter(object):
    # Return the estimated number of bits needed in a Bloom 
    # Filter that will store numKeys (n in the slides) keys, using numHashes 
    # hash functions, and that will have a
    # false positive rate of maxFalsePositive .
  
    def __bitsNeeded(self, numKeys, numHashes, maxFalsePositive):
        phi = 1- (maxFalsePositive)**(1/numHashes)
        return int( (numHashes)/(1-phi**(1/numKeys)))
            
    
    # Create a Bloom Filter that will store numKeys keys, using 
    # numHashes hash functions, and that will have a false positive 
    # rate of maxFalsePositive.
   
    def __init__(self, numKeys, numHashes, maxFalsePositive):
        
       
        self.__numKeys= numKeys
        
        self.__numHashes= numHashes
        
        self.__maxFalsePositive= maxFalsePositive
         
         # will need to use __bitsNeeded to figure out how big
        # of a BitVector will be needed
       
        self.__size= self.__bitsNeeded(numKeys, numHashes, maxFalsePositive)
        
        self.__bitVector= BitVector (size= self.__size)
         
        self.__numBits= 0
    
    # insert the specified key into the Bloom Filter.
    # Doesn't return anything, since an insert into 
    # a Bloom Filter always succeeds!

    def insert(self, key):
        for i in range(1, self.__numHashes+1):
            k= BitHash(key, i) % self.__size
            if self.__bitVector[k] ==0:
                self.__bitVector[k]= 1
                self.__numBits+= 1
                
 
    
    # Returns True if key MAY have been inserted into the Bloom filter. 
    # Returns False if key definitely hasn't been inserted into the BF.
      def find(self, key):
        for i in range (1, self.__numHashes+1):
            k= BitHash(key, i) % self.__size
            if self.__bitVector[k] == 0:
                return False
        return True
            
       
    
       
    # Returns the PROJECTED current false positive rate based on the
    # ACTUAL current number of bits actually set in this Bloom Filter. 

       def falsePositiveRate(self):
        phi= (self.__size - self.__numBits) / self.__size
        return (1- phi)**(self.__numHashes)
        
       
    # Returns the current number of bits ACTUALLY set in this Bloom Filter
   
    def numBitsSet(self):
        return self.__numBits


       

def __main():
    numKeys = 100000
    numHashes = 4
    maxFalse = .05
    
    
    # create the Bloom Filter
    B = BloomFilter(numKeys, numHashes, maxFalse)
    
    f = open("wordlist.txt", "r")
    
    # read the first numKeys words from the file and insert them 
    # into the Bloom Filter. Close the input file.
    
    line= f.readline()

    for i in range(numKeys):
        B.insert(line)
        line= f.readline()
    
    f.close()     
  

    # Print out what the PROJECTED false positive rate should 
  
    
    print ("Projected False Positive Rate:", B.falsePositiveRate())

    # how many are missing from the Bloom Filter, 
    # This should report that 0 words are  
    # missing from the Bloom Filter.
    
    
    f = open("wordlist.txt", "r")

    numMiss=0
    line= f.readline()

    for i in range(numKeys):
        if not B.find(line):
            numMiss += 1
        line= f.readline()

    print ("Number of False Negatives:" , numMiss )
            
    
    # Read words that have never been entered to get false positives
    
    # Print out the percentage rate of false positives.

    numFalse=0
    for i in range (numKeys):
        if B.find(line)== True:
            numFalse+=1  
        line= f.readline()
            
    print ("Number of False Positives:" ,numFalse/ numKeys)
    
    f.close()     
    
    #Results
    #Projected False Positive Rate: 0.05012067788662986
    #Number of False Negatives: 0
    #Number of False Positives: 0.05022    
    
    
if __name__ == '__main__':
    __main()       

