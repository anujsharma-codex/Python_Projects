print("Task 1")
with open('learning_python.txt') as file:    
     content=file.read()
     print(f"\n{content}\n{"---"*30}"*3)
print("Task 2")
with open('learning_python.txt') as file:
    content=file.read()
    print(content)
print("Task 3")
with open('learning_python.txt') as file:
    for line in file:
        print(line.strip())
print("Task 4")
Lines=[]
with open('learning_python.txt') as file:
    for line in file:
        Lines.append(line.strip())
for n in Lines:
    print(n)