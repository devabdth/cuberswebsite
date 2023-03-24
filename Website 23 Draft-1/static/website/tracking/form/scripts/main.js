const formSubmission= async ()=> {
	const statusMsg= document.getElementById('status-msg');
	const idField= document.getElementById('project-id-field');
	if (idField.value.trim().length < 8) {
		idField.style.outline= '2px red solid';
		statusMsg.innerHTML= 'Enter a valid Project ID!'
		return
	}
	idField.style.outline= 'var(--secondaryColor)';
	statusMsg.innerHTML= ''


	const accessKeyField= document.getElementById('project-access-key-field');
	if (accessKeyField.value.trim().length < 12) {
		accessKeyField.style.outline= '2px red solid';
		statusMsg.innerHTML= 'Enter a valid Project Access Key!'
		return
	}
	accessKeyField.style.outline= 'var(--secondaryColor)';
	statusMsg.innerHTML= ''

	const confirmationButton= document.getElementById('form-submission');
	confirmationButton.onclick= ()=> {}
	const clearButton= document.getElementById('form-clearation');
	clearButton.onclick= ()=> {}
	statusMsg.innerHTML= 'Loading...'
	const payload= {
		id: idField.value.trim(),
		accessKey: accessKeyField.value.trim()
	}

	const res= await fetch(
		'./', {
			method: "PATCH",
			body: JSON.stringify(payload),
			header: {
				'Content-Type': 'application/json'
			}
		}
	);

	if (res.status === 200) {
		window.open('./', '_self');
		return;
	}

	if (res.status === 500) {
		statusMsg.innerHTML= 'Failed, Try again later!';
		confirmationButton.innerHTML= 'Failed';
		setTimeout(()=> {
			confirmationButton.innerHTML= 'Submit';
			confirmationButton.onclick= ()=> {formSubmission();}
			clearButton.onclick= ()=> {formClearation();}
		}, 3000);
		return;
	}

	if (res.status === 403) {
		statusMsg.innerHTML= 'Wrong Access Key';
		accessKeyField.value= '';
		confirmationButton.innerHTML= 'Failed';
		setTimeout(()=> {
			confirmationButton.onclick= ()=> {formSubmission();}
			confirmationButton.innerHTML= 'Submit';
			clearButton.onclick= ()=> {formClearation();}

		}, 3000);
		return;
	}

	if (res.status === 404) {
		statusMsg.innerHTML= 'There is no project with the same ID!';
		confirmationButton.innerHTML= 'Failed!';
		setTimeout(()=> {
			confirmationButton.onclick= ()=> {formSubmission();}
			confirmationButton.innerHTML= 'Submit';
			clearButton.onclick= ()=> {formClearation();}
		}, 3000);
		return;
	}


}

const formClearation= ()=> {
	const idField= document.getElementById('project-id-field');
	idField.value= '';
	const accessKeyField= document.getElementById('project-access-key-field');
	accessKeyField.value= '';
}