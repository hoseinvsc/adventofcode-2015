def check_hash(input_hash):
    if input_hash[:5] == '00000':
        return True
    else:
        return False
a = check_hash('00000bbb59dde95cd605bea9065f44530')
print (a)