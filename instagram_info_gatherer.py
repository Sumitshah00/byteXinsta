# instagram_info_gatherer.py

from instapy import InstaPy

def gather_instagram_info(username):
    # Initialize InstaPy session
    session = InstaPy(username=<your_instagram_username>, password=<your_instagram_password>)
    session.login()

    # Gather information
    target_user = session.grab_profile(username)
    media_count = target_user['media_count']
    follower_count = target_user['follower_count']
    following_count = target_user['following_count']
    bio = target_user['biography']
    external_url = target_user['external_url']

    # Print gathered information
    print(f"Username: {username}")
    print(f"Media count: {media_count}")
    print(f"Follower count: {follower_count}")
    print(f"Following count: {following_count}")
    print(f"Bio: {bio}")
    print(f"External URL: {external_url}\n")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python instagram_info_gatherer.py <target_username>")
        sys.exit(1)

    target_username = sys.argv[1]
    gather_instagram_info(target_username)