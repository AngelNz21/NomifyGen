let properNames = [];

function fetchProperNames(limit, gender) {
    fetch(`/proper-names?limit=${limit}&gender=${gender}`)
        .then(response => response.json())
        .then(data => {
            properNames = data.proper_names;
            displayNames(properNames);
        })
        .catch(error => {
            console.error("Error fetching proper names:", error);
        });
}

function displayNames(names) {
    const nameList = document.getElementById("nameList");
    nameList.innerHTML = "";

    names.forEach(name => {
        const li = document.createElement("li");
        li.textContent = name;
        nameList.appendChild(li);
    });
}

window.addEventListener("load", function() {
    fetchProperNames(10, "all");
});

document.getElementById("getNames").addEventListener("click", function() {
    const limit = document.getElementById("limit").value;
    const gender = document.getElementById("gender").value;
    fetchProperNames(limit, gender);
});

document.getElementById("sortAsc").addEventListener("click", function() {
    const sortedNames = [...properNames].sort();
    displayNames(sortedNames);
});

document.getElementById("sortDesc").addEventListener("click", function() {
    const sortedNames = [...properNames].sort().reverse();
    displayNames(sortedNames);
});
