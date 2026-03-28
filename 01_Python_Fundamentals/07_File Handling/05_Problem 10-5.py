file='like_programming_reasons.txt'
with open('like_programming_reasons.txt','a', encoding='utf-8')as file:
    while True:
        reason=input("Enter why do you like programming (Press enter to stop)\n: ").strip()
        if reason=='':
            break
        file.write(reason.title()+'\n')
