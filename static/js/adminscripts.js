// Function to add a user to the list dynamically
function addUserToList(username) {
    const userList = document.getElementById('user-list');
    const listItem = document.createElement('li');
    listItem.textContent = username;
    userList.appendChild(listItem);
  }

  // Handle form submission
  document.addEventListener('DOMContentLoaded', function() {
      const addUserForm = document.getElementById('add-user-form');
      addUserForm.addEventListener('submit', (event) => {

        // Get form data
        const usertype = document.getElementById('usertype').value;
        const sequencenumber = document.getElementById('sequencenumber').value;
        const min = parseInt(document.getElementById('min').value);
        const max = parseInt(document.getElementById('max').value);
        const department = document.getElementById('department').value;

        // Loop to create and add users
        for (let i = min; i <= max; i++) {
          const username = `${sequencenumber}${i.toString().padStart(2, '0')}`;
          addUserToList(username);
        }
      });

      // Search Functionality
      const searchInput = document.getElementById('search-input');
      const userRows = document.querySelectorAll('.user-row'); // Select rows with the class "user-row"

      searchInput.addEventListener('keyup', () => {
        const searchTerm = searchInput.value.toLowerCase();
        userRows.forEach(row => {
          const usernameCell = row.querySelector('td:first-child');
          const username = usernameCell.textContent.toLowerCase();
          if (username.includes(searchTerm)) {
            row.style.display = ''; // Show the row
          } else {
            row.style.display = 'none'; // Hide the row
          }
        });
      });
  });
