const messageSubmit = () => {
	const nameField = document.getElementById("name");
	const emailField = document.getElementById("email");
	const msgField = document.getElementById("msg");


	if (nameField.value.trim().length < 8) {
		nameField.style.borderColor = "red";
		return;
	}
	nameField.style.borderColor = "white";

	const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
	if (!(String(emailField.value.trim()).toLowerCase().match(re))) {
		emailField.style.borderColor = "red";
		return;
	}
	emailField.style.borderColor = "white";

	if (msgField.value.trim().length < 20) {
		msgField.style.borderColor = "red";
		return;
	}
	msgField.style.borderColor = "white";



}

const clear = () => {
	const nameField = document.getElementById("name");
	const emailField = document.getElementById("email");
	const msgField = document.getElementById("msg");

	// TODO
	nameField.value = "":
	emailFeild.value = "";
	msgField.value = "";

}
