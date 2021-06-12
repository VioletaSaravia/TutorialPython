print("Hello")
num_char = len("Hello")
print(num_char)


def test(test1):
    file1 = open('demo.txt', 'w')
    print(test1, file=file1)
    file1.close()


test("Hola Violeta")
