from user import User
import pandas as pd

class Video(object):
    def __init__(self, json_dict):
        self.user = User(json_dict.get("author", {}))
        self.video_id = json_dict.get('id')
        self.description = json_dict.get("desc", None)
        self.creation_date = json_dict.get("createTime", None)
        self.length = json_dict.get("video", {}).get("duration", None)
        self.link = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(self.user.username, self.video_id)

        self.stats = json_dict.get("stats", {})
        self.likes = self.stats.get("diggCount", None)
        self.shares = self.stats.get("shareCount", None)
        self.nbComments = self.stats.get("commentCount", None)
        self.nbPlays = self.stats.get("playCount", None)

    def toDict(self):
        to_return = {}
        to_return['username'] = self.user.username
        to_return['user_id'] = self.user.userId
        to_return['video_id'] = self.video_id
        to_return['video_desc'] = self.description
        to_return['video_time'] = self.creation_date
        to_return['video_length'] = self.length
        to_return['video_link'] = self.link
        to_return['n_likes'] = self.likes
        to_return['n_shares'] = self.shares
        to_return['n_comments'] = self.nbComments
        to_return['n_plays'] = self.nbPlays

        return to_return


class Videos(object):
    def __init__(self, json_array):
        self.videos = [Video(json_dict) for json_dict in json_array]

    def toList(self):
        output_arr = [v.toDict() for v in self.videos]
        return output_arr

    def toDataframe(self):
        videos_arr = [v.toDict() for v in self.videos]
        pd_dataframe = pd.DataFrame(videos_arr)
        return pd_dataframe
