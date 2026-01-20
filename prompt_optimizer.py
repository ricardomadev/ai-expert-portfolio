class PromptOptimizer:
    def __init__(self, model="gpt-4"):
        self.model = model

    def optimize(self, draft_prompt):
        # Scientifically-backed prompt engineering strategies
        optimized = f"System: You are an expert assistant.\\nTask: {draft_prompt}\\nConstraints: Be concise and factual."
        return optimized

if __name__ == "__main__":
    optimizer = PromptOptimizer()
    print(optimizer.optimize("Tell me about quantum computing."))
