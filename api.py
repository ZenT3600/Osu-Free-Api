from requests_html import HTMLSession


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


# Base User URL --> https://osu.ppy.sh/users/{USERMAME}
def return_player_profile(username):
    session = HTMLSession()
    req = session.get(f"https://osu.ppy.sh/users/{username}")
    req.html.render()
    return req


# <div class="value-display__value">
def get_player_stats(req):
    tags = req.html.find(".value-display__value")
    values = []
    for i, tag in enumerate(tags):
        if i < 6:
            values.append(tag.text)
        else:
            break
    return dict(zip(Global.labels, values))


# <div class="profile-rank-count__item"> --> <div>
def get_player_score_count(req):
    parents = req.html.find(".profile-rank-count__item")
    scores = []
    for parent in parents:
        try:
            scores.append(parent.find("div")[0].text)
        except:
            pass
    return dict(zip(Global.scores, scores))


# <div class="bbcode">
def get_player_about(req):
    return req.html.find(".bbcode")[0].text


# <div class="play-detail"> /// <span class="play-detail__pp">[0] --> <span> /// <a class="play-detail__title">
def get_player_best_score(req):
    pp = req.html.find(".play-detail__pp")[0].find("span")[0].text[:-2]
    try:
        pp = "".join(pp.split(","))
    except:
        pass
    title = req.html.find(".play-detail__title")[0].text
    link = req.html.find(".play-detail__title")[0].attrs["href"]
    return {"title": title, "link": link, "pp": pp}


def get_player_first_place_plays(req):
    try:
        return req.html.find(".title")[4].find("span")[0].text
    except:
        return 0


def get_player_playstyle(req):
    try:
        return req.html.find(".profile-links__item")[2].find("span")[0].text
    except:
        return None
    

def get_player_socials(req):
    socials = []
    try:
        i = 4
        while True:
            socials.append(req.html.find(".profile-links__item")[i].find("a")[0].text)
            i += 1
    except:
        return socials


def get_player_most_played_map(req):
    title = req.html.find(".beatmap-playcount__title")[0].text
    link = req.html.find(".beatmap-playcount__title")[0].attrs["href"]
    count = req.html.find(".beatmap-playcount__count")[0].text
    return {"title": title, "link": link, "count": count}


def get_player_favorite_maps(req):
    try:
        return [favorite.text for favorite in req.html.find(".osu-layout__col-container")[0].find(".beatmapset-panel__header-text")[::2]]
    except:
        return 0


if __name__ == '__main__':
    req = return_player_profile(input("User: "))
    print()
    print(f"Stats: {get_player_stats(req)}\n")
    print(f"Score Count: {get_player_score_count(req)}\n")
    print(f"Best Score: {get_player_best_score(req)}\n")
    print(f"First Places: {get_player_first_place_plays(req)}\n")
    print(f"Most Played Map: {get_player_most_played_map(req)}\n")
    print(f"Favorite Maps: {get_player_favorite_maps(req)}\n")
    print(f"PlayStyle: {get_player_playstyle(req)}\n")
    print(f"Socials: {get_player_socials(req)}\n")
    print(f"About: {get_player_about(req)}\n")
