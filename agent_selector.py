"""
class AgentSelector():
    is_available = None
    available_since = None
    roles = None

    def __init__(self):
        pass

    def select_agent(self):
        pass
"""


agent_list = {
    'agent_1': {'is_available': 1, 'available_since': 2, 'roles': 'spanish speaker'},
    'agent_2': {'is_available': 1, 'available_since': 3, 'roles': 'sales'}
    }

selection_mode_list = ['all available', 'least busy', 'random']


def select_agent(agent_list, selection_mode):
    
    selected_agent_list = []
    selection_mode = selection_mode.lower()

    if selection_mode == 'all available':
        selected_agent_list.append(agent_list) 
    if selection_mode == 'least busy':
        selected_agent_list.append(agent_list)
    if selection_mode == 'random':
        selected_agent_list.append(agent_list)

    return selected_agent_list


selected_agents = select_agent(agent_list, 'All available')
print(selected_agents)
