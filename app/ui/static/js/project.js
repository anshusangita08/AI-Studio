function filterProjects() {
  const searchText = document.getElementById('project-search').value.toLowerCase();
  const projectCards = document.querySelectorAll('.project-card');
  
  projectCards.forEach(card => {
    const projectName = card.querySelector('h2').textContent.toLowerCase();
    if (projectName.includes(searchText)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}