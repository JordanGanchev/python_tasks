from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = deque(int(x) for x in input().split(', '))

box_of_eegs = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)

    elif egg == 13:
        papers.append(paper)
        paper_first = papers.popleft()
        paper_end = papers.pop()
        papers.append(paper_first)
        papers.appendleft(paper_end)

    elif egg + paper <= 50:
        box_of_eegs += 1

if box_of_eegs != 0:
    print(f"Great! You filled {box_of_eegs} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '. join([str(x) for x in eggs])}")

if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")