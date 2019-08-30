import random
from battle.classes.game import Person,bcolor
from battle.classes.magic import Spell
from battle.classes.inventory import Item


#Black Magic
fire = Spell('Fire' ,10,160, 'Black')
thunder = Spell('Thunder' ,20,260, 'Black')
blizzard = Spell('Blizzard' ,30,360, 'Black')
meteor = Spell('Meteor' ,50,560, 'Black')
quake = Spell('Quake' ,60,660, 'Black')

#White Magic
cure = Spell('Cure',13,160,'White')
cura = Spell('Cura',16,260,'White')

#Some Items
potion = Item('Potion','potion','Heals 50 HP',50)
hipotion = Item('Hipotion','potion','Heals 100 Hp',100)
elixer = Item('Elixer','elixer','Fully restore HP/MP',9000)
grenade = Item('Grenada','attack','Deals 500 Damage',500)

#Instatiate Peopla
player1 = Person('Kesi',200,100,300,50,[fire,thunder,quake,cura,cure],[potion,hipotion,elixer,grenade])
player2 = Person('Benji',300,200,300,50,[fire,thunder,quake,cura,cure],[potion,hipotion,elixer,grenade])
player3 = Person('Manee',400,300,300,50,[fire,thunder,quake,cura,cure],[potion,hipotion,elixer,grenade])

enemy1 = Person('enemy1',1100,65,45,25,[],[])
enemy2 = Person('enemy2',1200,130,95,50,[],[])

players =[player1,player2,player3]
enemies = [enemy1,enemy2]
running = True
i=0

print(bcolor.FAIL + bcolor.BOLD + 'Anemy attack'+bcolor.ENOC)

while running:
    print('=============')
    for player in players:
        player.get_stat()

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input('Choose action:')  # we count start at 0
        index = int(choice) - 1

        if index == 0: #attack
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg) #point to array of anemies
            print('You attack ',enemies[enemy].name,'for',dmg,'points of damage.')

        elif index == 1: #magic
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) -1
            if magic_choice == -1:
                continue
            # magic_dmg = player.generate_spell_danger(magic_choice)
            # spell = player.get_spell_name(magic_choice)
            # cost = player.get_spell_mp_cost(magic_choice)

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            #cost = player.get_spell_mp_cost(magic_choice)
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolor.FAIL + 'Not enough Mp')
                continue

            dmg = spell.dmg
            if spell.type =='White':
                player.heal(dmg)
                print('You are heal')

            player.reduce_mp(spell.cost)
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(magic_dmg)
            print(bcolor.OKBLUE+'\n'+spell.name+ 'deals', str(magic_dmg),'points odf danage')

        elif index == 2:
            player.choose_item()
            item_choice = int(input('Choose item'))-1
            if item_choice == -1:
                continue

            item = player.item[item_choice]
            if item.type =='potion':
                player.heal(item.prop)
                print('You are heal',item.prop)

            if item.type == 'elixer':
                player.hp = player.maxhp
                player.mp = player.maxmp

            if item.type == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolor.FAIL + 'Attack enemy :',int(item.prop))

    enemy_choice =1
    player_len = len(players)
    enemy = player.choose_target(enemies)
    enemy_dmg = enemies[enemy].generate_damage()
    target = random.randrange(0, player_len)
    players[target].take_damage(enemy_dmg) #point to array
    print('Enemy attacks for ', enemy_dmg)
    print('==============================')
    #print('Enemy HP:',bcolor.FAIL + str(enemies[enemy].name),':', str(enemies[enemy].get_hp()))

    defeated_enimies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enimies = 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players = 1;

    if enemy.get_hp() == 2:
        print(bcolor.FAIL, 'You win!')
        running = False

    elif player.get_hp() == 2:
        print(bcolor.OKGREEN, 'You lost!')
        running = False

