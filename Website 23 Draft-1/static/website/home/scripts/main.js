const consultingSubmission= async ()=> {
	const nameField= document.querySelector('div#free-consultent-from input#name');
	const emailField= document.querySelector('div#free-consultent-from input#email');
	const urlField= document.querySelector('div#free-consultent-from input#url');
	const msgField= document.querySelector('div#free-consultent-from textarea#msg');
	const statusMsg= document.querySelector('div#free-consultent-from p#free-consultent-form-status');

	if (nameField.value.trim() < 8) {
		nameField.style.borderColor= 'red';
		statusMsg.innerHTML= 'Enter your full name!'
		return;
	}
	nameField.style.borderColor= 'var(--secondaryColor)'
	statusMsg.innerHTML= '';

    const re =
        /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    if (!String(emailField.value.trim().toLowerCase()).match(re)) {		
    	emailField.style.borderColor= 'red';
		statusMsg.innerHTML= 'Enter your email!'
		return;
	}
	email.style.borderColor= 'var(--secondaryColor)'
	statusMsg.innerHTML= '';
	
	if (msgField.value.trim() < 32) {
		msgField.style.borderColor= 'red';
		statusMsg.innerHTML= 'Make your message more detailed to help us helping you!'
		return;
	}
	msgField.style.borderColor= 'var(--secondaryColor)'
	statusMsg.innerHTML= '';

	const payload= {
		name: nameField.value.trim(),
		email: emailField.value.trim(),
		url: urlField.value.trim(),
		msg: msgField.value.trim(),
	}

	const submissionButton= document.querySelector('div#free-consultent-from button#free-consultent-submit');
	submissionButton.onclick= ()=> {}
	submissionButton.style.opacity= 0.5;

	const clearButton= document.querySelector('div#free-consultent-from button#free-consultent-clear');
	clearButton.onclick= ()=> {}

	statusMsg.innerHTML= 'Loading...';
	try {
		const res= await fetch(
			'/global/leads/consult', {
				method: "POST",
				body: JSON.stringify(payload),
				header: {
					'Content-Type': 'application/json'
				}
			}
		);

		if (res.status === 201) {
			consultingCleartion();
			statusMsg.innerHTML= 'Message Submitted Successfully!';
			submissionButton.onclick= ()=> {consultingSubmission();}
			submissionButton.innerHTML= 'Submit Ticket';
			submissionButton.style.opacity= 1;
			clearButton.onclick= ()=> {consultingCleartion();}

			return;
		}


		if (res.status === 401) {
			consultingCleartion();
			statusMsg.innerHTML= 'You\'ve an message submitted once before!';
			submissionButton.onclick= ()=> {consultingSubmission();}
			submissionButton.innerHTML= 'Submit Ticket';
			submissionButton.style.opacity= 1;
			clearButton.onclick= ()=> {consultingCleartion();}
			return;
		}

		if (res.status === 500) {
			statusMsg.innerHTML= 'Please, Try again later!';
			submissionButton.onclick= ()=> {consultingSubmission();}
			submissionButton.innerHTML= 'Submit Ticket';
			submissionButton.style.opacity= 1;
			clearButton.onclick= ()=> {consultingCleartion();}
			return;

		}

		

	} catch (e) {
		console.log(e);
		submissionButton.innerHTML= 'Failed';
		setTimeout(()=> {
			submissionButton.onclick= ()=> {consultingSubmission();}
			submissionButton.innerHTML= 'Submit Ticket';
			submissionButton.style.opacity= 1;
			clearButton.onclick= ()=> {consultingCleartion();}
		})
	}

	
}

const consultingCleartion= ()=> {
	document.querySelector('div#free-consultent-from input#name').value= '';
	document.querySelector('div#free-consultent-from input#email').value= '';
	document.querySelector('div#free-consultent-from input#url').value= '';
	document.querySelector('div#free-consultent-from textarea#msg').value= '';
	document.querySelector('div#free-consultent-from p#free-consultent-form-status').value= '';
}