class TimeMap:

    def __init__(self):
        self.key_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_map:
             self.key_map[key] = []
        
        self.key_map[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
            if key not in self.key_map:
                return ""
            mood = self.key_map[key]
            l = 0
            r = len(mood) - 1
            res = ''
            while l <= r:
                mid = (l + r) // 2
                if mood[mid][0] <= timestamp:
                    l = mid + 1
                    res = mood[mid][1]
                elif mood[mid][0] > timestamp:
                    r = mid - 1
            return res                
