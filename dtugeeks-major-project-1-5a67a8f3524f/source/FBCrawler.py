import csv
import datetime
import json
import os
import urllib.request
import ownModule


def get_graph_url(graph_url, APP_ID, APP_SECRET):
    post_args = "/tagged/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
    post_url = graph_url + post_args
    return post_url


def get_json_response(post_url):
    web_response = urllib.request.urlopen(post_url)
    readable_page = web_response.read().decode("utf-8")
    json_post_data = json.loads(readable_page)
    return json_post_data


def get_all_posts(graph_url, APP_ID, APP_SECRET):
    post_url = get_graph_url(graph_url, APP_ID, APP_SECRET)
    json_post_data = get_json_response(post_url)
    fb_posts = json_post_data['data']
    while 'paging' in json_post_data.keys() and 'next' in json_post_data['paging'].keys():
        post_url = json_post_data['paging']['next']
        json_post_data = get_json_response(post_url)
        fb_posts.extend(json_post_data['data'])

    return fb_posts


def main():
    APP_ID = '416379438547915'
    APP_SECRET = 'e1c66cb8409855dcf19bf01cb8bdcd6a'
    bank_name = 'HDFC.bank'
    graph_url = "https://graph.facebook.com/" + bank_name
    json_fb_posts = get_all_posts(graph_url, APP_ID, APP_SECRET)

    post_no = 1
    starting_download_time = datetime.datetime.now()
    # pass the name of the folder you wish to create relative to the project directory to the below function
    file_folder = ownModule.createFileFolder('outputFiles')
    file_folder += os.path.sep
    with open(ownModule.removeFileIfExists(file_folder + bank_name + "FaceBookPosts.csv"), 'w', newline='') as csvfile:
        spam_writer = csv.writer(csvfile, delimiter='|',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spam_writer.writerow(["Post", "Time"])
        for post in json_fb_posts:
            if 'message' in post.keys():
                print(post['message'])
                post['message'] = post['message'].replace("\n", ' ')
                spam_writer.writerow([post['message'], post['created_time']])
                if post_no == 1:
                    starting_download_time = post['created_time']
                post_no += 1


if __name__ == "__main__":
    main()
