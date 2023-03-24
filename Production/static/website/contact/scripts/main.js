const sendMessageConfirmation = async() => {
    const nameField = document.querySelector('section#send-message input#name-field');
    const emailField = document.querySelector('section#send-message input#email-field');
    const messageField = document.querySelector('section#send-message textarea#message-field');
    const confirmartionButton = document.querySelector('section#send-message button#send-msg-submission');
    const statusMsg = document.querySelector('section#send-message p#send-msg-form-status');

    statusMsg.innerHTML = '';
    if (nameField.value.trim().length < 8 || nameField.value.trim().length > 32) {
        nameField.style.outline = '1px red solid';
        statusMsg.innerHTML = `Please, Enter your &nbsp<span class='underline'>"Full Name"</span>!`;
        return;
    }

    nameField.style.outline = `1px var(--secondaryColor) solid`;
    statusMsg.innerHTML = '';

    const re =
        /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

    if (!String(emailField.value.trim().toLowerCase()).match(re)) {
        emailField.style.outline = '1px red solid';
        statusMsg.innerHTML = `Please, Enter your a valid&nbsp<span class='underline'>"Email"</span>!`;
        return;
    }

    emailField.style.outline = `1px var(--secondaryColor) solid`;
    statusMsg.innerHTML = '';

    if (messageField.value.trim().length == 0) {
        messageField.style.outline = '1px red solid';
        statusMsg.innerHTML = `Please, Write us a&nbsp<span class='underline'>message</span>!`;
        return;
    }

    if (messageField.value.trim().length < 32) {
        messageField.style.outline = '1px red solid';
        statusMsg.innerHTML = `Please, Make your&nbsp<span class='underline'>message</span>&nbspmore detailed!`;
        return;
    }
    messageField.style.outline = `1px var(--secondaryColor) solid`;
    
    statusMsg.innerHTML= 'Loading...!';
    confirmartionButton.onclick= ()=> {}
    confirmartionButton.style.opacity= '0.8';
    payload= {
        name: nameField.value.trim(),
        email: emailField.value.trim(),
        message: messageField.value.trim(),
    }

    try {
        const res= await fetch(
            '/global/leads/tickets/', {
                method: "POST",
                body: JSON.stringify(payload),
                header: {
                    'Content-Type': 'application/json'
                }

            }
        );

        console.log(res.status)
        if(res.status === 201) {
            sendMessageClearation();
            statusMsg.innerHTML= 'Lesgooo! You\'re subscribed now!';
            confirmartionButton.style.opacity= '1';
            confirmartionButton.onclick= ()=> { sendMessageConfirmation() };
            return;
        }

        statusMsg.innerHTML= 'Failed! Please, Try again later!';
        confirmartionButton.style.opacity= '1';
        confirmartionButton.onclick= ()=> { sendMessageConfirmation() };
    } catch (e) {
        console.log(e);
        statusMsg.innerHTML= 'Failed! Please, Try again later!';
        confirmartionButton.style.opacity= '1';
        confirmartionButton.onclick= ()=> { sendMessageConfirmation() };
    }

}

const sendMessageClearation = () => {
    const nameField = document.querySelector('section#send-message input#name-field');
    nameField.value= '';

    const emailField = document.querySelector('section#send-message input#email-field');
    emailField.value= '';

    const messageField = document.querySelector('section#send-message textarea#message-field');
    messageField.value= '';


}

const subscribeConfirmation = async() => {
    const nameField= document.querySelector('section#subscribe input.single-line-field#name-field')
    const emailField= document.querySelector('section#subscribe input.single-line-field#email-field')
    const topicsLegend= document.querySelector('section#subscribe div#form > label');
    const topicsCheckboxes= document.getElementsByClassName('topic-checkbox');
    const confirmartionButton = document.querySelector('section#subscribe button#send-msg-submission');
    const statusMsg = document.querySelector('section#subscribe p#subscribe-form-status');

    statusMsg.innerHTML = '';
    if (nameField.value.trim().length < 8 || nameField.value.trim().length > 32) {
        nameField.style.outline = '1px red solid';
        statusMsg.innerHTML = `Please, Enter your &nbsp<span class='underline'>"Full Name"</span>!`;
        return;
    }

    nameField.style.outline = `1px var(--secondaryColor) solid`;
    statusMsg.innerHTML = '';

    const re =
        /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

    if (!String(emailField.value.trim().toLowerCase()).match(re)) {
        emailField.style.outline = '1px red solid';
        statusMsg.innerHTML = `Please, Enter your a valid&nbsp<span class='underline'>"Email"</span>!`;
        return;
    }

    emailField.style.outline = `1px var(--secondaryColor) solid`;
    statusMsg.innerHTML = '';

    let selectedTopics= [];
    for (let e of topicsCheckboxes){
        if (e.checked) selectedTopics.push(e.id);
    }

    if (selectedTopics.length === 0) {
        topicsLegend.style.color= 'red';
        statusMsg.innerHTML= "Please, select the&nbsp<span class='underline'>Topics</span>&nbsp you are interested in!"
        return;
    }
    statusMsg.innerHTML= 'Loading...!';
    confirmartionButton.onclick= ()=> {}
    confirmartionButton.style.opacity= '0.8';
    payload= {
        name: nameField.value.trim(),
        email: emailField.value.trim(),
        topics: selectedTopics,
    }

    try {
        const res= await fetch(
            '/global/leads/newsletter/', {
                method: "POST",
                body: JSON.stringify(payload),
                header: {
                    'Content-Type': 'application/json'
                }

            }
        );

        console.log(res.status)
        if(res.status === 201) {
            subscribeClearation();
            statusMsg.innerHTML= 'Lesgooo! You\'re subscribed now!';
            confirmartionButton.style.opacity= '1';
            confirmartionButton.onclick= ()=> { subscribeConfirmation() };
            return;
        }

        statusMsg.innerHTML= 'Failed! Please, Try again later!';
        confirmartionButton.style.opacity= '1';
        confirmartionButton.onclick= ()=> { subscribeConfirmation() };
    } catch (e) {
        console.log(e);
        statusMsg.innerHTML= 'Failed! Please, Try again later!';
        confirmartionButton.style.opacity= '1';
        confirmartionButton.onclick= ()=> { subscribeConfirmation() };
    }


}

const subscribeClearation = () => {
    const nameField= document.querySelector('section#subscribe input.single-line-field#name-field')
    nameField.value= '';

    const emailField= document.querySelector('section#subscribe input.single-line-field#email-field')
    emailField.value= '';

    const topicsCheckboxes= document.getElementsByClassName('topic-checkbox');
    for (let e of topicsCheckboxes) e.checked= false;

}