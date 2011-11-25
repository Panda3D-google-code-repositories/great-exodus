'''
Created on 4 nov. 2011

@author: JD219546
'''
from game_engine.factories.ShipFactory import ShipFactory
from game_engine.displacement.MovementManager import MovementManager
from game_engine.factories.GalaxyFactory import GalaxyFactory
from game_engine.game_objects.star_systems.StarSystem import StarSystem
from game_engine.factories.StarSystemFactory import StarSystemFactory
from game_engine.factories.StarSystemSectorFactory import StarSystemSectorFactory
from game_engine.PlayerStatus import PlayerStatus
from game_engine.GameStatus import GameStatus

class GameEngine(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.movement_manager = MovementManager()
        self.accurate_movment_ships = []
        self.approximate_movement_ships = []
        
    def create_initial_movement_lists(self):
        
        for ship in ShipFactory.get_ship_list():
            ship_sector = ship.get_star_system_sector()
            if PlayerStatus.player_is_in_star_system_sector(ship_sector):
                self.accurate_movment_ships.append(ship)
            else:
                self.approximate_movement_ships.append(ship)        
        
    def update(self):
        print "GameEngine update"
        ship_list = ShipFactory.get_ship_list()
        i = 0
        '''
        for galaxy in GalaxyFactory.galaxies_list:
            galaxy.move_ships()
        
        '''
        '''
        i = 0
        for ship in ShipFactory.get_ship_list():
            if PlayerStatus.player_is_in_star_system_sector(ship.star_system_sector):
                #print("Player in system")
                MovementManager.move_ship_random_accurately(ship)
            else:
                if GameStatus.subiteration_corresponds(i):
                    #print("My turn to fly")
                    MovementManager.move_ship_random_approximately(ship)
            i += 1
        pass
        '''
        
        MovementManager.move_ships_random_accurately(self.accurate_movment_ships)
        i = GameStatus.subiteration
        for i in range(GameStatus.subiteration,len(self.approximate_movement_ships), GameStatus.subiterations):
            #print("My turn to fly")
            MovementManager.move_ship_random_approximately(self.approximate_movement_ships[i])
        pass
        

    def create_ships_in_star_system_sector(self, star_system_sector, nb_ships = 0):
        '''
        Help function to create ships for testing.
        Will not be part of final project.
        '''        
        for i in range(nb_ships):
            ShipFactory.create_cargo_in_star_system(star_system_sector)
            ShipFactory.create_scout_in_star_system(star_system_sector)
            
    def create_galaxies(self, nb_galaxies = 1):
        for i in range(nb_galaxies):
            GalaxyFactory.create_galaxy()
            
    def create_star_systems(self, galaxy, nb_star_systems = 1):
        for i in range(nb_star_systems):
            StarSystemFactory.create_star_system(galaxy)
            
    def create_star_system_sectors(self, star_system, nb_star_system_sectors = 1):
        for i in range(nb_star_system_sectors):
            StarSystemSectorFactory.create_star_system_sector(star_system)