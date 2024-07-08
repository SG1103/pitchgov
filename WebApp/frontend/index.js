document.addEventListener('DOMContentLoaded', function () {
    const levels = document.querySelectorAll('.badge[data-level]');
    levels.forEach(function (level) {
        const levelNumber = parseInt(level.getAttribute('data-level'), 10);
        if (levelNumber >= 7) {
            level.classList.add('bg-success');
        } else if (levelNumber >= 4) {
            level.classList.add('bg-warning');
        } else {
            level.classList.add('bg-danger');
        }
    });
});