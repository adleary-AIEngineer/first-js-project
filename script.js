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
const expense_form = document.getElementById("expense_form");

// application state //
let selectedBox = null;

// functions //
//function updateDetails(boxId) {
    //const selectedDetail = detailData[boxId];
// async function updateDetails(boxId) {
//   const response = await fetch(`http://127.0.0.1:5000/api/details/${boxId}`);
//   const selectedDetail = await response.json();
    
//   let listHTML = "";
// // adds items to listHTML from detail_data dict in app.py
//   if (selectedDetail.items && selectedDetail.items.length > 0) {
//     for (const item of selectedDetail.items) {
//       listHTML += `<li>${item}</li>`
//     }
//   };

//   details.innerHTML = 
//     `<h2>${selectedDetail.title}</h2>
//     <p>${selectedDetail.description}</p>
//     <ul>${listHTML}</ul>`;
// }

// POST new expense to server
function newExpense(formVariables) {
  async function newExpense(formVariables){
    try{
      const response = await fetch(`http://127.0.0.1:5000/api/expenses`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: {formVariables}
       });
        // Always check if the HTTP status code is OK (200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse and log the JSON response data
        const data = await response.json();
        console.log("Response from Flask:", data);

    } catch (error) {
        console.error("Error sending POST request:", error);
    }
}
  }; 


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

// 2. Attach a submit event listener.

expense_form.addEventListener("submit", function (event) {
// add in function to take the input and save the data to variables

// 3. Prevent the browser's default form submission (so it doesn't reload the page).
    event.preventDefault();
// 4. Build the expense object from the form fields.
    const formData = new FormData(event.target);
    const formVariables = Object.fromEntries(formData.entries());
// 5. For now, simply console.log(expense).
    console.log("all data saved to object", formVariables);
// Convert amount to a number.
    formVariables.amount = Number(formVariables);
    newExpense();
//6. send to server
    // const response = await fetch(...);


// Send formVariables with fetch().
// Wait for Flask's response.
// Log the response.
// Verify the new expense appears in GET /api/expenses.
});

