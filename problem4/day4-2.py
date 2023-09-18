import hashlib
#In part2 we should find one that starts with six zeroes
def hashLib(key, zeros = 6):
    target = '0' * zeros
    nonce = 0
    
    while True:
        data = key + str(nonce)
        data = data.encode()
        hash_hex = hashlib.md5(data).hexdigest()
        
        if hash_hex[:zeros] == target:
            return nonce
        
        nonce += 1

key = "yzbqklnj"
result = hashLib(key)
print (result)