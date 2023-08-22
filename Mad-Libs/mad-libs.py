import time
input('''Hello world!
Today we're gonna make a story.
All you need to do is to answer the questions
      
begin?''')

print('''
----------------------------------------------------------------
''')

first_name = input("think of a first name: ")
last_name = input("think of a last name: ")
gender = input("what are the pronouns of that person. Write it like 'she her her' or 'he him his' or whatever else: ").split()

food = input("think of a food: ")
town = input("think of a small town name: ")
city = input("think of a large city name: ")
monster = input("think of a singular monster like a 'dragon': ")
enemies = input("think of some enemies like 'goblins' or 'robbers': ")
weak_weapon = input("think of a weak weapon: ")
strong_weapon = input("think of a strong weapon: ")
action = input(f"think of an action you can do with the {strong_weapon} like 'stabbed': ")

story = f"There were once a peasant named {first_name} {last_name}. {gender[0]} was living in {town} with {gender[2]} parents; "
story += f"ms. and mr. {last_name}. One day in a newspaper {first_name} read that there was a {monster} on the loose in the city attacking people. "
story += f"{first_name} decided to embark on a journey to defeat the {monster}. {gender[0]} picked up some {food}, a {weak_weapon} and was out the door. "
story += f"On the way to the city {gender[0]} saw some {enemies} terrorizing a small town and {gender[0]} decided to attack them and save the small town. "
story += f"{first_name} pulled out {gender[2]} trusty {weak_weapon} and began slaying down the {enemies} one by one. "
story += f"In the end the biggest and last of the {enemies} dropped a {strong_weapon}. {first_name} picked it up and went on {gender[2]} way. "
story += f"After a large while of walking and eating {food} {first_name} {last_name} finally reached the city. "
story += f"{gender[0]} asked a random person on the street where the {monster} was and they answered that the {monster} was near the west wall of the city. "
story += f"{first_name} picked up the {strong_weapon} and ran over there. {first_name} saw the monster, ran up its back and {action} it in its head. "
story += f"{first_name} was considered to be a hero and a good friend of the city for killing the {monster} and the king said; 'thank you for saving the city from the {monster}. "
story += f"We will remember you as a hero and we're gonna make a statue. '{first_name} {last_name} the savior''"

print("\n")
new_story = story.split(". ")
for line in new_story:
    print(line + ". ")
    time.sleep(3)


input("the end")