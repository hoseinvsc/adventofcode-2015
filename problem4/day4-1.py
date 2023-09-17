import hashlib
def hashLib(key, zeros = 5):
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