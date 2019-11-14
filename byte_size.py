def byte_size(string):
    return len(string.encode('utf-8'))


print(byte_size('Python'))
print(byte_size('Hello Python'))