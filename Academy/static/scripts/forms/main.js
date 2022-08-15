const validation = async () => {
	const nameField = document.getElementById("name");
	const emailField = document.getElementById("email");
	const phoneField = document.getElementById("phone");
	const addressField = document.getElementById("address");
	const governField = document.getElementById("govern");
	const stateField = document.getElementById("state");
	const birthField = document.getElementById("birth");

	if (nameField.value.trim().length < 8) {
		nameField.style.borderColor = "red";
		showToast({borderColor: "red", msg: "Please, Enter a valid Name!"});
		return;
	}
	nameField.style.borderColor = "white";

	const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
	if (!(String(emailField.value.trim()).toLowerCase().match(re))) {
		emailField.style.borderColor = "red";
		showToast({borderColor: "red", msg: "Please, Enter a valid E-mail!"});
		return;
	}
	emailField.style.borderColor = "white";


	const phoneRe = "^01[0-2,5]{1}[0-9]{8}$";
	const phoneReTwo = "^01[0-2,5]{1}[0-9]{7}$";
	if (!(String(phoneField.value.trim()).toLowerCase().match(phoneRe))) {
		phoneField.style.borderColor = "red";
		showToast({borderColor: "red", msg: "Please, Enter a valid Phone Number!"});
		return;
	}
	phoneField.style.borderColor = "white";

	if (addressField.value.trim().length < 8) {
		addressField.style.borderColor = "red";
		showToast({borderColor: "red", msg: "Please, Enter a valid Address!"});
		return;
	}
	addressField.style.borderColor = "white";

	if (stateField.value.trim().length === 0) {
		stateField.style.borderColor = "red";
		showToast({borderColor: "red", msg: "Please, Enter your state!"});
		return;
	}
	stateField.style.borderColor = "white";

	if (governField.value.trim().length === 0) {
		governField.style.borderColor = "red";
		showToast({borderColor: "red", msg: "Please, Enter your governrate!"});
		return;
	}
	governField.style.borderColor = "white";


	try {
		const maxBirthDate = new Date(Date.UTC(2004, 12, 01, 00, 00, 00));
		const minBirthDate = new Date(Date.UTC(1994, 12, 01, 00, 00, 00));

		const enteredBirthDate = new Date(birthField.value);
		if (maxBirthDate < enteredBirthDate || enteredBirthDate < minBirthDate) {
			birthField.style.borderColor = "red";
			return;
		}

	} catch (e) {
		birthField.style.borderColor = "red";
		return;
	}
	birthField.style.borderColor = "white";


	// Prepare data of the server & send it;
	try {
		const url = window.location.href;
		let courseId = (url.split("/"))[4];
		courseId = parseInt(courseId);
		
		const payload = {
			name: nameField.value.trim(),
			email: emailField.value.trim(),
			phone: phoneField.value.trim(),
			address: {
				address: addressField.value.trim(),
				state: stateField.value.trim(),
				govern: governField.value.trim(),
			},
			birth: birthField.value.trim(),
			courseId: courseId,
		}
		showToast({borderColor: "white", msg: "Loading..."});
		const res = await fetch("http://127.0.0.1:3000/forms/post/", {
			method: "post",
			body: JSON.stringify(payload),
			headers: { "Content-Type": "application/json" },
		}
		);
	
		if (res.status === 201){
			showToast({borderColor: "green", msg: "Your application submitted successfully!"});
			nameField.value = "";
			emailField.value = "";
			phoneField.value = "";
			addressField.value = "";
			state: stateField.value = ""
			govern: governField.value = "";
			return;
		}
		showToast({borderColor: "red", msg: "Failed to create your application!"})


		
	} catch (e) {
		console.log(e);
	}

}


const showToast = (props) => {
	const toastDiv = document.getElementById("toast");
	const toastText = document.getElementById("toast-text");

	toastDiv.style.borderColor = props.borderColor;
	toastText.innerHTML = props.msg;
	toastDiv.style.display = "block";

	setInterval(()=> {
		toastDiv.style.display = "none";
	}, 5000)
}


