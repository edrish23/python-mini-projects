import wikipedia

query = wikipedia.summary(input("enter your query:"),sentences = 2)
print(query)
