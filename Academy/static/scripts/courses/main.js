const search = () => {
	const nameField = document.getElementById("name");
	const instructorField = document.getElementById("instructor");

	if (nameField.value.trim().length == 0 && instructorField.value.trim().length == 0 && spaceField.value.trim().length == 0) {
		nameField.style.borderColor = "red";
		instructorField.style.borderColor = "red";
		return;
	}

	nameField.style.borderColor = "white";
	instructorField.style.borderColor = "white";

	const nameToken = `course=${nameField.value}`
	const instructorToken = `instructor=${instructorField.value}`

	console.log(nameToken);
	console.log(instructorToken);

	open(`./?${nameToken}&${instructorToken}`)
}
