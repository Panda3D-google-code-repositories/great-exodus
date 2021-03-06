'''
Created on 4 nov. 2011

@author: JD219546
'''
from game_engine.GameEngine import GameEngine
from gui.Gui import Gui
from time import sleep
from time import clock
from game_engine.PlayerStatus import PlayerStatus
from game_engine.factories.StarSystemFactory import StarSystemFactory
from game_engine.factories.GalaxyFactory import GalaxyFactory
from game_engine.factories.StarSystemSectorFactory import StarSystemSectorFactory
from game_engine.GameStatus import GameStatus
from game_engine.factories.ShipFactory import ShipFactory
from game_engine.serialization.UniverseSerialization import UniverseSerialization
from game_engine.displacement.MovementManager import MovementManager
from gui.PlayerMoveObserver import PlayerMoveObserver

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.game_engine = GameEngine()
        
        self.player_status = PlayerStatus()
        self.gui = Gui()
        self.move_player_observer = PlayerMoveObserver(self.gui.player_scene, self.player_status)
        self.max_iterations = 100
        self.subiterations = 30
        GameStatus.subiterations = self.subiterations        
        self.main_clock = float(1)/ self.subiterations       
        
    def start_main_loop(self):
        start_ = clock()
        print "Starting main loop"
        while True:
            #print "Iterating ..."
            st = clock()
            self.game_engine.update()
            self.gui.update()
            iteration_time = clock() - st
            if iteration_time < self.main_clock:
                sleep_time = self.main_clock - iteration_time
            else:
                sleep_time = 0
            sleep(sleep_time)
            if GameStatus.iteration == 10:
                self.player_status.set_position_in_universe(StarSystemSectorFactory.star_systems_sectors_list[4])
            if GameStatus.iteration == 20:
                self.player_status.set_position_in_universe(StarSystemSectorFactory.star_systems_sectors_list[2])
            if GameStatus.iteration == 30:
                self.player_status.set_position_in_universe(StarSystemSectorFactory.star_systems_sectors_list[1])
            if GameStatus.iteration == 40:
                self.player_status.set_position_in_universe(StarSystemSectorFactory.star_systems_sectors_list[0])
            print("Iteration : ",GameStatus.iteration," main_clock = ",self.main_clock," iteration time = ",iteration_time," and sleep time : ",sleep_time)            
            GameStatus.move_to_next_iteration(self.subiterations)
            if GameStatus.iteration == self.max_iterations:
                break
            
            
        end_ = clock()
        print("Execution time = ",end_-start_," and expected : ",self.max_iterations*self.main_clock)
        
    def create_universe(self, nb_galaxies, nb_star_systems_per_galaxy, nb_star_system_sectors_per_star_system, nb_ships_per_sector):
        UniverseSerialization.load_universe("game_engine/game_objects/database/RealisticUniverse.xml")
        '''
        self.game_engine.create_galaxies(nb_galaxies)
        for galaxy in GalaxyFactory.galaxies_list:
            #print "For each gal"
            self.game_engine.create_star_systems(galaxy, nb_star_systems_per_galaxy)
            for star_system in galaxy.star_systems_list:
                #print "for each star"
                self.game_engine.create_star_system_sectors(star_system, nb_star_system_sectors_per_star_system)
                for star_system_sector in star_system.star_system_sectors_list:
                    #print "For each sector"
                    self.game_engine.create_ships_in_star_system_sector(star_system_sector, nb_ships_per_sector)
        '''
                    
    def display_universe(self):
        print("There are",len(GalaxyFactory.galaxies_list),"galaxies")
        print("There are",len(StarSystemFactory.star_systems_list),"star systems")
        print("There are",len(StarSystemSectorFactory.star_systems_sectors_list),"star system sectors")
        print("There are",len(ShipFactory.ship_list),"ships")
        '''
        for galaxy in GalaxyFactory.galaxies_list:
            print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
            galaxy.print_star_systems()
            for star_system in StarSystemFactory.star_systems_dict[galaxy]:
                print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                star_system.print_star_system_sectors()
                for star_system_sector in StarSystemSectorFactory.star_systems_sectors_dict[star_system]:
                    #star_system_sector.print_spaceships()
                    pass        
        '''
        
    def set_player_position_in_universe(self, star_system_sector):
        self.player_status.set_position_in_universe(star_system_sector)