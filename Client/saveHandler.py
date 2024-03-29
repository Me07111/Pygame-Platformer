import json
import os
class SaveHandler:
    def __init__(self):
        self.maps = self.loadMaps(False)


    def loadMaps(self,save : bool) -> list[list[list[str]]]:
        print(os.getcwd())
        loadedMap = open("save.json","r")
        maps = json.loads(loadedMap.read())
        loadedMap.close()
        if(save):
            self.maps = maps
        return maps
    
    def loadMap(self,index : int) -> list[list[str]]:
        return self.loadMaps(True)[index]
    
    def saveMap(self,map : list[list[str]], index : int):
        self.maps[index] = map
        self.saveMaps()
    
    def saveMaps(self):
        f = open("save.json","w")
        json.dump(self.maps, f, ensure_ascii = True,indent = 6)
        f.close()