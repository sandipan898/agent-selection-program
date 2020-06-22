import random


def create_agent_list():
    """ Used to make a agent data list if needed """

    while True:
        agent_list = []
        agent_id = input("Enter an unique agent id: ")
        is_available = input("Is the agent available?(0/1) ")
        available_since = input("Available Since: ")
        roles = input("Enter the role of the agent: ")
        agent_list.append({
            'agent_id': agent_id, 'is_available': is_available, 'available_since': available_since, 'roles': roles
        })
        op = input("Want to add more agent?(y/n)").lower()
        if op == 'n':
            break
    print(agent_list)
    print("\nAgent-data:")
    for item in agent_list:
        print("\n")
        for k, v in item.items():
            print("{}: {}".format(k, v))
    return agent_list


def select_agent(agent_list, selection_mode, issue_role):
    """ check the conditions based on selection mode and returns the agent id of selected agents """

    selected_agents = None
    selection_mode = selection_mode.lower()
    for item in agent_list:
        if item['is_available']:

            if selection_mode == 'all available':
                selected_agents = [i['agent_id'] for i in agent_list]
            available_time_list = [i['available_since'] for i in agent_list]

            if selection_mode == 'least busy':
                max_time = max(available_time_list)
                selected_agents = [i['agent_id'] for i in agent_list if i['available_since'] == max_time]

            if selection_mode == 'random':
                selected_agents = [random.choice(agent_list)['agent_id']]

    return selected_agents


# selection_mode_list = ['all available', 'least busy', 'random']
# agent_list = create_agent_list()
"""
Statically creating a agent list
we can create a list by user input by using the create_agent_list() function
"""
agent_list = [
    {'agent_id': 1, 'is_available': 1, 'available_since': 2, 'roles': 'sales'},
    {'agent_id': 2, 'is_available': 1, 'available_since': 3, 'roles': 'spanish speaker'},
    {'agent_id': 3, 'is_available': 0, 'available_since': 2, 'roles': 'sales'},
    {'agent_id': 4, 'is_available': 1, 'available_since': 1, 'roles': 'support'},
    {'agent_id': 5, 'is_available': 1, 'available_since': 3, 'roles': 'sales'},
]
mode = input("Enter agent selection mode (all available, least busy or random): ")
selected_agents = select_agent(agent_list, mode)

print("\n*********Selected agents with their data*********\n")
for a_id in selected_agents:
    for i in agent_list:
        if i['agent_id'] == a_id:
            print("Agent-{}  Available_since: {}  Role: {}".format(a_id, i['available_since'], i['roles']))
