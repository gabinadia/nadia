#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import product
import heapq
import json


# In[2]:


# Predicates and objects mapping
objects = ['A', 'B', 'C', 'D']
predicates = {
    "on": [],
    "on_table": [],
    "clear": [],
    "holding": []
}

# Define the problem instance
problem = {
    "domain": "BLOCKS",
    "objects": objects,
    "initial_state": {
        "CLEAR": ['B'],
        "ONTABLE": ['D'],
        "ON": [('B', 'C'), ('C', 'A'), ('A', 'D')],
        "HANDEMPTY": []
    },
    "goal_state": {
        "ON": [('D', 'C'), ('C', 'A'), ('A', 'B')]
    }
}

# Printing predicates and object mappings
print("Predicates:")
print(json.dumps(predicates, indent=4))

print("\nObjects:")
print(json.dumps(problem, indent=4))


# In[3]:


{
    "key1": "value1",
    "key2": [
        "value2",
        "value3"
    ],
    "key3": {
        "nested_key": "nested_value"
    }
}


# In[4]:


from itertools import product

class Action:
    def __init__(self, name, types=(), unique=False, same=False):
        self.name = name
        self.types = types
        self.unique = unique
        self.same = same

    def generate_grounding(self, *args):
        return f"{self.name}({', '.join(args)})"

class PlanningDomain:
    def __init__(self, actions=()):
        self.actions = tuple(actions)

    def generate_groundings(self, objects):
        grounded_actions = []
        for action in self.actions:
            parameters = [objects[type_] for type_ in action.types]
            combinations = set()

            for param_set in product(*parameters):
                param_set_frozen = frozenset(param_set)

                if action.unique and len(param_set_frozen) != len(param_set):
                    continue

                if action.same and param_set_frozen in combinations:
                    continue

                combinations.add(param_set_frozen)
                grounded_actions.append(action.generate_grounding(*param_set))

        return grounded_actions

# Define your actions
actions = [
    Action("pick-up", types=["block"], unique=True),
    Action("put-down", types=["block"]),
    Action("stack", types=["block", "block"], same=True)
]

# Create a PlanningDomain with defined actions
planning_domain = PlanningDomain(actions)

# Define objects for grounding
objects = {
    "block": ["A", "B", "C"]
}

# Generate grounded actions
grounded_actions = planning_domain.generate_groundings(objects)

# Print grounded actions
for grounded_action in grounded_actions:
    print(grounded_action)


# In[ ]:


class PlanningAction:
    def __init__(self, name, parameters=(), preconditions=(), effects=(), unique=False, same=False):
        self.name = name
        if len(parameters) > 0:
            self.types, self.arg_names = zip(*parameters)
        else:
            self.types = tuple()
            self.arg_names = tuple()
        self.preconditions = preconditions
        self.effects = effects
        self.unique = unique
        self.same = same

    def generate_grounding(self, *args):
        return GroundedPlanningAction(self, *args)

    def __str__(self):
        arg_list = ','.join(['%s' % pair for pair in zip(self.arg_names)])
        return '%s(%s)' % (self.name, arg_list)

# Define your grounded action class
class GroundedPlanningAction:
    def __init__(self, action, *args):
        self.action = action
        self.arguments = args

    def __str__(self):
        return f'{self.action.name}({", ".join(str(arg) for arg in self.arguments)})'

# Example usage
action_params = [
    ("block", "?x"),
    ("block", "?y


# In[7]:


def flatten_nested_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_nested_list(item))
        else:
            flat_list.append(item)
    return flat_list


# In[8]:


nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
result = flatten_nested_list(nested_list)
print(result)


# In[9]:


class PlanningState:

    def __init__(self, predicates, functions, predecessor=None):
        self.predicates = frozenset(predicates)
        self.functions = tuple(functions.items())
        self.f_dict = functions
        self.predecessor = predecessor

    def apply(self, action):
        new_predicates = set(self.predicates)
        new_predicates |= set(action.effects)
        new_predicates -= set(action.preconditions)

        new_functions = dict()
        new_functions.update(self.functions)

        return PlanningState(new_predicates, new_functions, (self, action))

    def extract_plan(self):
        plan = list()
        current_state = self
        while current_state.predecessor is not None:
            plan.append(current_state.predecessor[1])
            current_state = current_state.predecessor[0]

        plan.reverse()
        return plan

    def __hash__(self):
        return hash((self.predicates, self.functions))

    def __eq__(self, other):
        return ((self.predicates, self.functions) ==
                (other.predicates, other.functions))

    def __lt__(self, other):
        return hash(self) < hash(other)


# In[10]:


def null_heuristic():
    return 0


# In[11]:


# Print actions and action combinations
print("Actions:")
[print(action.__str__()) for action in planning_domain.actions]


# In[13]:


print("Actions:")
for action in planning_domain.actions:
    print(action.__str__())


# In[ ]:




