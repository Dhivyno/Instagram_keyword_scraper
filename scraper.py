
def inputting():
    print("""
    ---------------------------------------------------------------------------------
    INSTRUCTIONS TO USE:
            
    Input your username, password, target account and keyword or keysentence when prompted to search for posts from target account that contain keyword or keysentence.
            
    It will print the index of each post and the link to the first image in the command line and then download the post images and captions into a seperate folder named after the target account and index of post.
    ---------------------------------------------------------------------------------
    """)


    username = input("Enter the username of your account:  ")
    password = input("Enter the password of your account:  ")
    target = input("Enter the username of the target account:  ")
    keyword = input("Enter the keyword or sentence you are looking for in the target account's posts:  ")
    return username, password, target, keyword

def scrape(username, password, target, keyword):

    import instaloader
    import pandas as pd

    # Create an instance of Instaloader class
    bot = instaloader.Instaloader()

    try:
        bot.login(user=username,passwd=password)
    except:
        print("ERROR LOGGING INTO ACCOUNT")


    
    # Loading a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, target)


    
    # Retrieving all posts in an object
    posts = profile.get_posts()
    counter = 0
    
    # Iterating and downloading all the individual posts
    for index, post in enumerate(posts, 1):
        try:
            if keyword in post.caption:
                print(index, post.url)
                bot.download_post(post, target=f"{profile.username}_{index}")
                counter += 1
            else:
                print(index)
        except:
            continue

    print(str(counter) + " posts found with keyword: " + keyword)

if __name__ == "__main__":
    username, password, target, keyword = inputting()
    scrape(username, password, target, keyword)