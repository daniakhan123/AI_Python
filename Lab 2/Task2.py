import random

class Server:
    def __init__(self, id):
        self.id = id
        self.load = random.choice(["Underloaded", "Balanced", "Overloaded"])

    def __str__(self):
        return f"Server {self.id}: {self.load}"

class LoadBalancer:
    def __init__(self):
        self.servers = [Server(i) for i in range(1, 6)]

    def display_servers(self, message):
        print(message)
        for server in self.servers:
            print(server)
        print("----------------------------")

    def balance_load(self):
        underloaded = [s for s in self.servers if s.load == "Underloaded"]
        overloaded = [s for s in self.servers if s.load == "Overloaded"]
        
        while overloaded and underloaded:
            ol = overloaded.pop()
            ul = underloaded.pop()
            print(f"Moving load from Server {ol.id} to Server {ul.id}")
            ol.load = "Balanced"
            ul.load = "Balanced"
            
system = LoadBalancer()
system.display_servers("Initial Server Loads:")
    
system.balance_load()
    
system.display_servers("Final Server Loads:")

