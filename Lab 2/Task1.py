class Environment:
    def __init__(self):
        self.grid = ['safe', 'vulnerable', 'safe',
                     'safe', 'vulnerable', 'vulnerable',
                     'safe', 'safe', 'safe']

    def get_percept(self, agent_location):
        return self.grid[agent_location]

    def safe_system(self, agent_location):
        self.grid[agent_location] = 'safe'

    def display_grid(self, agent_location):
        print(f"Agent Location: {agent_location}")
        grid_with_agent = self.grid[:]
        grid_with_agent[agent_location] = '.'
        for i in range(0, 9, 3):
            print(" | ".join(grid_with_agent[i:i + 3]))
        print()


class SimpleReflexAgent:
    def __init__(self):
        self.position = 0 

    def act(self, percept, grid):
        if percept == 'vulnerable':
            grid[self.position] = 'safe'
            return 'Patched'
        else:
            return 'No action'

    def move(self):
        if self.position < 8:
            self.position += 1
        return self.position


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.act(percept, environment.grid)
        print(f"Step {step + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")
        environment.display_grid(agent.position)
        agent.move()


agent = SimpleReflexAgent()
environment = Environment()

run_agent(agent, environment, 9)
