document.addEventListener('DOMContentLoaded', function () {
  const asideToggleBtn = document.getElementById('aside-toggle');
  const container = document.querySelector('.container');

  if (asideToggleBtn && container) {
    asideToggleBtn.addEventListener('click', () => {
      container.classList.toggle('sidebar-collapsed');
    });
  }

  // Existing theme toggle code if any
  const themeToggleBtn = document.getElementById('theme-toggle');
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', newTheme);
    });
  }
});
