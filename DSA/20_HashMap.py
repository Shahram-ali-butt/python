class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _get_bucket_(self, key):
        index = hash(key) % self.size
        return self.buckets[index]

    def put(self, key, value):
        bucket = self._get_bucket_(key)
        for i, (k,v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key,value)
                    return
        bucket.append((key,value))

    def get(self, key):
        bucket = self._get_bucket_(key)
        for (k,v) in bucket:
             if k == key:
                  return v
        raise KeyError(f"key {key} not found.")

    def remove(self, key):
        bucket = self._get_bucket_(key)
        for i, (k,v) in enumerate(bucket):
            if k == key:
                return bucket.pop(i)
        raise KeyError(f"Key {key} not found.")

    def __str__(self):
         return str({i: bucket for i, bucket in enumerate(self.buckets) if(bucket)})

myMap = HashMap()
# print(myMap)
# print("---")
myMap.put("user1", "Shahram")
myMap.put("user1", "Harmain")
# print(myMap)
# print("---")
myMap.put("user2", "Shahram")
myMap.put("user3", "Abdullah")
myMap.put("user4", "Mehmood")
myMap.put("user11", "Haider")
print(myMap)
print("---")
myMap.put("user11", "Ibrahim")
myMap.remove("user3")    
print(myMap)
print("---")
