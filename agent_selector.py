agent_list = [
    {'agent_id': 1, 'is_available': 1, 'available_since': 2, 'roles': 'spanish speaker'},
    {'agent_id': 2, 'is_available': 1, 'available_since': 3, 'roles': 'sales'},
]

selection_mode_list = ['all available', 'least busy', 'random']


def select_agent(agent_list, selection_mode):
    """ check the conditions based on selection mode and returns the agent id of selected agents """
    
    selected_agent_list = []
    selection_mode = selection_mode.lower()
    available_time_list = [i['available_since'] for i in agent_list]

    if selection_mode == 'all available':
        selected_agent_list.append([i['agent_id'] for i in agent_list]) 
    if selection_mode == 'least busy':
        selected_agent_list.append(max(available_time_list))
    if selection_mode == 'random':
        selected_agent_list.append([i['agent_id'] for i in agent_list])

    return selected_agent_list


selected_agents = select_agent(agent_list, 'All available')
print(selected_agents)
