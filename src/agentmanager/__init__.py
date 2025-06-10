import threading
import time

class Agent(threading.Thread):
    def __init__(self, name, work_time):
        super().__init__()
        self.name = name
        self.work_time = work_time

    def run(self):
        print(f"[{self.name}] Agente empezando su tarea...")
        for i in range(1, 4):
            print(f"[{self.name}] trabajando... paso {i}")
            time.sleep(self.work_time)  # Simula trabajo
        print(f"[{self.name}] tarea finalizada.")

class AgentManager:
    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def run_all(self):
        for agent in self.agents:
            agent.start()
        for agent in self.agents:
            agent.join()
