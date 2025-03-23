import numpy as np

def detect_deadlock(processes, resources, allocation, request):
    work = np.zeros(resources)
    finish = [False] * processes

    # Calculate available resources
    for j in range(resources):
        work[j] = sum(allocation[i][j] for i in range(processes)) - sum(request[i][j] for i in range(processes))

    # Find a safe sequence (if exists)
    safe_sequence = []
    while len(safe_sequence) < processes:
        allocated = False
        for i in range(processes):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(resources)):
                safe_sequence.append(i)
                work += allocation[i]
                finish[i] = True
                allocated = True
                break
        if not allocated:
            return True, "Deadlock detected!"

    return False, f"No deadlock detected. Safe sequence: {safe_sequence}"
