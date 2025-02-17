books = [{
    'book': "book1",
    'author': "me",

},
{
    'book': "book2",
    'reviews':
    {
        'selina': "I love ittt!",
        'crystal': "the best thing i've ever read"
    }
    
},
{'book': 'book3',
 'author': 'teyewy'}]
'''
def get_reviews():
    for book in books:
        if 'reviews' in book:
            print(book['reviews'])
get_reviews()'''

'''
def test():
    reviews = [book['reviews'] for book in books if 'reviews' in book]
    print(reviews)

test()'''

#guard clause, reverse

""" user = {'username': 'test', 'age': 1}



def authenticate_user(user):
    if not user:
        return "User data missing"
    if not isinstance(user, dict):
        return "Invalid user format"
    if "username" not in user:
        return "Username missing"
    if not isinstance(user["username"], str):
        return "Invalid user format"
    if "password" not in user:
        return "password missing"                 
    if isinstance(user["password"], str):
        return "invalid password format"
    if user["username"] == "admin" and user["password"] == "securepassword":
                            return "Access Granted"
    else:
                            return "Invalid credentials" """