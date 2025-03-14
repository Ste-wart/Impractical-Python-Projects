"""Generate funny names by randomly combining names from 2 seprate lists."""
import sys
import random


def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print('Welcome to the Psych `Sidekick Name Picker.`\n')
    print('A name just like Sean would pick for Gus:\n\n')

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill", "Bob", 'Bowel Noises',
             'Boxelder', "Bud", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
             'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat','Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman',
             'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim',
             'Huckleberry','Huggy', 'Ignatious', 'Jimbo', "Joe", 'Johnny', 'Lemongrass',
             'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid', 'Mr Peabody',
             'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
             'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff',
             'Scut', "Sid", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
             'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
             'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston", 'Worms')

    middle = ('The Big News', 'Grunts', 'Tinkie Winkie', 'Beenie-Weenie',
              'Stinkbug', 'Lite', 'Pottin Soil', 'The Squirts', 'Jazz Hands',
              'Oil-Can')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
            'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        i = random.randint(1, 10)
        middle_name = random.choice(middle)

        print('\n\n')
        # Trick IDLE by using "fatal error" setting to print name in red.
        if i % 2 == 1:
            print(f'{first_name} {middle_name} {last_name}', file=sys.stderr)
        else:
            print(f'{first_name} {last_name}', file=sys.stderr)
        print('\n\n')

        try_again = input('\n\nTry again/ (Press Enter else n to quit)\n ')

        if try_again.lower() == 'n':
            break

    input('\nPress Enter to exit.')


if __name__ == '__main__':
    main()
