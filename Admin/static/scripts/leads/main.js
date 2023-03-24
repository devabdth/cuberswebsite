const addLead = () => {
	const overlay = document.getElementById('lead-dialog-overlay');
	const dialog = document.getElementById('lead-dialog');
	overlay.style.display = "flex";
	dialog.style.display = "flex";
}

let currentCategory;
const sumbitLead = async () => {
	const nameField = document.getElementById('name');
	const phoneField = document.getElementById('phone');
	const emailField = document.getElementById('email');
	const agentNameField = document.getElementById('agentName');
	const positionField = document.getElementById('position');
	const addressField = document.getElementById('address');
  	const categoriesBtn = document.getElementById(`categories-dropbtn`);


	const msg = document.getElementById('submit-msg');

	if (nameField.value.trim().length <= 8 || nameField.value.trim().length >= 32) {
		nameField.style.borderColor = "red";
		msg.innerHTML = "Please, Enter a valid Name";
		msg.innerTEXT = "Please, Enter a valid Name";
		msg.style.color = 'red';
		return;
	}
	nameField.style.borderColor = "#666";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';

	const phoneRe = "^01[0-2,5]{1}[0-9]{8}$";
	if (!String(phoneField.value.trim()).match(phoneRe)) {
		phoneField.style.borderColor = "red";
		msg.innerHTML = "Please, Enter a valid Phone Number";
		msg.innerTEXT = "Please, Enter a valid Phone Number";
		msg.style.color = 'red';
		return;
	}
	phoneField.style.borderColor = "#666";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';

	const emailRe = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
	if (!String(emailField.value.trim()).toLowerCase().match(emailRe)) {
		emailField.style.borderColor = "red";
		msg.innerHTML = "Please, Enter a valid Email";
		msg.innerTEXT = "Please, Enter a valid Email";
		msg.style.color = 'red';
		return;
	}
	emailField.style.borderColor = "#666";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';


	if (agentNameField.value.trim().length <= 8 || agentNameField.value.trim().length >= 32) {
		agentNameField.style.borderColor = "red";
		msg.innerHTML = "Please, Enter a valid Agent Name";
		msg.innerTEXT = "Please, Enter a valid Agent Name";
		msg.style.color = 'red';
		return;
	}
	agentNameField.style.borderColor = "#666";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';

	if (positionField.value.trim().length === 0){
		positionField.style.borderColor = "red";
		msg.innerHTML = "Please, Enter a valid Agent position";
		msg.innerTEXT = "Please, Enter a valid Agent position";
		msg.style.color = 'red';
		return;
	}
	positionField.style.borderColor = "#666";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';

	if (addressField.value.trim().length === 0){
		addressField.style.borderColor = "red";
		msg.innerHTML = "Please, Enter a valid Agent position";
		msg.innerTEXT = "Please, Enter a valid Agent position";
		msg.style.color = 'red';
		return;
	}
	addressField.style.borderColor = "#666";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';

	if (currentCategory === undefined){
		categoriesBtn.style.border = "2px red solid";
		msg.innerHTML = "Please, Enter a valid Agent position";
		msg.innerTEXT = "Please, Enter a valid Agent position";
		msg.style.color = 'red';
		return;
	}
	categoriesBtn.style.border = "none";
	msg.innerHTML = "";
	msg.innerTEXT = "";
	msg.style.color = '#333';

	try {
		payload = {
			name: nameField.value.trim(),
			email: emailField.value.trim(),
			phone: phoneField.value.trim(),
			agentName: agentNameField.value.trim(),
			position: positionField.value.trim(),
			address: addressField.value.trim(),
			category: currentCategory,
		}

		const res = await fetch('./', {
			method: 'post',
			body: JSON.stringify(payload),
			headers: { "Content-Type": "application/json" },
		})

		if (res.status === 201) {
			window.open('.', '_self');
			return;
		}

		msg.innerHTML = "Failed to add lead, Please try again Later!";
		msg.innerTEXT = "Failed to add lead, Please try again Later!";
		msg.style.color = 'red';

	} catch (e) {
		console.log(e);
		msg.innerHTML = "Failed to add lead, Please try again Later!";
		msg.innerTEXT = "Failed to add lead, Please try again Later!";
		msg.style.color = 'red';


	}

}

const closeLeadsDialog = () => {
	const overlay = document.getElementById('lead-dialog-overlay');
	const dialog = document.getElementById('lead-dialog');
	overlay.style.display = "none";
	dialog.style.display = "none";

}

const toggleCategoriesDropdown = () => {
  document.getElementById(`categories-dropdown`).classList.toggle("show");
}

const filter = () => {
  var input, filter, ul, li, a, i;
  input = document.getElementById("category-search");
  filter = input.value.toUpperCase();
  div = document.getElementById("categories-dropdown");
  button = div.getElementsByTagName("button");
  for (i = 0; i < button.length; i++) {
    txtValue = button[i].textContent || button[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      button[i].style.display = "";
    } else {
      button[i].style.display = "none";
    }
  }
}


const chooseCategory = (category, lang) => {
  const btn = document.getElementById(`categories-dropbtn`);
  currentCategory = category;
  btn.innerHTML = currentCategory;
  btn.innerText = currentCategory;
  btn.textContent = currentCategory;

  toggleCategoriesDropdown();

}

