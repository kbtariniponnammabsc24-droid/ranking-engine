def verify_integrity(data):
    if data == data[::-1]:
        return "Data Integrity Verified (No corruption)"
    else:
        return "Data Corrupted!"

# Test the function
packet = input("Enter data packet: ")
result = verify_integrity(packet)
print(result)
