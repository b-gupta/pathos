import sys
import heapq

ps = [ 500, 700, 1000, 1400, 2000, 6000 ]

def find_pair(prices, amount):
    if len(prices) < 2:
        return None

    i = 0
    j = len(prices)-1
    pair = None

    while i < j:
        s = prices[j] + prices[i]
        diff = amount - s
        if diff > 0:
            pair = (prices[i], prices[j])
            i += 1
        elif diff < 0:
            j -= 1
        else:
            return (prices[i], prices[j])
    return pair

def find_n(prices, amount, n):
    if len(prices) < n:
        return None

    heap = []
    i = 0
    s = 0
    while i < n:
        heap.append(prices[i])
        s += prices[i]
        i += 1
    if s > amount:
        return None

    diff = amount - s

    heapq.heapify(heap)

    while i < len(prices):
        low = heapq.heappop(heap)
        stack = [low]
        diff = diff + low - prices[i]
        while diff < 0 and len(heap) != 0:
            diff -= low
            low = heapq.heappop(heap)
            stack.append(low)
            diff += low
        if diff < 0:
            heap += stack
            return heap
        heap += stack[0:-1]
        heap.append(prices[i])
        heapq.heapify(heap)
        i += 1
    return heap

def test():
    print ps
    print find_pair(ps, 2400)
    print find_pair(ps, 10000)
    print find_pair(ps, 500)
    print find_pair(ps, 2300)
    print find_pair(ps, 2500)
    print find_n(ps, 3300, 3)
    print find_n([1, 2, 3, 5, 8, 13], 15, 3)

if __name__ == '__main__':
    #test()
    args = sys.argv[1:]
    filename = args[0]
    amount = int(args[1])
    pmap = {}
    plist = []

    with open(filename) as f:
        for line in f:
            tokens = line.split(',')
            item = tokens[0]
            price = int(tokens[1])
            pmap[price] = item
            plist.append(price)
        pair = find_pair(plist, amount)
        if pair:
            p1 = pair[0]
            p2 = pair[1]
            print "{} {}, {} {}".format(pmap[p1], p1, pmap[p2], p2)
        else:
            print 'Not possible'

        triple = find_n(plist, amount, 3)
        if triple:
            print 'triple:',
            for t in triple:
                print pmap[t], t,
            print
        else:
            print 'Triple not possible'


