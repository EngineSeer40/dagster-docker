from instaloader import Instaloader, Profile

# https://medium.com/@nikhilbadveli6/how-to-extract-social-media-content-for-free-6e8edefbea7f

def fetch_from_instagram(L, user_name, MAX_POSTS=200):
    """
    Fetch instagram data from Instagram. We can use the Instagram API to fetch the data.
    """

    def get_comments(pst, MAX_COMMENTS=200):
        """
        This is a helper function to get the comments from a post.
        :param pst:
        :param MAX_COMMENTS:
        :return:
        """
        comments = []
        for cmt in pst.get_comments():
            comments.append(
                (pst.mediaid, cmt.created_at_utc.strftime('%Y-%m-%d %H:%M:%S'), cmt.text, cmt.owner.username))
            if len(comments) >= MAX_COMMENTS:
                break
        return comments

    # Get the profile of the requested user
    profile = Profile.from_username(L.context, username=user_name)

    # Get the posts of the user
    # Do not use the Instagram app or another instance of InstaLoader() while scraping the data.
    scraped_posts = []
    scraped_comments = []
    print('Fetching posts from Instagram for {}...'.format(user_name))
    for post in profile.get_posts():
        scraped_posts.append((post.mediaid, post.date, post.owner_username, post.caption, post.likes, post.comments))
        # scraped_comments.extend(get_comments(post))

        if len(scraped_posts) >= MAX_POSTS:
            break
    print('Fetching posts from Instagram for {}...Done'.format(user_name))

    # Save the scraped data in two .csv files - one for posts and the other for comments
    df_posts = pd.DataFrame(scraped_posts,
                            columns=['mediaid', 'date', 'owner_username', 'caption', 'likes', 'comments'])
    df_posts.to_csv('data/Instagram' + user_name + '_instagram_posts' + '.csv', index=False)


# Initialize the instagram API using instaloader
L = Instaloader()

# Login to instagram
L.login(user=insta_config['username'], passwd=insta_config['password'])

# Instagram profile username from which you would like to scrape.
username = 'myanimelistofficial'

fetch_from_instagram(L, username)