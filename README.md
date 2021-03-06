# Osu-Free-Api
An alternative to the osu! api which does not need any access key



# Installation
Put the "api.py" file in the same directory of your project, then:
```python
import api
# Do Stuff...
```



# Documentation
### Return Player Profile:
Returns a request object that can be used with the other functions that this repository offers
```python
request = api.return_player_profile(input("Username: "))
# Do stuff with 'request'...
```

### Get Player Stats:
Returns basic stats about a player
```python
print(api.get_player_stats(request))
# Example: {'global ranking': '#302,489',
#            'local ranking': '#3,226',
#            'playtime': '2d 13h 21m',
#            'medals': '37',
#            'pp': '1,320'}
```

### Get Player Score Count:
Returns how many SSX, SS, SX, S and A scores a player has performed
```python
print(api.get_player_score_count(request))
# Example: {'SSX': '5', 'SS': '5', 'SX': '64', 'S': '93', 'A': '143'}
```

### Get Player Best Score:
Returns the player's best score
```python
print(api.get_player_best_score(request))
# Example: {'title': 'Mizuoto to Curtain by MIMI feat. Hatsune Miku',
#            'link': 'https://osu.ppy.sh/beatmaps/2025941',
#            'pp': '89'}
```

### Get Player First Place Plays Count:
Returns how many first place plays a player has performed
```python
print(api.get_player_first_place_plays(request))
# Example: 4
```

### Get Player PlayStyle:
Return the player's playstyle
```python
print(api.get_player_playstyle(request))
# Example: Keyboard, Tablet
```

### Get Player Socials:
Returns a list containing all of the player's known social medias
```python
print(api.get_player_socials(request))
# Example: ['ZenT3600#8117']
# // Yes That's Actually Me, DM Me If You Have Any Questions \\
```

### Get Player Most Played Map:
Returns the player's most played map, along with its retry count
```python
print(api.get_player_socials(request))
# Example: {'title': "Putin's Boner [Akitoshi's Normal] by Helblinde",
#            'link': 'https://osu.ppy.sh/beatmaps/1559211',
#            'count': '186'}
```

### Get Player Favorite Maps:
Return a list containing the player's favorite maps
```python
print(api.get_player_favorite_maps(request))
# Example: ['Mizuoto to Curtain',
#            'Bass Slut (Original Mix)',
#            'MAYDAY (Nightcore Mix)',
#            'Inochi ni Kirawarete Iru.',
#            'Lemon']
```

### Get Player About:
Returns a string containing the content of the player's about page
```python
print(api.get_player_about(request))
# Example: Idk, something probably
```

### Get Mapset Page:
Returns a request object that can be used with the other functions that this repository offers
```python
map = api.return_mapset_page(int(input("Code: ")))
# Do something with map...
```

### Get Mapset Difficulty Codes:
Returns the various difficulty codes of the mapset in an array
```python
print(api.get_mapset_difficulty_codes(map))
# Example: ['#osu/2258751', '#osu/2258753', '#osu/2258857', '#osu/2258752', '#osu/2256655']
```

### Select Specific Difficulty:
Returns a request to the beatmap's specific difficulty page
```python
diff = api.return_specific_mapset_difficulty(beatmap_code, difficulty_code)
# Do something with diff...
```

### Get Difficulty Stats:
Returns a dictionary containing the stats for a specific difficulty:
```python
print(api.get_difficulty_stats(diff))
# Example: {'length': '2:49',
#            'bpm': '160',
#            'circle num': '261',
#            'slider num': '151',
#            'circle size': '4',
#            'hp drain': '5', 'accuracy':
#            '6', 'ar': '7',
#            'sr': '3.47'}
```

### Get Mapset Stats:
Returns a dictionary containing the stats of a whole mapset
```python
print(api.get_mapset_stats(map))
# Example: {'title': 'Less Than Three (Ricardo Autobahn Remix)',
#            'author': 'Becky', 'mapper': 'Sonnyc',
#            'status': 'Ranked'}
```

### Get Mapset Likes
Returns both the likes and plays a mapset has
```python
print(api.get_mapset_likes(map))
# Example: {'plays': '2,925', 'likes': '11'}
```

### Get Mapset Description
Returns a string containing the description of a map
```python
print(api.get_mapset_description(map))
# Example: Idk, something probably
```

### Return News Page
Returns a request to osu's news page that can be used with the other functions that this repository offers
```python
news = api.return_news_page()
# Do something with news...
```

### Get Most Recent News
Returns a dictionary with the most recent news' title, content and date
```python
print(api.get_most_recent_news(news))
# Example: {'title': 'Monthly Beatmapping Contests Return',
#            'content': "It's time for a new way to flaunt your beatmapping capabilities. Find out what it takes to become osu!'s next Elite Mapper!",
#            'date': '5 Jan 2020', 'link': 'https://osu.ppy.sh/home/news/2020-01-05-monthly-beatmapping-contests-return'}
```

### Get News At Index
Returns a dictionary with the title, content and date of the news at given index
Returns None if index is greater than 10, for pagination purposes
```python
print(api.get_news_at_index(news, 3))
# Example: {'title': 'osu! Mapping Olympiad #3 Results (osu!mania)',
#            'content': 'The judging for the first osu!mania Mapping Olympiad contest has been completed! Congratulations to PianoLuigi, the first osu!mania Mapping Olympian and our newest Elite Mapper!',
#            'date': '27 Dec 2019', 'link': 'https://osu.ppy.sh/home/news/2020-01-05-monthly-beatmapping-contests-return'
```

### Return Specific News Page
Returns a request to a specific news page that can be used with the other functions that this repository offers
```python
spec = api.return_specific_news_page()
# Do something with spec...
```

### Get Full News Content
Returns The Full Content Of A Specific News
```python
print(api.get_full_news_content(spec))
# Idk, something probably
```

### Get Forums Codes
Returns the available forum codes
```python
print(api.get_forums_codes())
# {'development': 2,
#  'gameplay': 13,
#  'tournaments': 55,
#  'skinning': 15,
#  'help': 5,
#  'mapping discussion': 56,
#  'modding queues': 60,
#  ...
#  ..
#  .}
```

### Return Forums Page
Returns a request to osu's forums page that can be used with the other functions that this repository offers
```python
forums = return_forums_page(CODE)
# Do something with forums
```

### Get Newest Post For The Category
Returns the newest post for the selected category
```python
print(api.get_newest_post(forums)
# {'title': 'How to properly "report" or handle Mixed Skins.',
#  'author': 'Dntm8kmeeatu',
#  'replies': '39', 'views':
#  '28,130', 'timeago':
#  '3 months ago',
#  'link': 'https://osu.ppy.sh/community/forums/topics/704698'}
```

### Return Specific Post Page
Returns a request to a specific post's page that can be used with the other functions that this repository offers
```python
post = return_post_page("https://osu.ppy.sh/community/forums/topics/704698")
# Do something with post
```

### Get Post's Question
Returns a post's question
```python
print(api.get_post_question(post))
# Idk, something probably
```

### Get Post's Answers
Returns a list containing the post's answers
```python
print(api.get_post_answers(post))
# ['Is it ok to post mixed skin outside osu community?', 'A Lunime user that plays osu!', ..., .., .]
```

### Get Leaderboard Codes
Returns the available leaderboard codes
```python
print(api.get_leaderboards_codes())
# {0: "performance",
#  1: "score",
#  2: "country"}
```

### Return Leaderboard Page
Returns a request to osu's leaderboard page that can be used with the other functions that this repository offers
```python
leader = api.return_leaderboards_page(CODE)
# Do smoething with leader...
```

### Get N Leaderboard Spots
Returns as leaderboard spots as n in an ordered list
Returns None if n is >= 50
```python
print(api.get_n_leaderboard_spots(3))
#Example: ['WhiteCat', 'Vaxei', 'Alumetri']
```

### Return LiveStreams Page
Returns a request to osu's livestreams page that can be used with the other functions that this repository offers
```python
streams = api.return_streams_page(CODE)
# Do smoething with streams...
```

### Get LiveStreams List
Returns a list of dictionaries containing the current livestreams' data
```python
print(api.get_current_streams(streams))
# Example: [{'streamer': 'BeasttrollMC',
#             'viewers': '901'},
#            {'streamer': 'Aricin98',
#             'viewers': '134'},
#            {'streamer': 'customallosu', 'viewers': '69'}]
```

### Return Contest Page
Returns a request to osu's livestreams page that can be used with the other functions that this repository offers
```python
contests = api.return_contests_page(CODE)
# Do smoething with contests...
```

### Get Contests List
Returns a list of dictionaries containing contests' data
```python
print(api.get_contests_list(contests))
# Example: [{'title': 'Monthly Beatmapping Contests 2020: #1',
#             'date': 'January 3, 2020 - January 26, 2020',
#             'type': 'beatmap'},
#            {'title': 'osu!idol 2019 Finals',
#             'date': 'Ended December 18, 2019',
#             'type': 'music'}
```


# Requirements:
* requests-html
* typing



# Reminder:
This project is a WIP, so if you notice any bugs or think of a new cool feature I could add,
feel free to let me know about it
* Discord: ZenT3600#8117
* Instagram: @zent3600official
* Reddit: u/ZenT3600
