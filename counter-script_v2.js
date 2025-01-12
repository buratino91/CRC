async function updateVisitorCount() {
    try {
        console.log('Updating count...');
        // First make POST request to increment count
        const updateResponse = await fetch('https://8t8k35g0qh.execute-api.us-east-1.amazonaws.com/views', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!updateResponse.ok) {
            throw new Error(`HTTP error! status: ${updateResponse.status}`);
        }

        // Then fetch the updated count
        const getResponse = await fetch('https://5aha908gwf.execute-api.us-east-1.amazonaws.com/getViews');
        
        if (!getResponse.ok) {
            throw new Error(`HTTP error! status: ${getResponse.status}`);
        }
        
        const data = await getResponse.json();
        console.log('Received data:', data);
        document.getElementById('visitorCount').textContent = data.Count;
        
    } catch (error) {
        console.error('Detailed error:', error);
        console.error('Error name:', error.name);
        console.error('Error message:', error.message);
        document.getElementById('visitorCount').textContent = 'Error loading count';
    }
}
// Call the function when the page loads
document.addEventListener('DOMContentLoaded', updateVisitorCount);