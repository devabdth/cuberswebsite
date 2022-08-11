
const contactSubmit = () => {
  const nameField = document.getElementById('name-field');
  const emailField = document.getElementById('email-field');
  const phoneField = document.getElementById('phone-field');
  const msgField = document.getElementById('msg-field');

  if(nameField.value.length === 0) {
    nameField.style.borderColor = 'red';
    return;
  }

  if(emailField.value.length === 0) {
    nameField.style.borderColoe = 'white';
    emailField.style.borderColor = 'red';
    return;
  }

  if(phoneField.value.length === 0) {
    nameField.style.borderColor = 'white';
    emailField.style.borderColor = 'white';
    phoneField.style.borderColor = 'red';
    return;
  }

  if(msgField.value.length < 20) {
    nameField.style.borderColor = 'white';
    emailField.style.borderColor = 'white';
    phoneField.style.borderColor = 'white';
    msgField.style.borderColor = 'red';
    return;      
  }

  nameField.style.borderColor = 'white';
  emailField.style.borderColor = 'white';
  phoneField.style.borderColor = 'white';
  msgField.style.borderColor = 'white';

  const msg = {
    sender: nameField.value,
    senderPhone: phoneField.value,
    senderEmail: emailField.value,
    msg: msgField.value,
  }

  nameField.value = '';
  emailField.value = '';
  phoneField.value = '';
  msgField.value = '';

  console.log(msg);
}
