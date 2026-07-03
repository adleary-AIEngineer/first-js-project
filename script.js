// data //
/*const detailData = {
  expenses: {
    title: "Expenses",
    description: "Track your spending and monthly budget.",
    items: [
      "Groceries - $84",
      "Gas - $32",
      "Internet - $45"
    ]
  },
  income: {
    title: "Income",
    description: "Monitor salary, dividends, and other income."
  },
  reports: {
    title: "Reports",
    description: "view spending trends and financial summaries."
  },
  settings: {
    title: "Settings",
    description: "Configure application preferences."
  }
};*/

// DOM elements //

const boxes = document.querySelectorAll(".box");
const details = document.getElementById("details");

// application state //
let selectedBox = null;

// functions //
//function updateDetails(boxId) {
    //const selectedDetail = detailData[boxId];
async function updateDetails(boxId) {
  const response = await fetch(`http://127.0.0.1:5000/api/details/${boxId}`);
  const selectedDetail = await response.json();
    
  let listHTML = "";

  if (selectedDetail.items && selectedDetail.items.length > 0) {
    for (const item of selectedDetail.items) {
      listHTML += `<li>${item}</li>`
    }
  };

  details.innerHTML = 
    `<h2>${selectedDetail.title}</h2>
    <p>${selectedDetail.description}</p>
    <ul>${listHTML}</ul>`;
}


// event listeners //
boxes.forEach(box => {
    box.addEventListener("click", function () {
      //console.log("Before", selectedBox);

      if (selectedBox) {
        //console.log("Removing", selectedBox.id);
        selectedBox.classList.remove("selected");
        }
        
        box.classList.add("selected");
        selectedBox = box;

        //console.log("After:", selectedBox.id);
        updateDetails(box.id); //prints information to the panel//
    });
}); 