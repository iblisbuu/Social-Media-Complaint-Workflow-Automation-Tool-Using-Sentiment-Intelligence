__author__ = 'shubham'

import ownModule
import tweepy

# Twitter API credentials

consumer_key = "RGVO3CTujE60TW5IQy1JwmyxF"
consumer_secret = "ziWzApZCAqlwOt3xK3L0B02VjEsDFZg4Fniy76TsTLKgtnjqlG"
access_key = "1587880604-1tjWpdETzVE4fPALCGeNs6O2oHi4y8ShwIsDQSl"
access_secret = "wJHBahm2y3KnTXuuj2JX18GAolaHVMnLKZ7Ygc0LxnQMH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)


def get_all_hash(name):
    hashtag = name
    api = tweepy.API(auth)
    print("Tweets downloading has started !!")
    maxTweets = 100  # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits
    fName = 'HDFCTweets.txt'  # We'll store the tweets in a text file.

    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None

    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1

    tweets = []
    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    file_folder = ownModule.createFileFolder()
    if '\\' in file_folder:
        file_folder += '\\'
    else:
        file_folder += '/'
    with open(ownModule.removeFileIfExists(file_folder + fName), 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    tweets.append(tweet.text)
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

    return tweets


def main():
    hash_tag = "#HDFC"
    tweets = get_all_hash(hash_tag)
    file_folder = ownModule.createFileFolder()
    if '\\' in file_folder:
        file_folder += '\\'
    else:
        file_folder += '/'
    save_file = open(ownModule.removeFileIfExists(file_folder + "HDFCTweets" + '.txt'), 'a')
    post_no = 1
    for tweet in tweets:
        print(tweet)
        save_file.write("POST No: " + str(post_no) + " ")
        save_file.write(tweet.encode('ascii', 'ignore').decode())
        save_file.write("\n")
        post_no += 1
    save_file.close()


if __name__ == "__main__":
    main()
