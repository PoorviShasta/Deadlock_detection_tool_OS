document.getElementById('deadlockForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const processes = document.getElementById('processes').value;
    const resources = document.getElementById('resources').value;
    
    const allocationMatrix = document.getElementById('allocation').value
        .trim().split(/\s*[,|\s]\s*/).map(Number);
    const requestMatrix = document.getElementById('request').value
        .trim().split(/\s*[,|\s]\s*/).map(Number);

    const allocation = [];
    const request = [];
    for (let i = 0; i < processes; i++) {
        allocation.push(allocationMatrix.slice(i * resources, (i + 1) * resources));
        request.push(requestMatrix.slice(i * resources, (i + 1) * resources));
    }

    const response = await fetch('/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ processes, resources, allocation, request })
    });

    const result = await response.json();
    document.getElementById('result').innerText = result.message;
});
