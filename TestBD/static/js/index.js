GetValue()

document.querySelector(".add").addEventListener('click',()=>{
let name = document.querySelector(".name").value;
let surname = document.querySelector(".surname").value;
let age = document.querySelector(".age").value;
const postData = {
    student_name: name,
    student_surname: surname,
    student_age: age
    };
    
    axios.post('crud/', postData)
    .then(function (response) {
        document.querySelectorAll(".table_field").forEach(e=>{e.remove()});
        GetValue()
    })
    .catch(function (error) {
        console.error('POST error:', error);
    });
});

function GetValue()
{
    axios.get('crud/')
  .then(function (response) {
var existingElement = document.querySelector(".fields");
for (var i = 0; i < response.data.length; i++) {
var newDiv = document.createElement("tr");
newDiv.className = "table_field"
newDiv.innerHTML = `<th scope="col">${response.data[i].student_name}</th>
<th scope="col">${response.data[i].student_surname}</th>
<th scope="col">${response.data[i].student_age}</th>
<th scope="col">
<button class="btn btn-primary" id= '${response.data[i].id}' value= '${response.data[i].id}' onclick="DeleteValue(this.value)">Delete</button>
</th>`;

existingElement.insertAdjacentElement('afterend', newDiv);
}
  })
  .catch(function (error) {
    console.error('GET error:', error);
  });
};

function DeleteValue(value){
    axios.delete(`crud/delete/${value}`)
  .then(function (response) {
    document.querySelectorAll(".table_field").forEach(e=>{e.remove()});
    GetValue()
  })
  .catch(function (error) {
    console.error('Delete error:', error);
  });
}
