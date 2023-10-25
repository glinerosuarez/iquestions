# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use binary search

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(logn)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(2n)$$

# Code
```
class TimeMap:

    def __init__(self):
        self.ts_data = dict()
        self.value_data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ts_data:
            self.ts_data[key].append(timestamp)
            self.value_data[key].append(value)
        else:
            self.ts_data[key] = [timestamp]
            self.value_data[key] = [value]

    def get(self, key: str, timestamp: int) -> str:
        ts = self.ts_data.get(key, None)
        value = None
        if ts is None or len(ts) == 0 or ts[0] > timestamp:
            return ""
        
        l, r = 0, len(ts) - 1
        while l <= r:
            mid = l + (r - l)//2
            if ts[mid] <= timestamp:
                value = mid if value is None else max(value, mid)
                l = mid + 1
            else:
                r = mid - 1

        return "" if value is None else self.value_data[key][value]
        #return value
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```