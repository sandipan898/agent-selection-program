import random

agent_list = [
    {'agent_id': 1, 'is_available': 1, 'available_since': 2, 'roles': 'spanish speaker'},
    {'agent_id': 2, 'is_available': 1, 'available_since': 3, 'roles': 'sales'},
]

selection_mode_list = ['all available', 'least busy', 'random']


def select_agent(agent_list, selection_mode):
    """ check the conditions based on selection mode and returns the agent id of selected agents """
    
    selection_mode = selection_mode.lower()
    available_time_list = [i['available_since'] for i in agent_list]

    if selection_mode == 'all available':
        selected_agents = [i['agent_id'] for i in agent_list]

    if selection_mode == 'least busy':
        max_time = max(available_time_list)
        selected_agents = [i['agent_id'] for i in agent_list if i['available_since'] == max_time]

    if selection_mode == 'random':
        selected_agents =  random.choice(agent_list)['agent_id']

    return selected_agents


#selected_agents = select_agent(agent_list, 'All available')
selected_agents = select_agent(agent_list, 'random')

print(selected_agents)
