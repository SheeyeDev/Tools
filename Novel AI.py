# @Sheeye

# Artificial Intelligence to write books!
# Try number one... I don't expect it to go to well as you can see hahahaha

# D = 01.08.2022

import random

file = open('Story.rtf', 'w+')
printed = 0

#Brain - things to remember
name = "Josh"
name2 = "Josh"
weather_type = "good"
pronoun = "he"
pronoun2 = "him"
pronoun3 = "boy"
pronoun4 = "his"
expressedOpinion=5

introduce = {
    0 : "NAME was a PRONOUN3 like any other.",
    1 : "NAME never really fit with people PRONOUN4 age.",
    2 : "NAME was considered pretty unique.",
    3 : "NAME was a typical PRONOUN3.",
    4 : "NAME was a PRONOUN3 with big dreams."
}
describe_appearance = {
    0 : "COLOR eyes, TYPE2 hair and impressed everyone with PRONOUN2 TYPE1 figure. ",
    1 : "TYPE2 aura around PRONOUN2. ",
    2 : "hair of COLOR color, and a TYPE2 face. ",
    3 : "golden locks and amber eyes. ",
    4 : "unmatched beauty and incredible strength. ",
    5 : "a lot of ambition and stuborness. "
}

color = {
    0 : "blue like the ocean",
    1 : "golden",
    2 : "ruby",
    3 : "black as the darkest night",
    4 : "white as snow",
    5 : "emerald",
    6 : "rainbow colored",
    7 : "wine red"
}

type2 = {
    0 : "innocent",
    1 : "intriguing",
    2 : "dazzling"
}

type1 = {
    0 : "muscular",
    1 : "slender"
}
describe_weather = {
    0 : "It was ADJECTIVE1 outside. ",
    1 : "NAME looked at the sky - it was ADJECTIVE1. ",
    2 : "The weather was ADJECTIVE2. "
}

weather_adjective1 = {
    "bright" : "good",
    "raining" : "storm",
    "drizzling" : "storm",
}

weather_adjective2 = {
    "calm" : "good",
    "unstable" : "storm"
}

weather_adjective_poetic = {
    "good1" : "Warm rays of sun were embracing NAME. ",
    "good2" : "The heat was slightly tampered by a nice breeze. ",
    "good3" : "It was the middle of summer. ",
    "good4" : "The heat was so intense that sweat started to accumulate on NAME's forehead. ",
    "good5" : "It's really nice weather' NAME thought to themselves. ",
    "good6" : "The sunny and mild afternoon weather was perfect for taking a walk. ",
    "good7" : "Hot. Humid. Sweat. drenching. oppressive . HEAT. Even the trees were looking for shade. ",
    "good8" : "Evening sky had turned to molten brass. ",
    "good9" : "Sun cast a luminescent glow. ",
    "good10" : "The day was out of sync with NAME's mood. ",
    "storm6" : "The sound of raindrops falling on the ground was drowning out all other noise. ",
    "storm7" : "Thunder could be heard in the background. ",
    "storm8" : "NAME hated rain, so they weren't a big fan. ",
    "storm9" : "The humidity caused all sorts of bugs to start crawling onto the surface. ",
    "storm10": "A web of clouds, back-lit by the failing sun, mist billowed through the trees and over the fields and hung low in the air, masking the camp in a ghostly gray. ",
    "storm11": "The wind was icy and withering. ",
    "storm12": "Lightning flashed across the sky and temporarily illuminated the darkness.",
    "storm13": "The humidity caused all sorts of bugs to start crawling onto the surface. ",
}

reached = {
    0 : "Finally, NAME reached ",
    1 : "PRONOUN4 legs led PRONOUN2 to ",
    2 : "Before PRONOUN2 spread ",
    3 : "NAME found themselves in "
}
locations = {
    0 : "forest",
    1 : "mountains",
    2 : "desert"
}
locations_descriptions = {
    "forest1" : "There must have been tens of kinds of trees, which NAME has never seen before.",
    "forest2" : "The orchiestra of the birds singing above NAME made PRONOUN2 really feel at peace.",
    "forest3" : "This calming greenery filled NAME with great relief.",
    "forest4" :  "Bees hummed in and out of the pennyroyal.",
    "forest5": "The trees lashed and crashed against each other like drum sticks in the hands of a giant.",
    "forest6": "Were it not for the bright moon in the night sky, PRONOUN would have lost his way in this dusky forest.",
    "forest7": "The deeper NAME went into the forest, the more fragrant it became.",
    "forest8": "It was easy for NAME to find themselves roaming the inviting forest for hours.",
    "mountains1" : "Walking uphill made PRONOUN2 tire quickly.",
    "mountains2" : "NAME could see the snowy mountaintops in the far distance.",
    "mountains3" : "It was a nice change of scenery from the usual plains.",
    "mountains4" : "The mist grabbed at the ankle of the mountain.",
    "mountains5" : "The mountains rose as great rocky declarations of hope to the vast sky.",
    "mountains6" : "The view before NAME as PRONOUN climbed atop the high hill was truly something to behold.",
    "desert1" : "The dust devil swirled across the canyon like a rattlesnake on the hunt.",
    "desert2" : "The desert was a warm and expansive golden brown, as wide open as it is ever possible to imagine.",
    "desert3" : "NAME could only hear whistling of the wind, throwing sound into PRONOUN4 mouth.",
    "desert4" : "The intense sun blazed down on this harsh yet amazingly beautiful wilderness of red rocks.",
    "desert5": " Every time your eyes wander back to study the distant rocky landscape it seems as if it were merely a projection onto the horizon.",
    "desert6": " Unberable heat was making NAME far from comfortable."
}

action_intentions = {
    "NAME adventured into unknown territories." : "change_location",
    "NAME marched forward." : "change_location",
    "NAME set out on a journey." : "change_location",
    #"PRONOUN sat down and rested" : "rest"
}

action_adjective = {
    "walked": "speed",
    "run": "speed",
    "met": "no",
    "sat": "emotion",
    "sang": "loudness"
}

opinion = {
    0: "NAME found it ADJECTIVE. ",
    1 :"But NAME didn't mind it. ",
    2 : "NAME was lost in thought. "
}

opinion_adj = {
    0 : "funny",
    1 : "annoyning",
    2 : "pretty cool"
}

def new_line():
    global printed
    global file
    printed+=1
    if printed>=3:
        printed=0
        file.write("\n\n")


def change_pronouns(string):
    global name
    if string.__contains__("NAME"):
        string = string.replace("NAME", name)
        if name != pronoun.capitalize():
            name = pronoun.capitalize()
        else:
            name = name2
    if string.__contains__("PRONOUN2"):
            string = string.replace("PRONOUN2",pronoun2)
    if string.__contains__("PRONOUN3"):
            string = string.replace("PRONOUN3",pronoun3)
    if string.__contains__("PRONOUN4"):
            string = string.replace("PRONOUN4",pronoun4)
    if string.__contains__("PRONOUN"):
            string = string.replace("PRONOUN", pronoun)
    return string

def describe_hero():
    global name
    global file
    global printed
    n = random.randint(0, len(introduce)-1)
    string = introduce[n]
    string = change_pronouns(string)
    print(string,end=" ")
    file.write(string+" ")
    new_line()
    print(name,"had ",end='')
    file.write(name+" had ")
    if name!= pronoun.capitalize():
        name = pronoun.capitalize()
    else:
        name = name2
    n = random.randint(0, len(describe_appearance)-1)
    string = describe_appearance[n]
    if string.__contains__("COLOR"):
        n = random.randint(0, len(color) - 1)
        string = string.replace("COLOR", color[n])
    if string.__contains__("TYPE2"):
        n = random.randint(0, len(type2) - 1)
        string = string.replace("TYPE2", type2[n])
    if string.__contains__("TYPE1"):
        n = random.randint(0, len(type1) - 1)
        string = string.replace("TYPE1", type1[n])
    if string.__contains__("PRONOUN2"):
        string = string.replace("PRONOUN2", pronoun2)
    print(string,end='')
    file.write(string)
    new_line()

def express_opinion():
    global file
    global printed
    n = random.randint(0, len(opinion)-1)
    string = opinion[n]
    if string.__contains__("NAME"):
        string = string.replace("NAME",pronoun)
        if string.__contains__("ADJECTIVE"):
            n = random.randint(0, len(opinion_adj) - 1)
            string = string.replace("ADJECTIVE", opinion_adj[n])
    print(string,end='')
    file.write(string)
    new_line()

def set_weather():
    global name
    global file
    global printed
    global expressedOpinion
    global weather_type
    n = random.randint(0, len(describe_weather)-1)
    string = describe_weather[n]
    if string.__contains__("NAME"):
        string = string.replace("NAME",name)
        if name != pronoun.capitalize():
            name = pronoun.capitalize()
        else:
            name = name2
    if string.__contains__("ADJECTIVE1"):
        adj,typer = random.choice(list(weather_adjective1.items()))
        string = string.replace("ADJECTIVE1",adj)
        weather_type = typer
        print(string,end=" ")
        file.write(string+" ")
        printed += 1
        new_line()
    elif string.__contains__("ADJECTIVE2"):
        adj,typer = random.choice(list(weather_adjective2.items()))
        string = string.replace("ADJECTIVE2",adj)
        weather_type = typer
        print(string,end='')
        file.write(string)
        printed += 1
        new_line()

    #generate poetic phrase
    d = 0
    while True:
        c = random.randint(0, 100)
        if d==0:
            c=100
        if c-d>=20:
            i = [""]
            for key in weather_adjective_poetic:
                if key.__contains__(weather_type):
                    i.append(weather_adjective_poetic[key])
            n = random.randint(0, len(i)-1)
            if i[n].__contains__("NAME"):
                i[n] = i[n].replace("NAME",name)
                name = pronoun.capitalize()
            print(i[n],end='')
            file.write(i[n])
            printed += 1
            if printed >= 3:
                printed = 0
                file.write("\n\n")
            d+=15
        else:
            break
    # c=random.randint(0,100)
    # if c>=50:
    #     if expressedOpinion>=3:
    #         expressedOpinion=0
    #         express_opinion()
    #

def change_locations():
    global name
    global file
    global printed
    n = random.randint(0, len(locations)-1)
    co = random.randint(0,len(reached)-1)
    str = reached[co]
    str = change_pronouns(str)
    print(str,locations[n],". ",end="")
    file.write(str+locations[n]+". ")
    printed += 1
    if printed >= 3:
        printed = 0
        file.write("\n")
    d = 0
    while True:
        c = random.randint(0, 100)
        if d==0:
            c=100
        if c-d>=20:
            i = [""]
            for key in locations_descriptions:
                if key.__contains__(locations[n]):
                    i.append(locations_descriptions[key])
            nr = random.randint(0, len(i)-1)
            if i[nr].__contains__("NAME"):
                i[nr] = i[n].replace("NAME",name)
                name = pronoun.capitalize()
            print(change_pronouns(i[nr]))
            file.write(change_pronouns(i[nr]))
            new_line()
            d+=15
        else:
            break

if __name__ == '__main__':
    #global file
    set_weather()
    describe_hero()
    for i in range(100):
        n = random.randint(0, len(action_intentions) - 1)
        for x in action_intentions:
            if n==0:
                str = x
                if action_intentions[str]=="change_location":
                    str = change_pronouns(str)
                    print(str)
                    file.write(str)
                    change_locations()





# &ally 369518