class BaseRepo:
    def __init__(self, model):
        self.model = model

    async def get(self):
        return f"one - {self.model}"

    async def list(self):
        return f"many - {self.model}"

    async def delete(self):
        return f"remove - {self.model}"

    async def update(self):
        return f"update - {self.model}"

    async def craete(self, schema):
        return f"update - {self.model}"
