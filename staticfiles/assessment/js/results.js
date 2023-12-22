document.addEventListener('DOMContentLoaded', () => {
  const reputationScoreElement =
	document.getElementById('reputation-score').textContent;
  const reputationScore = parseFloat(reputationScoreElement);

  console.log(reputationScore);
  console.log(typeof (reputationScore));

  // Update progress bar
  const progressBar = document.getElementById('progress');
  if (reputationScore < 0) {
    // If negative, make the progress bar red
    progressBar.style.backgroundColor = '#FF0000';
    progressBar.style.width = Math.abs(reputationScore) + '%';
  } else {
    progressBar.style.width = reputationScore + '%';
    console.log(`${reputationScore}%`);
  }

  // Update result message and color
  const resultMessageElement =
	document.getElementById('result-message');
  if (reputationScore > 0) {
    resultMessageElement.textContent = 'Resource is harmless!';
    resultMessageElement.style.color = '#4CAF50';
  } else if (reputationScore === 0) {
    resultMessageElement.textContent = 'Resource is safe!';
    resultMessageElement.style.color = '#FFA500';
  } else {
    resultMessageElement.textContent = 'Resource is harmful!';
    resultMessageElement.style.color = '#FF0000';
  }
});
