class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys:
            self.keys[key].append((timestamp, value))
        else:
            self.keys[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keys:
            return ""
        
        search_list = self.keys[key]
        best = ""

        low = 0
        high = len(search_list) - 1

        while (low <= high):
            mid = low + (high - low)//2

            current_timestamp, current_value = search_list[mid]

            if current_timestamp <= timestamp:
                best = current_value
                low = mid + 1
            else:
                high = mid - 1

        
        return best
        
