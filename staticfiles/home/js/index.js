document.addEventListener('DOMContentLoaded', () => {
  const envVar = document.getElementById('ENV_VAR');
  const apiKey = envVar.value;
  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      'X-Apikey': apiKey
    }
  };

  const threatChart = new Chart(
    document.getElementById('myChart'),
    {
      type: 'doughnut',
      data: {
        labels: [],
        datasets: []
      }
    }
  );

  fetch('https://www.virustotal.com/api/v3/popular_threat_categories',
    options)
    .then(response => response.json())
    .then(response => {
      console.log(response.data);
      for (item of response.data.slice(0, 10)) {
        const randomColor = getRandomColor();

        threatChart.data.labels.push(item);
        threatChart.data.datasets.push({
          label: item,
          data: [Math.floor(Math.random() * 30) + 1],
          backgroundColor: randomColor,
          borderColor: randomColor,
          borderWidth: 1
        });
      }
      threatChart.update();
    })
    .catch(err => console.error(err));

  function getRandomColor () {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 6)];
    }
    return color;
  }
});
