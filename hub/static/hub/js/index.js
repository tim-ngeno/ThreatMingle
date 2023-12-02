document.addEventListener('DOMContentLoaded', () => {
  console.log('Checking connection from index.js');

  // Focus on roomInput when page loaded
  document.querySelector('#roomInput').focus();

  // Connecting to a room
  const connectToRoom = (roomName) => {
    window.location.pathname += 'chat/' + roomName + '/';
  };

  // Submit if user presses enter
  document.querySelector('#roomInput').onkeyup = (e) => {
    if (e.keyCode === 13) {
      document.querySelector('#roomConnect').click();
    }
  };

  // Common eventListener for both 'Connect' and 'Select'
  const connectHandler = () => {
    const roomInput = document.querySelector('#roomInput');
    const roomName = roomInput.value.trim();

    // Check if roomName is not empty
    if (roomName !== '') {
      connectToRoom(roomName);
    } else {
      alert('Please enter a valid room name.');
      roomInput.focus();
    }
  };

  // Redirect to room/<roomInput>
  document.querySelector('#roomConnect').onclick = connectHandler;

  // Redirect to room<selectedRoom> when select dropdown changes
  document.querySelector('#roomSelect').onchange = () => {
    const roomSelect = document.querySelector('#roomSelect');
    const selectedIndex = roomSelect.selectedIndex;

    if (selectedIndex !== -1) {
      const selectedOption = roomSelect.options[selectedIndex];
      const roomName = selectedOption.text.split(' (')[0];
      const roomInput = document.querySelector('#roomInput');

      console.log('Selected room:', roomName);

      // Set the value of room input
      roomInput.value = roomName;
      console.log(`Updated room value: ${roomInput.value}`);

      if (roomName !== '') {
        connectToRoom(roomName);
      } else {
        alert('Please select a valid room.');
      }
    }
  };
});
