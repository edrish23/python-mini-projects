from googlesearch import search

query = input("Enter query to search:")
for i in search(query, start=0 ,stop=10):
    print(i)
