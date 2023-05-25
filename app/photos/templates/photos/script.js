// script.js

// Artwork data
const artworkData = [
    { title: 'Artwork 1', image: 'cat1.jpg' },
    { title: 'Artwork 2', image: 'cat2.jpg' },
    { title: 'Artwork 3', image: 'cat3.jpg' },
    { title: 'Artwork 4', image: 'cat4.jpg' },
    { title: 'Artwork 5', image: 'cat5.jpg' },
    // Add more artwork data here
  ];
  
  // Items per page
  const itemsPerPage = 2;
  
  // Calculate the number of pages
  const numPages = Math.ceil(artworkData.length / itemsPerPage);
  
  // Display artwork on a specific page
  function displayArtwork(pageNumber) {
    const artworkContainer = document.getElementById('artwork-container');
    artworkContainer.innerHTML = '';
  
    const startIndex = (pageNumber - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
  
    for (let i = startIndex; i < endIndex && i < artworkData.length; i++) {
      const artwork = artworkData[i];
  
      const artworkElement = document.createElement('div');
      artworkElement.classList.add('artwork');
  
      const imageElement = document.createElement('img');
      imageElement.src = `images/${artwork.image}`;
      imageElement.alt = artwork.title;
  
      const titleElement = document.createElement('h3');
      titleElement.textContent = artwork.title;
  
      const artistElement = document.createElement('p');
      artistElement.textContent = artwork.artist;
  
      artworkElement.appendChild(imageElement);
      artworkElement.appendChild(titleElement);
      artworkElement.appendChild(artistElement);
  
      artworkContainer.appendChild(artworkElement);
    }
  }
  
  // Generate pagination links
  function generatePagination() {
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = '';
  
    for (let i = 1; i <= numPages; i++) {
      const pageLink = document.createElement('a');
      pageLink.href = '#';
      pageLink.textContent = i;
  
      pageLink.addEventListener('click', function() {
        displayArtwork(i);
      });
  
      pagination.appendChild(pageLink);
    }
  }
  
  // Initial page load
  displayArtwork(1);
  generatePagination();