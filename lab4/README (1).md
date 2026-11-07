# AI Lab 4 - A* Search

## About This Lab
In this lab, I worked with A* search and Uniform Cost Search (UCS). I used a small graph to find a path from the starting node S to the goal node G.

## What I Did
- Implemented A* search in Python.
- Compared A* with Uniform Cost Search.
- Changed the heuristic value of node C to 10.
- Checked how the heuristic change affected the result.

## Results
With the original heuristic, A* found the path S → A → C → G with a total cost of 6.

UCS also found the same path with a cost of 6.

When I changed h(C) to 10, A* selected the path S → B → G with a cost of 9.

## Files
- `lab4_astar_audit.py` - Python code
- `output_trace.txt` - Program output
- `Lab4_Report.docx` - Lab report

## How to Run
Open the terminal and run:

```bash
python lab4_astar_audit.py
```

## Conclusion
This lab helped me understand how A* uses the heuristic to choose nodes. I also learned that an overestimated heuristic can lead to a path that is not optimal.