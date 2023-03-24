const selectedleads = [];
let leadsData;

const setupLeadsData = (leads) => {
	leadsData = JSON.parse(leads);
}

const toggleLeadsDropdown = () => {
  document.getElementById(`leads-dropdown`).classList.toggle("show");
}

const filter = () => {
  var input, filter, ul, li, a, i;
  input = document.getElementById("leads-search");
  filter = input.value.toUpperCase();
  div = document.getElementById("leads-dropdown");
  button = div.getElementsByTagName("button");
  for (i = 0; i < button.length; i++) {
    txtValue = button[i].textContent || button[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      button[i].style.display = "";
    } else {
      button[i].style.display = "none";
    }
  }
}

const createLeadsCards = () => {
	const selectedleadsDiv = document.getElementById('selected-leads');
	selectedleadsDiv.innerHTML = '';
	for (lead in selectedleads) {
		const card = document.createElement('p');
		card.innerHTML = leadsData[lead]['name'];
		card.innerText = leadsData[lead]['name'];
		card.textContent = leadsData[lead]['name'];
		selectedleadsDiv.append(card);
	}
}

const chooseLead = (lead) => {
  const btn = document.getElementById(`leads-dropbtn`);
  if(! selectedleads.includes(lead)) {
		  selectedleads.push(lead);
  }
		  createLeadsCards();
		  toggleLeadsDropdown();
}

