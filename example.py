print('hello')
print()

# Побитовые операции
x = 4
y = 3
print('Bitwise OR', x | y)
print('Bitwise exclusive OR', x ^ y)
print('Bitwise AND', x & y)
print('Bit left shift', x << 3)
print('Bit right shift', x >> 1)
print('bit inversion', -x)
print()

# Адрес в памяти
string = 'Hi, '
print(id(string))
string += 'my name is Demetrius'
print(id(string))

# bytes
string_bytes = b"hello"
print(type(string_bytes))
for element in string_bytes:
    print(string_bytes)
