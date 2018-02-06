class SimplePasswordBackend:
    def authenticate(self, request, password=None):
        print(password)
