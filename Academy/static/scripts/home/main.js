const showToast = (props) => {
    const toastDiv = document.getElementById("toast");
    const toastText = document.getElementById("toast-text");

    toastDiv.style.borderColor = props.borderColor;
    toastText.innerHTML = props.msg;
    toastDiv.style.display = "flex";

    setTimeout(() => {
        toastDiv.style.display = "none";
    }, 5000)
}


const getNotified = async () => {
       const nameField = document.getElementById('notification-name');
    const emailField = document.getElementById('notification-email');

    if (nameField.value.trim().length < 8) {
        nameField.style.borderColor = 'red';
        showToast({ borderColor: 'red', msg: `Please, Enter your name!` });
        return;
    }
    nameField.style.borderColor = 'white';

    const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    if (!(String(emailField.value.trim()).toLowerCase().match(re))) {
        emailField.style.borderColor = "red";
        showToast({ borderColor: "red", msg: "Please, Enter a valid E-mail!" });
        return;
    }
    emailField.style.borderColor = "white";

    try {
        showToast({ borderColor: "white", msg: "Loading..." });
        const payload = {
            name: nameField.value.toLowerCase().trim(),
            email: emailField.value.toLowerCase().trim(),
        }

        const res = await fetch(
            "http://127.0.0.1:3000/subscriptions/",
            {
                method: "post",
                body: JSON.stringify(payload),
                headers: { "Content-Type": "application/json" },
            }
        );
        return;

        if (res.status === 201) {
            nameField.value = "";
            emailField.value = "";
            showToast({ borderColor: "#4ea827", msg: "Thanks for subscribing to our notifications!" });
            return;

        }
        if (res.status === 301) {
            emailField.value = "";
            showToast({ borderColor: 'red', msg: "This email already subscribed to our notifications!" });
            return;

        }
        showToast({ borderColor: "red", msg: "Please, Try again later!" });

    } catch (error) {

    }

}

