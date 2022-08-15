window.addEventListener('scroll', (event) => {
	const header = document.getElementById('header');
	let offset = document.documentElement.scrollTop || document.body.scrollTop;

	if (offset === 0) {
		header.style.backgroundColor = 'transparent';
		return;
	}

	header.style.backgroundColor = '#111';
});
