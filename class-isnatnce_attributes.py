# class Website:
#     def __init__(self, title):#>>> title of website
#         self.title = title

# ws = Website('My Website Title')
# print(ws.__dict__)# >>>dictionary

# #creating another instance(need to pass another title)
# ws_two = Website('Second Website Title')
# print(ws_two.__dict__)


#class
class DifferentWebsite:
    title = 'My class title'

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)