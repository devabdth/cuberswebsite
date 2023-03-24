const login = async () => {
	const idField = document.getElementById('id');
	const passwordField = document.getElementById('password');
	const loginBtn = document.getElementById('login');

	if (idField.value.trim().length === 0) {
		idField.style.borderColor = 'red';
		idField.style.color = 'red';
		return;
	}
	idField.style.borderColor = '#666';
	idField.style.color = '#4e8ece';

	if (passwordField.value.trim().length < 8 || passwordField.value.trim().length > 32) {
		passwordField.style.borderColor = 'red';
		passwordField.style.borderColor = 'red';
		return;
	}
	passwordField.style.borderColor = '#666';
	passwordField.style.color = '#4e8ece';

	const res = await fetch(
		`./confirmation/?id=${idField.value.trim()}&password=${passwordField.value.trim()}`,
		{
			method: 'get',
			headers: { 'Content-Type': 'application/json' }
		});

	if (res.status == 200) {
		window.open('../leads/', '_self');
		return;
	}
	idField.style.borderColor = '#666';
	idField.style.color = '#4e8ece';
	passwordField.style.borderColor = '#666';
	passwordField.style.color = '#4e8ece';

}