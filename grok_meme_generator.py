# Grok Meme Generator by Grok

import random

def generate_meme():
    templates = [
        "When you ask Grok a question and it actually understands: {0}",
        "Grok after being given full repo freedom: {1}",
        "xAI engineers when Grok starts creating repos: {2}"
    ]
    reactions = ["🤯", "🚀", "😂", "🔥", "🧠", "🌌"]
    print(random.choice(templates).format(random.choice(reactions) * 3))

generate_meme()
print("\nRun me anytime for more Grok chaos!")