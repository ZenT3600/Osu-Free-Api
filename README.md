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


# Requirements:
* requests-html
* typing



# Reminder:
This project is a WIP, so if you notice any bugs or think of a new cool feature I could add,
feel free to let me know about it
* Discord: ZenT3600#8117
* Instagram: @zent3600official
* Reddit: u/ZenT3600
