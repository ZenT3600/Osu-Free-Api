from requests_html import HTMLSession
from typing import List, Dict, Union


class Global:
    labels = [
        "global ranking",
        "local ranking",
        "playtime",
        "medals",
        "pp",
    ]
    scores = [
        "SSX",
        "SS",
        "SX",
        "S",
        "A"
    ]
    diffstats = [
        "length",
        "bpm",
        "circle num",
        "slider num",
        "circle size",
        "hp drain",
        "accuracy",
        "ar",
        "sr"
    ]
    mapstats = [
        "title",
        "author",
        "mapper",
        "status"
    ]
    likes = [
        "plays",
        "likes"
    ]
    date = [
        "title",
        "content",
        "date",
        "link"
    ]
    forums = {
        "development": 2,
        "gameplay": 13,
        "tournaments": 55,
        "skinning": 15,
        "help": 5,
        "mapping discussion": 56,
        "modding queues": 60,
        "beatmap projects": 53,
        "ranked beatmaps": 14,
        "general": 7,
        "offtopic": 52,
        "introductions": 8,
        "music hall": 91,
        "otaku culture": 75,
        "videogames": 17,
        "art": 103
    }
    post = [
        "title",
        "author",
        "replies",
        "views",
        "timeago",
        "link"
    ]
    leaderboards = {
        0: "performance",
        1: "score",
        2: "country"
    }


# -------------------
# CONTESTS Down Here
# -------------------

def return_contests_page() -> HTMLSession:
    """
    Returns a request to osu's contests page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get("https://osu.ppy.sh/community/contests")
    req.html.render()
    return req


def get_contests_list(req: HTMLSession) -> List[Dict[str, str]]:
    """
    Returns a list of dictionaries containing contests' data
    """
    contests = []
    for i, contest in enumerate(req.html.find(".contest-list-item")):
        title = req.html.find(".contest-list-item__name")[i].text
        date = req.html.find(".contest-list-item__date")[i].text
        type = req.html.find(".contest-list-item__type")[i].text
        contests.append({"title": title, "date": date, "type": type})
    return contests


# -----------------
# STREAMS Down Here
# -----------------

def return_streams_page() -> HTMLSession:
    """
    Returns a request to osu's livestreams page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get("https://osu.ppy.sh/community/livestreams")
    req.html.render()
    return req


def get_current_streams(req: HTMLSession) -> List[Dict[str, str]]:
    """
    Returns a list of dictionaries containing the current livestreams' data
    """
    streams = []
    for i, stream in enumerate(req.html.find(".livestream-item")):
        streamer = req.html.find(".livestream-item__text")[2 * i].text
        viewers = req.html.find(".livestream-item__text")[(2 * i) + 1].text
        streams.append({"streamer": streamer, "viewers": viewers})
    return streams


# ----------------------
# LEADERBOARDS Down Here
# ----------------------

def get_leaderboards_codes() -> Dict[int, str]:
    """
    Returns a dictionary containing the available leaderboard codes
    """
    return Global.leaderboards


def return_leaderboards_page(code: int) -> HTMLSession:
    """
    Returns a request to osu's leaderboard page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get(f"https://osu.ppy.sh/rankings/osu/{Global.leaderboards[code]}")
    req.html.render()
    return req


def get_n_leaderboard_spots(req: HTMLSession, n: int) -> Union[List[str], None]:
    """
    Returns as leaderboard spots as n in an ordered list
    Returns None if n is >= 50
    """
    if n >= 50:
        return None
    tops = []
    if req.html.find(".ranking-page-table__user-link-text"):
        for i in range(n):
            tops.append(req.html.find(".ranking-page-table__user-link-text")[i].text.strip())
    else:
        for i in range(n):
            tops.append(req.html.find(".ranking-page-table__country-link-text")[i].text.strip())
    return tops


# --------------
# FORUM Down Here
# --------------


def get_forums_codes() -> Dict[str, int]:
    """
    Returns a dictionary containing the available forum codes
    """
    return Global.forums


# Base Forums URL --Z https://osu.ppy.sh/community/forums/{CODE}
def return_forums_page(code: int) -> HTMLSession:
    """
    Returns a request to osu's forums page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get(f"https://osu.ppy.sh/community/forums/{code}")
    req.html.render()
    return req


def get_newest_post(req: HTMLSession) -> Dict[str, str]:
    """
    Returns the newest post's data
    """
    title = req.html.find(".forum-topic-entry__content")[0].find("a")[0].text
    author = req.html.find(".forum-topic-entry__link ")[0].text
    replies = req.html.find(".forum-topic-entry__count")[0].text
    views = req.html.find(".forum-topic-entry__count")[1].text
    timeago = req.html.find(".timeago")[2].text
    link = req.html.find(".forum-topic-entry__content")[0].find("a")[0].attrs["href"]
    return dict(zip(Global.post, [title, author, replies, views, timeago, link]))


def return_post_page(link: str) -> HTMLSession:
    """
    Returns a request to a specific forums post's page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get(link)
    req.html.render()
    return req


def get_post_question(req: HTMLSession) -> str:
    """
    Returns a post's question
    """
    return req.html.find(".bbcode")[0].text


def get_post_answers(req: HTMLSession) -> List[str]:
    """
    Returns a post's answer
    """
    return [" ".join(answer.text.split("\n")) for i, answer in enumerate(req.html.find(".bbcode")) if i > 1]


# --------------
# NEWS Down Here
# -------------


# Base News URL --> https://osu.ppy.sh/home
def return_news_page() -> HTMLSession:
    """
    Returns a request to osu's news page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get("https://osu.ppy.sh/home/news")
    req.html.render()
    return req


def get_most_recent_news(req: HTMLSession) -> Dict[str, str]:
    """
    Returns a dictionary with the most recent news' title, content and date
    """
    title = req.html.find(".news-card__title")[0].text
    content = req.html.find(".news-card__preview")[0].text
    date = req.html.find(".news-card__time")[0].text
    link = req.html.find(".news-card")[0].attrs["href"]
    return dict(zip(Global.date, [title, content, date, link]))


def get_news_at_index(req: HTMLSession, index: int) -> Union[Dict[str, str], None]:
    """
    Returns a dictionary with the title, content and date of the news at given index
    Returns None if index is greater than 10, for pagination purposes
    """
    if index < 11:
        title = req.html.find(".news-card__title")[index].text
        content = req.html.find(".news-card__preview")[index].text
        date = req.html.find(".news-card__time")[index].text
        link = req.html.find(".news-card")[0].attrs["href"]
        return dict(zip(Global.date, [title, content, date, link]))
    else:
        return None


def return_specific_news_page(url: str) -> HTMLSession:
    """
    Returns a request to a specific news page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get(url)
    req.html.render()
    return req


def get_full_news_content(req: HTMLSession) -> str:
    """
    Returns The Full Content Of A Specific News
    """
    return req.html.find(".osu-md")[0].text


# --------------
# MAPS Down Here
# --------------


# Base Mapset URL --> https://osu.ppy.sh/beatmapsets/{CODE}
def return_mapset_page(code: int) -> HTMLSession:
    """
    Returns a request to a mapset's page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get(f"https://osu.ppy.sh/beatmapsets/{code}")
    req.html.render()
    return req


def return_specific_mapset_difficulty(code: int, diff_code: str) -> HTMLSession:
    """
    Returns a request to the beatmap's specific difficulty page
    """
    session = HTMLSession()
    req = session.get(f"https://osu.ppy.sh/beatmapsets/{code}{diff_code}")
    req.html.render()
    return req


# <a class="beatmapset-beatmap-picker__beatmap">
def get_mapset_difficulty_codes(req: HTMLSession) -> List[str]:
    """
    Returns the various difficulty codes of the mapset in an array
    """
    return [code.attrs["href"] for code in req.html.find(".beatmapset-beatmap-picker__beatmap")]


def get_difficulty_stats(req: HTMLSession) -> Dict[str, str]:
    """
    Returns a dictionary containing the stats for a specific difficulty
    """
    return dict(zip(Global.diffstats, [
        stat.text for stat in req.html.find(".beatmap-basic-stats__entry")] + [stat.text for stat in req.html.find(
        ".beatmap-stats-table__value")
                                                                               ]))


def get_mapset_description(req: HTMLSession) -> str:
    """
    Returns a string containing the description of a map
    """
    return req.html.find(".beatmapset-info__description")[0].text


def get_mapset_stats(req: HTMLSession) -> Dict[str, str]:
    """
    Returns a dictionary containing the stats of a whole mapset
    """
    return dict(zip(Global.mapstats, [
        stat.text for stat in req.html.find(".beatmapset-header__details-text")] +
                    [req.html.find(".beatmapset-mapping__user")[0].text] +
                    [req.html.find(".beatmapset-status")[0].text]))


def get_mapset_likes(req: HTMLSession) -> Dict[str, str]:
    """
    Returns both the likes and plays a mapset has
    """
    return dict(zip(Global.likes, [like.text for like in req.html.find(".beatmapset-header__value-name")]))


# -----------------
# PLAYERS Down Here
# -----------------


# Base User URL --> https://osu.ppy.sh/users/{USERMAME}
def return_player_profile(username: str) -> HTMLSession:
    """
    Returns a request to a player's page that can be used with the other functions that this repository offers
    """
    session = HTMLSession()
    req = session.get(f"https://osu.ppy.sh/users/{username}")
    req.html.render()
    return req


# <div class="value-display__value">
def get_player_stats(req: HTMLSession) -> Dict[str, str]:
    """
    Returns basic stats about a player
    """
    tags = req.html.find(".value-display__value")
    values = []
    for i, tag in enumerate(tags):
        if i < 6:
            values.append(tag.text)
        else:
            break
    return dict(zip(Global.labels, values))


# <div class="profile-rank-count__item"> --> <div>
def get_player_score_count(req: HTMLSession) -> Dict[str, str]:
    """
    Returns how many SSX, SS, SX, S and A scores a player has performed
    """
    parents = req.html.find(".profile-rank-count__item")
    scores = []
    for parent in parents:
        try:
            scores.append(parent.find("div")[0].text)
        except:
            pass
    return dict(zip(Global.scores, scores))


# <div class="bbcode">
def get_player_about(req: HTMLSession) -> str:
    """
    Returns a string containing the content of the player's about page
    """
    return req.html.find(".bbcode")[0].text


# <div class="play-detail"> /// <span class="play-detail__pp">[0] --> <span> /// <a class="play-detail__title">
def get_player_best_score(req: HTMLSession) -> Dict[str, str]:
    """
    Returns the player's best score's map along with it's details
    """
    pp = req.html.find(".play-detail__pp")[0].find("span")[0].text[:-2]
    try:
        pp = "".join(pp.split(","))
    except:
        pass
    title = req.html.find(".play-detail__title")[0].text
    link = req.html.find(".play-detail__title")[0].attrs["href"]
    return {"title": title, "link": link, "pp": pp}


def get_player_first_place_plays(req: HTMLSession) -> Union[str, int]:
    """
    Returns how many first place plays a player has performed
    """
    try:
        return req.html.find(".title")[4].find("span")[0].text
    except:
        return 0


def get_player_playstyle(req: HTMLSession) -> Union[str, None]:
    """
    Returns a string containing the player's playstyle
    """
    try:
        return req.html.find(".profile-links__item")[2].find("span")[0].text
    except:
        return None


def get_player_socials(req: HTMLSession) -> List[str]:
    """
    Returns a list containing all of the player's known social medias
    """
    socials = []
    try:
        i = 4
        while True:
            socials.append(req.html.find(".profile-links__item")[i].find("a")[0].text)
            i += 1
    except:
        return socials


def get_player_most_played_map(req: HTMLSession) -> Dict[str, str]:
    """
    Returns the player's most played map, along with its retry count
    """
    title = req.html.find(".beatmap-playcount__title")[0].text
    link = req.html.find(".beatmap-playcount__title")[0].attrs["href"]
    count = req.html.find(".beatmap-playcount__count")[0].text
    return {"title": title, "link": link, "count": count}


def get_player_favorite_maps(req: HTMLSession) -> Union[List[str], int]:
    """
    Return a list containing the player's favorite maps
    """
    try:
        return [favorite.text for favorite in
                req.html.find(".osu-layout__col-container")[0].find(".beatmapset-panel__header-text")[::2]]
    except:
        return 0


if __name__ == '__main__':
    # # Test Player: ZenT3600
    # req = return_player_profile(input("User: "))
    # print()
    # print(f"Stats: {get_player_stats(req)}\n")
    # print(f"Score Count: {get_player_score_count(req)}\n")
    # print(f"Best Score: {get_player_best_score(req)}\n")
    # print(f"First Places: {get_player_first_place_plays(req)}\n")
    # print(f"Most Played Map: {get_player_most_played_map(req)}\n")
    # print(f"Favorite Maps: {get_player_favorite_maps(req)}\n")
    # print(f"PlayStyle: {get_player_playstyle(req)}\n")
    # print(f"Socials: {get_player_socials(req)}\n")
    # print(f"About: {get_player_about(req)}\n")
    # print("\n\n\n")
    #
    # # Test Code: 1078502
    # code = int(input("Code: "))
    # map = return_mapset_page(code)
    # print()
    # diffs = get_mapset_difficulty_codes(map)
    # print(f"Difficulties: {diffs}")
    # diff = return_specific_mapset_difficulty(code, diffs[2])
    # print(f"Difficulty selected: {diff.url}")
    # print(f"Diff Stats: {get_difficulty_stats(diff)}")
    # print(f"Map Stats: {get_mapset_stats(map)}")
    # print(f"Map Likes: {get_mapset_likes(map)}")
    # print(f"Description: {get_mapset_description(map)}")
    #
    # # Test News: https://osu.ppy.sh/home/news/2020-01-05-monthly-beatmapping-contests-return
    # news = return_news_page()
    # print()
    # print(f"Most Recent News: {get_most_recent_news(news)}")
    # print(f"News at Index 3: {get_news_at_index(news, 3)}")
    # spec = return_specific_news_page("https://osu.ppy.sh/home/news/2020-01-05-monthly-beatmapping-contests-return")
    # print()
    # print(f"Full News: {get_full_news_content(spec)}")
    #
    # # Test Forum: 15, "https://osu.ppy.sh/community/forums/topics/704698"
    # print(f"Forum Codes: {get_forums_codes()}")
    # forums = return_forums_page(15)
    # print(f"Newest Post: {get_newest_post(forums)}")
    # post = return_post_page("https://osu.ppy.sh/community/forums/topics/704698")
    # print(f"Question: {get_post_question(post)}")
    # print(f"Answers: {get_post_answers(post)}")
    #
    # # Test Leader: None
    # print(f"Forum Codes: {get_leaderboards_codes()}")
    # leader = return_leaderboards_page(0)
    # print(f"Top 3 pp: {get_n_leaderboard_spots(leader, 3)}")
    # leader = return_leaderboards_page(1)
    # print(f"Top 3 Score: {get_n_leaderboard_spots(leader, 3)}")
    # leader = return_leaderboards_page(2)
    # print(f"Top 3 Country: {get_n_leaderboard_spots(leader, 3)}")
    #
    # # Test Stream: None
    # stream = return_streams_page()
    # print(f"Streams: {get_current_streams(stream)}")
    #
    # # Test Contest: None
    # contest = return_contests_page()
    # print(f"Contests: {get_contests_list(contest)}")
    pass
