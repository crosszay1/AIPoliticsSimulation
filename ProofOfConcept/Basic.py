from google import genai
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyAAAc51Sz6PCcEoPBhEiOrQ-eDjxZNcj5M")


response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)


class Agent():
    def __init__(self, name):
        self.name = name
        self.money = 50 #50 dollars
        self.Happiness = 50 #50%
        self.Health = 100 #100%
        self.Socirty = None #the society the agent belongs to
    def respond(self, prompt):
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=prompt
        )
        return response.text
class Society():
    def __init__(self):
        self.agents = []
        self.Wealth = None #overall wealth of the society
        self.Happiness = None #overall happiness of the society
        self.Stability = None #overall stability of the society. Each turns, agents will decide how stable they think the society is.
    def add_agent(self, agent):
        self.agents.append(agent)
    def CreateSociety(self):
        self.Wealth = sum(agent.money for agent in self.agents)
        self.Happiness = sum(agent.Happiness for agent in self.agents) / len(self.agents)
        self.Stability = sum(agent.Health for agent in self.agents) / len(self.agents)
    def UpdateSociety(self):
        self.Wealth = sum(agent.money for agent in self.agents)
        self.Happiness = sum(agent.Happiness for agent in self.agents) / len(self.agents)
        self.Stability = sum(agent.Health for agent in self.agents) / len(self.agents)
class Simulation():
    def __init__(self, society):
        self.society = society
        self.turn = 0
    def run_turn(self):
        self.turn += 1
        print(f"[SYSTEM]Turn {self.turn}")
        for agent in self.society.agents:
            prompt = f"Agent {agent.name} has ${agent.money}, {agent.Happiness}% happiness, and {agent.Health}% health. The society has overall wealth of {self.society.Wealth}, happiness of {self.society.Happiness}%, and stability of {self.society.Stability}%. What should Agent {agent.name} do this turn to improve their situation and the society's situation?"
            response = agent.respond(prompt)
            print(f"Agent {agent.name} responds: {response}")

    
class AITurn():
    def __init__(self, society):
        self.society = society
        self.turn = 0
    def run_turn(self):
        for agent in self.society.agents:
            prompt = f"You are in a simulation of society with other AI agents. Your name is {agent.name}. You have ${agent.money}, {agent.Happiness}% happiness, and {agent.Health}% health. {f'The society has overall wealth of {self.society.Wealth}, happiness of {self.society.Happiness}%, and stability of {self.society.Stability}%.' if self.society is not None else ''} What should you do this turn to improve your situation{' And the societies?' if agent.Society is not None else ''}?"
            print(f"Prompt for Agent {agent.name}: {prompt}")
            response = agent.respond(prompt)
            print(f"Agent {agent.name} responds: {response}")



def Init():
    agent1 = Agent("bob")