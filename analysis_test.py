from TikTokApi import TikTokApi
import pandas as pd
import json
from video import Videos


class analyticsEngineTrends(object):
    def __init__(self, api, seedUsers=None, nbTrendingVids = 1000) -> None:
        self.api = api
        self.seedUsers = seedUsers
        self.trending_videos = []

        if self.seedUsers:
            seedUsersId = [self.api.getUser(username)["userInfo"]["user"]["id"]
                           for username in seedUsers]
            suggested = [self.api.getSuggestedUserbyID(count=25, startingId=s_id)
                         for s_id in seedUsersId]

            for user in suggested:
                print(user)
                userVids = api.byUsername(user, count=10)
                temp = Videos(userVids)
                self.videos += temp
            
        else:
            temp = api.trending(count=nbTrendingVids,
                                          custom_verifyFp="")
            self.trending_videos = Videos(temp)

        return


def main():
    api = TikTokApi()
    n_videos = 100
    username = "tiktok"
    output_file_json = "./output/videos.json"
    output_file_csv = "./output/videos.csv"
    userVids = api.byUsername(username, count=n_videos)
    users = api.getUser(username)

    analysticsEngine = analyticsEngineTrends(api, nbTrendingVids=100000)
    trending_videos = analysticsEngine.videos

    with open("./output/trends.json", 'w') as outfile:
        json.dump(trending_videos, outfile)

    trending_videos.toDataframe().to_csv("./output/videos_trending.csv", sep=";", index=False, encoding="utf-8")

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
