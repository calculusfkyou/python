# while True:
#     try:
#         n=int(input())
#         words=[]  
#         no_vowel=[]
#         for i in range(n):
#             words.append(input())
#             t=""
#             for j in range(len(words[i])):
#                 if words[i][j]!="A" and words[i][j]!="E" and words[i][j]!="I" and words[i][j]!="O" and words[i][j]!="U":
#                     t+=words[i][j]
#             no_vowel.append(t)
#         message=str(input())
#         temp=""
#         for i in range(len(message)):
#             temp+=message[i]
#             c=no_vowel.count(temp)
#             if c!=0:
#                 ind=no_vowel.index(temp)
#                 if i!=len(message)-1:
#                     print(words[ind],end=" ")
#                 else:
#                     print(words[ind])
#                 temp=""
#     except EOFError:
#         break
def get_no_vowel_words(words):
    no_vowel_words = set()
    for word in words:
        no_vowel = ''.join(c for c in word if c not in 'AEIOU')
        no_vowel_words.add(no_vowel)
    return no_vowel_words

def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    no_vowel_words = get_no_vowel_words(words)

    message = input()
    temp = ""
    for char in message:
        temp += char
        if temp in no_vowel_words:
            ind = [i for i, word in enumerate(words) if ''.join(c for c in word if c not in 'AEIOU') == temp]
            print(words[ind[0]], end=" ")
            temp = ""

if __name__ == "__main__":
    main()
