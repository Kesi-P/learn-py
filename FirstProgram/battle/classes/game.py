import random
from battle.classes.magic import Spell

class bcolor:
    HEADER ='\033[95m'
    OKBLUE ='\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENOC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,item):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk +10
        self.df =df
        self.magic = magic
        self.item = item
        self.actions = ['Attack','Magic','Item']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    # def generate_spell_danger(self, i):
    #     mgl = self.magic[i]["dmg"] - 5
    #     mgh = self.magic[i]["dmg"] +5
    #     return random.randrange(mgl,mgh)

    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg
        if self.hp == self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def reduce_mp(self,cost):
        self.hp -= cost

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return  self.maxmp

    # def get_spell_name(self,i):
    #     return self.magic[i]['name']

    def get_spell_mp_cost(self,i):
        return int(Spell.cost)

    def choose_action(self):
        i = 1
        print(bcolor.BOLD+self.name)
        print('Action')
        for item in self.actions:
            print(str(i)+ ':',item)
            i += 1

    def choose_target(self,enemies):
        i = 1
        print('Target')
        for enemy in enemies:
            print('\n', enemy.name)
            i += 1
        target_choice = int(input("Choose target:")) -1
        return target_choice

    def choose_magic(self):
        i =1
        print('Magic')
        for Spe_ll in self.magic:
            print('     ' + str(i)+ ':', Spe_ll.name,'{cost : ', str(Spe_ll.cost),'}')
            i += 1

    def choose_item(self):
        i =1
        print('Item')
        for item in self.item:
            print('     ' + str(i)+':',item.name,'- Description :', item.description)
            i+=1

    def get_enemy_stats(self):
        hp_bar = ''
        bar_ticks = (int(self.hp) / int(self.maxhp)) * 100/4

        while bar_ticks >0:
            hp_bar += '█' #the point
            bar_ticks -= 1

        while len(hp_bar)<50:
            hp_bar += ' ' #the white space

        print(self.name + str(self.mp), '/', str(self.maxmp), '|',hp_bar, '|')


    def get_stat(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100/4
        mp_bar =''
        mp_ticks = (self.mp/self.maxmp) * 100/10
        while bar_ticks >0:
            hp_bar += '█' #the point
            bar_ticks -= 1

        while len(hp_bar)<25:
            hp_bar += ' ' #the white space

        while mp_ticks > 0:
            mp_bar += '█'  # the point
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '  # the white space

        print(self.name      + str(self.hp),'/',str(self.maxmp),'|',hp_bar,             '|' , str(self.mp),'/',str(self.maxmp),'|',mp_bar,         '|')
        print(bar_ticks)