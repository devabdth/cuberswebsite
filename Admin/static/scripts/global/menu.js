let menuOpened = true;
const toggleMenu = () => {
	const menu = document.getElementById('menu');
	const fragment = document.getElementById('fragment');
	const toggleButton = document.getElementById('toggle-button');
	const tabs = ['leads', 'mailing', 'processes', 'logout'].map((title) => document.getElementById(title));
	const titles = ['leads-title', 'mailing-title', 'processes-title', 'logout-title'].map((title) => document.getElementById(title));
	if (menuOpened) {
		for (var i in titles) {
			tabs[i].style.justifyContent = 'space-between !important';
			titles[i].style.display = "none";
		}
		menu.style.width = '5%';
		menuOpened = false;
		toggleButton.innerHTML = ">"
		fragment.style.marginLeft = '5%'
		return;
	}
	menu.style.width = '12.5%';
	menuOpened = true;
	toggleButton.innerHTML = "x"
	fragment.style.marginLeft = '12.5%'
	for (var i in titles) {
		tabs[i].style.justifyContent = 'center !important';
		titles[i].style.display = "block";
	}
}


const leads = () => {
	const url = window.location.href.split('leads');
	if (url.length == 1) {
		window.open(`${url[0]}/leads/`)
	}
}

const mailing = () => {
	const url = window.location.href.split('mailing');
	if (url.length == 1) {
		window.open(`../mailing/`, '_self')
	}
}

const processes = () => {
	const url = window.location.href.split('processes');
	if (url.length == 1) {
		window.open(`../processes/`, '_self')
	}
}