const search = () => {
	const instructorField = document.getElementById("instructor");

	if (instructorField.value.trim().length == 0) {
		instructorField.style.borderColor = "red";
		return;
	}

	instructorField.style.borderColor = "white";

	const instructorToken = `instructor=${instructorField.value}`


	open(`./?${instructorToken}`)
}
