class stairs:
    n = 2
    def climbing(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climbing(n-1) + self.climbing(n-2)
