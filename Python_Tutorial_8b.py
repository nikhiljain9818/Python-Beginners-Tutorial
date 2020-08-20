# ask user for the following input and print as dictionary
# {'name', 'age', 'fav_movies', 'fav_songs'}

user = {}
name = input("Enter Name: ")
age = int(input("Enter your age: "))
fav_movie = input("Enter your FAV movies sep by comma: ").split(",")
fav_songs = input("Enter your FAV songs sep by comma: ").split(",")

user['name'] = [name]
user['age'] = [age]
user['fav_movies'] = [fav_movie]
user['fav_songs'] = [fav_songs]
#for diff key in same line
#print(user)

#for diff keys in diff lines 
for i, j in user.items():
    print(f"{i} : {j}")
