// Chrome extension popup script
document.getElementById('scan-button').addEventListener('click', async () => {
    const text = document.getElementById('input-text').value;
    try {
        const response = await fetch('http://localhost:5000/scan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });
        const result = await response.json();
        if (result.error) {
            document.getElementById('result').innerHTML = `❌ Error: ${result.error}`;
        } else {
            const alert = result.is_fake ? '🔴 Likely Fake!' : '✅ Credible!';
            document.getElementById('result').innerHTML = `
                ${alert}<br>
                Confidence: ${(result.confidence * 100).toFixed(1)}%<br>
                Explanation: ${result.explanation}
            `;
        }
    } catch (error) {
        document.getElementById('result').innerHTML = '❌ Failed to connect to the server.';
    }
});