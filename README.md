# How to run

Question 1 (will start on port 3001):

```
	npm install
	npm start &
	curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http::/localhost:3001/messages
	curl -i http::/localhost:3001/messages/test
```

Question 2:

```
	python find_pair.py [file] [amount]

```

Question 3:
```
	python x01.py [x01 string]

```


# Answers to questions
```
1.

As you acquire more users and the volume of messages increases, several issues
arise with this implementation:
	- in memory map used to store messages will get too large, and you may need
	  to store messages on disk
	- a single server will not be able to handle requests from a large number of
	  users, especially if they are sending requests simultaneously. To handle
	  many users:
	  - run multiple servers behind a load balancer
	  - store messages in a shared database

As a side note, we don't need to be too concerend with collisions since we are
using sha256.

2.

This algorithm will take O(n) time since the input list of prices are in sorted
order and in the worst case (two items are in the middle) we go through them all
once.

Bonus question is implemented within find_pair

3.

This algorithm will take O(2^n) where n represents the number of x's. For each x
we branch twice (once for 0 and once for 1).
```
