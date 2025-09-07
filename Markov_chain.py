import random

class CharMarkovGenerator:
    def __init__(self):
        self.model = {}
        self.order = 1
    
    def train(self, text, n=4):
        self.order = n
        for i in range(len(text) - n):
            state = text[i:i+n]
            next_char = text[i+n]
            if state not in self.model:
                self.model[state] = []
            self.model[state].append(next_char)
    
    def generate(self, length=300, seed=None):
        if not self.model:
            return "Model is empty. Train it first."
        
        # Start from seed or random state
        if seed and len(seed) >= self.order:
            state = seed[-self.order:]
            output = seed
        else:
            state = random.choice(list(self.model.keys()))
            output = state
        
        for _ in range(length - len(output)):
            next_chars = self.model.get(state)
            if not next_chars:
                break
            next_char = random.choice(next_chars)
            output += next_char
            state = output[-self.order:]
        
        return output


# Example usage
if __name__ == "__main__":
    # Training text: Shakespeare excerpt
    training_text = """
    It is a truth universally acknowledged, that a single man in possession 
    of a good fortune, must be in want of a wife. However little known the 
    feelings or views of such a man may be on his first entering a neighbourhood, 
    this truth is so well fixed in the minds of the surrounding families, that 
    he is considered as the rightful property of some one or other of their daughters.
    """

    
    generator = CharMarkovGenerator()
    generator.train(training_text, n=5)  # 5-char context
    
    # Generate new Shakespeare-like text
    print("=== Generated Text ===")
    print(generator.generate(400, seed="However"))
