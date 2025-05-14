document.addEventListener("DOMContentLoaded", function () {
    const addProjectBtn = document.getElementById("add-project-btn");
    const addProjectForm = document.getElementById("add-project-form");
    const cancelBtn = document.getElementById("cancel-btn");

    addProjectBtn.addEventListener("click", function () {
        addProjectForm.style.display = "block";
    });

    cancelBtn.addEventListener("click", function () {
        addProjectForm.style.display = "none";
    });
});
