def check_hash(input_hash):
    if input_hash[:5] == '00000':
        return True
    else:
        return False
a = check_hash('00000bbb59dde95cd605bea9065f44530')
print (a)


def check_hash_prefix(hash_str):
    # Check if the input is a valid hash (must be a string of numbers)
    if not hash_str.isdigit():
        return False

    # Extract the first 5 digits of the hash
    prefix = hash_str[:5]

    # Check if the prefix is all zeros
    if prefix == '00000':
        return True
    else:
        return False

# Loop from "abcd000000" to "abcd999999"
for i in range(1000000):
    hash_value = f"abcd{i:06d}"  # Format the index as a 6-digit number with leading zeros
    result = check_hash_prefix(hash_value)

    if result:
        print(f"Found a hash with prefix '00000': {hash_value}")
        break
else:
    print("No hash with prefix '00000' found.")
