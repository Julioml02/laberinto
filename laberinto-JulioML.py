# laberinto
# Proyecto del laberinto del curso 23-24


class Game:
    def __init__(self):
        self.maze = None
     
    def create_wall(self):
        return Wall()


    # Otra forma para el método create_door, pero no me funciona todavía
    # def create_door(self, side1, side2, opened):
    #        door = Door()
    #        door.open=opened
    #        door.side1 = side1
    #        door.side2 = side2 
    #        return door

    
    def create_door(self, side1, side2):
        door = Door(side1, side2)
        return door

    def create_room(self, id):
        room= Room(id)
        room.north= self.create_wall()
        room.east = self.create_wall()
        room.south= self.create_wall()
        room.west = self.create_wall()
        return room
   
    def create_maze(self):
        return Maze()   
    
    def  make2RoomsMazeFM(self):
        game = Game()
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        door = game.create_door(room1, room2)
        room1.south= door
        room2.north = door
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)       
        return self.maze

    def make2RoomsMaze(self):
        self.maze= Maze()
        room1 = Room(1)
        room2 = Room(2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        door= Door(room1, room2)
        room1.south = door
        room2.north = door
        return self.maze

           
class MapElement:
    def __init__(self):
        pass
       
    def entrar(self):
        pass


class Maze(MapElement):
    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)

    def entrar(self):
        self.rooms[0].entrar()

               
class Hoja(MapElement):
    def accept(self, visitor):
        visitor.visitHoja(self)


class Decorator(Hoja):
    def __init__(self, component):
        self.component = component

        
class Contenedor(MapElement):
    def __init__(self):
        self.hijos=[]
        
    def agregarhijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarhijo(self, hijo):
        self.hijos.remove(hijo)


class Room(MapElement):
    def __init__(self, id):         
        self.north = Wall()
        self.east = Wall()
        self.west = Wall()
        self.south = Wall()
        self.id = id

    def entrar (self):
        print("Entrando a la habitación", self.id)

             
class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
        
    def entrar(self):
        if self.opened:
            self.side1.entrar()
        else:
            print("¡La puerta está bloqueada!")

              
class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need any special attributes
       
    def entrar(self):
        print("¡No puedes entrar por aquí! No atraviesas paredes")


class BombedGame(Game):
    def create_wall(self):
        return BombedWall()


class BombedWall(Wall):
    def __init__(self):
        self.active = False
        
    def entrar(self):
        if self.active: 
            print("BOOOOM!! La bomba ha explotado")
        return super().entrar()


game = Game()
game.make2RoomsMaze()
game.maze.entrar()


game = Game()
game.make2RoomsMazeFM()


game = BombedGame()
game.make2RoomsMazeFM()
game.maze.entrar()
