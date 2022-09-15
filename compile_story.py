import os

story = '''The trees stood like sentinels, their leaves rustling in the wind. The sun had long since set, and the only light came from the moon, which cast a pale glow over the forest. The forest was a place of legend and myth, and it was said that dragons still roamed its depths. It was also said that wizards still lived in the forest, hiding from the world in their towers. The main character, a young boy named Sylas, had always been fascinated by the stories of the Forest. He had often dreamed of visiting the forest, and now, finally, he was going to get his chance. Sylas's parents had been killed by a dragon, and he had been taken in by the wizard, Kyzax. Kyzax had told Sylas that he was special, that he had the potential to be a great wizard. And so, on this night, Sylas was setting out into the Forest, on a quest to find the dragons and wizards that lived there. He was not afraid, for he knew that he was the chosen one, destined to save the world from the evil that was coming.'''


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)



files = os.listdir('story/')

for file in files:
    content = open_file('story/%s' % file)
    story = story + '\n\n' + content

save_file('story.txt', story)