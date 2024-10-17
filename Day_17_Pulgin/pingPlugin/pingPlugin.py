import os

from pluginInterface import plugingInterface
class pingplugin(plugingInterface):
    def execute(self,address):
        response = os.system(f"ping -n 1 {address}")
        if response ==0:
            return f"{address} is reachable"
        else:
            return f"{address} is not rechable"