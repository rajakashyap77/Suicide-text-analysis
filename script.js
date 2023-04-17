document.getElementById('predict-button').addEventListener('click', function() {
    var inputText = document.getElementById('input-text').value;  // Get input text from the form
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/predict', true);  // Send a POST request to the Flask API
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            var prediction = response.prediction;  // Get the prediction result from the response
            alert('Prediction: ' + prediction);  // Display the prediction result
        } else {
            alert('Error: ' + xhr.statusText);
        }
    };
    xhr.onerror = function() {
        alert('Error: ' + xhr.statusText);
    };
    xhr.send(JSON.stringify({text: inputText}));  // Send the input text as JSON in the request body
});
