'''My day with automats for discrete maths lab'''

import random
from graphviz import Digraph

class Me:
    '''Me class'''
    def __init__(self) -> None:
        self.state = 'sleep'
        self.show = 'zzz...'
        self.emotions = ["it'll be a bad day(", \
"Sounds it will be a good day because it's off day!", "Today will be very hard and productive day"]
        self.today_vibe = random.choice(self.emotions)
        self.hours = [0] + [i / 2 for i in list(range(1, 48))] + [24]
        self.dot = Digraph('MyDay')
        self.dot.attr(rankdir='LR')

    @property
    def day(self):
        '''Whole day'''
        print("Hello!\nMy name is Ostap\nThis is my day here!\n")
        self.morning()

    def morning(self):
        '''my day morning'''
        for hour in self.hours[:14]:
            if self.state == 'sleep' and hour in range(6):
                print(self.show)
                self.state = None
                self.show = None
            elif self.today_vibe == self.emotions[1]:
                print(self.emotions[1])
                self.off_day()
                break
            elif hour == 6:
                self.show = 'Rise and shine! ' + self.today_vibe
                self.state = 'wake_up'
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 6.5:
                self.state = 'eat'
                self.show = "It's time for breakfast and preparing for uni!"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
                if self.today_vibe == self.emotions[0]:
                    print('\n' + self.emotions[0])
                    self.bad_day()
                elif self.today_vibe == self.emotions[2]:
                    print('\n' + self.emotions[2])
                    self.hard_day()

    def bad_day(self):
        '''bad day is going'''
        time_for_preparing = random.choice([7, 7.5])
        test = random.choice([0, 1])
        taken = 1
        day = 1

        for hour in self.hours[14:]:
            if taken and time_for_preparing == 7:
                self.state = 'preparing'
                self.show = "I mustn't hurry up, I'll leave home on time."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
                taken = 0
            elif taken and time_for_preparing == 7.5:
                self.state = 'preparing'
                self.show = "Hurry up!"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
                taken = 0
            elif hour == 8:
                self.state = 'trip'
                self.show = "Where is the tram?? I need to be in time."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif not test and hour == 8.5:
                self.state = 'park'
                self.show = "I'm only in the Stryiskyi park, I'll be late today("
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
            elif test and hour == 8.5:
                self.state = 'run_park'
                self.show = "I'm only in the Stryiskyi park, I must run because of test!!"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
                print('...')
                if time_for_preparing == 7.5:
                    print('I was late only for 10 minutes.')
                else:
                    print('I was on time.')
            elif day and hour in self.hours[24:26]:
                self.state = 'study'
                self.show = "It's hard to study, today is so haaaard..."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
                day = 0
            elif hour == 13:
                self.state = 'eat'
                self.show = "I need rest and to eat, so let's go to trapezna!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 18:
                self.state = 'study'
                self.show = "I've learnt approximately nothing, it's awfull. I go home, \
maybe at home I'll be able to study better("
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 18.5:
                self.state = 'trip'
                self.show = "Finally, I'm going home by tram."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 20:
                self.state = 'study'
                self.show = "I'm home and I'm trying to study, but cannot, I'm tired!!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 23:
                self.state = 'sleep'
                self.show = "I want to sleep, so good night, it was non-productive and bad day, \
I've not done almost anything!("
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)

    def off_day(self):
        '''off day is going'''
        rush = [1, 0]
        jam = [1, 0]
        eating = [1, 0]
        for hour in self.hours[14:]:
            if hour == 9:
                self.state = 'eat'
                self.show = "While I was eating, \
I took a message with invitation to join to my friends at 15:00, I agree!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 10:
                film = ['Dune', 'Shadow and Bone', '3 Body Problem', 'Nemo']
                self.state = 'rest'
                self.show = f"I'm watching film '{random.choice(film)}'!😍"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 13:
                self.state = 'preparing'
                self.show = "I dunno what I want to wear today..."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 13.5:
                self.show = "Finally, I found THE outfit"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 14:
                if rush:
                    self.state = 'trip'
                    self.show = "I cannot sit to anything, buses don't exist!!!\nHow to be in time?"
                    print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                    print(self.show)
                else:
                    self.state = 'trip'
                    self.show = "I sit in the bus immediately!"
                    print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                    print(self.show)
            elif hour == 14.5:
                if jam:
                    self.show = "OMG! Traffic jam!?!?!?"
                    print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                    print(self.show)
            elif hour == 15:
                if jam:
                    self.show = "I'm in the bus yet, I'll be late("
                    print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                    print(self.show)
                else:
                    self.state = 'rest'
                    self.show = "I met my friends and we're going to cafeteria now!"
                    print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                    print(self.show)
            elif hour == 15.5:
                if jam:
                    self.state = 'rest'
                    self.show = "I met my friends and they were angry to me!"
                    print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                    print(self.show)
            elif hour == 17 and eating:
                self.state = 'eat'
                self.show = "We're eating croissants, so tasty!😋"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 21.5:
                self.state = 'trip'
                self.show = "I need to go home already, so I say: 'bye' to friends and go home."
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 22 and not eating:
                self.state = 'eat'
                self.show = "I'm very hungry!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 22.5:
                self.state = 'sleep'
                self.show = "Good night!\nIt was a fantastic day!"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)

    def hard_day(self):
        '''hard day is going'''
        time_for_preparing = random.choice([7, 7.5])
        test = random.choice([0, 1])
        taken = 1
        day = 1

        for hour in self.hours[14:]:
            if taken and time_for_preparing == 7:
                self.state = 'preparing'
                self.show = "I mustn't hurry up, I'll leave home on time."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
                taken = 0
            elif taken and time_for_preparing == 7.5:
                self.state = 'preparing'
                self.show = "Hurry up!"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
                taken = 0
            elif hour == 8:
                self.state = 'trip'
                self.show = "Where is the tram?? I need to be in time."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif not test and hour == 8.5:
                self.state = 'park'
                self.show = "I'm only in the Stryiskyi park, I'll be late today("
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
            elif test and hour == 8.5:
                self.state = 'run_park'
                self.show = "I'm only in the Stryiskyi park, I must run because of test!!"
                print(f"\nIt's {int(hour)}:30" + ' (state="' + self.state + '")')
                print(self.show)
                print('...')
                if time_for_preparing == 7.5:
                    print('I was late only for 10 minutes.')
                else:
                    print('I was on time.')
            elif day and hour in self.hours[24:26]:
                self.state = 'study'
                self.show = "It's hard to study, today is so haaaard..."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
                day = 0
            elif hour == 13:
                self.state = 'eat'
                self.show = "I need rest and to eat, so let's go to trapezna!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 14:
                self.state = 'study'
                self.show = "I have a lecture now!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 18:
                self.state = 'study'
                self.show = "I've learnt so much today!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 18.5:
                self.state = 'trip'
                self.show = "Finally, I'm going home by tram."
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 20:
                self.state = 'study'
                self.show = "I'm home and I'm trying to study, but cannot, I'm tired!!"
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)
            elif hour == 23:
                self.state = 'sleep'
                self.show = "I want to sleep, so good night, it was non-productive and bad day, \
I've not done almost anything!("
                print(f"\nIt's {int(hour)}:00" + ' (state="' + self.state + '")')
                print(self.show)

if __name__ == '__main__':
    ostap = Me()
    ostap.day
