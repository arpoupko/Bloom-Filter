
import random
import time

# setup a list of random 64-bit values to be used by BitHash
__bits = [0] * (64*1024)
__rnd = random.Random()

# A bunch of seeds to be used to start the hashing and
# create the equivalent of many different hash functions
__BitHashSeeds = None
__MAX_SEEDS = 1000

# seed the generator to produce repeatable results
__rnd.seed("BitHash random numbers") 

# fill the list of hashing values
for i in range(64*1024): 
    __bits[i] = __rnd.getrandbits(64)

def BitHash(s, hashFuncNum = 1):
    s = str(s)
    h = __BitHashSeeds[hashFuncNum-1]
    for c in s: 
        h  = (((h << 1) | (h >> 63)) ^ __bits[ord(c)])
        h &= 0xffffffffffffffff
    return h

# this function causes subsequent calls to BitHash to be based on new random 
# seeds. This is useful in the event that client code needs a new hash 
# function, for example, for Cuckoo Hashing. 
def ResetBitHash():
    global __BitHashSeeds
    if not __BitHashSeeds: __BitHashSeeds = [0] * __MAX_SEEDS
    for i in range(__MAX_SEEDS): 
        __BitHashSeeds[i] = __rnd.getrandbits(64) 
        
ResetBitHash() # set up the seeds in advance of the first BitHash call  


def __main():
    # use BitHash to get two hash values for each of a bunch of strings
    # and print them out.
    v1 = BitHash("foo");  v2 = BitHash("foo", 2);  print(hex(v1), hex(v2))
    v1 = BitHash("bar");  v2 = BitHash("bar", 2);  print(hex(v1), hex(v2))
    v1 = BitHash("baz");  v2 = BitHash("baz", 2);  print(hex(v1), hex(v2))
    v1 = BitHash("blat"); v2 = BitHash("blat",2);  print(hex(v1), hex(v2))
    
    # now reset BitHash so that it is effectively a new set of hash functions, 
    # and print out the hash values for the same words.
    print("\nresetting BitHash to a new set of hash functions\n")
    ResetBitHash()
    
    v1 = BitHash("foo");  v2 = BitHash("foo", 2);  print(hex(v1), hex(v2))
    v1 = BitHash("bar");  v2 = BitHash("bar", 2);  print(hex(v1), hex(v2))
    v1 = BitHash("baz");  v2 = BitHash("baz", 2);  print(hex(v1), hex(v2))
    v1 = BitHash("blat"); v2 = BitHash("blat",2);  print(hex(v1), hex(v2))

    # now reset BitHash again so that it is effectively yet another set of 
    # hash functiona, and print out the hash values for the same words.
    print("\nresetting BitHash to yet another set of hash functions\n")
    ResetBitHash()
    
    v1 = BitHash("foo");  v2 = BitHash("foo", 3);  print(hex(v1), hex(v2))
    v1 = BitHash("bar");  v2 = BitHash("bar", 3);  print(hex(v1), hex(v2))
    v1 = BitHash("baz");  v2 = BitHash("baz", 3);  print(hex(v1), hex(v2))
    v1 = BitHash("blat"); v2 = BitHash("blat",3);  print(hex(v1), hex(v2))

def __main2():
    numBuckets = int(input("How many buckets? "))
    while True:
        s = input("string to hash? ")
        hashValue = BitHash(s) % numBuckets
        print("Hash value:", hashValue)
        
if __name__ == '__main__':
    __main()       
                
                       

