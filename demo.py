from agentmanager import Agent, AgentManager

manager = AgentManager()

# Crea dos agentes con diferente tiempo de "trabajo" por paso
agent1 = Agent("AlphaAgent", work_time=1)
agent2 = Agent("BetaAgent", work_time=0.7)

manager.register(agent1)
manager.register(agent2)

manager.run_all()
print("Todos los agentes han terminado sus tareas.")
