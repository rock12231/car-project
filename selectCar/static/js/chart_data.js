//myChart
const data = {
    labels: {{ dataX | safe }},
datasets: [{
    label: 'My First Dataset',
    data: {{ dataY | safe }},
    backgroundColor: [
    'rgb(255, 99, 132)',
    'rgb(255, 159, 64)',
    'rgb(255, 205, 86)',
    'rgb(75, 192, 192)',
    'rgb(54, 162, 235)',
    'rgb(153, 102, 255)'
    ],
    backgroundColor: [
    'rgba(255, 99, 132, 0.8)',
    'rgba(255, 159, 64, 0.8)',
    'rgba(255, 205, 86, 0.8)',
    'rgba(75, 192, 192, 0.8)',
    'rgba(54, 162, 235, 0.8)',
    'rgba(153, 102, 255, 0.8)',
    ],
    borderWidth: 1
            }]
        };

const config = {
    type: 'bar',
    data: data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    },
};


const myChart = new Chart(
    document.getElementById('myChart'),
    config
);
