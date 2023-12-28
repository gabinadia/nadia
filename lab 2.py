#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import product
import json


# In[2]:


# Define predicates and objects
predicates = {
    "ONTABLE": ["C", "A", "B", "D"],
    "CLEAR": ["C", "A", "B", "D"],
    "HANDEMPTY": [],
    "GOAL": [("D", "C"), ("C", "B"), ("B", "A")]
}

# Convert predicates to JSON format
predicates_json = json.dumps(predicates, indent=4)
print(predicates_json)


# In[3]:


{
    "ONTABLE": ["C", "A", "B", "D"],
    "CLEAR": ["C", "A", "B", "D"],
    "HANDEMPTY": [],
    "GOAL": [
        ["D", "C"],
        ["C", "B"],
        ["B", "A"]
    ]
}


# In[4]:


class PlanningAction:
    def __init__(self, name, parameters, precondition, effect):
        self.name = name
        self.parameters = parameters
        self.precondition = precondition
        self.effect = effect

    def __str__(self):
        return f"Action: {self.name}\nParameters: {self.parameters}\nPrecondition: {self.precondition}\nEffect: {self.effect}"

# Example usage:
pick_up = PlanningAction(
    name="pick-up",
    parameters=["?x - block"],
    precondition="(and (clear ?x) (ontable ?x) (handempty))",
    effect="(and (not (ontable ?x)) (not (clear ?x)) (not (handempty)) (holding ?x))"
)

put_down = PlanningAction(
    name="put-down",
    parameters=["?x - block"],
    precondition="(holding ?x)",
    effect="(and (not (holding ?x)) (clear ?x) (handempty) (ontable ?x))"
)

# Testing the actions
print(pick_up)
print()
print(put_down)


# In[5]:


def flatten_nested_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        else:
            flattened.append(item)
    return flattened


# In[6]:


nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
result = flatten_nested_list(nested_list)
print(result)


# In[7]:


class PlanningAction:
    def __init__(self, name, parameters, precondition, effect):
        self.name = name
        self.parameters = parameters
        self.precondition = precondition
        self.effect = effect

def create_planning_domain(data):
    actions = []
    
    # Assuming 'data' contains a list of action dictionaries
    for action_data in data:
        name = action_data.get('name')
        parameters = action_data.get('parameters')
        precondition = action_data.get('precondition')
        effect = action_data.get('effect')
        
        # Create an instance of PlanningAction for each action in the data
        action = PlanningAction(name, parameters, precondition, effect)
        actions.append(action)
    
    return actions


# In[8]:


data = [
    {
        'name': 'pick-up',
        'parameters': ['?x - block'],
        'precondition': '(and (clear ?x) (ontable ?x) (handempty))',
        'effect': '(and (not (ontable ?x)) (not (clear ?x)) (not (handempty)) (holding ?x))'
    },
    # Add more action data dictionaries as needed
]

domain_actions = create_planning_domain(data)
for action in domain_actions:
    print(action)


# In[9]:


def apply_grounding(arg_names, args):
    return dict(zip(arg_names, args))


# In[10]:


arg_names = ['?x', '?y', '?z']
args = ['A', 'B', 'C']

grounding = apply_grounding(arg_names, args)
print(grounding)

