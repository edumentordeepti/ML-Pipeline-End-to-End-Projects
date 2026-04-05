async function predict() {
  
    const cylinders = document.getElementById("cylinders").value;
    const displacement = document.getElementById("displacement").value;
    const horsepower = document.getElementById("horsepower").value;
    const weight = document.getElementById("weight").value;
    const acceleration = document.getElementById("acceleration").value;
    const origin = document.getElementById("origin").value;

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({

            cylinders: parseFloat(cylinders),
            displacement: parseFloat(displacement),
            horsepower: parseFloat(horsepower),
            weight: parseFloat(weight),
            acceleration: parseFloat(acceleration),
            origin: parseFloat(origin),
        })
    });

    const data = await response.json();
    console.log("API Response:", data);

    if (data.predicted_mpg && !isNaN(data.predicted_mpg)) {
        document.getElementById("result").innerText =
            "Predicted MPG: " + Number(data.predicted_mpg).toFixed(2);
    } else {
        document.getElementById("result").innerText =
            "Error: " + JSON.stringify(data);
    }
}