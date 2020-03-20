class Invoice:

#     def __init__(self, client, total):
#         self._client = client
#         self._total = total
    
#     def formatter(self):
#         return f'{self._client} owes: ${self._total}'

#     @property
#     def client(self):
#         return self._client

#     @client.setter
#     def client(self, client):
#         self._client = client

#     @property
#     def total(self):
#         return self._total

# google = Invoice('Google', 100)

# print(google.client)

# google.client = 'Yahoo'

# print(google.client)


    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'
#wraps around the property you are working with
    @property
    def client(self):
        return self._client #

    #if you want to over ride the client value
    @client.setter
    def client(self, client):
        #overide the value in the class
        self._client = client

    @property                  #two properties and these take care of our getters so this allows us to get the values of client and total.
    def total(self):
        return self._total  #

google = Invoice('Google', 100)
print(google.client)
#over ride the value
google.client = 'Yahoo'

print(google.client)

