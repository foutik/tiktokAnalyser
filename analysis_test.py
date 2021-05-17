from TikTokApi import TikTokApi
import pandas as pd
import json
from video import Videos


class analyticsEngineTrends(object):
    def __init__(self, seedUsers, api) -> None:
        self.seedUsers = seedUsers
        self.api = api
        self.seedUsersId = [self.api.getUser(username)["userInfo"]["user"]["id"]
                            for username in seedUsers]

        self.suggested = [self.api.getSuggestedUserbyID(count=25, startingId=s_id)
                          for s_id in self.seedUsersId]

        return


def main():
    api = TikTokApi()
    n_videos = 100
    username = "tiktok"
    output_file_json = "./output/videos.json"
    output_file_csv = "./output/videos.csv"
    userVids = api.byUsername(username, count=n_videos)
    users = api.getUser(username)

    trends = api.trending(count=100, custom_verifyFp="")

    with open("./output/trends.json", 'w') as outfile:
        json.dump(trends, outfile)

    with open("./output/user.json", 'w') as outfile:
        json.dump(users, outfile)

    with open("./output/response.json", 'w') as outfile:
        json.dump(userVids, outfile)

    videos = Videos(userVids)

    with open(output_file_json, 'w') as outfile:
        json.dump(videos.toList(), outfile)

    videos.toDataframe().to_csv(output_file_csv, sep=";", index=False, encoding="utf-8")


if __name__ == "__main__":
    main()
