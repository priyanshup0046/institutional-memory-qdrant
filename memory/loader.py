import json, glob

def load_memories(path="dataset/*.json"):
    memories = []
    for file in glob.glob(path):
        with open(file) as f:
            memories.append(json.load(f))
    return memories
