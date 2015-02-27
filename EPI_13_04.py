# Implement a cache
# ISBN lookup and LRU
# TODO: Finish Leetcode LRU


class IsbnCash:

    def __init__(self):
        self.cache = {}
        #   a dict to store {ISBN : [Price, Queue_Node]}

        # self.queue = Queue()

    # insert