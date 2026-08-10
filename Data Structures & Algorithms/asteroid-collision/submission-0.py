class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        
        s = []

        for elem in asteroids:
            isalive = True
            while s and (s[-1] > 0 and elem < 0):
                if abs(elem) > abs(s[-1]):
                    s.pop()
                elif abs(s[-1]) == abs(elem):
                    s.pop()
                    isalive = False
                    break
                else:
                    isalive = False
                    break
            
            if isalive:
                s.append(elem)

        return s
